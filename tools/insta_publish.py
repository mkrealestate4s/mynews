# -*- coding: utf-8 -*-
"""publish/insta.json 을 읽어 인스타 캐러셀을 발행한다 (공식 Graph API).

    python3 tools/insta_publish.py --dry-run     # 토큰 없이 전 과정 점검
    python3 tools/insta_publish.py               # 실제 발행

환경변수:
    IG_USER_ID        인스타 비즈니스/크리에이터 계정의 IG User ID
    IG_ACCESS_TOKEN   장기 액세스 토큰 (60일마다 갱신)
    IG_API_BASE       기본 https://graph.facebook.com/v21.0
                      (Instagram Login 방식이면 https://graph.instagram.com/v21.0)

발행 순서 (Meta 콘텐츠 발행 API):
    1. 장마다 컨테이너 생성   POST /{ig}/media?image_url=..&is_carousel_item=true
    2. 캐러셀 컨테이너 생성   POST /{ig}/media?media_type=CAROUSEL&children=..&caption=..
    3. 발행                  POST /{ig}/media_publish?creation_id=..

**이미지는 바이트로 못 올린다** — 공개 HTTPS URL 만 받는다. 우리 카드는 이미
깃페이지에 올라가 있으므로 그 URL을 그대로 쓴다.
**인스타에는 임시저장이 없다** — media_publish 는 즉시 공개된다. 그래서
insta.json 의 status 가 ready 일 때만 발행하고, 발행 기록을 남겨 중복을 막는다.

비공식 자동화 라이브러리는 쓰지 않는다 — 계정 제한 사유다.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
JOB = ROOT / "publish/insta.json"
POSTED = ROOT / "publish/insta-posted.json"
# 기본은 **인스타 로그인 방식**(graph.instagram.com) — 페이스북 페이지가 필요 없어
# 개인 운영에 맞다. 페이스북 로그인 방식으로 토큰을 받았다면
# IG_API_BASE=https://graph.facebook.com/v21.0 을 넣어야 한다. 둘은 호스트만 다르고
# 엔드포인트 모양이 같아서 이 스크립트는 그대로 쓸 수 있다.
# `or` 로 받는다 — 액션에서 미설정 변수는 빈 문자열로 넘어오므로
# os.environ.get(key, default) 로는 기본값이 적용되지 않는다.
BASE = os.environ.get("IG_API_BASE") or "https://graph.instagram.com/v21.0"
UA = {"User-Agent": "mynews-insta/1"}


def _api_soft(method: str, path: str, params: dict, token: str) -> dict | None:
    """실패해도 멈추지 않는 호출 — 있으면 좋은 정보(할당량 등)에 쓴다."""
    try:
        return _api(method, path, params, token)
    except SystemExit:
        return None


def _api(method: str, path: str, params: dict, token: str) -> dict:
    url = f"{BASE.rstrip('/')}/{path.lstrip('/')}"
    data = {**params, "access_token": token}
    body = urllib.parse.urlencode(data).encode()
    req = (urllib.request.Request(url, data=body, headers=UA, method="POST")
           if method == "POST" else
           urllib.request.Request(f"{url}?{urllib.parse.urlencode(data)}",
                                  headers=UA, method="GET"))
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        raise SystemExit(f"❌ API {method} {path} → {e.code}\n{detail}") from e


def _reachable(url: str) -> tuple[bool, str]:
    """이미지 URL이 인스타 서버에서 받아갈 수 있는 상태인지 확인."""
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            ct = r.headers.get("Content-Type", "")
            n = r.headers.get("Content-Length", "?")
            ok = r.status == 200 and "jpeg" in ct.lower()
            return ok, f"{r.status} {ct} {n}B"
    except Exception as e:                       # 네트워크가 막힌 환경도 있다
        return False, f"확인 불가: {type(e).__name__}"


def load_job() -> dict:
    if not JOB.exists():
        raise SystemExit(f"발행 지시서가 없습니다 — {JOB}\n"
                         "  python3 tools/make_insta_post.py 로 먼저 만드세요.")
    return json.loads(JOB.read_text(encoding="utf-8"))


def already_posted(job_id: str) -> dict | None:
    if not POSTED.exists():
        return None
    log = json.loads(POSTED.read_text(encoding="utf-8"))
    return next((r for r in log.get("posted", []) if r["job_id"] == job_id), None)


def record(job_id: str, media_id: str, permalink: str) -> None:
    log = (json.loads(POSTED.read_text(encoding="utf-8"))
           if POSTED.exists() else {"schema": 1, "posted": []})
    log["posted"].insert(0, {"job_id": job_id, "media_id": media_id,
                             "permalink": permalink,
                             "at": time.strftime("%Y-%m-%dT%H:%M:%S+0000", time.gmtime())})
    log["posted"] = log["posted"][:200]
    POSTED.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def wait_ready(container: str, token: str, tries: int = 30) -> None:
    """컨테이너가 FINISHED 가 될 때까지 기다린다. ERROR 면 이유를 그대로 보여준다."""
    for i in range(tries):
        r = _api("GET", container, {"fields": "status_code,status"}, token)
        code = r.get("status_code")
        if code == "FINISHED":
            return
        if code == "ERROR":
            raise SystemExit(f"❌ 컨테이너 처리 실패: {r.get('status')}")
        time.sleep(min(2 + i, 10))
    raise SystemExit("❌ 컨테이너가 준비되지 않았습니다 (시간 초과)")


def check_account(ig: str, token: str) -> None:
    """계정이 발행 자격을 갖췄는지 확인한다 — 전환·토큰 발급 직후 먼저 이걸 돌린다.

    account_type 이 BUSINESS 또는 MEDIA_CREATOR 여야 발행이 된다(개인 계정은 불가).
    content_publishing_limit 은 발행 권한이 실제로 열려 있을 때만 응답하므로
    자격 확인과 남은 할당량 확인을 겸한다.
    """
    me = _api("GET", ig, {"fields": "id,user_id,username,account_type"}, token)
    print(f"  계정  @{me.get('username', '?')}  (id {me.get('user_id') or me.get('id')})")
    print(f"  토큰  ✓ 유효  ·  {BASE}")

    # account_type 은 호스트·버전에 따라 안 내려오는 경우가 있다.
    # 값이 있을 때만 판정하고, 없으면 발행 시도로 확인한다(여기서 막지 않는다).
    kind = me.get("account_type")
    if kind is None:
        print("  유형  (응답에 없음 — 발행 단계에서 확인됩니다)")
    elif kind in ("BUSINESS", "MEDIA_CREATOR"):
        print(f"  유형  {kind} ✓ 발행 가능")
    else:
        print(f"  유형  {kind} ❌ 프로페셔널 계정이 아닙니다")
        raise SystemExit("설정 → 계정 유형 및 도구 → 프로페셔널 계정으로 전환 (무료)")

    lim = _api_soft("GET", f"{ig}/content_publishing_limit",
                    {"fields": "quota_usage,config"}, token)
    if lim and lim.get("data"):
        d = lim["data"][0]
        cap = (d.get("config") or {}).get("quota_total", 25)
        print(f"  할당량  24시간 내 {d.get('quota_usage', 0)}/{cap}건 사용")
    else:
        print("  할당량  조회 불가 (이 방식에서는 제공되지 않을 수 있습니다 · 하루 25건)")


def main() -> None:
    ap = argparse.ArgumentParser(description="인스타 캐러셀 발행")
    ap.add_argument("--dry-run", action="store_true",
                    help="API를 호출하지 않고 지시서·이미지·한도만 점검")
    ap.add_argument("--check", action="store_true",
                    help="계정 유형·토큰·남은 할당량만 확인 (발행하지 않음)")
    ap.add_argument("--force", action="store_true", help="이미 발행한 job_id도 다시 발행")
    a = ap.parse_args()

    if a.check:
        ig, token = os.environ.get("IG_USER_ID"), os.environ.get("IG_ACCESS_TOKEN")
        if not ig or not token:
            raise SystemExit("❌ IG_USER_ID · IG_ACCESS_TOKEN 환경변수가 필요합니다.")
        print("■ 계정 점검")
        check_account(ig, token)
        return

    job = load_job()
    p = job["post"]
    imgs = p["images"]
    print(f"■ {job['job_id']} · {job['channel']} · {job['media_type']}")
    print(f"  캐러셀 {len(imgs)}장 · 캡션 {len(p['caption'])}자 · 태그 {len(p['hashtags'])}개")

    if job.get("status") != "ready":
        print(f"⏸  status={job.get('status')} — 발행하지 않습니다.")
        return
    dup = already_posted(job["job_id"])
    if dup and not a.force:
        print(f"⏭  이미 발행됨 ({dup['at']}) {dup.get('permalink') or dup['media_id']}")
        return

    bad = 0
    for im in imgs:
        ok, info = _reachable(im["url"])
        print(f"  {'✓' if ok else '·'} {im['n']}. {im['url'].rsplit('/', 1)[-1]}  {info}")
        bad += (not ok)
    if bad:
        msg = (f"{bad}장을 확인하지 못했습니다 — 이미지가 아직 배포되지 않았거나 "
               "JPEG가 아닙니다. 인스타 서버가 이 URL을 직접 받아가므로 "
               "공개 상태여야 합니다.")
        if a.dry_run:
            print(f"⚠️  {msg}")
        else:
            raise SystemExit(f"❌ {msg}")

    if a.dry_run:
        print("\n[드라이런] 여기까지 통과. 실제 발행은 --dry-run 없이 실행하세요.")
        return

    ig, token = os.environ.get("IG_USER_ID"), os.environ.get("IG_ACCESS_TOKEN")
    if not ig or not token:
        raise SystemExit("❌ IG_USER_ID · IG_ACCESS_TOKEN 환경변수가 필요합니다.")

    children = []
    for im in imgs:
        r = _api("POST", f"{ig}/media",
                 {"image_url": im["url"], "is_carousel_item": "true"}, token)
        children.append(r["id"])
        print(f"  올림 {im['n']}/{len(imgs)} → {r['id']}")

    r = _api("POST", f"{ig}/media",
             {"media_type": "CAROUSEL", "children": ",".join(children),
              "caption": p["caption"]}, token)
    carousel = r["id"]
    print(f"  캐러셀 컨테이너 {carousel}")
    wait_ready(carousel, token)

    r = _api("POST", f"{ig}/media_publish", {"creation_id": carousel}, token)
    media_id = r["id"]
    link = _api("GET", media_id, {"fields": "permalink"}, token).get("permalink", "")
    record(job["job_id"], media_id, link)
    print(f"✅ 발행 완료 — {link or media_id}")


if __name__ == "__main__":
    main()
