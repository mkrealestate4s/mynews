# -*- coding: utf-8 -*-
"""포스트 페이지에 인스타(임장로그) 이미지 다운로드 섹션을 추가한다.

- article 밖에 두므로 blogText()의 복사 텍스트에는 영향이 없다.
- img.card-art 는 테마 전환 시 src가 바뀌므로 인스타 이미지는 img.insta-art 로 분리한다.
"""
import pathlib, re, sys

POST = pathlib.Path(sys.argv[1])
SLUG = sys.argv[2]          # 예: isipdae
s = POST.read_text(encoding="utf-8")

CSS = """
/* ── 인스타(임장로그) 이미지 받기 ─────────────────────────── */
#insta .cards-hint b{color:var(--ink)}
.iscroll{display:flex;align-items:flex-start;gap:14px;overflow-x:auto;
  scroll-snap-type:x mandatory;padding:6px 0 14px;-webkit-overflow-scrolling:touch}
.iscroll .imgwrap{scroll-snap-align:start}
.iscroll img{height:auto;border-radius:10px;border:1px solid var(--line);
  scroll-snap-align:start;flex:none;display:block}
.iscroll.car img{width:272px;max-width:62vw;aspect-ratio:4/5}
.iscroll.reel img{width:216px;max-width:50vw;aspect-ratio:9/16}
.ilabel{display:flex;align-items:baseline;gap:10px;margin:22px 0 6px}
.ilabel .t{font-weight:700;font-size:1.02rem}
.ilabel .s{color:var(--mute);font-size:.82rem}
"""
assert "#insta" not in s, "이미 인스타 섹션이 있습니다"
s = s.replace("</style>", CSS + "</style>", 1)

def row(kind, folder, ratio):
    imgs = "\n    ".join(
        f'<img class="insta-art" data-file="{SLUG}-{n}.png" '
        f'src="../images/cards/{folder}/{SLUG}-{n}.png" '
        f'alt="{kind} {i}/6" loading="lazy">'
        for i, n in enumerate(NAMES, start=1))
    return f'  <div class="iscroll {ratio}">\n    {imgs}\n  </div>'

NAMES = [re.search(r'data-file="' + SLUG + r'-([0-9]{2}-[a-z]+)\.png"', m).group(1)
         for m in re.findall(r'<img class="card-art"[^>]*>', s)[:6]]
assert len(NAMES) == 6, NAMES

SECTION = f'''<div class="trace"></div>

<section id="insta">
  <h2>인스타(임장로그)용 이미지</h2>
  <p class="cards-hint">위 카드뉴스와 같은 내용을, 인스타 규격으로 다시 조판한 것입니다 —
    채널명은 <b>임장로그</b>입니다. 이미지를 눌러 <b>복사</b>·<b>저장</b>하세요.
    폰에서는 이미지를 <b>길게 눌러 저장</b>하는 게 가장 확실합니다.</p>

  <div class="ilabel"><span class="t">캐러셀 · 4:5</span>
    <span class="s">1080 × 1350 · 카드 번호 순서(1→6)로 올리세요</span></div>
{row("캐러셀", "carousel", "car")}

  <div class="ilabel"><span class="t">릴스 · 9:16</span>
    <span class="s">1080 × 1920 · 하단 400px는 인스타 UI 자리로 비워 뒀습니다</span></div>
{row("릴스", "reels", "reel")}

  <p class="cards-hint" style="margin-top:16px">나레이션 스크립트·자막·초수와 인스타 캡션·해시태그는
    <a href="../publish/reels/{POST.stem}-script.txt" style="color:var(--teal)">여기</a>에 있습니다.</p>
</section>

'''
s = s.replace("<div class=\"trace\"></div>\n\n<footer>", SECTION + "<footer>", 1)

# 버튼 배선에 인스타 이미지 포함 (테마 전환 대상에는 넣지 않는다)
s = s.replace("document.querySelectorAll('img.card-art').forEach(function(img){\n    var wrap=document.createElement('div');wrap.className='imgwrap';",
              "document.querySelectorAll('img.card-art,img.insta-art').forEach(function(img){\n    var wrap=document.createElement('div');wrap.className='imgwrap';")

POST.write_text(s, encoding="utf-8")
print("added #insta with", NAMES)
