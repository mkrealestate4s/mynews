# -*- coding: utf-8 -*-
"""인스타 캐러셀 발행 지시서와 JPEG 파생을 만든다.

    python3 tools/make_insta_post.py [slug]        # slug 생략 시 publish/manifest.json

내는 것:
  images/cards/carousel-jpg/<접두어>-NN.jpg   — 인스타 API가 PNG를 안 받는다
  publish/insta.json                          — 발행 지시서 (액션이 읽는다)

**왜 JPEG를 따로 뽑나** — 인스타 콘텐츠 발행 API는 image_url 로 JPEG 만 받는다.
PNG를 넘기면 컨테이너 생성 단계에서 거부된다.
**왜 4:4:4로 저장하나** — 기본 4:2:0은 색해상도를 절반으로 줄여 앰버(#FFB020)
글자 경계가 뭉갠다. 평면 그래픽 + 얇은 글자에는 subsampling=0 이 눈에 띄게 낫다.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://mkrealestate4s.github.io/mynews"
QUALITY = 95

# 인스타 제약 (Meta 문서)
MAX_CAPTION = 2200
MAX_TAGS = 30
CAROUSEL_MIN, CAROUSEL_MAX = 2, 10
MAX_BYTES = 8 * 1024 * 1024


def today_slug() -> str:
    m = json.loads((ROOT / "publish/manifest.json").read_text(encoding="utf-8"))
    return m["post"]["slug"]


def parse_caption(script_path: pathlib.Path) -> tuple[str, list[str]]:
    """스크립트 파일의 '■ 인스타 캡션' 블록 → (캡션 본문, 해시태그 목록).

    해시태그는 캡션 끝에 이미 붙어 있다. 개수·길이를 검사할 수 있게 분리해서
    돌려주고, 실제 발행 캡션은 본문 + 태그를 다시 이어 만든다.
    """
    text = script_path.read_text(encoding="utf-8")
    m = re.search(r'■ 인스타 캡션[^\n]*\n\n(.+?)\n═+', text, re.S)
    if not m:
        raise SystemExit(f"캡션 블록을 찾지 못했습니다 — {script_path.name}")
    block = m.group(1).strip()

    lines = block.split("\n")
    tags: list[str] = []
    while lines and (not lines[-1].strip() or lines[-1].lstrip().startswith("#")):
        ln = lines.pop().strip()
        if ln:
            tags = re.findall(r'#[^\s#]+', ln) + tags
    return "\n".join(lines).rstrip(), tags


def make_jpegs(slug: str) -> list[pathlib.Path]:
    from PIL import Image

    stem = slug.split("-", 3)[-1]                     # 2026-08-26-isipdae → isipdae
    src_dir = ROOT / "images/cards/carousel"
    out_dir = ROOT / "images/cards/carousel-jpg"
    out_dir.mkdir(parents=True, exist_ok=True)

    srcs = sorted(src_dir.glob(f"{stem}-*.png"))
    if not srcs:
        raise SystemExit(f"캐러셀 PNG가 없습니다 — {src_dir}/{stem}-*.png")

    out = []
    for p in srcs:
        q = out_dir / (p.stem + ".jpg")
        im = Image.open(p).convert("RGB")
        # subsampling=0 → 4:4:4. 앰버 글자 경계를 지키기 위한 선택이다.
        im.save(q, "JPEG", quality=QUALITY, subsampling=0, optimize=True,
                progressive=False)
        out.append(q)
    return out


def build(slug: str) -> dict:
    stem = slug.split("-", 3)[-1]
    script = ROOT / f"publish/reels/{slug}-script.txt"
    if not script.exists():
        raise SystemExit(f"릴스 스크립트가 없습니다 — {script}")

    body, tags = parse_caption(script)
    caption = (body + "\n\n" + " ".join(tags)).strip()
    jpegs = make_jpegs(slug)

    problems = []
    if not CAROUSEL_MIN <= len(jpegs) <= CAROUSEL_MAX:
        problems.append(f"캐러셀은 {CAROUSEL_MIN}~{CAROUSEL_MAX}장이어야 합니다 (지금 {len(jpegs)})")
    if len(caption) > MAX_CAPTION:
        problems.append(f"캡션 {len(caption)}자 — 한도 {MAX_CAPTION}자")
    if len(tags) > MAX_TAGS:
        problems.append(f"해시태그 {len(tags)}개 — 한도 {MAX_TAGS}개")
    for p in jpegs:
        if p.stat().st_size > MAX_BYTES:
            problems.append(f"{p.name} {p.stat().st_size / 1e6:.1f}MB — 한도 8MB")

    from PIL import Image
    sizes = {Image.open(p).size for p in jpegs}
    if len(sizes) > 1:
        # 캐러셀은 첫 장 비율로 전체가 잘린다 — 비율이 섞이면 뒷장이 잘린다.
        problems.append(f"이미지 크기가 섞였습니다 {sorted(sizes)}")

    if problems:
        raise SystemExit("발행 지시서를 만들 수 없습니다:\n  - " + "\n  - ".join(problems))

    no = json.loads((ROOT / "publish/manifest.json").read_text(encoding="utf-8"))
    return {
        "schema": 1,
        "job_id": f"{slug}-carousel",
        # ready = 액션이 발행한다. hold 로 바꿔 두면 건너뛴다.
        # 인스타 API에는 '임시저장'이 없다 — 발행하면 즉시 공개된다.
        "status": "ready",
        "channel": "임장로그",
        "media_type": "CAROUSEL",
        "post": {
            "report_no": no["post"]["report_no"],
            "slug": slug,
            "caption": caption,
            "caption_chars": len(caption),
            "hashtags": tags,
            "images": [{"n": i + 1,
                        "url": f"{SITE}/images/cards/carousel-jpg/{p.name}",
                        "bytes": p.stat().st_size}
                       for i, p in enumerate(jpegs)],
        },
    }


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else today_slug()
    job = build(slug)
    out = ROOT / "publish/insta.json"
    out.write_text(json.dumps(job, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    p = job["post"]
    print(f"{out.relative_to(ROOT)} — {slug}")
    print(f"  캐러셀 {len(p['images'])}장 · 캡션 {p['caption_chars']}자 · 태그 {len(p['hashtags'])}개")
    for im in p["images"]:
        print(f"  {im['n']}. {im['url'].rsplit('/', 1)[-1]}  {im['bytes'] / 1000:.0f}KB")


if __name__ == "__main__":
    main()
