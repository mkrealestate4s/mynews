# -*- coding: utf-8 -*-
"""리포트 #112 (2026-11-01) 목동9단지 재건축 시공사 입찰 현장설명회 D-1. #111을 복제해 교체한다.

메인 검색어: 목동9단지 재건축

수치와 검산
  사건일과 오늘의 간격: 입찰공고 10/23(9일 전, 배경) · 참가신청 마감 10/31(어제) · 현장설명회 11/2(내일, 리드).
  목동9단지 (MTN 10/23 · 헤럴드경제 · 아루뉴스 · 비즈니스포스트 보도):
    예정 공사비 2조6,067억원(부가세 제외) · 3.3㎡당 980만원 · 지하4~지상49층 3,961세대
    입찰보증금 800억원(현금 500억 + 이행보증증권 300억) · 공동도급 불허 · 사업시행자 한국자산신탁
    참가신청 10/31 · 현설 11/2 · 입찰 마감 2027-01-11 · 2027년 1분기 선정 목표 · 삼성물산·GS건설 관심(관측)
  목동 시공사 현황 (뉴시스 10/20 · 서울경제TV 10/28): 6단지 DL이앤씨 · 10단지 현대건설 확정,
    8 대우 · 12 GS · 13 삼성 우협. 5곳 공사비 합 9조1,773억, 모두 단독 응찰. 4단지 입찰 마감 11/16.
  계획 가구수 (#98 · 뉴시스): 14단지 5,123 · 10 4,248 · 9 3,961 · 13 3,852 · 12 2,810 · 4 2,436 · 6 2,184 · 8 1,881
    대시보드 세로 (5,123 → 86%): 71.3 · 66.5 · 64.7 · 47.2 · 40.9
  3.3㎡당 공사비(만원, #98): 4단지 1,010 · 10 990 · 9 980 · 12 980 · 13 980 · 8 965
    가로 (1,010 → 100): 98.0 · 97.0 · 97.0 · 97.0 · 95.5
  보증금 비중: 800/26,067 = 3.07% → 공사비의 약 3%

단정하지 않은 것
  · 3,961세대·49층은 계획(확정 전) · 삼성물산·GS건설은 관측, 현설 참석은 입찰 아님
  · 조합원 지위 양도 제한은 단계마다 다름 → 사업시행자·정비사업 정보몽땅 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-31-newland6.html"
DST = ROOT / "posts/2026-11-01-mokdong9.html"
SLUG, PRE = "2026-11-01-mokdong9", "mk9"
NO, DATE = 112, "2026-11-01"
PREV_SLUG = "nl1031-"
BANNED = ["신규택지", "김포 아라", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "목동9단지 재건축 내일 현설, 공사비 2.6조"
DESC = ("목동9단지 재건축 시공사 입찰 현장설명회가 11월 2일 열립니다. 예정 공사비 2조6,067억원, 3.3㎡당 980만원, "
        "최고 49층 3,961세대 계획입니다. 입찰 마감은 2027년 1월 11일이고 공동도급은 허용하지 않습니다. "
        "목동은 시공사가 정해진 5곳이 모두 단독 응찰이었습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="입찰보증금 800억원, 컨소시엄 불가, 입찰 마감 2027년 1월 11일. 목동 첫 경쟁입찰이 될지, 단지별 시공사 현황과 함께 정리했습니다.">
<meta property="og:type" content="article">
<meta property="og:image" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:url" content="{URL}">
<link rel="canonical" href="{URL}">
<link rel="alternate" type="application/rss+xml" title="부동산 인사이트 RSS" href="../feed.xml">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"NewsArticle",
 "headline":"{TITLE}",
 "description":"{DESC}",
 "image":"{OG}",
 "datePublished":"{DATE}","dateModified":"{DATE}",
 "author":{{"@type":"Organization","name":"부동산 인사이트"}},
 "publisher":{{"@type":"Organization","name":"부동산 인사이트"}},
 "mainEntityOfPage":"{URL}","inLanguage":"ko"}}
</script>'''

HEADER = f'''<header>
  <div class="eyebrow">2026 · 11월 부동산 키워드 리포트 #{NO}</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">목동9단지 재건축<br>내일 현설, 공사비 2.6조</h1>
  <p class="sub"><strong>목동9단지 재건축</strong> 시공사 입찰 현장설명회가 <strong>내일(11월 2일)</strong> 열립니다. 예정 공사비는 <strong>2조6,067억원</strong>, 3.3㎡당 980만원이고 최고 49층 3,961세대 계획입니다. 입찰 마감은 <strong>2027년 1월 11일</strong>입니다. <span class="mark">목동은 지금까지 시공사가 정해진 5곳이 모두 단독 응찰이었습니다. 9단지가 첫 경쟁이 될지가 관전 포인트입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 목동9단지</div><div class="kw">11월 2일</div>
      <p>시공사 입찰 <strong>현장설명회</strong>.</p></div>
    <div class="kcard"><div class="hot">예정 공사비</div><div class="kw">2조6,067억</div>
      <p>3.3㎡당 <strong>980만원</strong>.</p></div>
    <div class="kcard"><div class="hot">계획 규모</div><div class="kw">3,961세대</div>
      <p>최고 <strong>49층</strong>, 확정 전.</p></div>
    <div class="kcard"><div class="hot">입찰 마감</div><div class="kw">1월 11일</div>
      <p>2027년. <strong>컨소시엄 불가</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>목동 재건축 단지별 계획 가구수 (가구 · 아래 숫자는 단지)</h3>
    <span class="badge">9단지는 세 번째</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5,123</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:71.3%">4,248</div><div class="barv" style="--h:71.3%"></div></div>
      <div class="col"><div class="v gtx" style="--h:66.5%">3,961</div><div class="barv" style="--h:66.5%"></div></div>
      <div class="col dim"><div class="v" style="--h:64.7%">3,852</div><div class="barv" style="--h:64.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:47.2%">2,810</div><div class="barv" style="--h:47.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:40.9%">2,436</div><div class="barv" style="--h:40.9%"></div></div>
    </div>
    <div class="collbl"><span>14</span><span>10</span><span>9</span><span>13</span><span>12</span><span>4</span></div>
    <p class="cap">모두 재건축 후 계획 가구수라 한 축에 놓았습니다. 막대 길이는 최댓값 5,123가구를 기준으로 맞췄습니다. 심의 단계에서 바뀔 수 있는 계획 수치이며, 뉴시스(10월 20일)·머니투데이방송(10월 6~23일) 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 목동9단지 재건축 내일 현설, 공사비 2.6조"),
    ("02-sched", "목동9단지 시공사 선정, 내일부터 1월 11일까지"),
    ("03-cost", "3.3㎡당 980만원, 목동 다른 단지와 거의 같은 선"),
    ("04-size", "계획 3,961세대, 목동에서 세 번째 규모"),
    ("05-rule", "입찰보증금 800억, 컨소시엄은 안 된다"),
    ("06-check", "목동9단지 재건축 체크 3가지"),
]
imgs = "\n".join(
    f'    <img class="card-art" data-file="{PRE}-{n}.png" src="../images/cards/report/{PRE}-{n}.png"'
    f' alt="카드뉴스 {i}/6 · {d}" loading="lazy" width="1080" height="1080">'
    for i, (n, d) in enumerate(CARDNAMES, 1))
CARDS = f'''<section id="cards">
  <h2>카드뉴스로 한눈에</h2>
  <p class="cards-hint">옆으로 넘기며 핵심만. 이미지를 저장해 활용하셔도 좋습니다.</p>
  <div class="ilabel"><span class="s">현재 테마의 카드 6장</span><button class="allbtn" type="button" data-all="theme" data-fn="cards" data-count="6">⬇ 6장 전체 저장</button></div>
  <div class="cards">
{imgs}
  </div>
</section>'''

ARTICLE = '''<article data-tags="목동9단지재건축,목동9단지,목동재건축,목동신시가지,양천구재건축,시공사선정,현장설명회,삼성물산,GS건설,재건축입찰">
  <h2>목동9단지 재건축 내일 현설, 공사비 2.6조</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 목동9단지 재건축 내일 현설, 공사비 2.6조"></span>

  <p>목동9단지 재건축 시공사 입찰 현장설명회가 내일(11월 2일) 열립니다. 사업시행자 한국자산신탁은 10월 23일 입찰공고를 냈고, 참가를 원하는 건설사는 어제(10월 31일)까지 참가신청서를 내야 했습니다. 내일 현장설명회에 참석해야 입찰 자격이 생깁니다. <span class="mark">예정 공사비는 2조6,067억원(부가세 제외)입니다.</span></p>

  <h3>목동9단지 재건축 시공사 선정 일정</h3>
  <div class="chart" data-img="카드뉴스 2번 · 목동9단지 시공사 선정, 내일부터 1월 11일까지">
    <h3>목동9단지 시공사 입찰 일정</h3>
    <h4>입찰공고</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.23</span>
      <span class="desc">사업시행자 한국자산신탁 공고.</span></div>
    <h4>현장설명회</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.2</span>
      <span class="desc">내일. 참가신청은 10월 31일 마감.</span></div>
    <h4>입찰 마감</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">1.11</span>
      <span class="desc">2027년. 입찰제안서 제출.</span></div>
    <h4>선정 목표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">1분기</span>
      <span class="desc">2027년 시공사 선정, 이어 사업시행계획인가 추진.</span></div>
    <p class="cap">머니투데이방송(10월 23일)·헤럴드경제·위클리한국주택경제 보도 기준입니다. 선정 시기는 목표이며 유찰되면 밀립니다.</p>
  </div>
  <p>현장설명회에서 입찰 마감까지 두 달 넘게 걸립니다. 입찰제안서 마감은 2027년 1월 11일, 시공사 선정은 2027년 1분기가 목표입니다. 업계에서는 삼성물산과 GS건설이 관심을 보이는 것으로 전해집니다. <span class="mark">다만 이건 관측입니다. 현장설명회 참석도 입찰이 아닙니다.</span> 목동10단지는 1차 현장설명회에 6개사가 왔지만 입찰서는 현대건설 한 곳만 냈습니다.</p>

  <h3>목동9단지 재건축 공사비, 3.3㎡당 980만원</h3>
  <div class="chart" data-img="카드뉴스 3번 · 3.3㎡당 980만원, 목동 다른 단지와 거의 같은 선">
    <h3>목동 재건축 3.3㎡당 예정공사비 (만원)</h3>
    <div class="bar"><label>4단지</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,010</div></div></div>
    <div class="bar"><label>10단지</label>
      <div class="rail"><div class="fill gray" style="width:98%">990</div></div></div>
    <div class="bar"><label>9단지</label>
      <div class="rail"><div class="fill" style="width:97%">980</div></div></div>
    <div class="bar"><label>12단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>13단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>8단지</label>
      <div class="rail"><div class="fill gray" style="width:95.5%">965</div></div></div>
    <p class="cap">모두 3.3㎡당 예정공사비(만원)라 한 축에 놓았습니다. 막대 길이는 최댓값 1,010만원을 기준으로 맞췄습니다. 9단지는 머니투데이방송(10월 23일), 나머지는 머니투데이방송(10월 6·8일)·머니투데이(10월 5일) 보도 기준입니다.</p>
  </div>
  <p>3.3㎡당 980만원은 목동 다른 단지(965만~1,010만원)와 거의 같은 선입니다. 총액 2조6,067억원은 목동10단지(약 2조6,135억원)와 비슷합니다. <span class="mark">공사비 차이가 작으니 승부는 이주비·단지명·공사비 인상 부담 같은 제안 조건에서 갈릴 가능성이 큽니다.</span></p>

  <h3>계획 3,961세대, 목동에서 세 번째 규모</h3>
  <span class="imgslot" hidden data-img="카드뉴스 4번 · 계획 3,961세대, 목동에서 세 번째 규모"></span>
  <p>목동9단지는 지하 4층~지상 49층, 3,961세대로 재건축할 계획입니다. 계획이 알려진 목동 단지 가운데 14단지(5,123가구)와 10단지(4,248가구) 다음입니다. 13단지(3,852가구)와 비슷하고 12단지(2,810가구)보다 1,151가구 많습니다. <span class="mark">세대수와 층수는 심의 단계마다 바뀔 수 있는 계획 수치라 확정 전입니다.</span></p>

  <h3>입찰보증금 800억, 컨소시엄은 안 된다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 입찰보증금 800억, 컨소시엄은 안 된다">
    <h3>목동9단지 입찰 조건과 목동 수주 현황</h3>
    <h4>입찰보증금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">800억</span>
      <span class="desc">현금 500억 + 이행보증증권 300억. 공사비의 약 3%.</span></div>
    <h4>공동도급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">불가</span>
      <span class="desc">컨소시엄 없이 한 회사가 단독으로 들어와야 한다.</span></div>
    <h4>앞서 정해진 목동 단지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">5곳</span>
      <span class="desc">6·10단지 확정, 8·12·13단지 우선협상. 모두 단독 응찰.</span></div>
    <p class="cap">입찰 조건은 위클리한국주택경제·헤럴드경제, 수주 현황은 뉴시스(10월 20일)·서울경제TV(10월 28일) 보도 기준입니다. 5곳 공사비 합계는 9조1,773억원입니다.</p>
  </div>
  <p>목동에서 시공사가 정해졌거나 우선협상 중인 곳은 5곳입니다. 6단지 DL이앤씨, 10단지 현대건설은 확정됐고 8단지 대우건설, 12단지 GS건설, 13단지 삼성물산은 우선협상대상자입니다. 5곳 공사비를 합치면 9조1,773억원인데 모두 단독 응찰이었습니다. <span class="mark">다음 경쟁 후보는 11월 16일 입찰을 마감하는 4단지와 대장주로 꼽히는 7단지, 그리고 9단지입니다.</span></p>

  <h3>목동9단지 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 목동9단지 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="mk9-06-check.png" src="../images/cards/report/mk9-06-check.png" alt="체크포인트 카드 · 1. 현설 참석은 입찰이 아니다, 2. 3,961세대는 계획 수치, 3. 조합원 지위는 따로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>목동9단지 재건축 상담에 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>현설 참석은 입찰이 아니다</strong>. 내일 몇 개사가 오든 실제 경쟁 여부는 1월 11일 입찰서 제출에서 갈립니다. 목동10단지는 6개사가 왔지만 입찰은 한 곳이었습니다.</li>
    <li><strong>3,961세대·49층은 계획 수치</strong>. 심의와 사업시행계획인가 단계에서 바뀔 수 있습니다. 분담금도 아직 정해지지 않았습니다.</li>
    <li><strong>조합원 지위는 따로 확인</strong>. 거래 제한은 사업 단계마다 다릅니다. 사고팔기 전에 사업시행자(한국자산신탁)·양천구청·정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>목동9단지 재건축</strong> 시공사 입찰 현장설명회가 11월 2일 열립니다. 예정 공사비 2조6,067억원(3.3㎡당 980만원), 최고 49층 3,961세대 계획이고 입찰 마감은 2027년 1월 11일입니다. 입찰보증금은 800억원이며 컨소시엄은 허용하지 않습니다. <span class="mark">목동은 앞선 5곳이 모두 단독 응찰이었습니다. 11월 16일 4단지 입찰 마감과 함께 첫 경쟁입찰이 나올지 봐야 합니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 목동9단지 입찰 조건은 머니투데이방송(2026-10-23)·헤럴드경제·위클리한국주택경제·비즈니스포스트, 목동 수주 현황은 뉴시스(2026-10-20)·서울경제TV(2026-10-28), 단지별 계획·공사비는 머니투데이방송(2026-10-06·08)·머니투데이(2026-10-05) 보도 기준입니다. 계획 세대수·층수는 확정 전이며 사업시행자 공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 머니투데이방송 목동9단지 시공사 선정 돌입(2026-10-23) · 헤럴드경제 공사비 2.6조 목동9단지 · 위클리한국주택경제 목동9단지 시공자 선정 · 비즈니스포스트 목동9단지 입찰공고 · 뉴시스 30조 목동 시공사 확정(2026-10-20) · 서울경제TV 목동 5곳 단독응찰(2026-10-28) · 머니투데이방송 목동 단지별 공사비(2026-10-06·08)<br>
  © 2026 부동산 인사이트 · 데이터 기준일 {DATE} · <a href="../index.html">← 홈으로</a>
</footer>'''

for _p in sorted((ROOT / "posts").glob("*.html")):
    if _p.name != DST.name and f"{PRE}-01-cover.png" in _p.read_text(encoding="utf-8"):
        raise SystemExit(f"접두어 {PRE} 를 {_p.name} 이 이미 쓰고 있다.")

src = SRC.read_text(encoding="utf-8")


def cut(text, start, end, block):
    a = text.index(start)
    b = text.index(end, a) + len(end)
    return text[:a] + block + text[b:]


out = cut(src, "<title>", "</script>", HEAD)
out = cut(out, "<header>", "</header>", HEADER)
out = cut(out, '<section id="dashboard">', "</section>", DASH)
out = cut(out, '<section id="cards">', "</section>", CARDS)
out = cut(out, "<article ", "</article>", ARTICLE)
out = cut(out, "<footer>", "</footer>", FOOTER)
out = re.sub(r'<div class="trace"></div>\n\n<section id="insta".*?</section>\n\n<footer>',
             '<div class="trace"></div>\n\n<footer>', out, count=1, flags=re.S)

assert PREV_SLUG not in out
for _b in BANNED:
    assert _b not in out, _b
assert out.count(f"리포트 #{NO}") == 1
assert f"데이터 기준일 {DATE}" in out
assert '</article>\n\n<div class="trace"></div>\n\n<footer>' in out
assert out.count("<script") == out.count("</script>")
for _m in re.finditer(r'<span class="imgslot"[^>]*>', out):
    assert out[_m.end():_m.end() + 7] == "</span>"
assert "—" not in out
assert 'rel="icon"' in out
assert out.count('data-all="theme"') == 1
# 검산
H = (5123, 4248, 3961, 3852, 2810, 2436)
for v, h in zip(H[1:], (71.3, 66.5, 64.7, 47.2, 40.9)):
    assert round(v / 5123 * 86, 1) == h, (v, h)
for v, w in zip((990, 980, 965), (98.0, 97.0, 95.5)):
    assert round(v / 1010 * 100, 1) == w, (v, w)
assert 500 + 300 == 800 and round(800 / 26067 * 100) == 3 and 3961 - 2810 == 1151
KW = "목동9단지 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("목동9단지재건축")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
