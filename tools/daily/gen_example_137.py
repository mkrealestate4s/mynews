# -*- coding: utf-8 -*-
"""리포트 #137 (2026-11-25 수) 종부세 비거주 1주택 공제. #136을 복제해 교체한다.

메인 검색어: 종부세 비거주 1주택
요일 종류: 수요일 대출·세금·제도 변화(Q&A형).
핫이슈 훑기: 6검색. 3개 매체 이상 겹친 새 청약·단지 건 없음(경희궁 에피트 특공 11/25 는 #126·#135 에서 다룸, 반포124 재심의 12/4).
  세제 쪽은 이형일 부총리 11/23 "거주·비거주 차등 유지"(뉴스1) · 이번 주 조세소위 심의(파이낸셜뉴스 11/18) · 여당 14억 통일 요구(이투데이·파이낸셜뉴스 11/10).

수치와 검산
  사건일과 오늘의 간격: 부총리 발언 11/23 → 2일. 조세소위 심의 이번 주.
  8/3 세제개편안: 실거주 1주택 공제 12억→14억 · 비거주 12억→9억(원안) · 세부담 상한 150→200%
  9/1 정부 수정(파이낸셜뉴스·한국경제·이투데이 9/1): 비거주 9억 철회 → 12억 유지 · 세부담 상한 150% 유지 · 실거주 14억은 그대로
  공정시장가액비율: 1주택 60→70%(정부안, 내년) · 조정대상지역 다주택·3주택 이상 2028년 80%
  세액공제 한도 2027 800만 · 2028 이후 600만 · 보유 기준 공제 2028 폐지(거주 기준으로)
  대시보드 세로 (80 → 86): 60 → 64.5 · 70 → 75.2
  카드2 가로 (14 → 100): 12 → 85.7 · 9 → 64.3
  카드4 예시 공시가 16억 · 비율 70% 가정: 공제 12억 → (16−12)×0.7 = 2.8억 · 14억 → 1.4억 · (철회된 9억 → 4.9억). 가로 (2.8 → 100): 1.4 → 50
  반포자이 시가 60억 실거주 1주택 연 1,100만원 증가는 서울경제 8월 원안 기준 추정

단정하지 않은 것
  · 최종 공제액: 국회 조세소위 심의 중. 여당은 거주 무관 14억 통일 요구
  · 불가피한 비거주 사유: 시행령에서 정한다는 정부 설명뿐, 범위 미정
  · 세액: 세율 구간·세액공제가 사람마다 달라 계산하지 않고 과세표준까지만 보였다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-24-mokdong12.html"
SLUG, PRE = "2026-11-25-jongbu-nonresident", "jbs"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 137, "2026-11-25"
PREV_SLUG = "mokdong12"
BANNED = ["목동12단지", "mk12-", "GS건설"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "종부세 비거주 1주택 공제, 14억 아직 확정 아닙니다"
DESC = ("종부세 비거주 1주택 공제를 두고 정부는 실거주 14억원, 비거주 12억원 차등을 유지하겠다고 11월 23일 밝혔고 "
        "여당은 14억원 통일을 요구합니다. 이번 주 국회 조세소위 심의를 앞두고 공제액, 일정, 예시 계산, 같이 바뀌는 공정시장가액비율을 질문별로 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="실거주 14억, 비거주 12억. 정부는 차등 유지, 여당은 14억 통일 요구. 이번 주 조세소위 심의.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">종부세 비거주 1주택,<br>공제 14억은 아직</h1>
  <p class="sub">정부는 <strong>실거주 14억원, 비거주 12억원</strong> 차등을 유지하겠다고 11월 23일 밝혔습니다. 여당은 거주와 상관없이 14억원으로 맞추자고 합니다. <span class="mark">이번 주 국회 조세소위에서 심의가 시작됩니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/23 발언</div><div class="kw">차등 유지</div>
      <p>정부는 <strong>거주·비거주</strong>를 나눈다.</p></div>
    <div class="kcard"><div class="hot">실거주 공제</div><div class="kw">14억</div>
      <p>지금 <strong>12억</strong>에서 올리는 안.</p></div>
    <div class="kcard"><div class="hot">비거주 공제</div><div class="kw">12억</div>
      <p>8월 원안 <strong>9억</strong>은 철회.</p></div>
    <div class="kcard"><div class="hot">국회</div><div class="kw">조세소위</div>
      <p>이번 주 <strong>심의</strong> 시작.</p></div>
  </div>

  <div class="colchart">
    <h3>1주택 공정시장가액비율 (%, 정부안)</h3>
    <span class="badge">공제와 같이 움직인다</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:64.5%">60%</div><div class="barv" style="--h:64.5%"></div></div>
      <div class="col"><div class="v gtx" style="--h:75.2%">70%</div><div class="barv" style="--h:75.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:86%">80%</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>지금</span><span>1주택 정부안</span><span>다주택 2028년</span></div>
    <p class="cap">2026년 세제개편안 보도 기준입니다. 80%는 조정대상지역 다주택·3주택 이상에 2028년 적용하는 안입니다. 국회 심의에서 바뀔 수 있습니다. 막대 길이는 80%를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 종부세 비거주 1주택, 공제 14억은 아직"),
    ("02-deduct", "공제, 지금 나온 숫자 세 가지"),
    ("03-when", "언제 정해지나"),
    ("04-example", "공시가 16억이면 과세표준은"),
    ("05-also", "공제 말고 같이 바뀌는 것"),
    ("06-check", "종부세 비거주 1주택 체크 3가지"),
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

ARTICLE = '''<article data-tags="종부세비거주1주택,종부세,종합부동산세,비거주1주택,1주택공제,종부세14억,공정시장가액비율,세제개편안,조세소위,보유세">
  <h2>종부세 비거주 1주택 공제, 14억 아직 확정 아닙니다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 종부세 비거주 1주택, 공제 14억은 아직"></span>

  <p><strong>3줄 요약</strong><br>종부세 비거주 1주택 공제는 정부안 기준 12억원, 실거주 1주택은 14억원입니다.<br>이형일 부총리가 11월 23일 이 차등을 유지하겠다고 밝혔고, 여당은 거주와 상관없이 14억원으로 맞추자고 요구합니다.<br>이번 주 국회 조세소위에서 심의가 시작되니, 집을 두고 다른 곳에 사는 1주택자는 결과를 보고 움직이는 게 순서입니다.</p>

  <p>종부세 비거주 1주택 공제가 다시 국회 테이블에 올라왔습니다. 이형일 부총리 겸 재정경제부 장관은 23일 종합부동산세에서 거주와 비거주를 나누는 방침을 그대로 가져가겠다고 밝혔습니다. 여당이 거주 여부를 따지지 말고 공제를 14억원으로 통일하자고 거듭 요구한 데 대한 답입니다. 국회 재정경제기획위원회는 이번 주 조세소위원회를 열어 종부세 등 세법개정안 심의에 들어갑니다. 자주 받는 질문 다섯 개로 나눠 정리했습니다.</p>

  <h3>종부세 비거주 1주택, 공제 얼마 받나요?</h3>
  <div class="chart" data-img="카드뉴스 2번 · 공제, 지금 나온 숫자 세 가지">
    <h3>1주택 종부세 기본공제 (공시가격 기준)</h3>
    <div class="bar"><label>실거주 (정부안)</label>
      <div class="rail"><div class="fill" style="width:100%">14억</div></div></div>
    <div class="bar"><label>비거주 (정부안 · 지금과 같음)</label>
      <div class="rail"><div class="fill gray" style="width:85.7%">12억</div></div></div>
    <div class="bar"><label>비거주 (8월 원안 · 철회)</label>
      <div class="rail"><div class="fill gray" style="width:64.3%">9억</div></div></div>
    <p class="cap">8월 3일 세제개편안과 9월 1일 정부 수정 보도 기준입니다. 여당은 거주와 상관없이 14억원을 요구하고 있어 국회에서 바뀔 수 있습니다. 막대 길이는 14억원을 기준으로 맞췄습니다.</p>
  </div>
  <p>지금 정부안대로면 12억원입니다. 현행과 같습니다. 실제로 사는 1주택자만 공제가 14억원으로 오르고, 집을 두고 다른 곳에 사는 1주택자는 12억원에 머뭅니다. 공시가격 기준이라 시세로는 이보다 높은 집까지 해당합니다.</p>
  <p>처음부터 이랬던 건 아닙니다. 8월 3일 세제개편안에서는 비거주 1주택 공제를 9억원으로 낮추는 안이었습니다. 발표 뒤 반발이 커지자 정부는 9월 1일 이 부분을 거둬들이고 12억원 유지로 고쳤습니다. 29일 만이었습니다. 같은 날 세부담 상한을 200%로 올리는 안도 함께 접었습니다.</p>
  <p>누가 영향을 받는지 보면, 직장 때문에 지방에 살면서 서울 집을 세놓은 사람, 자녀 학교 때문에 전세로 옮긴 사람, 부모를 모시러 집을 비운 사람이 다 비거주 1주택에 들어갑니다. 여당이 통일을 요구하는 이유가 여기 있습니다. 정부는 이런 경우 가운데 부득이한 사유를 시행령으로 정해 14억원을 인정할 수 있다는 입장입니다. 어떤 사유가 들어갈지는 아직 나오지 않았습니다.</p>
  <p>여당이 물러서지 않는 이유도 보도에 나옵니다. 개편이 그대로 가면 내년 재산세·종부세 고지서를 받는 비거주 1주택자의 불만이 커질 수 있다는 걱정입니다. 반대로 정부는 실거주를 우대하는 원칙이 흔들리면 정책 일관성이 무너진다고 봅니다. 그래서 이번 조세소위는 숫자 하나가 아니라 원칙을 두고 다투는 자리에 가깝습니다.</p>

  <h3>종부세 개편, 언제 확정되나요?</h3>
  <div class="chart" data-img="카드뉴스 3번 · 언제 정해지나">
    <h3>종부세 개편 일정</h3>
    <h4>정부 세제개편안</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">8월 3일</span>
      <span class="desc">실거주 14억, 비거주 9억으로 발표.</span></div>
    <h4>정부 수정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9월 1일</span>
      <span class="desc">비거주 12억 유지로 되돌림.</span></div>
    <h4>부총리 발언</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 23일</span>
      <span class="desc">거주·비거주 차등은 유지.</span></div>
    <h4>국회 조세소위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">이번 주</span>
      <span class="desc">세법개정안 심의 시작.</span></div>
    <p class="cap">파이낸셜뉴스·한국경제·이투데이(9월 1일), 뉴스1(11월 23일), 파이낸셜뉴스(11월 18일) 보도 기준입니다. 조세소위 세부 일정은 본회의 일정에 따라 조정될 수 있습니다.</p>
  </div>
  <p>국회를 통과해야 확정입니다. 정부안은 9월 초 국회에 제출됐고, 이번 주 조세소위에서 심의가 본격적으로 시작됩니다. 조세소위에서 여야가 합의한 내용이 상임위와 본회의를 거쳐야 법이 됩니다. 세법은 보통 연말 예산안과 함께 처리되기 때문에 12월 초까지는 결론을 지켜봐야 합니다.</p>
  <p>여기서 헷갈리기 쉬운 점이 있습니다. 법이 통과돼도 비거주 예외 사유는 시행령으로 정합니다. 그래서 국회 결론이 차등 유지로 나더라도, 내가 예외에 들어가는지는 시행령이 나와야 알 수 있습니다. 부총리도 국회 논의를 들어 보고 시행령에서 확정하겠다고 말했습니다.</p>

  <h3>종부세 비거주 1주택이면 세금 얼마나 달라지나요?</h3>
  <div class="chart" data-img="카드뉴스 4번 · 공시가 16억이면 과세표준은">
    <h3>공시가 16억원 1주택 과세표준 (예시)</h3>
    <div class="bar"><label>공제 12억 (비거주 정부안)</label>
      <div class="rail"><div class="fill gray" style="width:100%">2억8천만</div></div></div>
    <div class="bar"><label>공제 14억 (실거주 · 여당안)</label>
      <div class="rail"><div class="fill" style="width:50%">1억4천만</div></div></div>
    <p class="cap">과세표준 = (공시가격 − 공제) × 공정시장가액비율. 비율은 정부안 70%로 가정했습니다. 세율 구간과 고령·장기 세액공제는 사람마다 달라 세액은 계산하지 않았습니다. 막대 길이는 2억8천만원을 기준으로 맞췄습니다.</p>
  </div>
  <p>예시로 계산해 보면 과세표준이 두 배 차이 납니다. 공시가격 16억원짜리 집 한 채를 가진 사람을 예로 들겠습니다. 종부세는 공시가격에서 공제를 빼고 공정시장가액비율을 곱한 금액에 세율을 매깁니다. 비율을 정부안 70%로 놓으면 공제 12억원일 때 과세표준은 2억8천만원, 14억원일 때는 1억4천만원입니다.</p>
  <p>철회된 9억원 안이었다면 과세표준은 4억9천만원이었습니다. 9월 수정으로 비거주 1주택자의 부담이 그만큼 줄어든 셈입니다. 공제 차이 2억원에 비율 70%를 곱하면 과세표준 차이는 집값과 상관없이 1억4천만원으로 같습니다. 그래서 집값이 낮을수록 차이가 크게 느껴집니다. 공시가격 20억원이면 비거주 5억6천만원, 실거주 4억2천만원으로 실거주 쪽이 25% 적은 데 그치지만, 16억원 집은 두 배가 됩니다. 공제 논쟁이 공시가 12억~20억원 사이 1주택자에게 특히 중요한 이유입니다.</p>
  <p>공시가격이 14억원 아래인 집이라면 실거주자는 종부세 대상에서 빠지고, 비거주자는 12억원을 넘는 부분만큼 과세됩니다.</p>
  <p>고가 주택은 공제보다 다른 숫자가 더 크게 작용합니다. 서울경제는 8월 원안 기준으로 시가 60억원 반포자이에 실제로 사는 1주택자도 종부세가 연 1,100만원가량 늘어난다고 추정했습니다. 공제가 올라도 공정시장가액비율 인상과 세액공제 개편이 함께 들어오기 때문입니다. 내 집 기준 세액은 국세청 홈택스 종부세 모의계산으로 확인할 수 있습니다.</p>

  <h3>공제 말고 같이 바뀌는 건 뭔가요?</h3>
  <div class="chart" data-img="카드뉴스 5번 · 공제 말고 같이 바뀌는 것">
    <h3>함께 바뀌는 항목 (정부안)</h3>
    <h4>공정시장가액비율 · 1주택</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">70%</span>
      <span class="desc">지금 60%에서 올리는 안.</span></div>
    <h4>세부담 상한</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">150%</span>
      <span class="desc">200% 인상안은 9월에 철회.</span></div>
    <h4>세액공제 한도</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">600만</span>
      <span class="desc">2027년 800만원, 2028년부터 600만원.</span></div>
    <p class="cap">2026년 세제개편안과 9월 1일 수정 보도 기준입니다. 공정시장가액비율 인상은 여당 안에서도 신중론이 나와 국회에서 조정될 수 있습니다.</p>
  </div>
  <p>공정시장가액비율이 가장 큽니다. 1주택자 비율을 지금 60%에서 70%로 올리는 안이고, 조정대상지역 다주택자와 3주택 이상은 2028년 80%까지 올립니다. 비율이 10%포인트 오르면 같은 공제라도 과세표준이 그만큼 커집니다. 앞의 예시에서 비거주 1주택은 60%면 2억4천만원, 70%면 2억8천만원입니다. 공시가격 20억원 비거주 1주택이라면 4억8천만원에서 5억6천만원으로 8천만원 늘어납니다. 공제를 두고 다투는 사이에 비율 인상은 상대적으로 덜 주목받는데, 집값이 높을수록 이쪽 영향이 더 큽니다.</p>
  <p>세액공제도 바뀝니다. 오래 가진 것에 주던 보유 기준 공제를 2028년부터 없애고 실제로 산 기간을 따지는 거주 기준으로 바꿉니다. 한도는 2027년 800만원, 2028년 이후 600만원입니다. 비거주 1주택자는 공제와 세액공제 양쪽에서 실거주자보다 불리해지는 구조라, 이번 국회 심의에서 가장 다툼이 큰 대목입니다. 세부담 상한은 9월 수정 때 지금처럼 직전 연도의 150%로 남겼습니다.</p>

  <h3>올해 종부세 고지서도 바뀌나요?</h3>
  <p>아닙니다. 지금 논의되는 개정안은 국회를 통과한 뒤의 부과분에 적용됩니다. 올해 종부세는 현행법대로 공제 12억원, 공정시장가액비율 60%로 매겨지고, 납부 기간은 매년 12월 1일부터 15일까지입니다. 고지서가 오면 공시가격과 1세대 1주택 여부가 맞게 들어갔는지부터 보는 게 좋습니다.</p>
  <p>자주 헷갈리는 점이 하나 더 있습니다. 종부세는 매년 6월 1일에 누가 집을 갖고 있었는지를 기준으로 매깁니다. 6월 2일 이후에 집을 팔았어도 올해 고지서는 판 사람에게 나옵니다. 개편 뒤 거주 요건을 어떻게 따질지는 시행령에서 정해지니, 이사 시점을 정할 때 함께 확인해 두면 좋습니다.</p>
  <p>내년 공시가격도 변수입니다. 공제와 비율이 정해져도 공시가격이 오르면 과세표준이 함께 커집니다. 내년 공동주택 공시가격 안은 보통 3월에 열람이 시작되니 그때 의견을 낼 수 있습니다. 내 집 공시가격이 주변 시세보다 높게 잡혔다고 느껴지면 이 열람 기간을 놓치지 않는 게 가장 확실한 대비입니다.</p>

  <h3>종부세 비거주 1주택 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 종부세 비거주 1주택 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="jbs-06-check.png" src="../images/cards/report/jbs-06-check.png" alt="체크포인트 카드 · 1. 공제액은 국회 결론 뒤 확정, 2. 예외 사유는 시행령, 3. 올해 고지서는 현행법" loading="lazy" width="1080" height="1080">
    <figcaption>종부세 비거주 1주택자가 챙길 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>공제액은 국회 결론 뒤 확정</strong>. 정부안은 실거주 14억, 비거주 12억이고 여당은 14억 통일을 요구합니다.</li>
    <li><strong>예외 사유는 시행령</strong>. 부득이한 비거주로 인정받을지는 시행령이 나와야 압니다.</li>
    <li><strong>올해 고지서는 현행법</strong>. 공제 12억, 납부는 12월 1일부터 15일까지입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>종부세 비거주 1주택</strong> 공제는 정부안 기준 12억원으로 지금과 같고, 실거주 1주택만 14억원으로 오릅니다. 정부는 11월 23일 이 차등을 유지하겠다고 했고 여당은 14억원 통일을 요구해, 이번 주 시작되는 국회 조세소위가 갈림길입니다. 공정시장가액비율 70% 인상과 세액공제 개편도 같은 법안에 들어 있습니다. <span class="mark">올해 고지서는 현행법대로 나오니, 집을 비워 둔 1주택자는 연말 국회 결론과 시행령의 예외 사유를 보고 판단하는 게 순서입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 세무 자문이 아닙니다. 공제액·공정시장가액비율·세액공제 한도는 정부 세제개편안과 수정안 보도 기준이며 국회 심의에서 바뀔 수 있습니다. 예시의 과세표준은 공정시장가액비율 70%를 가정한 단순 계산입니다. 개인별 세액은 홈택스 모의계산이나 세무 전문가에게 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 뉴스1 이형일 "종부세 거주·비거주 차등 입장 그대로"(2026-11-23) · 파이낸셜뉴스 비거주 차등과세 부동산 세제 개편 담판 돌입(2026-11-18) · 파이낸셜뉴스 거주·비거주 차등원칙 견지한 정부(2026-11-10) · 이투데이 與 "실거주 안 따지고 종부세 공제 14억으로" · 파이낸셜뉴스·한국경제·이투데이 비거주 1주택 종부세 공제 12억 유지(2026-09-01) · 서울경제 시가 60억 반포자이 실거주 1주택 종부세(2026 세제개편안) · 파이낸셜뉴스 2026 세제 개편(2026-08-03)<br>
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
assert round(60 / 80 * 86, 1) == 64.5 and round(70 / 80 * 86, 1) == 75.2
assert round(12 / 14 * 100, 1) == 85.7 and round(9 / 14 * 100, 1) == 64.3
assert round((16 - 12) * 0.7, 2) == 2.8 and round((16 - 14) * 0.7, 2) == 1.4 and round((16 - 9) * 0.7, 2) == 4.9 and round((16 - 12) * 0.6, 2) == 2.4 and round((20 - 12) * 0.7, 2) == 5.6 and round((20 - 14) * 0.7, 2) == 4.2 and round(1 - 4.2 / 5.6, 2) == 0.25 and round((20 - 12) * 0.6, 2) == 4.8
KW = "종부세 비거주 1주택"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("종부세비거주1주택")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
