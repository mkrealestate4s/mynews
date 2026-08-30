# -*- coding: utf-8 -*-
"""1:1 카드 HTML을 4:5(1080x1350) 인스타 캐러셀용으로 재조판한다.

사용법 (카드 HTML이 있는 디렉터리에서):
    python3 make_carousel.py <slug> [테마...]
그 뒤 <theme>-car/*.html 을 1080x1437 창으로 렌더 → 상단 1080x1350 크롭.

캐러셀은 릴스와 달리 하단 UI가 이미지를 덮지 않으므로 여백을 고르게 쓴다.
"""
import pathlib, re, sys

from make_cards import VFRAME_CSS, fit_script

BASE = pathlib.Path(__file__).parent
SLUG = sys.argv[1]
THEMES = sys.argv[2:] or ["insta"]

# 카드 번호를 갤러리 썸네일에서도 읽을 수 있게 키운다.
#
# 폰 갤러리와 인스타 사진 선택 화면은 **파일명이 아니라 '추가된 시각'으로 정렬**한다.
# 6장을 한 번에 저장하면 시각이 사실상 같아져 순서가 뒤섞이고, 그러면 어느 게 1번인지
# 알 방법이 없다(2026-08-30 사용자 보고). 저장 순서도 고쳤지만, 마지막 근거는
# 카드에 적힌 번호다. 1:1 카드(블로그)는 건드리지 않고 캐러셀에서만 키운다.
EXTRA = """
html,body{height:1350px}
body{padding:92px 92px 200px}
.footwrap{bottom:66px}
.mid{padding:20px 0}
.top{align-items:center}
.pnum{font-size:27px;display:flex;align-items:baseline;gap:4px}
.pnum b{font-size:92px;font-weight:900;line-height:.9;letter-spacing:-.03em;
  color:var(--accent);font-family:inherit}
""" + VFRAME_CSS

n = 0
for th in THEMES:
    src = BASE / th
    out = BASE / f"{th}-car"; out.mkdir(exist_ok=True)
    for f in sorted(src.glob(f"{SLUG}-*.html")):
        html = f.read_text(encoding="utf-8").replace("</style>", EXTRA + "</style>", 1)
        html = html.replace("</body>", fit_script(0.97, 1.35) + "</body>", 1)
        # "01 / 06" 의 앞 숫자만 크게 (뒤 '/06' 은 작게 남겨 맥락을 준다)
        html, k = re.subn(r'<div class="pnum">\s*(\d+)\s*/\s*(\d+)\s*</div>',
                          r'<div class="pnum"><b>\1</b>/\2</div>', html, count=1)
        assert k == 1, f"{f.name}: 카드 번호(.pnum)를 찾지 못했습니다"
        (out / f.name).write_text(html, encoding="utf-8")
        n += 1
print("wrote", n, "carousel pages")
