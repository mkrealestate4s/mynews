# -*- coding: utf-8 -*-
"""리포트 #129 (2026-11-18 수) 리모델링 동의율 75%→70%. #128을 복제해 교체한다.

메인 검색어: 리모델링 동의율
요일 종류: 수요일 대출·세금·제도 변화 · Q&A형 (소제목 5개를 질문으로).

수치와 검산
  사건일과 오늘의 간격: 주택법 시행령 개정안 국무회의 의결 11/17(화), 오늘에서 1일 전(리드).
  리모델링 허가 동의율: 단지 전체 구분소유자·의결권 각 75% → 70%, 동 리모델링도 같은 방식 · 동별 50% 이상 요건 유지
  시행: 동의율·안전성 검토기관 2027-01-01 (그날 이후 허가 신청분부터) · 군인 거주의무 예외·지주택 혼인 특례 공포 즉시
  수직증축 안전성 검토: 한국건설기술연구원·국토안전관리원 + 한국부동산원 (2곳 → 3곳)
  군인: 수도권 분상제 주택, 10년 이상 장기복무, 인사발령 이전 시 공급방식·지역 제한 없이 예외, 예외 기간 거주 간주
  지주택: 조합원끼리 혼인 시 배우자 입주권 주택 수 제외, 세대주 요건·중복가입 금지 미적용
  예시 계산(가구 = 구분소유자로 단순화): 1,000 → 750 / 700 (50) · 500 → 375 / 350 (25) · 2,000 → 1,500 / 1,400 (100)
    대시보드 컬럼(75→86): 75 86 · 70 80.3 · 50 57.3
    카드2 가로(750→100): 700 93.3 · 카드4 가로(100→100): 25 25 · 50 50

단정하지 않은 것
  · 공포일·관보 원문 미확인(시행령 공포 즉시 조항은 공포일이 시행일) · 조합 설립 동의(3분의 2)는 주택법 본문 기준으로 이번 개정 보도에 없음
  · 특정 단지가 혜택을 본다는 관측은 쓰지 않음
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-17-mokdong4-rebid.html"
DST = ROOT / "posts/2026-11-18-remodeling-consent.html"
SLUG, PRE = "2026-11-18-remodeling-consent", "rmd"
NO, DATE = 129, "2026-11-18"
PREV_SLUG = "mokdong4-rebid"
BANNED = ["목동4단지", "· 특집", "유찰"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "리모델링 동의율 70%로 낮춘다, 우리 단지는 언제부터?"
DESC = ("리모델링 동의율이 75%에서 70%로 낮아집니다. 11월 17일 국무회의를 통과한 주택법 시행령 개정안으로, "
        "2027년 1월 1일 이후 허가 신청분부터 적용됩니다. 동별 50% 요건, 단지 규모별 계산, 같이 바뀐 3가지를 질문별로 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="1,000가구 단지면 찬성 750명이 700명으로 줄어듭니다. 내년 1월 1일 허가 신청분부터, 동별 50% 요건은 그대로입니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">리모델링 동의율 70%로<br>우리 단지는 언제부터?</h1>
  <p class="sub"><strong>리모델링 동의율</strong>이 <strong>75%에서 70%</strong>로 낮아집니다. 11월 17일 국무회의를 통과한 주택법 시행령 개정안입니다. <span class="mark">2027년 1월 1일 이후 허가를 신청하는 단지부터 적용되고, 동별 50% 요건은 그대로 남습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 제도 변화</div><div class="kw">70%</div>
      <p>리모델링 허가 동의율, <strong>75%에서 낮춤</strong>.</p></div>
    <div class="kcard"><div class="hot">적용 시점</div><div class="kw">2027.1.1</div>
      <p>이날 이후 <strong>허가 신청분</strong>부터.</p></div>
    <div class="kcard"><div class="hot">1,000가구 기준</div><div class="kw">−50명</div>
      <p>찬성 <strong>750명 → 700명</strong>.</p></div>
    <div class="kcard"><div class="hot">동별 요건</div><div class="kw">50%</div>
      <p>단지 전체 리모델링, <strong>그대로 유지</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>리모델링 동의율, 지금과 내년 (%)</h3>
    <span class="badge">5%p 낮아진다</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">75</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:80.3%">70</div><div class="barv" style="--h:80.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:57.3%">50</div><div class="barv" style="--h:57.3%"></div></div>
    </div>
    <div class="collbl"><span>지금</span><span>2027.1.1부터</span><span>동별(유지)</span></div>
    <p class="cap">국토교통부 발표를 전한 아시아경제·서울경제·재경일보(2026년 11월 17일) 보도 기준입니다. 단지 전체 리모델링의 구분소유자·의결권 동의율과 동별 동의 요건입니다. 막대 길이는 최댓값 75%를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 리모델링 동의율 75%에서 70%로"),
    ("02-rate", "리모델링 동의율, 1,000가구면 50명 덜 받는다"),
    ("03-when", "리모델링 동의율 70%, 허가 신청일이 기준이다"),
    ("04-size", "우리 단지는 몇 명 덜 받나"),
    ("05-more", "주택법 시행령 개정, 같이 바뀐 3가지"),
    ("06-check", "리모델링 단지 체크 3가지"),
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

ARTICLE = '''<article data-tags="리모델링동의율,리모델링,주택법시행령,아파트리모델링,수직증축,리모델링조합,지역주택조합,분양가상한제거주의무,한국부동산원,국토교통부">
  <h2>리모델링 동의율 70%로 낮춘다, 우리 단지는 언제부터?</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 리모델링 동의율 75%에서 70%로"></span>

  <p><strong>3줄 요약</strong><br>리모델링 동의율이 75%에서 70%로 낮아지는 주택법 시행령 개정안이 11월 17일 국무회의를 통과했습니다.<br>2027년 1월 1일 이후 리모델링 허가를 신청하는 단지부터 적용되고, 단지 전체 리모델링의 동별 50% 요건은 그대로입니다.<br>리모델링을 준비하는 단지 소유자라면 지금 모인 동의율과 허가 신청 시점을 같이 보면 됩니다.</p>

  <p>리모델링 동의율 기준이 내년부터 5%포인트 낮아집니다. 국토교통부는 17일 주택법 시행령 일부개정령안이 국무회의에서 의결됐다고 밝혔습니다. <span class="mark">핵심은 리모델링 허가를 신청할 때 받아야 하는 동의율을 75%에서 70%로 낮춘 것입니다.</span> 같은 개정안에 수직증축 안전성 검토기관 추가, 장기복무 군인의 거주의무 예외, 지역주택조합원끼리 결혼했을 때의 특례도 들어갔습니다. 검색창에 많이 묻는 질문 다섯 가지로 나눠 정리했습니다.</p>

  <h3>리모델링 동의율, 얼마나 낮아지나요?</h3>
  <div class="chart" data-img="카드뉴스 2번 · 리모델링 동의율, 1,000가구면 50명 덜 받는다">
    <h3>1,000가구 단지가 받아야 하는 동의 (명)</h3>
    <div class="bar"><label>지금 75%</label>
      <div class="rail"><div class="fill gray" style="width:100%">750</div></div></div>
    <div class="bar"><label>내년 70%</label>
      <div class="rail"><div class="fill" style="width:93.3%">700</div></div></div>
    <p class="cap">가구 수를 구분소유자 수로 단순화한 예시 계산입니다. 실제로는 구분소유자 수와 의결권 두 기준을 각각 채워야 합니다. 막대 길이는 최댓값 750명을 기준으로 맞췄습니다.</p>
  </div>
  <p>75%에서 70%로, 5%포인트 낮아집니다. 단지 전체를 리모델링할 때 전체 구분소유자와 의결권의 동의율 기준이 각각 70%로 내려가고, 한 동만 리모델링하는 경우도 같은 방식으로 낮아집니다.</p>
  <p>숫자로 바꿔 보면 차이가 보입니다. 1,000가구 단지라면 지금은 750명의 찬성이 있어야 허가 신청을 할 수 있는데, 내년부터는 700명이면 됩니다. 50명입니다. 리모델링을 추진하는 단지들은 보통 마지막 몇 퍼센트를 채우지 못해 몇 달씩 시간을 보냅니다. 연락이 닿지 않는 소유자, 해외에 있는 소유자, 끝까지 반대하는 소유자가 섞여 있기 때문입니다. 그 마지막 구간이 5%포인트 줄어든다는 게 이번 개정의 실제 의미입니다.</p>
  <p>70%는 한 번만 넘기면 되는 숫자가 아닙니다. 구분소유자 수와 의결권, 두 기준을 각각 넘겨야 합니다. 구분소유자는 집을 가진 사람의 수이고, 의결권은 보통 각자 가진 전용면적 비율로 셉니다. 그래서 작은 평형 소유자가 많이 찬성해도 큰 평형 소유자의 반대가 몰리면 의결권 쪽이 70%에 못 미칠 수 있습니다. 평형이 여럿 섞인 단지라면 조합이 두 숫자를 따로 공지하는지 보는 게 좋습니다.</p>
  <p>여기서 자주 헷갈리는 점이 있습니다. 이번에 낮아지는 건 리모델링 허가를 신청할 때의 동의율입니다. 리모델링주택조합을 세울 때 받는 동의(전체 3분의 2 이상, 동별 과반수)는 주택법 본문에 있는 기준이고, 이번 시행령 개정 보도에는 들어 있지 않습니다. 조합 설립은 이미 했고 허가 신청을 앞둔 단지가 이번 개정과 가장 직접 닿아 있습니다.</p>

  <h3>리모델링 동의율 70%, 언제부터 적용되나요?</h3>
  <div class="chart" data-img="카드뉴스 3번 · 리모델링 동의율 70%, 허가 신청일이 기준이다">
    <h3>주택법 시행령 개정, 시행 시점</h3>
    <h4>국무회의</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11/17</span>
      <span class="desc">주택법 시행령 일부개정령안 의결.</span></div>
    <h4>공포 즉시</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">즉시</span>
      <span class="desc">군인 거주의무 예외, 지역주택조합 혼인 특례.</span></div>
    <h4>동의율 · 검토기관</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">1월 1일</span>
      <span class="desc">2027년 1월 1일 이후 허가 신청분부터.</span></div>
    <p class="cap">아시아경제·서울경제·재경일보(2026년 11월 17일) 보도 기준입니다. 공포일과 관보 원문은 확인하지 못했습니다. 정확한 조문은 국가법령정보센터에서 공포된 시행령으로 확인하십시오.</p>
  </div>
  <p>2027년 1월 1일부터입니다. 기준은 단지가 리모델링 허가를 신청하는 날입니다. 그날 이후에 허가를 신청하면 70%가 적용되고, 올해 안에 신청하면 지금 기준인 75%를 채워야 합니다.</p>
  <p>그래서 동의율이 72~74% 언저리에 머물러 있는 단지라면 계산이 달라집니다. 연말까지 75%를 채우려고 무리하는 대신, 해가 바뀐 뒤 70% 기준으로 신청하는 쪽을 검토할 수 있습니다. 반대로 이미 75%를 넘긴 단지는 기다릴 이유가 없습니다. 어느 쪽이 나은지는 단지마다 남은 일정이 달라서 조합 총회와 공지에서 정해집니다.</p>
  <p>나머지 두 가지, 장기복무 군인의 거주의무 예외와 지역주택조합원 혼인 특례는 공포되는 날 바로 시행됩니다. 국무회의 의결 뒤 공포까지는 보통 며칠이 걸리므로, 정확한 날짜는 관보에 실린 날을 보면 됩니다.</p>

  <h3>우리 단지는 리모델링 동의 몇 명 덜 받나요?</h3>
  <div class="chart" data-img="카드뉴스 4번 · 우리 단지는 몇 명 덜 받나">
    <h3>단지 규모별 줄어드는 동의 수 (명)</h3>
    <div class="bar"><label>500가구</label>
      <div class="rail"><div class="fill gray" style="width:25%"></div><span class="railval" style="left:calc(25% + 12px)">25</span></div></div>
    <div class="bar"><label>1,000가구</label>
      <div class="rail"><div class="fill gray" style="width:50%">50</div></div></div>
    <div class="bar"><label>2,000가구</label>
      <div class="rail"><div class="fill" style="width:100%">100</div></div></div>
    <p class="cap">가구 수에 5%포인트를 곱한 단순 계산입니다. 실제 기준은 구분소유자 수와 의결권이라 상가 소유자 등이 섞이면 달라집니다. 막대 길이는 최댓값 100명을 기준으로 맞췄습니다.</p>
  </div>
  <p>가구 수에 5%를 곱하면 대략 나옵니다. 500가구 단지는 375명에서 350명으로 25명, 2,000가구 단지는 1,500명에서 1,400명으로 100명이 줄어듭니다. 단지가 클수록 줄어드는 사람 수도 커지는데, 큰 단지일수록 마지막 동의를 모으기가 더 어렵기 때문에 체감 차이는 숫자보다 클 수 있습니다.</p>
  <p>다만 동별 요건이 남아 있다는 점을 같이 봐야 합니다. 단지 전체 리모델링은 동마다 구분소유자와 의결권의 50% 이상 동의가 있어야 하는데, 이 요건은 이번에 바뀌지 않았습니다. 전체로는 70%를 넘겨도 반대가 몰린 동이 하나 있으면 허가 신청이 막힙니다. 예를 들어 10개 동 가운데 한 동만 찬성이 절반에 못 미쳐도 단지 전체 리모델링은 진행할 수 없습니다.</p>
  <p>실제 동의 수는 가구 수와 다를 수 있습니다. 한 사람이 여러 채를 가지고 있거나, 한 채를 여럿이 함께 가지고 있거나, 상가 소유자가 있는 경우입니다. 우리 단지의 정확한 숫자는 조합이 관리하는 동의서 현황으로 확인해야 합니다.</p>

  <h3>주택법 시행령 개정, 리모델링 말고 같이 바뀐 건요?</h3>
  <div class="chart" data-img="카드뉴스 5번 · 주택법 시행령 개정, 같이 바뀐 3가지">
    <h3>이번 개정에 함께 담긴 것</h3>
    <h4>수직증축 안전성 검토</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">3곳</span>
      <span class="desc">한국부동산원 추가. 기존 2곳에서 늘었다.</span></div>
    <h4>분양가상한제 거주의무</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">군인</span>
      <span class="desc">10년 이상 장기복무, 발령 이전 시 지역 제한 없이 예외.</span></div>
    <h4>지역주택조합</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">혼인</span>
      <span class="desc">조합원끼리 결혼해도 부부 모두 자격 유지.</span></div>
    <p class="cap">아시아경제·서울경제·리드경제(2026년 11월 17일) 보도 기준입니다.</p>
  </div>
  <p>세 가지가 더 있습니다. 첫째는 수직증축 리모델링의 안전성 검토기관입니다. 지금은 한국건설기술연구원과 국토안전관리원 두 곳이 맡는데, 여기에 한국부동산원이 더해져 세 곳이 됩니다. 수직증축은 층을 더 올리는 방식이라 구조 안전성 검토를 두 번 받아야 하고, 이 검토를 기다리는 시간이 길다는 지적이 많았습니다. 검토기관이 늘면 대기 시간이 줄어들 수 있습니다. 이 부분도 2027년 1월 1일부터입니다.</p>
  <p>둘째는 수도권 분양가상한제 주택의 거주의무 예외입니다. 10년 이상 장기복무한 군인이 인사발령으로 이사해야 할 때, 공급 방식과 관계없이, 이사 가는 지역에 제한 없이 예외를 인정받습니다. 예외를 인정받은 기간은 실제로 살지 않아도 거주한 것으로 칩니다. 지금까지 일반공급으로 분양받은 경우에는 수도권 밖으로 옮길 때만 예외가 됐습니다.</p>
  <p>셋째는 지역주택조합입니다. 조합원끼리 결혼하면 지금까지는 세대주 요건과 중복가입 금지 규정 때문에 한 명이 자격을 잃을 수 있었습니다. 앞으로는 배우자의 조합주택 입주권을 주택 수에 넣지 않고, 이 두 규정도 적용하지 않아 부부가 모두 조합원으로 남을 수 있습니다. 보도에서는 이를 '결혼 페널티' 해소라고 불렀습니다.</p>

  <h3>재건축 대신 리모델링, 이번 개정으로 뭐가 쉬워지나요?</h3>
  <p>문턱 하나가 낮아진 것이지 리모델링 전체가 쉬워진 건 아닙니다. 허가 신청 동의율은 내려가지만, 그 앞의 조합 설립 동의와 뒤의 안전성 검토, 건축심의, 분담금 협의는 그대로 남습니다. 동별 50% 요건도 그대로입니다.</p>
  <p>그래도 의미는 있습니다. 리모델링을 고르는 단지는 대부분 용적률이 이미 높아 재건축으로는 늘릴 수 있는 가구가 적은 곳입니다. 이런 단지는 재건축보다 리모델링이 현실적인 선택인 경우가 많은데, 그동안은 75%라는 높은 동의율이 발목을 잡았습니다. 이번 개정은 그 단지들의 마지막 구간을 조금 줄여 준 것입니다.</p>
  <p>매수를 생각하는 분이라면 단지가 지금 어느 단계에 있는지부터 보십시오. 조합 설립 전인지, 허가 신청을 앞뒀는지, 이미 허가를 받았는지에 따라 이번 개정이 미치는 영향이 다릅니다. 조합원 지위 양도와 거래 제한도 단계마다 다르므로 조합과 구청에서 확인해야 합니다.</p>

  <h3>리모델링 단지 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 리모델링 단지 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="rmd-06-check.png" src="../images/cards/report/rmd-06-check.png" alt="체크포인트 카드 · 1. 허가 신청 시점, 2. 동별 50%는 그대로, 3. 조합 공지로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>리모델링 동의율 70% 개정, 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>허가 신청 시점</strong>. 2027년 1월 1일 이후 신청분부터 70%입니다. 올해 신청하면 75%를 채워야 합니다.</li>
    <li><strong>동별 50%는 그대로</strong>. 전체 70%를 넘겨도 절반이 안 되는 동이 있으면 단지 전체 리모델링은 어렵습니다.</li>
    <li><strong>우리 단지 숫자는 조합에서</strong>. 동의서 현황과 조합원 지위 양도 여부는 조합과 관할 구청에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>리모델링 동의율</strong>이 75%에서 70%로 낮아집니다. 11월 17일 국무회의를 통과한 주택법 시행령 개정안이고, 2027년 1월 1일 이후 허가를 신청하는 단지부터 적용됩니다. <span class="mark">1,000가구 단지라면 찬성 750명이 700명으로 줄어듭니다. 다만 동별 50% 요건은 그대로라 반대가 몰린 동이 있으면 여전히 어렵습니다.</span> 수직증축 검토기관 추가, 군인 거주의무 예외, 지역주택조합 혼인 특례도 함께 바뀌었습니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 개정 내용은 국토교통부 발표를 전한 아시아경제·서울경제·재경일보·리드경제·골든타임즈(2026-11-17) 보도 기준입니다. 공포일과 조문은 국가법령정보센터의 공포된 시행령으로 확인하십시오. 단지 규모별 숫자는 가구 수를 구분소유자 수로 단순화한 예시 계산입니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 아시아경제 리모델링 동의율 75%→70% 완화(2026-11-17) · 서울경제 리모델링 동의율 75→70% 완화…조합원 '결혼 페널티' 해소(2026-11-17) · 재경일보 아파트 리모델링 동의율 70%로 완화…국무회의 통과(2026-11-17) · 리드경제 리모델링 동의율 70% 완화…결혼 페널티 해소(2026-11-17) · 골든타임즈 국토교통부 '주택법 시행령' 개정안, 국무회의 의결(2026-11-17)<br>
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
for v, h in zip((75, 70, 50), (86, 80.3, 57.3)):
    assert round(v / 75 * 86, 1) == h, (v, h)
assert round(700 / 750 * 100, 1) == 93.3
for n, d in ((500, 25), (1000, 50), (2000, 100)):
    assert round(n * 0.75) - round(n * 0.70) == d
KW = "리모델링 동의율"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("리모델링동의율")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
