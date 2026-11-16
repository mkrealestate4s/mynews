# -*- coding: utf-8 -*-
"""리포트 #128 (2026-11-17 화) 목동4단지 재건축 입찰 유찰. #127을 복제해 교체한다.

메인 검색어: 목동4단지 재건축
요일 종류: 화요일 재건축·재개발 대표 단지 · 해설형. 같은 단지 #124(11/13)의 '결과' 후속(새 사실: 단독 응찰·유찰).

수치와 검산
  사건일과 오늘의 간격: 입찰 마감·유찰 11/16(월) 14시, 오늘에서 1일 전(리드) · 재입찰 공고 이르면 11/17(한 매체).
  결과: 현대건설만 제안서 제출 → 경쟁 불성립 유찰 (뉴스핌·아주경제·머니투데이방송·녹색경제신문 11/16)
  현설 9/30 4개사(현대·포스코이앤씨·HDC현산·제일건설) → 입찰 1곳, 불참 3곳. 포스코이앤씨는 1단지·목4동 도심복합사업으로 관심 이동(보도)
  조합: 양천구청(공공지원자) 보고 뒤 재입찰 공고 · 재입찰 현설에 현대만 오면 수의계약 전환 가능, 총회 의결 필요 · 목표 2027년 2월 안 선정 총회
  공사비 1조6,389억4,000만원 · 3.3㎡당 1,010만원 · 보증금 600억. 비교 10단지 990 · 12·13단지 980 · 8단지 965 (#124)
  1,382가구 → 최고 49층 2,436가구(공공 293). 단순 나눗셈 16,389.4억/2,436 = 약 6.7억
    대시보드 컬럼(4→86): 4 86 · 1 21.5 · 3 64.5
    카드2 가로(4→100): 4 100 · 1 25
    카드4 가로(1010→100): 990 98.0 · 980 97.0 · 965 95.5
  목동 선정: 6단지 DL 86.2% · 10단지 현대 95.9%(두 차례 유찰 뒤) · 13단지 삼성 95.7%

단정하지 않은 것
  · 현대건설 시공 확정 아님(재입찰·총회 남음) · 재입찰 공고일은 매체마다 다름 · 계획 가구수·층수 확정 전
  · 다른 3개사가 빠진 이유는 보도된 포스코이앤씨 건만 쓴다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-16-junghwa-raon.html"
DST = ROOT / "posts/2026-11-17-mokdong4-rebid.html"
SLUG, PRE = "2026-11-17-mokdong4-rebid", "mkr"
NO, DATE = 128, "2026-11-17"
PREV_SLUG = "junghwa-raon"
BANNED = ["라온프라이빗", "중화동", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "목동4단지 재건축 유찰, 현설 4곳 중 1곳만 냈다"
DESC = ("목동4단지 재건축 시공사 입찰이 11월 16일 현대건설 단독 응찰로 유찰됐습니다. "
        "현장설명회 4개사 중 1곳만 입찰했고, 조합은 재입찰 공고를 냅니다. "
        "유찰 뒤 절차, 공사비 1,010만원 비교, 목동10단지 사례와 확인할 점을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="11월 16일 마감, 현대건설만 입찰해 유찰. 재입찰에서도 단독이면 수의계약으로 갈 수 있습니다. 조합 목표는 내년 2월 총회입니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">목동4단지 재건축 유찰<br>현설 4곳 중 1곳만 냈다</h1>
  <p class="sub"><strong>목동4단지 재건축</strong> 시공사 입찰이 <strong>11월 16일</strong> 마감됐고, 현대건설 한 곳만 입찰서를 내 유찰됐습니다. <span class="mark">조합은 재입찰 공고를 내고, 그때도 한 곳뿐이면 수의계약으로 갈 수 있습니다. 시공사가 정해진 건 아닙니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 입찰 결과</div><div class="kw">유찰</div>
      <p>11/16 마감, <strong>현대건설 단독</strong>.</p></div>
    <div class="kcard"><div class="hot">현설 → 입찰</div><div class="kw">4 → 1</div>
      <p>3개사가 <strong>입찰하지 않았다</strong>.</p></div>
    <div class="kcard"><div class="hot">3.3㎡당 공사비</div><div class="kw">1,010만</div>
      <p>총 약 <strong>1조6,389억원</strong>.</p></div>
    <div class="kcard"><div class="hot">조합 목표</div><div class="kw">2월</div>
      <p>내년 2월 안 <strong>시공사 선정 총회</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>목동4단지 재건축 입찰, 현설과 실제 입찰 (곳)</h3>
    <span class="badge">4곳 중 1곳만 입찰</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">4</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:21.5%">1</div><div class="barv" style="--h:21.5%"></div></div>
      <div class="col dim"><div class="v" style="--h:64.5%">3</div><div class="barv" style="--h:64.5%"></div></div>
    </div>
    <div class="collbl"><span>현설 참석</span><span>입찰</span><span>불참</span></div>
    <p class="cap">머니투데이방송(9월 30일)·뉴스핌·아주경제(11월 16일) 보도 기준입니다. 현장설명회에는 현대건설·포스코이앤씨·HDC현대산업개발·제일건설이 참석했고, 입찰서는 현대건설만 냈습니다. 막대 길이는 최댓값 4곳을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 목동4단지 재건축 유찰, 현설 4곳 중 1곳만 냈다"),
    ("02-result", "목동4단지 재건축 입찰, 4곳 왔는데 1곳만 냈다"),
    ("03-next", "유찰 다음은 재입찰, 또 단독이면 수의계약"),
    ("04-cost", "3.3㎡당 1,010만원, 목동 최고 조건에도 단독"),
    ("05-mokdong", "목동 앞선 단지들, 단독 응찰이 흔했다"),
    ("06-check", "목동4단지 재건축 체크 3가지"),
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

ARTICLE = '''<article data-tags="목동4단지재건축,목동4단지,목동4단지유찰,목동재건축,목동시공사선정,현대건설,양천구재건축,목동신시가지,재건축수의계약,재건축입찰">
  <h2>목동4단지 재건축 유찰, 현설 4곳 중 1곳만 냈다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 목동4단지 재건축 유찰, 현설 4곳 중 1곳만 냈다"></span>

  <p><strong>3줄 요약</strong><br>목동4단지 재건축 시공사 입찰이 11월 16일 오후 2시에 마감됐는데, 현대건설 한 곳만 입찰서를 내 유찰됐습니다.<br>조합은 양천구청에 결과를 보고한 뒤 재입찰 공고를 내고, 재입찰에서도 한 곳뿐이면 총회를 거쳐 수의계약으로 갈 수 있습니다.<br>조합원과 매수를 생각하는 분은 재입찰 공고일과 내년 2월로 잡힌 선정 총회 일정을 보면 됩니다.</p>

  <p>목동4단지 재건축 입찰은 지난주 글에서 "경쟁이 붙을까"로 다뤘던 건입니다. 답은 어제 나왔습니다. 9월 30일 현장설명회에는 4개사가 왔지만 실제로 입찰서를 낸 곳은 현대건설 하나였습니다. <span class="mark">3.3㎡당 1,010만원, 목동에서 가장 높은 공사비를 내걸었는데도 경쟁은 성립하지 않았습니다.</span> 아래에서 유찰이 무슨 뜻인지, 다음 절차가 어떻게 되는지, 앞선 목동 단지들은 어땠는지 차례로 정리했습니다.</p>

  <h3>목동4단지 재건축 입찰, 4곳 왔는데 1곳만 냈다</h3>
  <div class="chart" data-img="카드뉴스 2번 · 목동4단지 재건축 입찰, 4곳 왔는데 1곳만 냈다">
    <h3>현장설명회와 실제 입찰 (곳)</h3>
    <div class="bar"><label>현설 참석</label>
      <div class="rail"><div class="fill gray" style="width:100%">4</div></div></div>
    <div class="bar"><label>입찰서 제출</label>
      <div class="rail"><div class="fill" style="width:25%">1</div></div></div>
    <p class="cap">머니투데이방송(9월 30일)·뉴스핌·아주경제(11월 16일) 보도 기준입니다. 막대 길이는 최댓값 4곳을 기준으로 맞췄습니다.</p>
  </div>
  <p>결론부터 말하면 이번 입찰은 유찰입니다. 조합은 16일 오후 2시에 입찰을 마감했고, 제안서를 낸 곳은 현대건설뿐이었습니다. 현장설명회에 참석했던 포스코이앤씨·HDC현대산업개발·제일건설 3곳은 입찰하지 않았습니다.</p>
  <p>정비사업 시공사 경쟁입찰은 두 곳 이상이 들어와야 성립합니다. 한 곳만 내면 그 회사를 바로 고르는 게 아니라 입찰 자체가 무효가 되고 처음부터 다시 받습니다. 그래서 "현대건설 단독 응찰"과 "현대건설 선정"은 다른 말입니다. 어제 나온 건 앞의 것입니다.</p>
  <p>이 결과로 영향을 받는 사람은 크게 둘입니다. 하나는 조합원입니다. 시공사가 늦게 정해질수록 사업시행인가, 관리처분, 이주로 이어지는 뒷일정이 같이 밀립니다. 다른 하나는 목동4단지 매수를 저울질하는 실수요자입니다. 시공사가 어디냐에 따라 단지 이름(브랜드)과 설계안이 달라지기 때문에, 지금은 아직 그 그림이 정해지지 않은 단계라는 점을 알고 보셔야 합니다.</p>
  <p>빠진 3곳 중 이유가 보도된 곳은 포스코이앤씨 하나입니다. 1단지와 목4동 도심복합사업 쪽으로 관심을 옮겼다는 내용입니다. 나머지 두 곳은 따로 밝힌 이유가 없습니다. 현설 직후부터 "현대건설만 제안서 작업에 착수했다"는 관측이 있었는데, 결과가 그 관측대로 나왔습니다.</p>

  <h3>목동4단지 재건축 다음 절차, 재입찰 뒤 수의계약 가능</h3>
  <div class="chart" data-img="카드뉴스 3번 · 유찰 다음은 재입찰, 또 단독이면 수의계약">
    <h3>목동4단지 시공사 선정, 남은 단계</h3>
    <h4>1차 입찰</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11/16</span>
      <span class="desc">현대건설 단독 응찰로 유찰.</span></div>
    <h4>재입찰</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">공고</span>
      <span class="desc">양천구청 보고 뒤 공고. 현설부터 다시.</span></div>
    <h4>선정 총회</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">2월</span>
      <span class="desc">조합 목표. 단독이면 수의계약 의결.</span></div>
    <p class="cap">뉴스핌·녹색경제신문·아주경제(11월 16일) 보도 기준입니다. 재입찰 공고일은 "이르면 17일"(한 매체)과 "구청 보고 뒤"로 매체마다 다르게 나왔습니다.</p>
  </div>
  <p>다음 단계는 재입찰입니다. 목동 재건축은 양천구청이 공공지원자로 들어가 있어서, 조합은 입찰 결과를 구청에 먼저 보고하고 재입찰 공고를 냅니다. 한 매체는 이르면 17일 공고가 나갈 수 있다고 전했고, 다른 매체들은 날짜 없이 "구청 보고 뒤"라고만 썼습니다.</p>
  <p>재입찰도 현장설명회부터 다시 엽니다. 여기에 현대건설만 오면 경쟁입찰이 두 번 성립하지 않은 셈이 되고, 조합은 수의계약으로 돌릴 수 있습니다. 수의계약도 조합이 혼자 정하는 게 아니라 총회 의결을 거쳐야 합니다. 현대건설은 재입찰에 참여하겠다는 입장을 냈습니다.</p>
  <p>조합이 밝힌 목표는 내년 2월 안 시공사 선정 총회입니다. 재입찰 공고와 현설, 마감까지 보통 한두 달이 걸리므로 일정이 빠듯합니다. 여기서 자주 헷갈리는 점이 있습니다. 수의계약이라고 해서 조건이 아무렇게나 정해지는 건 아닙니다. 1차 입찰 때 제시한 공사비와 조건을 기준으로 협상하고, 그 결과를 조합원이 총회에서 찬반 투표로 정합니다.</p>
  <p>날짜로 보면 이렇습니다. 1차 입찰은 9월 21일 공고, 9월 30일 현설, 11월 16일 마감으로 공고부터 마감까지 56일이 걸렸습니다. 재입찰이 이보다 짧게 끝나더라도 공고, 현설, 마감, 총회 공고를 차례로 밟아야 합니다. 그래서 재입찰 공고일이 나오면 내년 2월 목표를 지킬 수 있을지 거의 가늠이 됩니다.</p>

  <h3>3.3㎡당 1,010만원, 목동 최고 조건에도 단독</h3>
  <div class="chart" data-img="카드뉴스 4번 · 3.3㎡당 1,010만원, 목동 최고 조건에도 단독">
    <h3>목동 단지별 3.3㎡당 예정 공사비 (만원)</h3>
    <div class="bar"><label>4단지</label>
      <div class="rail"><div class="fill" style="width:100%">1,010</div></div></div>
    <div class="bar"><label>10단지</label>
      <div class="rail"><div class="fill gray" style="width:98%">990</div></div></div>
    <div class="bar"><label>12·13단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>8단지</label>
      <div class="rail"><div class="fill gray" style="width:95.5%">965</div></div></div>
    <p class="cap">모두 같은 항목(3.3㎡당 예정 공사비, 만원)이라 한 축에 놓았습니다. 막대 길이는 최댓값 1,010만원을 기준으로 맞췄습니다. 머니투데이방송·뉴시스(9~10월) 보도 기준입니다.</p>
  </div>
  <p>목동4단지의 예정 공사비는 1조6,389억4,000만원, 3.3㎡당 1,010만원입니다. 목동 재건축 가운데 처음으로 1천만원을 넘긴 금액이고, 8단지(965만원)보다 45만원, 약 4.7% 높습니다. 입찰보증금도 600억원으로 컸습니다.</p>
  <p>예정 공사비를 계획 가구수 2,436가구로 단순히 나누면 1가구당 약 6억7천만원입니다. 상가와 공공 293가구까지 섞인 단순 나눗셈이라 실제 조합원 분담금과는 다르지만, 사업 규모를 가늠하는 데는 쓸 만합니다. 반대로 총 공사비를 3.3㎡당 단가로 나누면 공사 면적이 대략 16만2천 평(약 53만6천㎡)으로 나옵니다. 이 면적에 단가 차이를 곱하면, 10단지 수준(990만원)과 4단지(1,010만원)의 20만원 차이는 약 325억원, 8단지 수준(965만원)과의 45만원 차이는 약 730억원입니다. 3.3㎡당 몇십만원 차이도 사업 전체로는 수백억원이 됩니다. <span class="mark">공사비를 가장 높게 내걸어도 경쟁이 붙지 않았다는 건, 지금 건설사들이 사업장을 고르는 기준이 공사비 하나만은 아니라는 뜻입니다.</span> 목동에서만 1단지, 8단지 등 시공사를 찾는 단지가 줄줄이 남아 있어 건설사들이 한 곳에 힘을 몰아 두는 모습입니다.</p>

  <h3>목동 앞선 단지들, 단독 응찰이 흔했다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 목동 앞선 단지들, 단독 응찰이 흔했다">
    <h3>목동 시공사 선정 결과</h3>
    <h4>6단지 · DL이앤씨</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">86.2%</span>
      <span class="desc">6월 총회 찬성률.</span></div>
    <h4>10단지 · 현대건설</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">95.9%</span>
      <span class="desc">두 차례 유찰 뒤 선정, 10월 18일.</span></div>
    <h4>13단지 · 삼성물산</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">95.7%</span>
      <span class="desc">11월 7일 총회 찬성률.</span></div>
    <p class="cap">투표자 대비 찬성 비율입니다. 10단지는 1,624명 중 1,557명, 13단지는 1,884명 중 1,803명입니다. 헤럴드경제(6월)·머니투데이방송(10월 18일·11월 7일) 보도 기준입니다.</p>
  </div>
  <p>목동에서는 이번이 처음 있는 일이 아닙니다. 목동10단지는 두 차례 유찰 끝에 현대건설을 우선협상대상자로 정했고, 10월 18일 총회에서 투표자 1,624명 중 1,557명(95.9%)이 찬성했습니다. 4단지가 지금 밟는 길이 10단지와 거의 같습니다.</p>
  <p>6단지(DL이앤씨, 86.2%)와 13단지(삼성물산, 95.7%)도 경쟁 없이 한 회사를 놓고 찬반 투표를 했습니다. 단독 응찰이라도 조합원 다수가 찬성하면 사업은 그대로 굴러갑니다. 오히려 경쟁입찰을 다시 붙이느라 일정이 늘어지는 쪽이 조합에는 부담입니다. 현대건설이 4단지까지 가져가면 목동에서는 10단지에 이어 두 번째 시공권입니다.</p>
  <p>목동신시가지는 1~14단지, 14개 단지가 모두 재건축을 밟고 있습니다. 이 가운데 시공사가 정해진 곳은 6·10·13단지 세 곳이고, 12단지는 GS건설과 선정 절차를 진행 중입니다. 4단지가 다섯 번째 차례입니다. 1단지와 8단지도 시공사 선정을 앞두고 있어서, 건설사 입장에서는 목동 안에서도 고를 곳이 많습니다. 4단지 결과를 두고 "목동에서 경쟁입찰이 붙기는 어렵다"는 해석이 나오는 이유입니다.</p>
  <p>자주 헷갈리는 점 하나를 짚고 가면, 단독 응찰이 조합원에게 꼭 손해라는 뜻은 아닙니다. 경쟁이 없으면 건설사가 조건을 더 얹어 줄 이유가 줄어드는 건 맞습니다. 대신 조합은 수의계약 협상에서 1차 입찰 조건을 바탕으로 다시 요구할 수 있고, 마지막에는 조합원 투표로 받을지 말지를 정합니다. 결국 따져 볼 것은 현대건설이 낸 제안서의 공사비, 공사 기간, 이주비·사업비 조건입니다.</p>
  <p>목동4단지는 1986년 준공한 1,382가구 단지로, 최고 49층 2,436가구(공공 293가구 포함)로 다시 짓는 계획입니다. 늘어나는 가구는 1,054가구입니다. 이 숫자는 심의 단계마다 바뀔 수 있어 아직 확정 전입니다.</p>

  <h3>목동4단지 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 목동4단지 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="mkr-06-check.png" src="../images/cards/report/mkr-06-check.png" alt="체크포인트 카드 · 1. 재입찰 공고일, 2. 시공사는 아직 미정, 3. 가구수는 확정 전" loading="lazy" width="1080" height="1080">
    <figcaption>목동4단지 재건축 유찰 뒤 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>재입찰 공고일</strong>. 공고가 나오면 현설 날짜와 마감일이 같이 정해집니다. 조합 공지와 양천구청 고시에서 봅니다.</li>
    <li><strong>시공사는 아직 미정</strong>. 단독 응찰은 결과가 아니라 절차의 한 단계입니다. 수의계약도 총회 의결이 있어야 정해집니다.</li>
    <li><strong>2,436가구는 확정 전</strong>. 조합원 지위 양도와 거래 제한은 조합·양천구청·정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>목동4단지 재건축</strong> 시공사 입찰은 11월 16일 현대건설 단독 응찰로 유찰됐습니다. 현설에 온 4개사 중 3곳이 빠졌고, 3.3㎡당 1,010만원이라는 목동 최고 공사비도 경쟁을 만들지 못했습니다. <span class="mark">다음은 재입찰 공고이고, 그때도 한 곳뿐이면 10단지처럼 수의계약과 총회 투표로 갑니다. 조합 목표는 내년 2월입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 입찰 결과는 뉴스핌·아주경제·머니투데이방송·녹색경제신문(2026-11-16) 보도, 공사비·현설은 머니투데이방송(2026-09-21·30)·뉴시스(2026-09-14) 보도, 단지별 찬성률은 헤럴드경제(2026-06-28)·머니투데이방송(2026-10-18·11-07) 보도 기준입니다. 시공사 선정과 계획 가구수는 확정 전이며 조합 공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 뉴스핌 '공사비 1.6조' 목동4단지, 현대건설 단독 입찰(2026-11-16) · 아주경제 공사비 1000만원 넘어도 경쟁 불발(2026-11-16) · 머니투데이방송 목동4단지, 현대건설 단독 응찰(2026-11-16) · 녹색경제신문 목동4단지 유찰(2026-11-16) · 머니투데이방송 목동4단지 현설에 4개사(2026-09-30) · 뉴시스 목동 재건축 공사비도 '평당 1000만원' 시대(2026-09-14) · 머니투데이방송 목동10단지·13단지 시공사 선정(2026-10-18·11-07)<br>
  © 2026 부동산 인사이트 · 데이터 기준일 {DATE} · <a href="../index.html">← 홈으로</a>
</footer>'''

exec(open(pathlib.Path(__file__).parent / "g_tail.py", encoding="utf-8").read().replace("DST.write_text", "pass  # "), globals())
for v, h in zip((4, 1, 3), (86, 21.5, 64.5)):
    assert round(v / 4 * 86, 1) == h
A = 16389.4e8 / 1010e4
assert round(A / 1000) == 162 and round(A * 3.3058 / 1000) == 536
assert round(20e4 * A / 1e8) == 325 and round(45e4 * A / 1e8) == 730
assert (56 == (30 - 21) + 31 + 16)
assert round(1010 / 965 * 100 - 100, 1) == 4.7 and round(16389.4 / 2436, 1) == 6.7
KW = "목동4단지 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("목동4단지재건축")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
