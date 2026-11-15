# -*- coding: utf-8 -*-
"""리포트 #127 (2026-11-16) 중화역 라온프라이빗 센트로. #126을 복제해 교체한다.

메인 검색어: 중화역 라온프라이빗 센트로

수치와 검산
  사건일과 오늘의 간격: 특공 11/16(오늘) · 1순위 해당 11/17(내일) · 견본주택 11/13 개관(3일 전) · 분양캘린더 보도 11/13~14(2~3일 전).
  단지 (리얼투데이 인용 분양캘린더 11/13~14 · 스트레이트뉴스 · 리버티코리아포스트): 중랑구 중화동 · 지하3층~지상26층 3개동 · 45~126㎡ 176가구 · 일반분양 113
    시공 라온건설 · 7호선 중화역 도보 3분 · 입주 2029년 2월 · 오피스텔 74실 별도(접수 11/25~26)
  공급(분양정보 사이트): 일반분양 113 = 특공 60 + 일반공급 53
  타입별 일반분양(분양정보 사이트): 45 7 · 58 17 · 59 20 · 70 26 · 84 35 (합 105, 나머지 8은 그 밖의 타입)
  분양가(만원, 분양정보 사이트): 45 65,800 · 59 95,600 · 84 127,700 · 126T 202,100 · 스트레이트뉴스 3.3㎡당 3,750만원 · 59 평균 93,530
  일정: 특공 11/16 · 1순위 해당(서울 2년 이상) 11/17 · 기타(서울 2년 미만·인천·경기) 11/18 · 2순위 11/19 · 발표 11/25 · 계약 12/7~9
  대시보드(35→86): 7 17.2 · 17 41.8 · 20 49.1 · 26 63.9
  가구(176→100): 113 64.2 · 60 34.1 · 53 30.1
  분양가(202,100→100): 127,700 63.2 · 95,600 47.3 · 65,800 32.6

단정하지 않은 것
  · 타입별 가구·분양가는 분양정보 사이트 정리 기준, 출처마다 차이(최저 6억1,900 vs 6억5,800) → 공고문 확인
  · 분양가상한제·전매제한·재당첨 제한은 확인 못 함 → 공고문
  · 63가구(176-113)를 조합원분이라 단정하지 않는다('일반분양 외')
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-15-gyeonghuigung-epit.html"
DST = ROOT / "posts/2026-11-16-junghwa-raon.html"
SLUG, PRE = "2026-11-16-junghwa-raon", "jhr"
NO, DATE = 127, "2026-11-16"
PREV_SLUG = "ghe-"
BANNED = ["경희궁", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "중화역 라온프라이빗 센트로 내일 1순위, 59㎡ 9억대"
DESC = ("중화역 라온프라이빗 센트로는 서울 중랑구 중화동 176가구(일반분양 113가구) 단지입니다. "
        "오늘 특별공급, 내일(11월 17일) 1순위 해당지역 접수이며 전용 59㎡는 9억원대로 안내됐습니다. 일정·분양가·확인할 점을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="중랑구 중화동 176가구, 일반분양 113가구. 1순위 해당지역 11월 17일, 발표 25일. 59㎡ 9억원대, 84㎡ 12억원대 안내.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">중화역 라온프라이빗 센트로<br>내일 1순위, 59㎡ 9억대</h1>
  <p class="sub"><strong>중화역 라온프라이빗 센트로</strong>는 서울 중랑구 중화동에 들어서는 <strong>176가구</strong> 단지로, 이 가운데 <strong>113가구</strong>가 일반분양입니다. 오늘(16일) 특별공급에 이어 <strong>내일(17일) 1순위 해당지역</strong> 접수가 열립니다. <span class="mark">전용 59㎡는 9억원대, 84㎡는 12억원대로 안내됐습니다. 같은 이름의 오피스텔 74실은 별개 상품이니 헷갈리지 마십시오.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 중화역 라온프라이빗 센트로</div><div class="kw">176가구</div>
      <p>일반분양 <strong>113가구</strong>.</p></div>
    <div class="kcard"><div class="hot">1순위 해당지역</div><div class="kw">11월 17일</div>
      <p>서울 <strong>2년 이상</strong> 거주자.</p></div>
    <div class="kcard"><div class="hot">59㎡ 분양가</div><div class="kw">9억원대</div>
      <p>3.3㎡당 <strong>3,750만원</strong> 보도.</p></div>
    <div class="kcard"><div class="hot">당첨자 발표</div><div class="kw">11월 25일</div>
      <p>계약 <strong>12/7~9</strong> · 입주 2029년 2월.</p></div>
  </div>

  <div class="colchart">
    <h3>중화역 라온프라이빗 센트로 타입별 일반분양 (가구)</h3>
    <span class="badge">84㎡가 가장 많다</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:17.2%">7</div><div class="barv" style="--h:17.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:41.8%">17</div><div class="barv" style="--h:41.8%"></div></div>
      <div class="col dim"><div class="v" style="--h:49.1%">20</div><div class="barv" style="--h:49.1%"></div></div>
      <div class="col dim"><div class="v" style="--h:63.9%">26</div><div class="barv" style="--h:63.9%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">35</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>45㎡</span><span>58㎡</span><span>59㎡</span><span>70㎡</span><span>84㎡</span></div>
    <p class="cap">모두 일반분양 가구 수라 한 축에 놓았습니다. 막대 길이는 최댓값 35가구를 기준으로 맞췄습니다. 다섯 타입 합계는 105가구이고 나머지 8가구는 그 밖의 타입입니다. 분양정보 사이트의 모집공고 정리 기준이며 확정 물량은 입주자모집공고문으로 확인하십시오.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 중화역 라온프라이빗 센트로 내일 1순위, 59㎡ 9억대"),
    ("02-mix", "176가구 중 일반분양 113가구"),
    ("03-sched", "1순위 17일, 발표는 25일"),
    ("04-price", "59㎡ 9억대, 84㎡ 12억대"),
    ("05-site", "중화역 3분, 26층 3개 동"),
    ("06-check", "중화역 라온프라이빗 센트로 체크 3가지"),
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

ARTICLE = '''<article data-tags="중화역라온프라이빗센트로,중화역라온프라이빗센트로분양가,중랑구아파트분양,중화동,서울청약,11월청약일정,라온건설,1순위청약,중화역,7호선역세권">
  <h2>중화역 라온프라이빗 센트로 내일 1순위, 59㎡ 9억대</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 중화역 라온프라이빗 센트로 내일 1순위, 59㎡ 9억대"></span>

  <p>중화역 라온프라이빗 센트로가 내일(11월 17일) 1순위 해당지역 청약을 받습니다. 서울 중랑구 중화동, 7호선 중화역에서 걸어서 3분 거리에 짓는 176가구 단지입니다. 오늘(16일)은 특별공급 날입니다. <span class="mark">전용 59㎡는 9억원대, 84㎡는 12억원대로 안내돼 있어 강북권 신축 시세와 견줘 보고 넣을지 정해야 합니다.</span></p>

  <h3>중화역 라온프라이빗 센트로, 176가구 중 일반분양 113가구</h3>
  <div class="chart" data-img="카드뉴스 2번 · 176가구 중 일반분양 113가구">
    <h3>중화역 라온프라이빗 센트로 공급 구성 (가구)</h3>
    <div class="bar"><label>전체</label>
      <div class="rail"><div class="fill gray" style="width:100%">176</div></div></div>
    <div class="bar"><label>일반분양</label>
      <div class="rail"><div class="fill" style="width:64.2%">113</div></div></div>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill gray" style="width:34.1%">60</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill gray" style="width:30.1%">53</div></div></div>
    <p class="cap">모두 가구 수라 한 축에 놓았습니다. 막대 길이는 전체 176가구를 기준으로 맞췄습니다. 일반분양 113가구는 특별공급 60가구와 일반공급 53가구를 합친 값입니다. 전체·일반분양은 분양캘린더 보도(11월 13~14일), 특공·일반 배분은 분양정보 사이트 기준입니다.</p>
  </div>
  <p>전용 45~126㎡ 176가구 가운데 청약으로 나오는 물량은 113가구입니다. 이 중 60가구가 오늘 특별공급으로, 53가구가 내일부터 일반공급으로 나옵니다. 타입별로는 84㎡가 35가구로 가장 많고 70㎡ 26가구, 59㎡ 20가구 순입니다. <span class="mark">1순위로 실제 경쟁하는 물량은 53가구 안팎이라 타입 하나에 열 가구 남짓입니다. 타입별 가구 수는 모집공고문에서 확인하십시오.</span></p>

  <h3>중화역 라온프라이빗 센트로 청약 일정, 1순위 17일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 1순위 17일, 발표는 25일">
    <h3>중화역 라온프라이빗 센트로 청약 일정</h3>
    <h4>1순위 해당지역</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.17</span>
      <span class="desc">화요일. 서울 2년 이상 거주자.</span></div>
    <h4>1순위 기타지역</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.18</span>
      <span class="desc">서울 2년 미만·인천·경기. 2순위는 19일.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.25</span>
      <span class="desc">계약은 12월 7~9일.</span></div>
    <p class="cap">특별공급 11월 16일 포함, 분양캘린더 보도(리얼투데이 인용, 11월 13~14일)와 분양정보 사이트 기준입니다. 청약홈 공고문으로 다시 확인하십시오.</p>
  </div>
  <p>일정은 특별공급 16일, 1순위 해당지역(서울 2년 이상 거주) 17일, 기타지역(서울 2년 미만·인천·경기) 18일, 2순위 19일입니다. 당첨자는 25일에 발표하고 계약은 12월 7~9일입니다. <span class="mark">서울에 산 지 2년이 안 됐다면 내일이 아니라 18일에 넣어야 합니다. 거주 기간 기준일은 공고문에서 확인하십시오.</span></p>

  <h3>중화역 라온프라이빗 센트로 분양가, 59㎡ 9억대</h3>
  <div class="chart" data-img="카드뉴스 4번 · 59㎡ 9억대, 84㎡ 12억대">
    <h3>중화역 라온프라이빗 센트로 타입별 분양가 (만원)</h3>
    <div class="bar"><label>126㎡</label>
      <div class="rail"><div class="fill gray" style="width:100%">202,100</div></div></div>
    <div class="bar"><label>84㎡</label>
      <div class="rail"><div class="fill" style="width:63.2%">127,700</div></div></div>
    <div class="bar"><label>59㎡</label>
      <div class="rail"><div class="fill gray" style="width:47.3%">95,600</div></div></div>
    <div class="bar"><label>45㎡</label>
      <div class="rail"><div class="fill gray" style="width:32.6%">65,800</div></div></div>
    <p class="cap">막대 길이는 최댓값 202,100만원을 기준으로 맞췄습니다. 분양정보 사이트의 모집공고 정리 기준이며 자료마다 금액이 조금씩 다릅니다(최저가 6억1,900만원으로 적은 곳도 있음). 확정 금액은 공고문으로 확인하십시오.</p>
  </div>
  <p>분양가는 3.3㎡당 3,750만원으로 보도됐습니다(스트레이트뉴스). 전용 59㎡는 평균 9억3,530만원, 분양정보 사이트 기준 9억5,600만원이고 84㎡는 12억7,700만원, 가장 큰 126㎡는 20억원을 넘습니다. 가장 작은 45㎡는 6억원대입니다. <span class="mark">계약금 비율과 중도금 대출 조건은 보도로 확인되지 않았습니다. 현금 계획은 공고문을 보고 세우십시오.</span></p>

  <h3>중화역 3분, 26층 3개 동</h3>
  <div class="chart" data-img="카드뉴스 5번 · 중화역 3분, 26층 3개 동">
    <h3>중화역 라온프라이빗 센트로 단지 개요</h3>
    <h4>역까지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3분</span>
      <span class="desc">7호선 중화역 도보 거리로 소개된다.</span></div>
    <h4>규모</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">26층</span>
      <span class="desc">지하 3층~지상 26층 3개 동. 시공은 라온건설.</span></div>
    <h4>입주 예정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2029.2</span>
      <span class="desc">당첨부터 입주까지 2년 3개월가량.</span></div>
    <p class="cap">분양캘린더 보도(11월 13~14일)·스트레이트뉴스·라온건설 보도자료 기준입니다.</p>
  </div>
  <p>단지는 지하 3층~지상 26층 3개 동이고 시공은 라온건설입니다. 견본주택은 11월 13일에 문을 열었습니다. 입주는 2029년 2월 예정입니다. 같은 이름으로 오피스텔 74실(전용 20~59㎡)도 나오는데, 이쪽은 11월 25~26일에 따로 접수하는 별개 상품입니다.</p>

  <h3>중화역 라온프라이빗 센트로 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 중화역 라온프라이빗 센트로 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="jhr-06-check.png" src="../images/cards/report/jhr-06-check.png" alt="체크포인트 카드 · 1. 거주 2년 기준 접수일, 2. 분양가는 공고문으로, 3. 오피스텔 74실은 별개" loading="lazy" width="1080" height="1080">
    <figcaption>중화역 라온프라이빗 센트로 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>내 접수일이 17일인지 18일인지</strong>. 서울 2년 이상 거주면 17일, 2년 미만이거나 인천·경기면 18일입니다. 통장 가입 기간·예치금은 청약통장 순위(가입)확인서로 확인하십시오.</li>
    <li><strong>분양가는 공고문 금액으로</strong>. 자료마다 금액이 조금씩 다릅니다. 층·타입별 금액은 청약홈 공고문이 정본입니다.</li>
    <li><strong>오피스텔 74실은 다른 상품</strong>. 이름이 같아도 아파트 청약과 별개이며 25~26일에 따로 접수합니다. 청약통장·주택 수 계산이 다르니 무엇에 넣는지 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>중화역 라온프라이빗 센트로</strong>는 중랑구 중화동 176가구(일반분양 113가구) 단지로, 내일(17일) 1순위 해당지역 접수를 받고 25일 당첨자를 발표합니다. 전용 59㎡는 9억원대, 84㎡는 12억원대로 안내됐습니다. <span class="mark">1순위 물량은 53가구 안팎으로 작습니다. 넣기 전에 공고문 금액으로 자금 계획부터 세우십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 단지 개요·일정은 리얼투데이를 인용한 분양캘린더 보도(2026-11-13~14)·스트레이트뉴스·리버티코리아포스트, 타입별 가구·분양가는 분양정보 사이트 정리 기준입니다. 최종 조건은 입주자모집공고문과 청약홈으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 서울경제TV [분양 캘린더] 중화역 라온프라이빗 센트로 등 10곳서 1681가구 청약(2026-11-13) · 파이낸셜뉴스 11월 셋째 주 전국 1681가구 공급(2026-11-13) · 오피니언뉴스 [이번주 분양] 전국 10곳 1681가구 청약 · 스트레이트뉴스 [살집 말집] 중화역 3분 라온프라이빗 센트로 59㎡ 9.35억 · 리버티코리아포스트 라온건설 중화역 라온프라이빗 센트로 11월 13일 견본주택 개관 · 분양정보 사이트 모집공고 정리<br>
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
for v, h in zip((7, 17, 20, 26), (17.2, 41.8, 49.1, 63.9)):
    assert round(v / 35 * 86, 1) == h, (v, h)
for v, w in zip((113, 60, 53), (64.2, 34.1, 30.1)):
    assert round(v / 176 * 100, 1) == w, (v, w)
assert 60 + 53 == 113
for v, w in zip((127700, 95600, 65800), (63.2, 47.3, 32.6)):
    assert round(v / 202100 * 100, 1) == w, (v, w)
KW = "중화역 라온프라이빗 센트로"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("중화역라온프라이빗센트로")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
