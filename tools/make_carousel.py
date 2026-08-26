# -*- coding: utf-8 -*-
"""1:1 카드 HTML을 4:5(1080x1350) 인스타 캐러셀용으로 재조판한다.

사용법 (카드 HTML이 있는 디렉터리에서):
    python3 make_carousel.py <slug> [테마...]
그 뒤 <theme>-car/*.html 을 1080x1437 창으로 렌더 → 상단 1080x1350 크롭.

캐러셀은 릴스와 달리 하단 UI가 이미지를 덮지 않으므로 여백을 고르게 쓴다.
"""
import pathlib, sys

BASE = pathlib.Path(__file__).parent
SLUG = sys.argv[1]
THEMES = sys.argv[2:] or ["report", "white", "editorial"]

EXTRA = """
html,body{height:1350px}
body{padding:92px 92px 200px}
.footwrap{bottom:66px}
.mid{padding:20px 0}
"""

n = 0
for th in THEMES:
    src = BASE / th
    out = BASE / f"{th}-car"; out.mkdir(exist_ok=True)
    for f in sorted(src.glob(f"{SLUG}-*.html")):
        html = f.read_text(encoding="utf-8").replace("</style>", EXTRA + "</style>", 1)
        (out / f.name).write_text(html, encoding="utf-8")
        n += 1
print("wrote", n, "carousel pages")
