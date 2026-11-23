# -*- coding: utf-8 -*-
"""리포트 #136 (2026-11-24 화) 목동12단지 재건축 GS건설 선정. #135를 복제해 교체한다.

메인 검색어: 목동12단지 재건축
요일 종류: 화요일 재건축·재개발 대표 단지(해설형).
핫이슈 훑기: 6검색. 목동12단지 GS건설 선정(한국경제 11/23 · 시공사 선정 총회 검색 상위) · 디에이치 반포124 분양가 심의 보류(재심의 12/4, 한국경제·서울경제 11/18)
  · 이혜훈 원펜타스 계약취소 요청. 반포124는 #130(11/19)로 2주 안이라 제외. 목동12단지가 화요일 종류와 맞아 오늘 씀.

수치와 검산
  사건일과 오늘의 간격: 시공사 선정 총회 11/22 → 2일. 발표 11/23 → 1일.
  공사비 약 1조7,887억(한국경제 11/23 · 조합 추산 1조7,888억 보도도 있음) · 3.3㎡당 980만원 · 1,860가구 15층 → 2,810가구 43층(계획)
  1차 입찰 GS 단독 응찰 유찰(머니투데이방송 8/31) · 2차 현설(9/8 보도) · 두 차례 단독 → 수의계약 · 제안 단지명 '리플리제 자이'
  목동: 10단지 현대 10/18 95.9% · 13단지 삼성 11/7 95.7% 2조3,763억 3,852세대 · 4단지 11/16 현대 단독 유찰 1,010만원 2,436가구 · 9단지 마감 2027-01-11 3,961세대 · 8단지 965만원
  대시보드 세로 (3,961 → 86): 3,852 → 83.6 · 2,810 → 61.0 · 2,436 → 52.9
  카드2 가로 (2,810 → 100): 1,860 → 66.2 · 증가 950 · 1.51배
  카드4 가로 (1,010 → 100): 980 → 97.0 · 965 → 95.5
  가구당 공사비 단순 평균: 12단지 178,870,000만/2,810 ≈ 6억3,656만 · 13단지 237,630,000만/3,852 ≈ 6억1,690만

단정하지 않은 것
  · 총회 찬성 비율: 검색에서 확인 못 함. 조합 공지로 확인 필요
  · '리플리제 자이'는 GS건설 제안명. 단지명 확정 아님
  · 가구수·층수는 심의 단계마다 바뀔 수 있는 계획
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-23-nov-week4-seoul.html"
SLUG, PRE = "2026-11-24-mokdong12", "mk12"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 136, "2026-11-24"
PREV_SLUG = "nov-week4-seoul"
BANNED = ["해링턴", "nw4-"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "목동12단지 재건축 GS건설 확정, 공사비 1.8조"
DESC = ("목동12단지 재건축 시공사로 GS건설이 11월 22일 총회에서 선정됐습니다. 공사비는 약 1조7,887억원, 3.3㎡당 980만원이고 "
        "1,860가구를 최고 43층 2,810가구로 다시 짓는 계획입니다. 두 차례 단독 응찰 뒤 수의계약으로 온 과정과 목동 단지별 시공사 현황을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="11월 22일 총회에서 GS건설 선정. 3.3㎡당 980만원, 1,860가구에서 2,810가구로. 목동 10·13·12단지 시공사 확정.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">목동12단지 재건축,<br>GS건설로 확정</h1>
  <p class="sub">목동12단지 재건축 조합이 11월 22일 총회에서 <strong>GS건설</strong>을 시공사로 뽑았습니다. 공사비는 <strong>약 1조7,887억원</strong>, 3.3㎡당 980만원입니다. <span class="mark">목동에서 시공사가 정해진 세 번째 단지입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/22 총회</div><div class="kw">GS건설</div>
      <p>두 차례 <strong>단독 응찰</strong> 뒤 선정.</p></div>
    <div class="kcard"><div class="hot">공사비</div><div class="kw">1조7,887억</div>
      <p>3.3㎡당 <strong>980만원</strong>.</p></div>
    <div class="kcard"><div class="hot">계획 가구</div><div class="kw">2,810가구</div>
      <p>지금 <strong>1,860가구</strong>에서 늘린다.</p></div>
    <div class="kcard"><div class="hot">최고 층수</div><div class="kw">43층</div>
      <p>지금 최고 <strong>15층</strong>, 확정 전.</p></div>
  </div>

  <div class="colchart">
    <h3>목동 재건축 단지별 계획 가구 (가구)</h3>
    <span class="badge">12단지는 셋째 규모</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">3,961</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:83.6%">3,852</div><div class="barv" style="--h:83.6%"></div></div>
      <div class="col"><div class="v gtx" style="--h:61%">2,810</div><div class="barv" style="--h:61%"></div></div>
      <div class="col dim"><div class="v" style="--h:52.9%">2,436</div><div class="barv" style="--h:52.9%"></div></div>
    </div>
    <div class="collbl"><span>9단지</span><span>13단지</span><span>12단지</span><span>4단지</span></div>
    <p class="cap">각 단지 입찰·총회 보도의 계획 가구수이며 심의 단계마다 바뀔 수 있습니다. 막대 길이는 최댓값 3,961가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 목동12단지 재건축, GS건설 확정"),
    ("02-size", "1,860가구가 2,810가구로"),
    ("03-path", "두 번 단독, 그래서 수의계약"),
    ("04-cost", "3.3㎡당 공사비, 목동 단지 비교"),
    ("05-map", "목동 시공사, 지금 어디까지"),
    ("06-check", "목동12단지 재건축 체크 3가지"),
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

ARTICLE = '''<article data-tags="목동12단지재건축,목동12단지,GS건설,목동재건축,리플리제자이,양천구재건축,시공사선정,수의계약,목동신시가지,재건축공사비">
  <h2>목동12단지 재건축 GS건설 확정, 공사비 1.8조</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 목동12단지 재건축, GS건설 확정"></span>

  <p><strong>3줄 요약</strong><br>목동12단지 재건축 시공사로 GS건설이 11월 22일 총회에서 선정됐습니다.<br>공사비는 약 1조7,887억원, 3.3㎡당 980만원이고 1,860가구를 최고 43층 2,810가구로 다시 짓는 계획입니다.<br>목동 14개 단지 가운데 시공사가 정해진 곳은 10·13·12단지 세 곳이 됐고, 다음 순서는 4단지 재입찰과 9단지 입찰 마감입니다.</p>

  <p>목동12단지 재건축 시공사가 GS건설로 정해졌습니다. GS건설은 지난 22일 열린 목동12단지 재건축정비사업조합 시공사 선정 총회에서 시공사로 선정됐다고 23일 밝혔습니다. 공사비는 약 1조7,887억원입니다. 입찰을 두 번 했는데 두 번 다 GS건설 한 곳만 들어와 수의계약으로 넘어갔고, 그 결과를 조합원 투표로 확정한 자리였습니다. 아래에서 규모, 선정 과정, 공사비, 목동 다른 단지와의 비교를 차례로 정리했습니다.</p>

  <h3>목동12단지 재건축, 1,860가구가 2,810가구로</h3>
  <div class="chart" data-img="카드뉴스 2번 · 1,860가구가 2,810가구로">
    <h3>목동12단지 지금과 계획 (가구)</h3>
    <div class="bar"><label>재건축 계획</label>
      <div class="rail"><div class="fill" style="width:100%">2,810가구</div></div></div>
    <div class="bar"><label>지금</label>
      <div class="rail"><div class="fill gray" style="width:66.2%">1,860가구</div></div></div>
    <p class="cap">입찰·총회 보도의 계획 기준입니다. 최고 층수는 15층에서 43층으로 바뀌는 계획이며 심의 단계에서 달라질 수 있습니다. 막대 길이는 2,810가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>결론부터 말하면 가구 수가 950가구 늘어납니다. 지금은 최고 15층, 1,860가구 단지인데 계획대로라면 최고 43층, 2,810가구가 됩니다. 1.51배입니다. 목동 재건축 단지 가운데서는 9단지(3,961세대), 13단지(3,852세대) 다음 규모입니다.</p>
  <p>늘어나는 950가구가 왜 중요한지도 봐야 합니다. 조합원 몫을 뺀 나머지가 일반분양과 공공 물량으로 나오는데, 일반분양이 많을수록 조합원이 내는 분담금이 줄어드는 구조입니다. 다만 일반분양과 공공 물량의 정확한 나눔은 사업시행계획 단계에서 정해지니 지금 숫자로 분담금을 계산하기는 이릅니다.</p>
  <p>자주 헷갈리는 점이 있습니다. 시공사가 정해졌다고 가구 수와 층수가 확정된 것은 아닙니다. 이 숫자는 정비계획 기준이고 건축심의와 사업시행인가를 거치며 바뀔 수 있습니다. 잠실 장미1·2·3차도 심의 과정에서 계획 가구가 5,105가구에서 5,129가구로 바뀐 적이 있습니다.</p>
  <p>누가 영향을 받는지도 나눠 볼 만합니다. 지금 사는 조합원 1,860가구는 새 아파트를 받는 대신 분담금과 이주를 준비해야 하고, 세입자는 언제 이사를 나가야 하는지가 궁금할 겁니다. 이주는 보통 관리처분계획인가 뒤에 시작되기 때문에 시공사 선정 단계에서는 아직 멀었습니다. 지금 전세 계약을 고민하는 분이라면 계약 기간 안에 이주가 시작될 가능성은 낮은 편이지만, 조합 일정이 빨라지는 경우도 있으니 조합 공지를 함께 보시는 게 좋습니다.</p>

  <h3>두 번 단독 응찰, 그래서 수의계약</h3>
  <div class="chart" data-img="카드뉴스 3번 · 두 번 단독, 그래서 수의계약">
    <h3>목동12단지 시공사 선정 흐름</h3>
    <h4>1차 입찰</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">8월</span>
      <span class="desc">GS건설 단독 응찰로 유찰.</span></div>
    <h4>2차 입찰</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9월</span>
      <span class="desc">2차 현장설명회 뒤 다시 GS건설 단독.</span></div>
    <h4>시공사 선정 총회</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 22일</span>
      <span class="desc">조합원 투표로 GS건설 선정.</span></div>
    <p class="cap">머니투데이방송(8월 31일·9월 8일)과 한국경제(11월 23일) 보도 기준입니다. 총회 찬성 비율은 조합 공지로 확인이 필요합니다.</p>
  </div>
  <p>목동12단지는 경쟁입찰이 성사되지 않았습니다. 7월 현장설명회에는 대우건설과 GS건설 등 4개사가 참석해 목동 첫 경쟁입찰이 나오나 하는 관측도 있었지만, 8월 말 1차 입찰 마감 때 입찰서를 낸 곳은 GS건설 하나였습니다. 9월 2차 입찰도 같은 모습이었습니다.</p>
  <p>정비사업 시공사 선정은 경쟁입찰이 원칙이지만 두 번 이상 유찰되면 조합이 수의계약으로 갈 수 있습니다. 12단지는 이 경로를 밟아 GS건설을 우선협상대상자로 정했고, 22일 총회에서 조합원 투표로 확정했습니다. 목동10단지(현대건설)와 13단지(삼성물산)도 같은 길이었습니다. 10단지는 투표자 95.9%, 13단지는 95.7%가 찬성했습니다.</p>
  <p>여기서 자주 헷갈리는 말이 우선협상대상자와 시공사 선정입니다. 우선협상대상자는 조합이 계약 조건을 먼저 협상할 상대로 정한 단계이고, 시공사 선정은 그 결과를 조합원 총회에서 의결한 단계입니다. 12단지는 22일 총회로 두 번째 단계까지 마쳤습니다. 다만 총회 의결 뒤에도 공사비와 세부 조건을 담은 도급 본계약은 따로 맺습니다. 12단지 총회의 찬성 비율은 이 글을 쓰는 시점까지 보도에서 확인하지 못했습니다.</p>
  <p>단독 응찰이 조합원에게 불리한가는 따로 따져 볼 문제입니다. 경쟁이 없으면 공사비와 조건을 놓고 협상할 지렛대가 약해진다는 지적이 있습니다. 반대로 사업 속도는 빨라집니다. 12단지는 공사비를 다른 목동 단지와 같은 3.3㎡당 980만원으로 맞췄으니, 숫자만 보면 단독이라고 공사비가 튄 것은 아닙니다.</p>

  <h3>목동12단지 공사비, 3.3㎡당 980만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 3.3㎡당 공사비, 목동 단지 비교">
    <h3>목동 재건축 3.3㎡당 공사비 (만원)</h3>
    <div class="bar"><label>4단지</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,010만</div></div></div>
    <div class="bar"><label>12단지</label>
      <div class="rail"><div class="fill" style="width:97%">980만</div></div></div>
    <div class="bar"><label>13단지 · 9단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980만</div></div></div>
    <div class="bar"><label>8단지</label>
      <div class="rail"><div class="fill gray" style="width:95.5%">965만</div></div></div>
    <p class="cap">각 단지 입찰공고·총회 보도의 예정 공사비 기준입니다. 막대 길이는 최댓값 1,010만원을 기준으로 맞췄습니다.</p>
  </div>
  <p>목동12단지의 3.3㎡당 공사비 980만원은 목동에서 중간 수준입니다. 13단지와 9단지가 같은 980만원이고, 8단지는 965만원, 4단지는 1,010만원으로 처음 1천만원을 넘겼습니다. 4단지와 비교하면 30만원, 약 3% 낮습니다.</p>
  <p>이 3%가 얼마나 큰지 12단지 공사비로 바꿔 보면 이렇습니다. 같은 면적을 3.3㎡당 1,010만원으로 지었다면 공사비는 약 1조8,435억원이 됩니다. 지금 금액보다 약 548억원 많습니다. 2,810가구로 나누면 가구당 약 1,950만원입니다. 공사비 단가가 조금만 움직여도 조합 전체로는 수백억원이 오가는 셈입니다.</p>
  <p>예시로 계산해 보면 감이 옵니다. 총공사비 1조7,887억원을 계획 가구 2,810가구로 단순히 나누면 가구당 약 6억3,700만원입니다. 같은 방식으로 13단지(2조3,763억원, 3,852세대)는 약 6억1,700만원입니다. 단지마다 평형 구성이 달라 정확한 비교는 아니지만, 짓는 데 드는 돈이 가구당 6억원을 넘는다는 점은 분담금을 생각할 때 기준이 됩니다.</p>
  <p>GS건설은 단지명으로 '리플리제 자이'를 제안했고 해외 설계사 겐슬러와 협업한 설계안을 내놨습니다. 다만 제안명은 확정된 이름이 아니고, 최종 단지명은 조합이 따로 정합니다.</p>

  <h3>목동 시공사, 지금 어디까지</h3>
  <div class="chart" data-img="카드뉴스 5번 · 목동 시공사, 지금 어디까지">
    <h3>목동 재건축 시공사 현황 (2026년 11월 24일)</h3>
    <h4>10단지 · 현대건설</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10월 18일</span>
      <span class="desc">총회 선정, 찬성 95.9%.</span></div>
    <h4>13단지 · 삼성물산</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 7일</span>
      <span class="desc">총회 선정, 찬성 95.7%.</span></div>
    <h4>12단지 · GS건설</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 22일</span>
      <span class="desc">총회 선정.</span></div>
    <h4>4단지 · 9단지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">재입찰</span>
      <span class="desc">4단지 현대 단독 유찰, 9단지는 내년 1월 마감.</span></div>
    <p class="cap">각 단지 총회·입찰 보도 기준입니다. 4단지는 11월 16일 마감에서 현대건설 한 곳만 응찰해 유찰됐고, 9단지 입찰 마감은 2027년 1월 11일입니다.</p>
  </div>
  <p>목동에서 시공사가 확정된 단지는 10·13·12단지 세 곳이 됐습니다. 세 곳 모두 단독 응찰 끝에 수의계약으로 왔고, 건설사도 현대건설, 삼성물산, GS건설로 겹치지 않았습니다. 목동 14개 단지가 대형 건설사별로 나뉘는 모양입니다.</p>
  <p>다음에 무엇이 열리는지도 적어 둡니다. 4단지는 재입찰 공고를 낸 뒤 다시 한 곳만 들어오면 수의계약으로 갈 수 있고, 조합은 내년 2월 총회를 목표로 잡고 있습니다. 9단지(3,961세대, 공사비 2조6,067억원)는 2027년 1월 11일 입찰 마감입니다. 목동 첫 경쟁입찰이 나올지는 9단지가 가늠자입니다.</p>
  <p>목동 재건축이 이렇게 빠르게 시공사를 정하는 배경도 볼 만합니다. 신시가지 14개 단지가 비슷한 시기에 지어져 재건축 일정도 비슷하게 몰렸고, 건설사들은 한 단지에 힘을 모으는 쪽을 택하고 있습니다. 그래서 단지마다 경쟁 대신 한 곳이 들어오는 모습이 반복됩니다. 남은 단지들도 이 흐름을 따를지, 9단지에서 처음으로 경쟁이 붙을지가 내년 초 목동 재건축의 관전 포인트입니다.</p>
  <p>12단지 자체로는 이제 공사 도급 본계약과 사업시행계획인가 준비가 남았습니다. 이 단계에서 가구 수와 평형 구성이 다시 조정될 수 있고, 조합원 분양 신청과 관리처분계획은 그 뒤입니다. 매수를 고민한다면 조합원 지위 양도가 가능한 단계인지부터 조합이나 정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하시는 게 순서입니다.</p>

  <h3>목동12단지 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 목동12단지 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="mk12-06-check.png" src="../images/cards/report/mk12-06-check.png" alt="체크포인트 카드 · 1. 계획 가구는 확정 전, 2. 제안 단지명은 확정 아님, 3. 조합원 지위 양도" loading="lazy" width="1080" height="1080">
    <figcaption>목동12단지 재건축을 볼 때 챙길 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>계획 가구는 확정 전</strong>. 2,810가구·43층은 심의와 인가를 거치며 바뀔 수 있습니다.</li>
    <li><strong>제안 단지명은 확정 아님</strong>. '리플리제 자이'는 GS건설 제안입니다.</li>
    <li><strong>조합원 지위 양도</strong>. 단계마다 다르니 조합·구청에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>목동12단지 재건축</strong> 시공사는 11월 22일 총회에서 GS건설로 확정됐습니다. 두 차례 단독 응찰 뒤 수의계약으로 왔고, 공사비는 약 1조7,887억원, 3.3㎡당 980만원입니다. 1,860가구를 최고 43층 2,810가구로 다시 짓는 계획입니다. <span class="mark">목동은 10·13·12단지 세 곳이 시공사를 정했고, 다음은 4단지 재입찰과 내년 1월 9단지 입찰 마감입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 공사비와 가구수는 입찰·총회 보도 기준이며 계획 가구·층수는 심의 단계에서 바뀔 수 있습니다. 총회 찬성 비율은 이 글에서 확인하지 못했습니다. 조합원 지위 양도 등 거래 조건은 조합·양천구청·정비사업 정보몽땅에서 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 한국경제 GS건설 목동12단지 재건축 수주(2026-11-23) · 머니투데이방송 목동12단지 GS건설 단독 응찰로 유찰(2026-08-31) · 머니투데이방송 성수2지구·목동12단지 2차 현설(2026-09-08) · 머니투데이방송 목동12단지 현설 4개사(2026-07-15) · 머니투데이방송 목동4단지 현대건설 단독 응찰(2026-11-16) · 머니투데이방송 목동10단지·13단지 시공사 선정(2026-10-18·11-07)<br>
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
for v, hh in ((3852, 83.6), (2810, 61.0), (2436, 52.9)):
    assert round(v / 3961 * 86, 1) == hh
assert round(1860 / 2810 * 100, 1) == 66.2 and 2810 - 1860 == 950 and round(2810 / 1860, 2) == 1.51
assert round(980 / 1010 * 100, 1) == 97.0 and round(965 / 1010 * 100, 1) == 95.5 and round(30 / 1010 * 100) == 3
assert round(178870000 / 2810 / 100) == 637 and round(17887 * 1010 / 980) == 18435 and 18435 - 17887 == 548 and round(5480000 / 2810) == 1950 and round(237630000 / 3852 / 100) == 617
KW = "목동12단지 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("목동12단지재건축")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
