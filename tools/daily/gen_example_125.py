# -*- coding: utf-8 -*-
"""리포트 #125 (2026-11-14) 서울 토지거래허가 신청 10월 집계. #124를 복제해 교체한다.

메인 검색어: 토지거래허가 신청

수치와 검산
  사건일과 오늘의 간격: 서울시 10월 토허 신청 집계 발표 11/13(어제, 1일). 만료 12/31(#88 배경).
  10월 신규 신청 3,947건, 전월(3,649) 대비 +8.2% · 9월 증가율 24.2% · 저점 8월 2,939 · 최대 4월 8,886(10월은 44.4%)
  7월 4,681(SBS Biz 8월 보도). 9월은 첫 발표 3,678에서 3,649로 고쳐 잡힌 값(11/13 발표 기준)
  건수 증가율: 강남3구·용산 20.6% · 한강벨트 7개구 784→860 9.7% · 서남권 4개구 708→775 9.5%
  신청가격: 강남3구·용산 9월 -0.41% → 10월 -0.92% · 한강벨트 +1.04% · 서남권 +0.89% · 강북권 +0.52%
  강남3구·용산 비중: 8월 11.9% · 9월 14.5% · 10월 16.2%
  누적: 2025-10-20 서울 전역 지정 뒤 2026-10월 말까지 63,447건
    대시보드 컬럼(8886→86): 8886 86 · 4681 45.3 · 2939 28.4 · 3649 35.3 · 3947 38.2
    카드3 가로(20.6→100): 9.7 47.1 · 9.5 46.1 · 8.2 39.8
    카드5 가로(16.2→100): 11.9 73.5 · 14.5 89.5

단정하지 않은 것
  · 12/31 만료 뒤 연장 여부는 발표 전(10/7 국감 '검토') · 신청가격은 허가 신청서의 가격이지 실거래가 아니다
  · 강남 하락이 이어질지는 전망하지 않는다(서울시도 "회복세 판단 이르다")
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-13-mokdong4.html"
DST = ROOT / "posts/2026-11-14-toheo-oct.html"
SLUG, PRE = "2026-11-14-toheo-oct", "th10"
NO, DATE = 125, "2026-11-14"
PREV_SLUG = "mokdong4"
BANNED = ["목동4단지", "1,010만", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "토지거래허가 신청 두 달째 증가, 강남은 내렸다"
DESC = ("서울 아파트 토지거래허가 신청이 10월 3,947건으로 두 달 연속 늘었습니다. "
        "강남3구·용산은 신청 건수가 20.6% 늘었지만 신청가격은 0.92% 내렸고, 한강벨트는 1.04% 올랐습니다. "
        "월별 추이, 권역별 건수와 가격, 12월 31일 만료를 앞두고 볼 것을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="10월 3,947건, 전월보다 8.2% 늘었습니다. 강남3구·용산은 건수 20.6% 증가, 신청가격은 0.92% 하락.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">토지거래허가 신청<br>두 달째 증가, 강남은 내렸다</h1>
  <p class="sub">서울 아파트 <strong>토지거래허가 신청</strong>이 10월 <strong>3,947건</strong>으로 두 달 연속 늘었습니다(서울시 11월 13일 발표). <span class="mark">강남3구·용산은 신청이 가장 많이 늘었는데, 신청가격은 오히려 0.92% 내렸습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 10월 신청</div><div class="kw">3,947건</div>
      <p>전월보다 <strong>8.2%</strong> 늘었다.</p></div>
    <div class="kcard"><div class="hot">강남3구·용산 가격</div><div class="kw">−0.92%</div>
      <p>9월 −0.41%에서 <strong>하락폭 확대</strong>.</p></div>
    <div class="kcard"><div class="hot">한강벨트 가격</div><div class="kw">+1.04%</div>
      <p>7개구, <strong>오름폭 확대</strong>.</p></div>
    <div class="kcard"><div class="hot">전역 지정 후 누적</div><div class="kw">6.3만건</div>
      <p>2025년 10월 20일부터 <strong>63,447건</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>서울 아파트 토지거래허가 신규 신청 (건)</h3>
    <span class="badge">8월 바닥 뒤 두 달째 증가</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">8,886</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:45.3%">4,681</div><div class="barv" style="--h:45.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:28.4%">2,939</div><div class="barv" style="--h:28.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:35.3%">3,649</div><div class="barv" style="--h:35.3%"></div></div>
      <div class="col"><div class="v gtx" style="--h:38.2%">3,947</div><div class="barv" style="--h:38.2%"></div></div>
    </div>
    <div class="collbl"><span>4월</span><span>7월</span><span>8월</span><span>9월</span><span>10월</span></div>
    <p class="cap">서울시 발표(4·8·9·10월은 2026년 11월 13일, 7월은 8월 발표) 기준입니다. 9월은 처음 3,678건으로 발표됐다가 이번 발표에서 3,649건으로 잡혔습니다. 막대 길이는 최댓값 8,886건을 기준으로 맞췄습니다. 5·6월은 빠져 있어 칸 사이 간격이 같지 않습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 토지거래허가 신청 두 달째 증가, 강남은 내렸다"),
    ("02-when", "서울 토지거래허가, 지정 1년과 남은 일정"),
    ("03-count", "신청이 가장 많이 는 곳은 강남3구·용산"),
    ("04-price", "그런데 가격은 강남만 내렸다"),
    ("05-share", "강남3구·용산 비중, 석 달째 커졌다"),
    ("06-check", "토지거래허가 신청 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="토지거래허가신청,토지거래허가구역,토허제,서울토지거래허가,강남3구,용산구,한강벨트,서울아파트,실거주의무,부동산규제">
  <h2>토지거래허가 신청 두 달째 증가, 강남은 내렸다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 토지거래허가 신청 두 달째 증가, 강남은 내렸다"></span>

  <p>토지거래허가 신청이 서울 아파트에서 두 달 연속 늘었습니다. 서울시가 11월 13일 발표한 집계를 보면 10월 신규 신청은 3,947건으로 9월(3,649건)보다 8.2% 많습니다. 8월 2,939건이 바닥이었고, 올해 가장 많았던 4월(8,886건)과 비교하면 44.4% 수준입니다. <span class="mark">눈에 띄는 건 강남3구·용산입니다. 신청 건수는 가장 많이 늘었는데 신청가격은 0.92% 내렸습니다.</span></p>

  <h3>서울 토지거래허가, 지정 1년과 남은 일정</h3>
  <div class="chart" data-img="카드뉴스 2번 · 서울 토지거래허가, 지정 1년과 남은 일정">
    <h3>서울 아파트 토지거래허가 일정</h3>
    <h4>서울 전역 지정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2025.10.20</span>
      <span class="desc">서울 25개구 아파트가 허가 대상이 됐다.</span></div>
    <h4>10월 말까지 누적 신청</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">63,447건</span>
      <span class="desc">지정 후 약 1년 동안 들어온 신규 신청.</span></div>
    <h4>지정 기간 끝</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">12월 31일</span>
      <span class="desc">연장 여부는 아직 발표 전이다.</span></div>
    <p class="cap">서울시 발표(2026-11-13)와 국정감사 보도(2026-10-07) 기준입니다. 10월 7일 국토부 장관은 연장을 "시장 상황을 보며 검토하겠다"고 했고, 11월 13일까지 결정을 알린 보도는 찾지 못했습니다.</p>
  </div>
  <p>서울 전역이 토지거래허가구역으로 묶인 지 1년이 지났습니다. 그동안 들어온 신규 신청은 63,447건입니다. 지금 지정은 12월 31일에 끝나고, 연장 여부는 아직 발표 전입니다. 10월 국정감사에서 국토부 장관은 "시장 상황을 보며 검토하겠다"고만 했습니다. <span class="mark">이번 10월 집계는 연장을 판단할 때 정부가 볼 숫자 가운데 하나입니다.</span></p>

  <h3>토지거래허가 신청, 가장 많이 는 곳은 강남3구·용산</h3>
  <div class="chart" data-img="카드뉴스 3번 · 신청이 가장 많이 는 곳은 강남3구·용산">
    <h3>권역별 10월 신청 건수 증가율 (전월 대비, %)</h3>
    <div class="bar"><label>강남3구·용산</label>
      <div class="rail"><div class="fill" style="width:100%">20.6</div></div></div>
    <div class="bar"><label>한강벨트 7개구</label>
      <div class="rail"><div class="fill gray" style="width:47.1%">9.7</div></div></div>
    <div class="bar"><label>서남권 4개구</label>
      <div class="rail"><div class="fill gray" style="width:46.1%">9.5</div></div></div>
    <div class="bar"><label>서울 전체</label>
      <div class="rail"><div class="fill gray" style="width:39.8%">8.2</div></div></div>
    <p class="cap">모두 9월 대비 10월 신청 건수 증가율이라 한 축에 놓았습니다. 막대 길이는 최댓값 20.6%를 기준으로 맞췄습니다. 한강벨트는 784건에서 860건, 서남권은 708건에서 775건입니다. 서울시 발표(2026-11-13) 기준입니다.</p>
  </div>
  <p>권역별로 보면 강남3구·용산의 신청 건수가 20.6% 늘어 증가율이 가장 높았습니다. 한강벨트 7개구는 784건에서 860건(9.7%), 서남권 4개구는 708건에서 775건(9.5%)으로 늘었습니다. 서울 전체 증가율 8.2%보다 모두 높습니다. 다만 전월 대비 증가율은 9월 24.2%에서 10월 8.2%로 낮아졌고, 서울시는 "주택시장 전반의 회복세로 판단하기에는 이르다"고 봤습니다.</p>

  <h3>그런데 가격은 강남만 내렸다</h3>
  <div class="chart" data-img="카드뉴스 4번 · 그런데 가격은 강남만 내렸다">
    <h3>권역별 10월 신청가격 변동 (전월 대비)</h3>
    <h4>강남3구·용산</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">−0.92%</span>
      <span class="desc">9월 −0.41%에서 하락폭이 커졌다.</span></div>
    <h4>한강벨트 7개구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">+1.04%</span>
      <span class="desc">오름폭이 커졌다.</span></div>
    <h4>서남권 4개구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">+0.89%</span>
      <span class="desc">올랐지만 오름세는 둔화.</span></div>
    <h4>강북권</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">+0.52%</span>
      <span class="desc">올랐지만 오름세는 둔화.</span></div>
    <p class="cap">신청가격은 허가 신청서에 적힌 가격으로, 계약이 끝난 실거래가와는 다릅니다. 서울시 발표(2026-11-13) 기준입니다.</p>
  </div>
  <p>신청가격은 흐름이 갈렸습니다. 강남3구·용산은 9월 −0.41%에 이어 10월 −0.92%로 하락폭이 커졌습니다. 반대로 한강벨트는 1.04% 올라 오름폭이 커졌고, 서남권(0.89%)과 강북권(0.52%)은 오르긴 했지만 속도가 줄었습니다. 서울시는 일부 단지의 입지와 신축 선호에 따른 상승 거래가 영향을 줬다고 분석했습니다. <span class="mark">신청가격은 신청서에 적힌 가격이라 실거래가와 같지 않다는 점은 감안해야 합니다.</span></p>

  <h3>강남3구·용산 비중, 석 달째 커졌다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 강남3구·용산 비중, 석 달째 커졌다">
    <h3>서울 토지거래허가 신청 중 강남3구·용산 비중 (%)</h3>
    <div class="bar"><label>8월</label>
      <div class="rail"><div class="fill gray" style="width:73.5%">11.9</div></div></div>
    <div class="bar"><label>9월</label>
      <div class="rail"><div class="fill gray" style="width:89.5%">14.5</div></div></div>
    <div class="bar"><label>10월</label>
      <div class="rail"><div class="fill" style="width:100%">16.2</div></div></div>
    <p class="cap">서울 전체 신규 신청 가운데 강남3구·용산이 차지한 비율입니다. 막대 길이는 최댓값 16.2%를 기준으로 맞췄습니다. 서울시 발표(2026-11-13) 기준입니다.</p>
  </div>
  <p>강남3구·용산이 서울 전체 신청에서 차지하는 비중은 8월 11.9%, 9월 14.5%, 10월 16.2%로 석 달째 커졌습니다. 가격이 내려간 지역에서 신청이 늘었다는 뜻입니다. 이 흐름이 이어질지는 11월 집계가 나와야 알 수 있습니다.</p>

  <h3>토지거래허가 신청 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 토지거래허가 신청 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="th10-06-check.png" src="../images/cards/report/th10-06-check.png" alt="체크포인트 카드 · 1. 12월 31일 연장 발표, 2. 신청가격은 실거래가가 아니다, 3. 실거주 조건은 구청 확인" loading="lazy" width="1080" height="1080">
    <figcaption>서울 아파트 토지거래허가 신청을 앞두고 확인할 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>12월 31일 연장 발표</strong>. 지금 지정은 연말에 끝납니다. 연장·조정 여부는 국토부·서울시 발표로 확인하십시오.</li>
    <li><strong>신청가격은 실거래가가 아니다</strong>. 단지 시세는 국토부 실거래가 공개시스템에서 계약이 끝난 가격으로 보십시오.</li>
    <li><strong>실거주 조건은 구청 확인</strong>. 허가 조건과 입주 기한, 예외는 사람·주택마다 다릅니다. 계약 전 해당 구청 토지거래허가 담당에 물어보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p>서울 아파트 <strong>토지거래허가 신청</strong>은 10월 3,947건으로 두 달 연속 늘었습니다. 강남3구·용산은 신청 건수가 20.6% 늘고 비중도 16.2%까지 커졌지만 신청가격은 0.92% 내렸고, 한강벨트는 1.04% 올랐습니다. <span class="mark">서울 전역 지정은 12월 31일에 끝나며, 연장 여부는 아직 발표 전입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 신청 건수·신청가격은 서울시 발표(2026-11-13, 파이낸셜뉴스·서울신문·베타뉴스 보도), 7월 건수는 SBS Biz(2026-08) 보도, 연장 검토 발언은 국정감사 보도(2026-10-07) 기준입니다. 신청가격은 허가 신청서 기준이며 실거래가와 다릅니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 파이낸셜뉴스 서울 아파트 토허 신청 2개월 연속 증가(2026-11-13) · 서울신문 서울 아파트 토허 신청 두 달 연속 증가(2026-11-13) · 베타뉴스 서울시, 10월 토허 신청 두 달째 늘었다(2026-11-13) · SBS Biz 7월 서울 아파트 토지거래허가신청 4681건(2026-08) · SBS Biz 9월 서울 아파트 토허신청 소폭 반등(2026-10)<br>
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
for v, h in zip((8886, 4681, 2939, 3649, 3947), (86, 45.3, 28.4, 35.3, 38.2)):
    assert round(v / 8886 * 86, 1) == h, (v, h)
for v, w in zip((9.7, 9.5, 8.2), (47.1, 46.1, 39.8)):
    assert round(v / 20.6 * 100, 1) == w, (v, w)
for v, w in zip((11.9, 14.5), (73.5, 89.5)):
    assert round(v / 16.2 * 100, 1) == w, (v, w)
assert round((3947 / 3649 - 1) * 100, 1) == 8.2 and round(3947 / 8886 * 100, 1) == 44.4
assert round((860 / 784 - 1) * 100, 1) == 9.7 and round((775 / 708 - 1) * 100, 1) == 9.5
assert round((3649 / 2939 - 1) * 100, 1) == 24.2
KW = "토지거래허가 신청"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("토지거래허가신청")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
