# -*- coding: utf-8 -*-
"""리포트 #130 (2026-11-19 목) 디에이치 반포124 예상 분양가 vs 원베일리 실거래. #129를 복제해 교체한다.

메인 검색어: 디에이치 반포124
요일 종류: 목요일 청약 단지 한 곳 깊게 · 비교형 (분양가 vs 주변 실거래). 이번 주 청약 단독 글은 #127(월) 다음 두 번째.

수치와 검산
  사건일과 오늘의 간격: 비즈워치 '12월 분양·25억 넘으면 잔금 대출 2억' 11/12 → 7일. 서울시 장애인 기관추천 안내
    '모집공고 11.27 예정' (신청 11/10~12) → 리드는 '공고 D-8'. #103(10/24) 뒤 26일, 새 숫자는 원베일리 비교·대출 2억.
  일반분양 1,832 (59㎡ 281 · 80㎡ 23 · 84㎡ 1,358 · 99㎡ 82 · 114㎡ 44 · 130㎡ 44) · 다른 매체 1,801 · 총 5,007
  3.3㎡당 8,000만~1억 거론 · 9,000만 가정 84㎡ 30억6,000 · 1억 가정 34억 · 59㎡ 9,000만 가정 22억5,000
  원베일리 84㎡: 2025년 3월 70억(12층, 3.3㎡당 2억 첫 돌파 보도) · 2025년 6월 72억(헤럴드경제, 등기부 기준)
  일정(계획): 공고 11/27 · 특공 12/7 · 1순위 12/8 · 특공 당첨 12/16 · 입주 2027년 하반기(보도)
  기관추천 장애인 특공 12세대(59A 1 · 59B 1 · 84A 4 · 84B 6), 포기서약 11/30 12시
  대시보드 세로 (2억 → 86): 1억 43 · 9,000만 38.7
  카드2 가로 (72 → 100): 70 97.2 · 34 47.2 · 30.6 42.5
  카드5: 30.6 − 2 = 28.6

단정하지 않은 것
  · 분양가: 업계 추정 · 일반분양 수: 공고 확인 · 원베일리 지금 시세: 2025년 거래라 현재 값 아님
  · 대출 한도 2억: 보도 인용, 개인 한도는 은행 · 시세차익: 관측
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-18-remodeling-consent.html"
SLUG, PRE = "2026-11-19-banpo124-vs-onebaily", "dbw"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 130, "2026-11-19"
PREV_SLUG = "remodeling-consent"
BANNED = ["리모델링 동의율", "주택법 시행령"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "디에이치 반포124 분양가, 원베일리 70억과 비교하면"
DESC = ("디에이치 반포124 모집공고가 11월 27일로 예정돼 있습니다. 84㎡ 분양가는 3.3㎡당 9,000만원 가정 시 30억6,000만원으로, "
        "옆 단지 래미안 원베일리 84㎡ 실거래 70억대의 절반이 안 됩니다. 일정, 평형, 필요한 자기 돈을 비교했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="84㎡ 추정 분양가 30억대, 원베일리 84㎡ 실거래 70억대. 25억 넘으면 잔금 대출 2억. 모집공고 11월 27일 예정.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">디에이치 반포124,<br>원베일리와 비교하면</h1>
  <p class="sub"><strong>디에이치 반포124</strong> 입주자 모집공고가 <strong>11월 27일</strong>로 예정돼 있습니다. 84㎡ 분양가는 업계 추정으로 30억원대이고, 바로 옆 래미안 원베일리 84㎡는 70억원대에 거래됐습니다. <span class="mark">다만 분양가는 아직 추정이고, 옆 단지 가격은 2025년 거래입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 공고 D-8</div><div class="kw">11월 27일</div>
      <p>입주자 <strong>모집공고</strong> 예정일.</p></div>
    <div class="kcard"><div class="hot">84㎡ 추정</div><div class="kw">30.6억</div>
      <p>3.3㎡당 <strong>9,000만원</strong> 가정.</p></div>
    <div class="kcard"><div class="hot">원베일리 84㎡</div><div class="kw">70억대</div>
      <p>2025년 <strong>실거래</strong> 보도.</p></div>
    <div class="kcard"><div class="hot">잔금 대출</div><div class="kw">2억</div>
      <p>분양가 <strong>25억 초과</strong> 시 (보도).</p></div>
  </div>

  <div class="colchart">
    <h3>3.3㎡당 가격, 원베일리와 반포124 (원)</h3>
    <span class="badge">추정 분양가는 절반 아래</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">2억</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:43%">1억</div><div class="barv" style="--h:43%"></div></div>
      <div class="col"><div class="v gtx" style="--h:38.7%">9,000만</div><div class="barv" style="--h:38.7%"></div></div>
    </div>
    <div class="collbl"><span>원베일리 84㎡ 거래</span><span>반포124 상단 추정</span><span>반포124 중간 추정</span></div>
    <p class="cap">원베일리는 2025년 3월 84㎡ 70억원 거래로 3.3㎡당 2억원을 처음 넘었다는 보도 기준입니다. 반포124는 업계에서 거론되는 추정치로 확정 분양가가 아닙니다. 막대 길이는 최댓값 2억원을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 디에이치 반포124 vs 원베일리"),
    ("02-vs", "디에이치 반포124 84㎡, 옆 단지 절반 아래"),
    ("03-when", "디에이치 반포124 공고까지 8일"),
    ("04-type", "넷 중 세 집은 84㎡"),
    ("05-cash", "대출은 2억, 나머지는 내 돈"),
    ("06-check", "반포124 청약 전 체크 3가지"),
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


ARTICLE = '''<article data-tags="디에이치반포124,반포124,반포주공1단지,래미안원베일리,반포청약,분양가상한제,로또청약,서초구청약,디에이치,현대건설">
  <h2>디에이치 반포124 분양가, 원베일리 70억과 비교하면</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 디에이치 반포124 vs 원베일리"></span>

  <p><strong>3줄 요약</strong><br>디에이치 반포124 입주자 모집공고가 11월 27일로 예정돼 있고, 1순위 청약은 12월 8일로 계획돼 있습니다.<br>84㎡ 분양가는 3.3㎡당 9,000만원을 가정하면 30억6,000만원으로, 옆 단지 래미안 원베일리 84㎡ 실거래 70억대의 절반이 안 됩니다.<br>분양가가 25억원을 넘으면 잔금 대출이 2억원에 그친다는 보도가 있어, 청약 전에 자기 돈부터 계산해야 합니다.</p>

  <p>디에이치 반포124 모집공고가 8일 앞으로 다가왔습니다. 반포주공1단지 1·2·4주구를 재건축한 5,007가구 단지이고, 서울시가 낸 장애인 특별공급 기관추천 안내문에 공고 예정일이 11월 27일로 적혀 있습니다. <span class="mark">가장 많이 묻는 건 결국 하나입니다. 옆 단지보다 얼마나 싸냐는 것입니다.</span> 분양가는 아직 확정 전이라 업계 추정으로 계산하고, 비교 대상은 길 하나 건너 있는 래미안 원베일리로 잡았습니다.</p>

  <h3>디에이치 반포124 분양가, 원베일리와 얼마나 차이 나나</h3>
  <div class="chart" data-img="카드뉴스 2번 · 디에이치 반포124 84㎡, 옆 단지 절반 아래">
    <h3>전용 84㎡ 가격 비교 (억원)</h3>
    <div class="bar"><label>원베일리 2025.6</label>
      <div class="rail"><div class="fill gray" style="width:100%">72</div></div></div>
    <div class="bar"><label>원베일리 2025.3</label>
      <div class="rail"><div class="fill gray" style="width:97.2%">70</div></div></div>
    <div class="bar"><label>반포124 1억 가정</label>
      <div class="rail"><div class="fill" style="width:47.2%">34</div></div></div>
    <div class="bar"><label>반포124 9,000만 가정</label>
      <div class="rail"><div class="fill" style="width:42.5%">30.6</div></div></div>
    <p class="cap">원베일리는 2025년 3월 70억원(12층) 거래와 2025년 6월 72억원(헤럴드경제, 등기부 기준) 보도 기준입니다. 반포124는 3.3㎡당 추정 단가에 84㎡ 공급면적을 곱한 가정치입니다. 막대 길이는 최댓값 72억원을 기준으로 맞췄습니다.</p>
  </div>
  <p>추정대로라면 절반이 안 됩니다. 업계에서는 디에이치 반포124 분양가를 3.3㎡당 8,000만원에서 1억원 사이로 거론하고, 9,000만원 안팎을 많이 봅니다. 9,000만원이면 84㎡가 30억6,000만원, 1억원이면 34억원입니다. 원베일리 84㎡는 2025년 3월 70억원에 거래되며 국민평형 처음으로 3.3㎡당 2억원을 넘었고, 6월에는 72억원 거래가 보도됐습니다.</p>
  <p>이렇게 차이가 나는 건 분양가상한제 때문입니다. 서초구는 상한제 적용 지역이라 분양가를 주변 시세가 아니라 땅값과 건축비 기준으로 정합니다. 그래서 새 아파트인데도 주변 기존 아파트보다 싸게 나오고, '로또 청약'이라는 말이 붙습니다. 비즈워치는 주변 시세와 비교해 20억~30억원의 시세차익을 기대할 수 있다고 봤습니다.</p>
  <p>다만 이 비교에는 빈칸이 두 개 있습니다. 하나는 반포124 분양가가 아직 추정이라는 점이고, 다른 하나는 원베일리 가격이 2025년 거래라는 점입니다. 1년 사이 강남 아파트값은 오르내림이 있었고, 지금 원베일리 84㎡가 얼마에 거래되는지는 국토교통부 실거래가 공개시스템에서 최근 거래월을 직접 봐야 합니다. 시세차익은 입주 때 시세에 따라 달라지는 관측이지 정해진 이익이 아닙니다.</p>
  <p>같은 반포 안에서 비교하는 이유도 있습니다. 원베일리는 2023년 입주한 신축이고, 반포124와 길 하나를 사이에 두고 있습니다. 학군과 한강 접근성이 비슷해서 반포124 입주 뒤 시세를 가늠할 때 가장 먼저 꼽히는 단지입니다. 다만 원베일리는 이미 입주한 단지이고 반포124는 2027년 하반기 입주 예정이라, 입주 시점의 금리와 대출 규제에 따라 실제 차이는 지금 계산과 달라질 수 있습니다.</p>

  <h3>디에이치 반포124 청약 일정, 공고까지 8일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 디에이치 반포124 공고까지 8일">
    <h3>디에이치 반포124 청약 일정 (계획)</h3>
    <h4>모집공고</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11/27</span>
      <span class="desc">확정 분양가와 자격 요건이 여기서 나온다.</span></div>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12/7</span>
      <span class="desc">특공 접수. 당첨 발표는 12월 16일 계획.</span></div>
    <h4>일반 1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12/8</span>
      <span class="desc">일반공급 1순위 접수 계획.</span></div>
    <p class="cap">서울시 장애인 특별공급 기관추천 안내(공고 11월 27일 예정)와 10월 보도된 계획 일정 기준입니다. 최종 일정은 모집공고와 청약홈으로 확인하십시오.</p>
  </div>
  <p>공고는 11월 27일 금요일로 예정돼 있습니다. 보도된 계획대로라면 12월 7일 특별공급, 12월 8일 일반 1순위를 받고, 특별공급 당첨자는 12월 16일 발표합니다. 공고부터 1순위까지 열하루뿐이라, 통장 순위와 무주택 여부는 공고 전에 미리 확인해 두는 게 좋습니다. 입주는 2027년 하반기로 보도됐습니다.</p>
  <p>장애인 특별공급 기관추천은 이미 진행됐습니다. 서울시 안내에 따르면 추천 물량은 12세대(59A 1, 59B 1, 84A 4, 84B 6)이고, 주민센터 신청은 11월 10일부터 12일까지였습니다. 추천을 받았지만 청약하지 않을 사람은 11월 30일 낮 12시까지 포기서약서를 내야 합니다. 추천을 받은 뒤 아무 말 없이 청약하지 않으면 다른 대기자에게 기회가 가지 않습니다. 그래서 포기할 생각이라면 기한 안에 서약서를 내는 게 맞습니다. 이 기한도 공고 사흘 뒤라 공고문을 보고 결정할 수 있습니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 일정은 10월에 나온 계획이고, 비즈워치는 11월 12일 기사에서 '12월 분양 예정, 분양가는 미공개'라고만 썼습니다. 날짜가 하루이틀 밀릴 수 있으니 청약홈 공고가 뜨는 날 다시 맞춰 보십시오.</p>
  <p>서초구는 투기과열지구라 1순위 자격이 까다롭습니다. 청약통장 가입 2년이 지나야 하고, 세대주여야 하며, 5년 안에 다른 집에 당첨된 적이 없어야 합니다. 서울 거주자 우선공급 비율과 거주 기간 요건은 공고문에 나오니, 이사한 지 얼마 안 된 분은 전입일을 먼저 확인해 두십시오. 예치금도 면적별로 다른데, 84㎡ 이하 서울은 300만원, 그보다 크면 더 많이 필요합니다.</p>

  <h3>평형 구성, 넷 중 세 집은 84㎡</h3>
  <div class="chart" data-img="카드뉴스 4번 · 넷 중 세 집은 84㎡">
    <h3>일반분양 평형별 가구 (가구)</h3>
    <div class="bar"><label>84㎡</label>
      <div class="rail"><div class="fill" style="width:100%">1,358</div></div></div>
    <div class="bar"><label>59㎡</label>
      <div class="rail"><div class="fill gray" style="width:20.7%"></div><span class="railval" style="left:calc(20.7% + 12px)">281</span></div></div>
    <div class="bar"><label>99㎡</label>
      <div class="rail"><div class="fill gray" style="width:6%"></div><span class="railval" style="left:calc(6% + 12px)">82</span></div></div>
    <div class="bar"><label>114·130㎡</label>
      <div class="rail"><div class="fill gray" style="width:3.2%"></div><span class="railval" style="left:calc(3.2% + 12px)">각 44</span></div></div>
    <p class="cap">일반분양 1,832가구 기준 보도입니다(80㎡ 23가구 별도). 다른 매체는 1,801가구로 보도했습니다. 막대 길이는 최댓값 1,358가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>84㎡가 1,358가구로 일반분양의 74%입니다. 59㎡는 281가구, 99㎡ 82가구, 114㎡와 130㎡가 각각 44가구, 80㎡가 23가구입니다. 일반분양 합계는 매체에 따라 1,832가구와 1,801가구로 31가구가 다르고, 최종 숫자는 공고문에 나옵니다.</p>
  <p>평형을 고를 때는 가격 구간을 같이 봐야 합니다. 9,000만원 가정으로 59㎡는 22억5,000만원, 84㎡는 30억6,000만원입니다. 59㎡는 25억원 아래이고 84㎡는 위입니다. 이 25억원이 잔금 대출 한도가 갈리는 선이라, 같은 단지라도 평형에 따라 필요한 자기 돈이 크게 달라집니다.</p>
  <p>당첨 가능성도 평형마다 다릅니다. 84㎡는 물량이 가장 많아 가점이 조금 낮아도 노려볼 여지가 있고, 59㎡는 281가구로 적은 데다 가격이 상대적으로 낮아 신청이 몰릴 가능성이 큽니다. 99㎡ 이상은 물량이 적고 가격이 높아 자금 여력이 있는 소수가 겨루는 구조입니다.</p>

  <h3>디에이치 반포124, 자기 돈은 얼마 필요하나</h3>
  <div class="chart" data-img="카드뉴스 5번 · 대출은 2억, 나머지는 내 돈">
    <h3>84㎡ 예시 계산 (3.3㎡당 9,000만 가정)</h3>
    <h4>추정 분양가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">30.6억</span>
      <span class="desc">84㎡, 확정 전 가정치.</span></div>
    <h4>잔금 주담대</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2억</span>
      <span class="desc">분양가 25억원 초과 시 한도(보도).</span></div>
    <h4>자기 돈</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">28.6억</span>
      <span class="desc">계약금·중도금 방식은 공고로.</span></div>
    <p class="cap">비즈워치(2026년 11월 12일) 보도 기준입니다. 개인별 대출 한도와 중도금 대출 여부는 모집공고와 은행에서 확인하십시오.</p>
  </div>
  <p>84㎡라면 28억원대가 내 돈이어야 합니다. 비즈워치는 분양가가 25억원을 넘으면 잔금을 치를 때 받는 주택담보대출 한도가 2억원에 그친다고 전했습니다. 30억6,000만원에서 2억원을 빼면 28억6,000만원입니다. 1억원 가정이면 34억원에서 2억원을 뺀 32억원입니다.</p>
  <p>그래서 이 단지는 당첨 가능성보다 자금 계획이 먼저입니다. 계약금 비율과 중도금 대출을 시공사가 알선하는지는 공고에 나오는데, 아직 공개되지 않았습니다. 당첨된 뒤 돈을 못 맞춰 계약을 포기하면 재당첨 제한 같은 불이익이 따를 수 있으니, 공고문의 자금 일정표를 먼저 보는 게 순서입니다.</p>
  <p>59㎡라면 계산이 조금 달라집니다. 9,000만원 가정으로 22억5,000만원이라 25억원 아래이고, 이 구간은 잔금 대출 한도가 2억원보다 큽니다. 다만 정확한 한도는 소득과 기존 대출에 따라 달라지므로 은행에서 미리 물어보는 게 좋습니다. 어느 평형이든 계약 뒤 실거주 의무가 붙는지도 공고문에서 같이 확인해야 합니다.</p>

  <h3>반포124 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 반포124 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="dbw-06-check.png" src="../images/cards/report/dbw-06-check.png" alt="체크포인트 카드 · 1. 11월 27일 공고문, 2. 자금 계획 먼저, 3. 시세차익은 관측" loading="lazy" width="1080" height="1080">
    <figcaption>디에이치 반포124 청약 전, 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>11월 27일 공고문</strong>. 확정 분양가, 거주 요건, 계약금 비율이 여기서 나옵니다.</li>
    <li><strong>자금 계획 먼저</strong>. 분양가 25억원을 넘으면 잔금 대출이 2억원이라는 보도가 있습니다. 내 한도는 은행에서 확인하십시오.</li>
    <li><strong>시세차익은 관측</strong>. 원베일리 70억대는 2025년 거래입니다. 최근 거래는 실거래가 공개시스템에서 보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>디에이치 반포124</strong> 모집공고가 11월 27일로 예정돼 있습니다. 84㎡ 분양가는 3.3㎡당 9,000만원 가정으로 30억6,000만원, 옆 단지 원베일리 84㎡ 실거래는 2025년 70억~72억원이었습니다. <span class="mark">추정대로면 절반이 안 되지만, 분양가는 확정 전이고 비교한 시세는 1년 전 거래입니다.</span> 25억원을 넘는 평형은 잔금 대출이 2억원이라 자기 돈이 28억원대 필요합니다. 1순위는 12월 8일 계획입니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 분양가는 업계 추정에 따른 가정 계산이고 확정 분양가는 입주자 모집공고로 확인하십시오. 원베일리 가격은 2025년 거래 보도 기준이며 현재 시세가 아닙니다. 청약 일정은 계획 단계 보도이고, 대출 한도는 개인별로 은행에서 확인해야 합니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 서울시 디에이치 반포124 장애인 특별공급 기관추천 안내(2026-11) · 비즈워치 반포124 12월 분양 예정(2026-11-12) · 이코노미스트 반포124 일반분양 1,801가구(2026-11-12) · 한국경제·아시아타임즈 반포124 일반분양 구성·일정(2026-10) · 헤럴드경제 원베일리 국평 72억(2025-10) · 국토교통부 실거래가 공개시스템<br>
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
for v, h in ((1, 43), (0.9, 38.7)):
    assert round(v / 2 * 86, 1) == h
for v, w in ((70, 97.2), (34, 47.2), (30.6, 42.5)):
    assert round(v / 72 * 100, 1) == w
assert round(30.6 - 2, 1) == 28.6 and round(9000 * 34 / 10000, 1) == 30.6
KW = "디에이치 반포124"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("디에이치반포124")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
