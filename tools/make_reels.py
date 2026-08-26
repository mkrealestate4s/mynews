# -*- coding: utf-8 -*-
"""1:1 카드 HTML을 9:16(1080x1920) 인스타 릴스용으로 재조판한다.

사용법 (카드 HTML이 있는 디렉터리에서):
    python3 make_reels.py <slug> "<릴스 상단 제목>" <리포트번호> [테마...]
(테마 미지정 시 insta — 인스타 채널 "임장로그" 전용 테마)
그 뒤 <theme>-reels/*.html 을 1080x2007 창으로 렌더 → 상단 1080x1920 크롭.

하단 400px는 인스타 UI(캡션·버튼)가 덮으므로 비워 둔다.
"""
import pathlib, re, sys

from make_cards import fit_script

BASE = pathlib.Path(__file__).parent
SLUG = sys.argv[1]
STRIP = sys.argv[2]        # 릴스 상단 고정 제목(키워드)
NO = sys.argv[3] if len(sys.argv) > 3 else ""   # 리포트 번호
THEMES = sys.argv[4:] or ["insta"]

# 9:16 전용 추가 CSS
EXTRA = """
html,body{height:1920px}
/* 인스타 릴스 UI가 하단 ~380px를 덮으므로 본문을 상단 안전영역에 몰아둔다 */
body{padding:92px 96px 580px}
.footwrap{bottom:436px}
.cta{position:absolute;left:96px;right:96px;bottom:516px;font-size:26px;color:var(--mute)}
.strip{flex:none;margin:26px 0 0;padding:22px 30px;border-left:6px solid var(--accent);
  background:var(--panel);border-radius:0 16px 16px 0}
.strip .sl{font-size:24px;color:var(--mute);letter-spacing:.1em;font-weight:700}
.strip .st{font-size:40px;font-weight:900;line-height:1.3;margin-top:6px;word-break:keep-all}
.mid{padding:26px 0}
/* 나란히 선 nowrap 패널은 세로 프레임에서 폭을 잡아먹어 확대를 막는다 → 위아래로 */
.duo{flex-direction:column;gap:18px}
"""

def convert(html, strip_html):
    # </style> 앞에 9:16 오버라이드 삽입 (뒤에 와야 우선 적용됨)
    html = html.replace("</style>", EXTRA + "</style>", 1)
    html = html.replace("</body>", fit_script(0.97, 1.45) + "</body>", 1)
    # .top 직후에 고정 제목 스트립 삽입
    m = re.search(r'(<div class="top">.*?</div></div>)', html, re.S)
    assert m, "top block not found"
    html = html[:m.end()] + strip_html + html[m.end():]
    # 하단 CTA
    html = html.replace('<div class="footwrap">',
                        '<div class="cta">▶ 팔로우 · 저장</div><div class="footwrap">', 1)
    return html

strip = (f'<div class="strip"><div class="sl">2026 · 8월 리포트 #{NO}</div>'
         f'<div class="st">{STRIP}</div></div>')

n = 0
for th in THEMES:
    d = BASE / th
    out = BASE / f"{th}-reels"; out.mkdir(exist_ok=True)
    for f in sorted(d.glob(f"{SLUG}-*.html")):
        (out / f.name).write_text(convert(f.read_text(encoding="utf-8"), strip), encoding="utf-8")
        n += 1
print("wrote", n, "reels pages")
