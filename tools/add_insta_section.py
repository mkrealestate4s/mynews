# -*- coding: utf-8 -*-
"""포스트 페이지에 인스타(임장로그) 이미지 받기 섹션을 추가한다.

로컬 블로그 자동포스팅 프로그램을 깨지 않기 위한 두 가지 제약:

1) **article 밖**에 둔다 — blogText()가 article.children만 훑으므로
   복사 텍스트의 [이미지1~6]이 그대로 유지된다.
2) **서빙되는 HTML에 <img> 태그를 남기지 않는다** — 인스타 이미지는 JS가
   data 속성에서 만들어 넣는다. HTML을 파싱하는 스크래퍼(requests+bs4 등)에는
   기존과 똑같이 카드 6장 + figure 1장만 보인다.
   또한 테마 전환은 img.card-art만 대상이므로 img.insta-art의 경로는 바뀌지 않는다.

사용법: python3 add_insta_section.py posts/<slug>.html <카드접두어>
"""
import pathlib, re, sys

POST = pathlib.Path(sys.argv[1])
SLUG = sys.argv[2]
s = POST.read_text(encoding="utf-8")
assert "#insta" not in s, "이미 인스타 섹션이 있습니다"

CSS = """
/* ── 인스타(임장로그) 이미지 받기 ─────────────────────────── */
#insta .cards-hint b{color:var(--ink)}
.iscroll{display:flex;align-items:flex-start;gap:14px;overflow-x:auto;
  scroll-snap-type:x mandatory;padding:6px 0 14px;-webkit-overflow-scrolling:touch}
.iscroll .imgwrap{scroll-snap-align:start}
.iscroll img{height:auto;border-radius:10px;border:1px solid var(--line);
  scroll-snap-align:start;flex:none;display:block}
.iscroll.car img{width:300px;max-width:66vw;aspect-ratio:4/5}
.iscroll.reel img{width:236px;max-width:54vw;aspect-ratio:9/16}
.iscroll .imgbtns{top:7px;right:7px;gap:5px}
.iscroll .imgbtns .cbtn{font-size:.68rem;padding:2px 9px}
.ilabel{margin:22px 0 6px}
.ilabel .t{font-weight:700;font-size:1.02rem}
.ilabel .s{color:var(--mute);font-size:.82rem;margin-left:8px}
"""
s = s.replace("</style>", CSS + "</style>", 1)

# 갤러리에서 카드 파일 접미어를 읽어온다 (01-cover 등)
NAMES = [re.search(r'data-file="' + SLUG + r'-([0-9]{2}-[a-z]+)\.png"', m).group(1)
         for m in re.findall(r'<img class="card-art"[^>]*>', s)[:6]]
assert len(NAMES) == 6, NAMES

SECTION = f'''<div class="trace"></div>

<section id="insta" data-slug="{SLUG}" data-files="{','.join(NAMES)}">
  <h2>인스타(임장로그)용 이미지</h2>
  <p class="cards-hint">위 카드뉴스와 같은 내용을, 인스타 규격으로 다시 조판한 것입니다 —
    채널명은 <b>임장로그</b>입니다. 이미지를 눌러 <b>복사</b>·<b>저장</b>하세요.
    폰에서는 이미지를 <b>길게 눌러 저장</b>하는 게 가장 확실합니다.</p>

  <div class="ilabel"><span class="t">캐러셀 · 4:5</span>
    <span class="s">1080 × 1350 · 카드 번호 순서(1→6)로 올리세요</span></div>
  <div class="iscroll car" data-folder="carousel" data-kind="캐러셀"></div>

  <div class="ilabel"><span class="t">릴스 · 9:16</span>
    <span class="s">1080 × 1920 · 하단 400px는 인스타 UI 자리로 비워 뒀습니다</span></div>
  <div class="iscroll reel" data-folder="reels" data-kind="릴스"></div>

  <p class="cards-hint" style="margin-top:16px">나레이션 스크립트·자막·초수와 인스타 캡션·해시태그는
    <a href="../publish/reels/{POST.stem}-script.txt" style="color:var(--teal)">여기</a>에 있습니다.</p>
</section>

'''
s = s.replace('<div class="trace"></div>\n\n<footer>', SECTION + "<footer>", 1)

# 인스타 이미지를 JS로 생성 — 버튼 배선보다 먼저 돌아야 한다
BUILD = """  /* ── 인스타 이미지 생성 (HTML에 img 태그를 남기지 않는다:
        로컬 포스팅 프로그램이 포스트 페이지를 파싱할 때 카드 6장만 보이게) ── */
  (function(){
    var sec=document.getElementById('insta');
    if(!sec)return;
    var slug=sec.dataset.slug, files=(sec.dataset.files||'').split(',').filter(Boolean);
    sec.querySelectorAll('.iscroll').forEach(function(row){
      var folder=row.dataset.folder, kind=row.dataset.kind||'';
      files.forEach(function(f,i){
        var im=document.createElement('img');
        im.className='insta-art';
        im.loading='lazy';
        im.dataset.file=slug+'-'+f+'.png';
        im.src='../images/cards/'+folder+'/'+slug+'-'+f+'.png';
        im.alt=kind+' '+(i+1)+'/'+files.length;
        row.appendChild(im);
      });
    });
  })();

  function downloadImg(img){"""
assert "  function downloadImg(img){" in s
s = s.replace("  function downloadImg(img){", BUILD, 1)

# 버튼 배선에 인스타 이미지 포함 (테마 전환 대상에는 넣지 않는다)
s = s.replace("document.querySelectorAll('img.card-art').forEach(function(img){\n    var wrap=document.createElement('div');wrap.className='imgwrap';",
              "document.querySelectorAll('img.card-art,img.insta-art').forEach(function(img){\n    var wrap=document.createElement('div');wrap.className='imgwrap';")

POST.write_text(s, encoding="utf-8")
print("added #insta (JS-built) with", NAMES)
