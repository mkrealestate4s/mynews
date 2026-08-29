# -*- coding: utf-8 -*-
"""포스트 페이지에 인스타(임장로그) 이미지 받기 섹션 + 전체 저장 버튼을 추가한다.

로컬 블로그 자동포스팅 프로그램을 깨지 않기 위한 3중 격리 (바꾸지 말 것):

1) **article 밖**에 둔다 — blogText()가 article.children만 훑으므로
   복사 텍스트의 [이미지1~6]이 그대로 유지된다.
2) **서빙되는 HTML에 <img> 태그를 남기지 않는다** — 인스타 이미지는 JS가
   data 속성에서 만들어 넣는다. HTML을 파싱하는 프로그램에는 기존과 똑같이
   <img> 7개(카드 6 + figure 1)만 보인다.
3) 인스타 이미지는 **img.insta-art** — 테마 전환은 img.card-art만 대상이므로
   경로가 덮이지 않는다.

전체 저장은 기기에 따라 두 경로를 쓴다 (버튼 문구도 그에 맞게 바뀐다):
  · 폰: navigator.share({files}) → 공유 시트에서 '이미지 저장' → 원본 그대로 사진앱에
  · PC: 무압축(store) ZIP을 브라우저에서 직접 만들어 내려받기 (외부 라이브러리 없음)

사용법: python3 add_insta_section.py posts/<slug>.html <카드접두어>
"""
import pathlib, re, sys

POST = pathlib.Path(sys.argv[1])
SLUG = sys.argv[2]
s = POST.read_text(encoding="utf-8")
# 어제 글을 복제해 쓰므로 CSS·JS 는 이미 들어 있고 섹션만 없는 상태가 정상이다.
# 예전 가드는 CSS 선택자 '#insta' 를 보고 오탐했다 → 실제 섹션 유무로 판단한다.
assert '<section id="insta"' not in s, "이미 인스타 섹션이 있습니다"
HAS_CSS = "#insta .cards-hint b" in s          # 복제본이면 True
HAS_JS = "insta-art" in s and "downloadImg" in s

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
.ilabel{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:22px 0 6px}
.ilabel .t{font-weight:700;font-size:1.02rem}
.ilabel .s{color:var(--mute);font-size:.82rem}
.allbtn{cursor:pointer;border:1px solid var(--teal);background:transparent;color:var(--teal);
  font:inherit;font-size:.78rem;font-weight:700;border-radius:999px;padding:4px 14px;
  margin-left:auto;white-space:nowrap;transition:opacity .15s}
.allbtn[disabled]{opacity:.5;cursor:default}
"""
if not HAS_CSS:
    s = s.replace("</style>", CSS + "</style>", 1)

# 갤러리에서 카드 파일 접미어를 읽어온다 (01-cover 등)
NAMES = [re.search(r'data-file="' + SLUG + r'-([0-9]{2}-[a-z]+)\.png"', m).group(1)
         for m in re.findall(r'<img class="card-art"[^>]*>', s)[:6]]
assert len(NAMES) == 6, NAMES


# 릴스 스크립트에서 [나레이션] 블록을 뽑아 통스크립트를 만든다 (없으면 버튼 생략)
SCRIPT = POST.parent.parent / "publish" / "reels" / f"{POST.stem}-script.txt"
NARR = ""
CAP = ""
if SCRIPT.exists():
    blocks = re.findall(r'\[나레이션\]\s*\n(.+?)\n\s*\n\[자막\]',
                        SCRIPT.read_text(encoding="utf-8"), re.S)
    NARR = "\n".join(b.strip() for b in blocks)
    print(f"나레이션 {len(blocks)}씬 · {len(NARR.replace(' ', '').replace(chr(10), ''))}자 임베드")
    # 인스타 캡션(해시태그 포함) — 앱에서 직접 올릴 때 붙여넣는 용도
    m = re.search(r'■ 인스타 캡션[^\n]*\n\n(.+?)\n═+',
                  SCRIPT.read_text(encoding="utf-8"), re.S)
    CAP = m.group(1).strip() if m else ""
    print(f"인스타 캡션 {len(CAP)}자 임베드" if CAP else "경고: 캡션 블록을 찾지 못했습니다")
else:
    print("경고: 스크립트 파일이 없어 나레이션·캡션 복사 버튼을 넣지 않습니다 —", SCRIPT)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def allbtn(kind, fn):
    return (f'<button class="allbtn" type="button" data-all="{kind}" '
            f'data-fn="{fn}" data-count="6">⬇ 6장 전체 저장</button>')


NARR_CHARS = len(NARR.replace(" ", "").replace("\n", ""))
NARR_SEC = round(NARR_CHARS / 5.5 + 0.6 * max(1, NARR.count("\n") + 1))
narrmeta = (f'{NARR.count(chr(10)) + 1}씬 · {NARR_CHARS}자 · 약 {NARR_SEC}초'
            if NARR else '스크립트 파일 없음')
narrbtn = ('<button class="allbtn" type="button" id="copyNarr">🎙 나레이션 전체 복사</button>'
           if NARR else '')
narrtext = esc(NARR)
capbtn = ('<button class="allbtn" type="button" id="copyCap">📋 캡션 · 해시태그 복사</button>'
          if CAP else '')
captext = esc(CAP)
capmeta = (f'{len(CAP)}자 · 해시태그 {CAP.count("#")}개' if CAP else '스크립트 파일 없음')

SECTION = f'''<div class="trace"></div>

<section id="insta" data-slug="{SLUG}" data-files="{','.join(NAMES)}">
  <h2>인스타(임장로그)용 이미지</h2>
  <p class="cards-hint">위 카드뉴스와 같은 내용을, 인스타 규격으로 다시 조판한 것입니다.
    채널명은 <b>임장로그</b>입니다. <b>캐러셀은 피드용, 릴스는 영상용</b>이라 비율이 다릅니다.
    전체 저장을 누르면 <b>원본 6장이 압축 없이</b> 저장됩니다. 안드로이드는 갤러리(다운로드 폴더),
    아이폰은 사진앱, PC는 zip입니다.</p>

  <div class="ilabel"><span class="t">캐러셀 · 4:5</span>
    <span class="s">1080 × 1350 · 피드에 카드 번호 순서(1→6)로</span>
    {allbtn("carousel", "carousel")}</div>
  <div class="iscroll car" data-folder="carousel" data-kind="캐러셀"></div>

  <div class="ilabel"><span class="t">인스타 캡션</span>
    <span class="s">{capmeta}</span>
    {capbtn}</div>
  <pre id="instacap" hidden>{captext}</pre>

  <div class="ilabel"><span class="t">릴스 · 9:16</span>
    <span class="s">1080 × 1920 · 하단 400px는 인스타 UI 자리</span>
    {allbtn("reels", "reels")}</div>
  <div class="iscroll reel" data-folder="reels" data-kind="릴스"></div>

  <div class="ilabel" style="margin-top:26px"><span class="t">나레이션 통스크립트</span>
    <span class="s">{narrmeta}</span>
    {narrbtn}</div>
  <pre id="narration" hidden>{narrtext}</pre>
  <p class="cards-hint" style="margin-top:10px">TTS(클로바더빙·VLLO)에 <b>한 번에 붙여넣는</b> 용도입니다.
    줄바꿈이 씬 경계입니다. 숫자는 TTS 오독을 막으려고 한글로 적었습니다.
    씬별 자막·초수와 인스타 캡션·해시태그는
    <a href="../publish/reels/{POST.stem}-script.txt" style="color:var(--teal)">전체 스크립트</a>에 있습니다.</p>
</section>

'''
_before = s
s = s.replace('<div class="trace"></div>\n\n<footer>', SECTION + "<footer>", 1)
# 앵커가 안 맞으면 str.replace 는 조용히 아무것도 하지 않는다 — 그대로 두면
# "added" 만 찍히고 섹션이 빠진 채 배포된다(2026-08-27 실제 발생).
assert s != _before, ('삽입 지점을 찾지 못했습니다 — </article> 뒤에 '
                      '구분선 div(class="trace")와 <footer>가 이어져 있어야 합니다')

# 블로그 카드 갤러리에도 전체 저장 버튼 (현재 테마의 6장)
s = s.replace(
    '<p class="cards-hint">옆으로 넘기며 핵심만. 이미지를 저장해 활용하셔도 좋습니다.</p>',
    '<p class="cards-hint">옆으로 넘기며 핵심만. 이미지를 저장해 활용하셔도 좋습니다.</p>\n'
    '  <div class="ilabel"><span class="s">현재 테마의 카드 6장</span>'
    + allbtn("theme", "cards") + '</div>')

# ── JS: 인스타 이미지 생성 + 전체 저장 ─────────────────────────────
JS = r"""  /* ── 인스타 이미지 생성 (HTML에 img 태그를 남기지 않는다:
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
    /* insta.html(고정 주소)에서 #insta 로 들어오면 앵커 점프가 이미지 생성 전에
       끝나 글 맨 위에 떨어진다 → 생성 후 다시 맞춘다(레이아웃 안정까지 한 번 더). */
    if(location.hash==='#insta'){
      var go=function(){sec.scrollIntoView();};
      requestAnimationFrame(go);
      setTimeout(go,350);
    }
  })();

  /* ── 전체 저장 ────────────────────────────────────────────
     폰: 공유 시트로 원본 그대로 (압축 없음)
     PC: 무압축 zip을 직접 만들어 내려받기 (외부 라이브러리 없음) */
  var UA=navigator.userAgent;
  var IOS=/iPad|iPhone|iPod/.test(UA)||(/Macintosh/.test(UA)&&navigator.maxTouchPoints>1);
  var ANDROID=/Android/.test(UA);
  var CAN_SHARE=(function(){
    try{
      if(!(navigator.share&&navigator.canShare&&window.File))return false;
      return navigator.canShare({files:[new File([new Uint8Array([137,80,78,71])],
        'probe.png',{type:'image/png'})]});
    }catch(e){return false;}
  })();
  /* 저장 경로 선택
     iOS  : 공유 시트만 사진앱에 닿는다 (a[download]는 Photos로 못 간다)
     안드로이드: 공유 시트에 '갤러리 저장'이 없는 기기가 많다 → 순차 다운로드
                (다운로드 폴더에 떨어지고 갤러리에서 바로 보인다)
     PC   : 무압축 zip */
  var MODE=(IOS&&CAN_SHARE)?'share':(ANDROID?'files':'zip');

  var CRCT=(function(){
    var t=new Uint32Array(256),n,c,k;
    for(n=0;n<256;n++){c=n;for(k=0;k<8;k++){c=(c&1)?(0xEDB88320^(c>>>1)):(c>>>1);}t[n]=c>>>0;}
    return t;
  })();
  function crc32(u8){
    var c=0xFFFFFFFF,i;
    for(i=0;i<u8.length;i++){c=CRCT[(c^u8[i])&0xFF]^(c>>>8);}
    return (c^0xFFFFFFFF)>>>0;
  }
  function zipStore(items){
    var enc=new TextEncoder(),local=[],central=[],off=0;
    items.forEach(function(f){
      var nm=enc.encode(f.name),crc=crc32(f.data),sz=f.data.length;
      var lh=new DataView(new ArrayBuffer(30));
      lh.setUint32(0,0x04034b50,true);lh.setUint16(4,20,true);lh.setUint16(6,0x0800,true);
      lh.setUint32(14,crc,true);lh.setUint32(18,sz,true);lh.setUint32(22,sz,true);
      lh.setUint16(26,nm.length,true);
      local.push(new Uint8Array(lh.buffer),nm,f.data);
      var cd=new DataView(new ArrayBuffer(46));
      cd.setUint32(0,0x02014b50,true);cd.setUint16(4,20,true);cd.setUint16(6,20,true);
      cd.setUint16(8,0x0800,true);
      cd.setUint32(16,crc,true);cd.setUint32(20,sz,true);cd.setUint32(24,sz,true);
      cd.setUint16(28,nm.length,true);cd.setUint32(42,off,true);
      central.push(new Uint8Array(cd.buffer),nm);
      off+=30+nm.length+sz;
    });
    var cdSize=central.reduce(function(a,b){return a+b.length;},0);
    var eo=new DataView(new ArrayBuffer(22));
    eo.setUint32(0,0x06054b50,true);
    eo.setUint16(8,items.length,true);eo.setUint16(10,items.length,true);
    eo.setUint32(12,cdSize,true);eo.setUint32(16,off,true);
    return new Blob(local.concat(central,[new Uint8Array(eo.buffer)]),{type:'application/zip'});
  }
  function filesDown(items){
    /* 안드로이드: 개별 원본을 순차로 내려받는다 (첫 파일 뒤 '여러 파일 다운로드' 확인이 한 번 뜰 수 있음) */
    items.forEach(function(f,i){
      setTimeout(function(){
        var url=URL.createObjectURL(f.blob);
        var a=document.createElement('a');a.href=url;a.download=f.name;
        document.body.appendChild(a);a.click();a.remove();
        setTimeout(function(){URL.revokeObjectURL(url);},4000);
      }, i*350);
    });
    say(items.length+'장을 내려받습니다. 갤러리/다운로드에서 확인하세요 ✓');
  }
  function zipDown(items,btn){
    var sec=document.getElementById('insta');
    var fn=(sec?sec.dataset.slug:'cards')+'-'+(btn.dataset.fn||'images')+'-'+items.length+'.zip';
    var url=URL.createObjectURL(zipStore(items));
    var a=document.createElement('a');a.href=url;a.download=fn;
    document.body.appendChild(a);a.click();a.remove();
    setTimeout(function(){URL.revokeObjectURL(url);},5000);
    say(items.length+'장을 zip으로 저장했습니다 ✓');
  }
  function saveAll(btn){
    var kind=btn.dataset.all,imgs;
    if(kind==='theme'){
      imgs=[].slice.call(document.querySelectorAll('#cards img.card-art'));
    }else{
      imgs=[].slice.call(document.querySelectorAll(
        '#insta .iscroll[data-folder="'+kind+'"] img'));
    }
    if(!imgs.length){say('이미지를 찾지 못했습니다');return;}
    var old=btn.textContent;
    btn.disabled=true;btn.textContent='모으는 중…';
    Promise.all(imgs.map(function(im,i){
      return fetch(im.src).then(function(r){
        if(!r.ok)throw new Error('HTTP '+r.status);
        return r.blob();
      }).then(function(b){
        return b.arrayBuffer().then(function(ab){
          return {name:im.dataset.file||('image'+(i+1)+'.png'),
                  data:new Uint8Array(ab),blob:b};
        });
      });
    })).then(function(items){
      var fl=items.map(function(f){
        return new File([f.blob],f.name,{type:'image/png'});
      });
      if(MODE==='share'&&navigator.canShare({files:fl})){
        return navigator.share({files:fl,title:document.title}).then(function(){
          say("공유 시트에서 '이미지 저장'을 누르세요 ✓");
        },function(e){
          if(e&&e.name==='AbortError')return;   /* 사용자가 취소한 경우 */
          filesDown(items);                     /* 공유가 실패하면 개별 저장 */
        });
      }
      if(MODE==='files'){filesDown(items);return;}
      zipDown(items,btn);
    }).catch(function(){
      say('전체 저장에 실패했습니다. 이미지를 하나씩 저장해 주세요');
    }).then(function(){
      btn.disabled=false;btn.textContent=old;
    });
  }
  var narrBtn=document.getElementById('copyNarr');
  if(narrBtn){
    narrBtn.addEventListener('click',function(e){
      e.preventDefault();
      var el=document.getElementById('narration');
      copyText(el?el.textContent.trim():'', '나레이션 통스크립트가 복사됐습니다 ✓');
    });
  }
  var capBtn=document.getElementById('copyCap');
  if(capBtn){
    capBtn.addEventListener('click',function(e){
      e.preventDefault();
      var el=document.getElementById('instacap');
      copyText(el?el.textContent.trim():'', '캡션과 해시태그가 복사됐습니다 ✓');
    });
  }
  document.querySelectorAll('.allbtn:not(#copyNarr):not(#copyCap)').forEach(function(b){
    var n=b.dataset.count||'6';
    b.textContent='⬇ '+n+'장 '+(MODE==='share'?'사진앱에 저장'
                                :MODE==='files'?'갤러리에 저장':'zip으로');
    b.title=MODE==='share'?"공유 시트에서 '이미지 저장'을 누르면 사진앱에 들어갑니다"
           :MODE==='files'?'원본 6장을 순차로 내려받습니다 (다운로드 폴더 → 갤러리)'
           :'무압축 zip으로 내려받습니다';
    b.addEventListener('click',function(e){e.preventDefault();saveAll(b);});
  });

  function downloadImg(img){"""
assert "  function downloadImg(img){" in s
if not HAS_JS:
    s = s.replace("  function downloadImg(img){", JS, 1)

# 버튼 배선에 인스타 이미지 포함 (테마 전환 대상에는 넣지 않는다)
s = s.replace(
    "document.querySelectorAll('img.card-art').forEach(function(img){\n"
    "    var wrap=document.createElement('div');wrap.className='imgwrap';",
    "document.querySelectorAll('img.card-art,img.insta-art').forEach(function(img){\n"
    "    var wrap=document.createElement('div');wrap.className='imgwrap';")

POST.write_text(s, encoding="utf-8")
print("added #insta + 전체 저장 버튼:", NAMES)
