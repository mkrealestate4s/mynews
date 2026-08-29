# -*- coding: utf-8 -*-
"""Generate theme variants of the graph-centric card news set."""
import pathlib

BASE = pathlib.Path(__file__).parent

THEMES = {
    "report": dict(
        bg="#0D1829", panel="#132239", ink="#F2F6FA", mute="#96A5BA",
        accent="#5EE6D0", accent2="#7C8CF8", line="#2C3E5A", rail="#0f1c30",
        fillgray="#2C3E5A", onfill="#0D1829", body="#DCE5EF",
        head="'Noto Serif KR',serif", headspace="0", headink="gtx",
    ),
    "white": dict(
        bg="#ffffff", panel="#f5f5f7", ink="#1d1d1f", mute="#6e6e73",
        accent="#0071e3", accent2="#0071e3", line="#e5e5ea", rail="#eeeef0",
        fillgray="#c7c7cc", onfill="#ffffff", body="#3a3a3c",
        head="'Noto Sans KR',sans-serif", headspace="-0.02em", headink="ink",
    ),
    "editorial": dict(
        bg="#F7F2E9", panel="#FFFDF8", ink="#2B2118", mute="#8A7B6C",
        accent="#C24D2C", accent2="#8A5A2B", line="#E4D9C6", rail="#EFE7D8",
        fillgray="#D2BC94", onfill="#FFFDF8", body="#4A3D2F",
        head="'Noto Serif KR',serif", headspace="0", headink="gtx",
    ),
}

# 인스타(임장로그) 전용 테마. 블로그 3테마와 분리해서 관리한다.
# 1:1로 만든 뒤 make_reels.py(9:16) / make_carousel.py(4:5)로 재조판해 쓴다.
#
# 팔레트에 'css' 키를 두면 그 테마에만 붙는 오버라이드가 된다(숫자체·곡률·격자 등).
# 'css' 는 HEAD_TPL 에 넘기지 않는다 — _NON_TPL 에서 걸러진다.
#
# 인스타 후보 테마(insta-*)는 검토용이다. 하나를 고르면 그 팔레트를 'insta' 로
# 옮기고 후보들은 삭제한다 — 매일 렌더에서 도는 인스타 테마는 언제나 한 종이다.

# 고정폭 숫자 + 곡률 0 + 플롯 영역 격자 (데이터 성격을 강조하는 계열)
_MONO_CSS = """
body{font-family:'IBM Plex Sans KR',sans-serif}
.eyebrow{font-family:'IBM Plex Mono',monospace;letter-spacing:.24em}
.pnum{font-family:'IBM Plex Mono',monospace}
.col .v,.zcol .zv,.hbar .lb .v,.duo .dv,.bignum,.tl .r .d,.statrow .big{
  font-family:'IBM Plex Mono',monospace;font-weight:700}
.panel,.colwrap,.zwrap,.duo .box,.fbox,.tl,.badge,.sched,
.hbar .railx,.hbar .fillx,.col .barv,.zcol .zbar,.cols,.zcols{border-radius:0}
/* 격자는 플롯 영역 안에만 — 축 라벨 뒤로 넘기지 않는다 */
.cols,.zcols{background-image:repeating-linear-gradient(
  to right,transparent 0 63px,var(--line) 63px 64px)}
"""


def _round(rad, body_font=None, extra=""):
    """곡률·본문 서체만 바꾸는 가벼운 오버라이드."""
    css = f"""
.panel,.colwrap,.zwrap,.duo .box,.fbox,.tl,.badge,.sched{{border-radius:{rad}}}
.hbar .railx,.hbar .fillx{{border-radius:{rad}}}
"""
    if body_font:
        css += f"body{{font-family:{body_font}}}\n"
    return css + extra


INSTA = {
    # ── 운영 테마 ──────────────────────────────────────────────────
    # '아이보리 명조' — 2026-08-29 어두운 판에서 밝은 판으로 전환(후보 A 채택).
    # 따뜻한 종이색 바탕 + 흰 패널 + 테라코타. 제목은 고운바탕(명조).
    # 테라코타(#C2542B)는 이 바탕에서 대비 5.4:1 — 큰 숫자뿐 아니라 강조 문구에도 쓸 수 있다.
    "insta": dict(
        bg="#FBF7F0", panel="#FFFFFF", ink="#191512", mute="#7C7065",
        accent="#C2542B", accent2="#C2542B", line="#E5DCCE", rail="#F1EADD",
        fillgray="#D8CDBA", onfill="#FFFFFF", body="#4A4038",
        head="'Gowun Batang',serif", headspace="0", headink="ink",
        css=_round("6px", "'IBM Plex Sans KR',sans-serif",
                   # 0선은 --line(연한 베이지)으로는 흰 패널에서 사라진다.
                   # 위/아래가 곧 의미인 차트라 기준선은 눈에 보여야 한다.
                   ".zcols::before{background:rgba(25,21,18,.40)}"),
    ),

    # ── 후보 테마 (검토용 · 결정되면 지운다) ────────────────────────
    # 이전 운영 테마 '터미널 데이터' — 되돌릴 때 쓴다.
    "insta-dark": dict(
        bg="#0B0B0C", panel="#131316", ink="#EDEDEF", mute="#8A8A93",
        accent="#FFB020", accent2="#FFB020", line="#26262C", rail="#0F0F11",
        fillgray="#2A2A31", onfill="#0B0B0C", body="#D6D6DB",
        head="'IBM Plex Sans KR',sans-serif", headspace="-0.01em", headink="ink",
        css=_MONO_CSS,
    ),
    # A. 아이보리 명조 → 채택되어 'insta' 로 옮겼다(위).
    # D. 앰버 포스터 — 브랜드 앰버를 밝은 판으로. 직각·굵은 활자, 피드에서 가장 세다.
    "insta-amber": dict(
        bg="#FFFFFF", panel="#FFF7E7", ink="#141210", mute="#6E655A",
        accent="#D97706", accent2="#F59E0B", line="#EBD8B4", rail="#F6EBD8",
        fillgray="#E4D2B2", onfill="#FFFFFF", body="#413A31",
        head="'Gothic A1',sans-serif", headspace="-0.035em", headink="ink",
        css=_round("0", "'Noto Sans KR',sans-serif",
                   ".top{padding-bottom:18px;border-bottom:3px solid var(--ink)}"
                   ".trace{height:3px;background:var(--ink)}"
                   ".zcols::before{background:rgba(20,18,16,.42)}"),
    ),
    # B. 민트 리포트 — 흰 바탕 + 민트 블록. 테두리 없이 면으로만 구분.
    "insta-mint": dict(
        bg="#FFFFFF", panel="#EDF7F4", ink="#0D2B26", mute="#5F8480",
        accent="#0B8C79", accent2="#0B8C79", line="#D3E9E4", rail="#E4F2EF",
        fillgray="#B4D9D2", onfill="#FFFFFF", body="#33544F",
        head="'Gothic A1',sans-serif", headspace="-0.025em", headink="ink",
        css=_round("20px", "'Noto Sans KR',sans-serif",
                   ".panel,.duo .box,.fbox,.zwrap,.colwrap{border-color:transparent}"),
    ),
    # C. 블루프린트 — 지금 테마의 밝은 판. 고정폭 숫자·격자·직각을 그대로 유지.
    "insta-blueprint": dict(
        bg="#F2F5FA", panel="#FFFFFF", ink="#0E2340", mute="#6B7C93",
        accent="#1A5FD6", accent2="#1A5FD6", line="#D5DEEB", rail="#E8EDF5",
        fillgray="#B9C7DA", onfill="#FFFFFF", body="#38495E",
        head="'IBM Plex Sans KR',sans-serif", headspace="-0.01em", headink="ink",
        css=_MONO_CSS,
    ),
    # E. 코랄 소프트 — 복숭아 바탕 + 흰 카드에 옅은 그림자. 가장 부드럽다.
    "insta-coral": dict(
        bg="#FFF5F2", panel="#FFFFFF", ink="#2A1A16", mute="#8A736C",
        accent="#E8452B", accent2="#FF8A5B", line="#F5DED6", rail="#FBE9E3",
        fillgray="#F7C9BB", onfill="#FFFFFF", body="#55423C",
        head="'Gothic A1',sans-serif", headspace="-0.02em", headink="ink",
        css=_round("28px", "'Noto Sans KR',sans-serif",
                   ".panel,.duo .box,.fbox,.zwrap,.colwrap{border-color:transparent;"
                   "box-shadow:0 6px 22px rgba(180,80,55,.10)}"),
    ),
}

# HEAD_TPL 의 서식 인자가 아닌 팔레트 키 — format() 에 넘기면 KeyError 가 아니라
# 조용히 무시되므로(**kwargs) 오타를 못 잡는다. 명시적으로 걸러 둔다.
_NON_TPL = {"headink", "css"}

# 인스타 아이브로 — 블로그는 월별 리포트 표기, 인스타는 채널 고정 문구를 쓴다
EYEBROW_INSTA = "임장로그 부동산 뉴스"

BRAND = {
    "report": "부동산 인사이트 · 데일리 키워드 리포트",
    "white": "부동산 인사이트 · 데일리 키워드 리포트",
    "editorial": "부동산 인사이트 · 데일리 키워드 리포트",
    "insta": "매일 아침, 부동산 데이터 한 장",   # 아이브로가 채널명을 달고 있어 중복 회피
}

HEAD_TPL = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8">
<link href="gf-local.css" rel="stylesheet">
<link href="gf2-local.css" rel="stylesheet">
<style>
:root{{--bg:{bg};--panel:{panel};--ink:{ink};--mute:{mute};
  --accent:{accent};--accent2:{accent2};--line:{line};--rail:{rail};
  --onfill:{onfill};--body:{body};--fillgray:{fillgray};
  --grad:linear-gradient(92deg,{accent},{accent2})}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1080px;overflow:hidden}}
body{{background:var(--bg);color:var(--ink);font-family:'Noto Sans KR',sans-serif;
  display:flex;flex-direction:column;position:relative;
  padding:84px 96px 170px;line-height:1.6}}
.mid{{min-height:0;overflow:hidden;flex:1;display:flex;flex-direction:column;justify-content:center}}
.serif{{font-family:{head};letter-spacing:{headspace}}}
.gtx{{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}}
.eyebrow{{color:var(--accent);font-weight:700;letter-spacing:.16em;font-size:26px}}
.top{{display:flex;justify-content:space-between;align-items:baseline;flex:none}}
.pnum{{color:var(--mute);font-size:26px;letter-spacing:.1em}}
.foot{{color:var(--mute);font-size:22px;line-height:1.3;display:flex;justify-content:space-between;align-items:center}}
.footwrap{{position:absolute;left:96px;right:96px;bottom:56px;height:70px}}
.trace{{height:2px;background:var(--line);position:relative;margin-bottom:28px}}
.trace::after{{content:"";position:absolute;right:0;top:50%;width:20px;height:20px;
  transform:translateY(-50%);border:4px solid var(--accent);border-radius:50%;background:var(--bg)}}
h1{{font-weight:900;line-height:1.12}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:22px;padding:40px 44px}}
/* horizontal bar */
.hbar{{margin-bottom:30px}}
.hbar .lb{{font-size:29px;font-weight:700;margin-bottom:10px;display:flex;justify-content:space-between;align-items:baseline}}
.hbar .lb .v{{font-weight:900;font-size:30px}}
.hbar .railx{{background:var(--rail);border-radius:12px;height:56px;position:relative}}
.hbar .fillx{{height:100%;border-radius:12px;background:var(--grad)}}
.hbar .fillx.gray{{background:var(--fillgray)}}
{extra}</style></head><body>
"""
FOOT = "</body></html>"

INK_OVERRIDE = ('.serif.gtx{-webkit-text-fill-color:var(--ink);background:none;color:var(--ink)}'
                '.fbox .n.gtx,.col .v.gtx,.hbar .v.gtx,.duo .dv.gtx,.bignum.gtx,'
                '.zcol .zv.gtx,.statrow .big.gtx{-webkit-text-fill-color:var(--accent);'
                'background:none;color:var(--accent)}')

_FIT_TPL = """
<script>
/* 세로 프레임(9:16 · 4:5) 자동 맞춤 — 1:1 기준 활자를 프레임 높이에 맞춰 확대한다.
   1:1 카드는 .mid 를 꽉 채우지만 세로로 늘린 프레임에서는 같은 활자가 가운데
   좁은 띠에만 모여 "눌린" 느낌이 된다. .mid 에 zoom 을 걸고 폭을 그만큼 줄여
   되레이아웃하면 글자·그래프가 함께 커진다.
   가로로 넘치는 경우(.duo 처럼 nowrap 패널이 나란히 선 카드)는 배율을 되돌린다. */
(function(){
  var m=document.querySelector('.mid'); if(!m) return;
  var kids=[].slice.call(m.children); if(!kids.length) return;
  function ink(z){
    var t=1e9,b=-1e9;
    kids.forEach(function(e){var r=e.getBoundingClientRect();
      if(r.height){t=Math.min(t,r.top);b=Math.max(b,r.bottom);}});
    return b>t?(b-t)/z:0;
  }
  function fit(){
    m.style.zoom='';m.style.width='';                  // 여러 번 불려도 같은 결과
    var cs=getComputedStyle(m);
    var pad=parseFloat(cs.paddingTop)+parseFloat(cs.paddingBottom);
    var rc=m.getBoundingClientRect(), box=rc.height, W=rc.width, z=1;
    function set(v){z=v;m.style.zoom=v;m.style.width=(W/v)+'px';}
    for(var i=0;i<12;i++){
      var h=ink(z); if(!h) return;
      var nz=Math.min(%(max)s,Math.max(1,box*%(fill)s/(h+pad)));
      if(Math.abs(nz-z)<0.004) break;
      set(nz);
    }
    for(var j=0;j<30 && m.scrollWidth>m.clientWidth+1 && z>1.01;j++) set(Math.max(1,z-0.02));
    m.dataset.fit=z.toFixed(3);
  }
  fit();
  document.fonts.ready.then(fit);                      // 폰트 로드 후 재측정
  window.addEventListener('load',fit);
})();
</script>
"""


def fit_script(fill=0.97, maxz=1.45):
    """세로 프레임용 자동 확대 스크립트. </body> 앞에 넣는다."""
    return _FIT_TPL % {"fill": fill, "max": maxz}


# 세로 프레임(9:16 · 4:5) 공통 오버라이드. make_reels / make_carousel 양쪽이 쓴다.
VFRAME_CSS = """
/* 나란히 선 nowrap 패널은 세로 프레임에서 폭을 잡아먹어 확대를 막는다 → 위아래로 */
.duo{flex-direction:column;gap:18px}
/* 제목은 줄바꿈을 금지한다. zoom 은 활자만 키우고 줄 폭은 그만큼 좁히므로,
   1:1 에서 한 줄에 겨우 들어가던 제목이 확대되면 마지막 글자만 다음 줄로
   떨어진다("… 없 / 다"). nowrap 으로 두면 가로 오버플로가 되어 fit_script 의
   배율 되돌리기가 작동해 저절로 두 줄 안에 들어맞는다.
   저자가 넣은 <br> 은 그대로 지켜진다. */
h1{white-space:nowrap}
"""


def render(slug, cards, extra_css="", outbase=None, themes=None, eyebrow=None):
    """카드 dict을 테마별로 렌더한다.

    themes=None  → 매일 쓰는 4종: 블로그 3테마 + 운영 인스타 테마('insta')
                   후보 테마(insta-*)는 이름을 직접 넘겨야 렌더된다.

    본문 토큰 (테마별로 치환된다):
      {{BRAND}}   블로그=부동산 인사이트 · 데일리 키워드 리포트 / 인스타=매일 아침, 부동산 데이터 한 장
      {{EYEBROW}} 블로그=eyebrow 인자 값 (예: "2026 · 8월 부동산 키워드 리포트") / 인스타=임장로그 부동산 뉴스
    """
    if any("{{EYEBROW}}" in b for b in cards.values()) and not eyebrow:
        raise ValueError("본문에 {{EYEBROW}} 가 있으면 eyebrow= 로 블로그용 문구를 넘겨야 합니다")
    base_dir = pathlib.Path(outbase) if outbase else BASE
    every = dict(THEMES, **INSTA)
    pool = ({**THEMES, "insta": INSTA["insta"]} if themes is None
            else {k: every[k] for k in themes})
    for theme, pal in pool.items():
        outdir = base_dir / theme
        outdir.mkdir(exist_ok=True)
        for css_name, font_dir in (("gf-local.css", "fonts"), ("gf2-local.css", "fonts2")):
            src = base_dir / css_name
            if src.exists():
                (outdir / css_name).write_text(
                    src.read_text().replace(f"url({font_dir}/", f"url(../{font_dir}/"))
        extra = extra_css
        if pal.get("headink") == "ink":
            extra += INK_OVERRIDE
        extra += pal.get("css", "")   # 테마별 오버라이드는 항상 마지막에
        head = HEAD_TPL.format(
            extra=extra, **{k: v for k, v in pal.items() if k not in _NON_TPL})
        # 후보 테마(insta-*)도 인스타 채널이다 — 브랜드·아이브로를 함께 따라가게 한다
        insta = theme in INSTA
        brand = BRAND["insta"] if insta else BRAND["report"]
        eb = EYEBROW_INSTA if insta else (eyebrow or "")
        for name, body in cards.items():
            body = body.replace("{{BRAND}}", brand).replace("{{EYEBROW}}", eb)
            (outdir / f"{slug}-{name}.html").write_text(head + body + FOOT, encoding="utf-8")
        print("wrote", theme)

def top(pnum):
    return ('<div class="top"><div class="eyebrow">2026 · 7월 부동산 키워드 리포트</div>'
            f'<div class="pnum">{pnum} / 05</div></div>')

def foot():
    return ('<div class="footwrap"><div class="trace"></div><div class="foot">'
            '<span>부동산 인사이트 · 데일리 키워드 리포트</span>'
            '<span>데이터 기준일 2026-07-17</span></div></div>')

def hbar(label, value, pct, gray=False):
    return (f'<div class="hbar"><div class="lb"><span>{label}</span>'
            f'<span class="v {"" if gray else "gtx"}">{value}</span></div>'
            f'<div class="railx"><div class="fillx{" gray" if gray else ""}" style="width:{pct}%"></div></div></div>')

def cards():
    c = {}
    c["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:34px;color:var(--mute);font-weight:500">요즘 청약 시장을 흔드는 세 글자</div>
  <h1 class="serif gtx" style="font-size:200px;margin:14px 0 30px">반세권</h1>
  <div style="display:flex;gap:12px;align-items:flex-end;height:120px;margin-bottom:30px">
    <div style="width:120px;height:34%;border-radius:10px 10px 0 0;background:var(--fillgray)"></div>
    <div style="width:120px;height:52%;border-radius:10px 10px 0 0;background:var(--fillgray)"></div>
    <div style="width:120px;height:74%;border-radius:10px 10px 0 0;background:var(--grad)"></div>
    <div style="width:120px;height:100%;border-radius:10px 10px 0 0;background:var(--grad)"></div>
    <div style="margin-left:18px;font-size:30px;color:var(--mute);align-self:flex-end;line-height:1.4;padding-bottom:2px">검색 관심도<br>급상승 중</div>
  </div>
  <div style="font-size:36px;color:var(--ink);font-weight:500">
    뜻 · 데이터 · 체크포인트, <span class="gtx" style="font-weight:700">그래프로 빠르게</span></div>
</div>""" + foot()

    c["02-meaning"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:60px;margin-bottom:40px">반세권이란?</h1>
  <div class="panel" style="text-align:center;padding:52px 44px;margin-bottom:40px">
    <div class="serif gtx" style="font-size:84px;font-weight:900">반도체 × 역세권</div>
    <div style="font-size:33px;color:var(--mute);margin-top:16px">반도체 산업단지 인근 주거 지역을 뜻하는 신조어</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-bottom:28px">
    대규모 반도체 시설이 들어서면 <strong>고소득 일자리·인구 유입·교통망 확충</strong>이
    함께 따라와 주거 수요가 몰린다는 논리입니다.</div>
  <div style="font-size:27px;color:var(--mute);margin-bottom:14px">대표 지역 · 반도체 벨트</div>
  <div style="display:flex;gap:14px">""" + "".join(
        f'<span style="border:1px solid var(--line);background:var(--panel);border-radius:999px;'
        f'padding:10px 28px;font-size:29px;font-weight:700">{r}</span>'
        for r in ["용인", "화성", "평택", "수원", "이천"]) + """
  </div>
</div>""" + foot()

    c["03-whynow"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:56px;margin-bottom:8px">7월, 물량이 말해준다</h1>
  <div style="font-size:29px;color:var(--mute);margin-bottom:40px">하반기 첫 분양 성수기 공급 규모 (가구)</div>
""" + hbar("전국 분양", "약 30,000", 100, gray=True) \
    + hbar("수도권", "약 20,000", 67, gray=True) \
    + hbar("반세권 물량", "8,256", 27.5) \
    + hbar("고덕국제신도시 5개 단지", "5,527", 18.4) + """
  <div style="font-size:29px;color:var(--body);margin-top:8px">
    삼성전자 평택캠퍼스 옆 고덕에만 <strong>반세권 물량의 3분의 2</strong>가 집중.</div>
</div>""" + foot()

    c["04-data"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:56px;margin-bottom:8px">데이터로 본 청약 양극화</h1>
  <div style="font-size:29px;color:var(--mute);margin-bottom:40px">2026 상반기 1순위 평균 청약 경쟁률</div>
""" + hbar("10대 건설사 브랜드 단지", "9.76 : 1", 100) \
    + hbar("그 외 건설사 단지", "2.17 : 1", 22, gray=True) + """
  <div class="serif gtx" style="font-size:96px;font-weight:900;line-height:1;margin-top:26px">4.5배</div>
  <div style="font-size:31px;color:var(--body);margin-top:12px">격차. 같은 반세권이어도 <strong>브랜드 단지에만</strong> 수요가 몰립니다.</div>
</div>""" + foot()

    c["05-check"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:54px;margin-bottom:30px">청약 전 체크포인트 3</h1>
  <div style="display:flex;flex-direction:column;gap:20px">""" + "".join(
        f'<div class="panel" style="display:flex;gap:30px;align-items:flex-start;padding:28px 36px">'
        f'<div class="serif gtx" style="font-size:48px;font-weight:900;line-height:1.1">0{i}</div>'
        f'<div><div style="font-size:33px;font-weight:700;margin-bottom:6px">{t}</div>'
        f'<div style="font-size:26px;color:var(--mute)">{d}</div></div></div>'
        for i, (t, d) in enumerate([
            ("반도체 업황 리스크", "집값은 반도체 경기와 동행. 2023~2025 불황기 평택은 2년 연속 하락"),
            ("브랜드·입지 확인", "1순위 자격은 한 번뿐. 브랜드·입지·분양가를 냉정하게 비교"),
            ("입주 물량·교통망 시점", "클러스터·광역 교통망 완공은 수년 뒤다. 실제 개통 시기를 확인"),
        ], start=1)) + """
  </div>
  <div style="font-size:23px;color:var(--mute);margin-top:26px">※ 시장 정보 제공 목적이며 특정 단지의 청약·투자를 권유하지 않습니다.</div>
</div>""" + foot()
    return c

if __name__ == "__main__":
    for theme, pal in THEMES.items():
        outdir = BASE / theme
        outdir.mkdir(exist_ok=True)
        extra = ('.serif.gtx{-webkit-text-fill-color:var(--ink);background:none;color:var(--ink)}' if pal['headink']=='ink' else '')
        head = HEAD_TPL.format(extra=extra, **pal)
        for name, body in cards().items():
            (outdir / f"{name}.html").write_text(head + body + FOOT, encoding="utf-8")
        # each theme dir needs the font css path one level up
        css = (BASE / "gf-local.css").read_text().replace("url(fonts/", "url(../fonts/")
        (outdir / "gf-local.css").write_text(css)
        print("wrote", theme)
