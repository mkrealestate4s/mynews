# -*- coding: utf-8 -*-
"""발행 지시서(manifest) 조회 모듈 — 로컬 네이버 포스팅 프로그램에 붙여 쓰는 용도.

사용 예:
    from naver_fetch_job import fetch_job, mark_done

    job = fetch_job()
    if job is None:
        print("발행할 작업 없음"); raise SystemExit(0)

    # job.title / job.body / job.blocks / job.images / job.tags / job.mode
    run_playwright_posting(job)      # 기존 자동입력 함수에 넘기기
    mark_done(job)                   # 중복 발행 방지 기록

표준 라이브러리만 사용합니다(추가 설치 불필요).
"""

import json
import os
import re
import tempfile
import urllib.request
from dataclasses import dataclass, field

MANIFEST_URL = "https://mkrealestate4s.github.io/mynews/publish/manifest.json"
QUEUE_URL = "https://mkrealestate4s.github.io/mynews/publish/queue.json"
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posted.log")
UA = {"User-Agent": "mynews-naver-poster/1"}


def _get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


@dataclass
class Job:
    job_id: str
    mode: str                  # "draft" = 임시저장까지, "publish" = 발행까지
    title: str
    title_alts: list
    body: str                  # 발행용 본문 전문 ([이미지N] 자리표시 포함)
    blocks: list               # [("text", "..."), ("image", 3), ...] 순서대로
    images: dict               # {1: 로컬파일경로, 2: ...}
    tags: list
    slug: str
    report_no: int
    raw: dict = field(default_factory=dict)


def _split_blocks(body):
    """본문을 텍스트/이미지 블록 순서로 쪼갠다. [이미지3 : 설명] → ("image", 3)"""
    out, pos = [], 0
    for m in re.finditer(r"\[이미지(\d+)[^\]]*\]", body):
        chunk = body[pos:m.start()].strip()
        if chunk:
            out.append(("text", chunk))
        out.append(("image", int(m.group(1))))
        pos = m.end()
    tail = body[pos:].strip()
    if tail:
        out.append(("text", tail))
    return out


def _already_posted(job_id):
    if not os.path.exists(STATE_FILE):
        return False
    with open(STATE_FILE, encoding="utf-8") as f:
        return any(line.strip() == job_id for line in f)


def fetch_job(download_images=True, image_dir=None):
    """지시서를 읽어 Job을 돌려준다. 발행할 게 없으면 None."""
    man = json.loads(_get(MANIFEST_URL))
    if man.get("status") != "ready":
        return None

    job_id = man["job_id"]
    if _already_posted(job_id):
        return None                      # 이미 처리한 작업 — 중복 발행 방지

    p = man["post"]
    body = _get(p["body_url"])

    images = {}
    if download_images:
        image_dir = image_dir or tempfile.mkdtemp(prefix="mynews_cards_")
        os.makedirs(image_dir, exist_ok=True)
        for im in p["images"]:
            path = os.path.join(image_dir, f"{p['slug']}-{im['n']:02d}.png")
            with open(path, "wb") as f:
                f.write(_get(im["url"], binary=True))
            images[im["n"]] = path

    return Job(
        job_id=job_id,
        mode=man.get("mode", "draft"),
        title=p["title"],
        title_alts=p.get("title_alts", []),
        body=body,
        blocks=_split_blocks(body),
        images=images,
        tags=p.get("tags", []),
        slug=p["slug"],
        report_no=p.get("report_no", 0),
        raw=man,
    )


def mark_done(job):
    """처리 완료 기록 — 다음 실행에서 같은 작업을 건너뛰게 한다."""
    with open(STATE_FILE, "a", encoding="utf-8") as f:
        f.write(job.job_id + "\n")


def fetch_queue(include_pending=True):
    """발행 후보 목록을 오래된 것부터 돌려준다. 로컬 posted.log에 있는 건 제외.

    같은 날 글이 여러 개거나 며칠 밀렸을 때 title.txt(한 칸)로는 앞선 글이
    덮여 사라지므로, 목록을 받아 순서대로 처리한다.

    반환: [{"slug","report_no","titles",...}, ...]  (오래된 순)
    """
    q = json.loads(_get(QUEUE_URL))
    wanted = {"designated", "pending"} if include_pending else {"designated"}
    items = [it for it in q.get("items", [])
             if it.get("status") in wanted and not _already_posted(it["slug"])]
    items.sort(key=lambda it: (it.get("date", ""), it.get("report_no", 0)))
    return items


def mark_slug_done(slug):
    """슬러그 단위 완료 기록 — fetch_queue로 처리한 항목에 사용."""
    with open(STATE_FILE, "a", encoding="utf-8") as f:
        f.write(slug + "\n")


if __name__ == "__main__":
    print("=== 발행 후보 목록 (오래된 순) ===")
    for it in fetch_queue():
        print(f"  #{it.get('report_no')} {it['date']} {it['slug']} [{it['status']}]")
        print(f"     → {it['titles'][0]}")
    print()

    j = fetch_job()
    if j is None:
        print("발행할 작업 없음 (status != ready 또는 이미 처리됨)")
    else:
        print("job_id :", j.job_id)
        print("mode   :", j.mode)
        print("제목   :", j.title)
        print("태그   :", " ".join("#" + t for t in j.tags))
        print("블록   :", [(k, v if k == "image" else len(v)) for k, v in j.blocks])
        for n, path in sorted(j.images.items()):
            print(f"  이미지{n} → {path}")
