# -*- coding: utf-8 -*-
"""리포트 #134 (2026-11-22 일) 동탄 신고가 2건 중 1건 · 한강벨트 10월 거래 73% 감소. #133을 복제해 교체한다.

메인 검색어: 동탄 신고가
요일 종류: 일요일 실거래 사례(비교형). 한강벨트 vs 반도체벨트 거래량, 동탄 신고가 단지 사례.
핫이슈 훑기: 잠실 래미안아이파크 줍줍(서울경제·파이낸셜뉴스 등) → 11/21 #133 으로 이미 씀. 오늘은 2주 규칙으로 제외.

수치와 검산
  사건일과 오늘의 간격: 서울경제 집계 보도 11/18 → 4일. 동탄 신고가 집계는 11/18까지 신고분.
  한강벨트 7개구(광진·성동·마포·동작·양천·영등포·강동) 10월 거래 2,865 → 770 (−73.1%, 전년 같은 달 대비)
  서울 전체 감소 폭보다 19.1%p 크다 → 서울 −54.0%
  반도체벨트(수원 영통·용인 기흥·화성 동탄) 10월 2,458 → 1,323 (−46.2%)
  동탄 11월(18일까지 신고) 211건 중 94건 신고가 = 44.5%
  동탄역 반도유보라 아이비파크8.0 73.6㎡ 15억5,800만 (직전 신고가 14억7,000만, +8,800만)
  대출 한도(10·15 대책): 15억 이하 6억 · 15억~25억 4억 · 25억 초과 2억
  대시보드 세로 (2,865 → 86): 770 → 23.1 · 2,458 → 73.8 · 1,323 → 39.7
  카드2 가로 (73.1 → 100): 54.0 → 73.9 · 46.2 → 63.2
  카드4 가로 (15.58 → 100): 14.7 → 94.4

단정하지 않은 것
  · 한강벨트는 10월, 동탄 신고가는 11월 중순 집계로 기간이 다르다. 한 축에 섞지 않는다.
  · 신고가 거래는 나중에 취소될 수 있다(실거래가 시스템 취소 내역 공개).
  · 수요 배경(성과급·사내대출)은 기사 진단이다.
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-21-jamsil-raemian-ipark.html"
SLUG, PRE = "2026-11-22-dongtan-high", "dth"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 134, "2026-11-22"
PREV_SLUG = "jamsil-raemian-ipark"
BANNED = ["래미안", "jrp-"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "동탄 신고가 2건 중 1건, 한강벨트는 거래 73% 줄었다"
DESC = ("동탄에서 11월 18일까지 신고된 아파트 매매 211건 중 94건(44.5%)이 신고가였습니다. 같은 때 한강벨트 7개구의 10월 거래는 작년보다 73.1% 줄었습니다. "
        "동탄역 반도유보라 아이비파크8.0 사례와 대출 한도로 두 지역이 갈린 이유를 비교했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="동탄 11월 매매 211건 중 94건 신고가. 한강벨트 10월 거래 2,865건에서 770건으로. 15억 아래 대출 6억이 가른 두 시장.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">동탄 신고가,<br>2건 중 1건</h1>
  <p class="sub">화성 <strong>동탄</strong>에서 11월 18일까지 신고된 아파트 매매 211건 가운데 <strong>94건</strong>이 신고가였습니다. 같은 때 서울 한강벨트 7개구는 10월 거래가 작년보다 <strong>73.1%</strong> 줄었습니다. <span class="mark">거래가 끊긴 곳과 값이 오르는 곳이 갈렸습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11월 동탄</div><div class="kw">44.5%</div>
      <p>매매 211건 중 <strong>94건</strong> 신고가.</p></div>
    <div class="kcard"><div class="hot">한강벨트 10월</div><div class="kw">−73.1%</div>
      <p>거래 2,865건 → <strong>770건</strong>.</p></div>
    <div class="kcard"><div class="hot">반도체벨트 10월</div><div class="kw">−46.2%</div>
      <p>영통·기흥·동탄, <strong>덜</strong> 줄었다.</p></div>
    <div class="kcard"><div class="hot">동탄 사례</div><div class="kw">15억5,800만</div>
      <p>73.6㎡, 직전보다 <strong>+8,800만</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>10월 아파트 거래량, 작년과 올해 (건)</h3>
    <span class="badge">한강벨트가 더 크게 줄었다</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">2,865</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:23.1%">770</div><div class="barv" style="--h:23.1%"></div></div>
      <div class="col dim"><div class="v" style="--h:73.8%">2,458</div><div class="barv" style="--h:73.8%"></div></div>
      <div class="col"><div class="v gtx" style="--h:39.7%">1,323</div><div class="barv" style="--h:39.7%"></div></div>
    </div>
    <div class="collbl"><span>한강 작년</span><span>한강 올해</span><span>반도체 작년</span><span>반도체 올해</span></div>
    <p class="cap">한강벨트는 광진·성동·마포·동작·양천·영등포·강동 7개구, 반도체벨트는 수원 영통·용인 기흥·화성 동탄입니다. 서울경제가 국토교통부 실거래가 공개시스템을 집계한 10월 거래량(작년 같은 달 대비)입니다. 막대 길이는 최댓값 2,865건을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 동탄 신고가 2건 중 1건"),
    ("02-drop", "10월 거래, 한강벨트가 가장 많이 줄었다"),
    ("03-high", "동탄 11월 매매, 44.5%가 신고가"),
    ("04-case", "동탄역 반도유보라 아이비파크8.0, 8,800만원 올랐다"),
    ("05-loan", "15억 아래는 대출 6억, 그래서 갈렸다"),
    ("06-check", "동탄 신고가, 사기 전에 볼 3가지"),
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

ARTICLE = '''<article data-tags="동탄신고가,동탄아파트,동탄실거래가,반도유보라아이비파크8.0,한강벨트,반도체벨트,화성동탄,아파트신고가,주택담보대출한도,10·15대책">
  <h2>동탄 신고가 2건 중 1건, 한강벨트는 거래 73% 줄었다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 동탄 신고가 2건 중 1건"></span>

  <p><strong>3줄 요약</strong><br>동탄 신고가 거래가 11월 들어 매매 두 건 중 한 건꼴로 나오고 있습니다.<br>같은 때 서울 한강벨트 7개구는 10월 거래가 작년 같은 달보다 73.1% 줄었습니다.<br>15억원 아래 집은 대출이 6억원까지 나와 실수요가 동탄 같은 경기 남부로 옮겨 간 것으로 풀이됩니다.</p>

  <p>동탄 신고가 소식이 이어지고 있습니다. 서울경제가 국토교통부 실거래가 공개시스템을 집계한 결과, 화성 동탄에서 11월 18일까지 신고된 아파트 매매 211건 가운데 94건이 종전 최고가를 넘었습니다. 비율로 44.5%입니다. 같은 기사에서 서울 한강벨트 7개구의 10월 거래는 2,865건에서 770건으로 줄었습니다. <span class="mark">한쪽은 거래가 끊기고 한쪽은 값을 새로 쓰는 흐름입니다.</span> 오늘은 두 지역의 숫자를 나란히 놓고 무엇이 갈랐는지 봅니다.</p>

  <h3>10월 거래, 한강벨트와 반도체벨트 비교</h3>
  <div class="chart" data-img="카드뉴스 2번 · 10월 거래, 한강벨트가 가장 많이 줄었다">
    <h3>10월 아파트 거래 감소율 (작년 같은 달 대비)</h3>
    <div class="bar"><label>한강벨트 7개구</label>
      <div class="rail"><div class="fill" style="width:100%">−73.1%</div></div></div>
    <div class="bar"><label>서울 전체</label>
      <div class="rail"><div class="fill gray" style="width:73.9%">−54.0%</div></div></div>
    <div class="bar"><label>반도체벨트 3곳</label>
      <div class="rail"><div class="fill gray" style="width:63.2%">−46.2%</div></div></div>
    <p class="cap">서울경제 집계(2026년 11월 18일 보도) 기준입니다. 서울 전체는 기사의 "한강벨트 감소 폭이 서울 전체보다 19.1%포인트 크다"는 문장으로 계산했습니다. 막대 길이는 최댓값 73.1%를 기준으로 맞췄습니다.</p>
  </div>
  <p>결론부터 말하면 거래는 어디서나 줄었지만 줄어든 정도가 크게 달랐습니다. 광진·성동·마포·동작·양천·영등포·강동 7개구를 묶은 한강벨트는 10월 거래가 작년 2,865건에서 올해 770건으로 73.1% 줄었습니다. 서울 전체 감소 폭보다 19.1%포인트 큰 숫자라 서울 전체는 54% 안팎 줄어든 셈입니다.</p>
  <p>수원 영통, 용인 기흥, 화성 동탄을 묶은 반도체벨트도 거래가 줄긴 했습니다. 작년 10월 2,458건에서 올해 1,323건으로 46.2% 감소했습니다. 다만 한강벨트와 비교하면 감소 폭이 27%포인트가량 작습니다. 한강벨트는 열 건 가운데 일곱 건 넘게 사라졌고, 반도체벨트는 절반가량이 남았다는 뜻입니다. 건수로 보면 한강벨트는 2,095건, 반도체벨트는 1,135건이 줄었습니다.</p>
  <p>한강벨트는 지난해까지 서울 집값 상승을 이끈 지역입니다. 강남3구 바로 다음 가격대라 갈아타기 수요가 몰렸던 곳인데, 지금은 매수자가 관망으로 돌아섰다는 보도가 이어집니다. 서울경제는 11월 20일 한국부동산원 주간 통계를 인용해 강남3구에 이어 용산·동작도 하락으로 돌아섰다고 전했습니다.</p>
  <p>누가 영향을 받는지도 갈립니다. 한강벨트에서 집을 팔고 더 비싼 곳으로 옮기려던 사람은 매수자를 찾기 어려워졌습니다. 파이낸셜뉴스는 11월 9일 강남3구에서 호가를 크게 낮춘 매물도 거래가 잘 붙지 않는다고 보도했습니다. 반대로 동탄처럼 15억원 아래 단지가 많은 곳은 매수 문의가 이어지면서 집주인이 호가를 올리는 흐름입니다.</p>

  <h3>동탄 신고가, 11월 매매의 44.5%</h3>
  <div class="chart" data-img="카드뉴스 3번 · 동탄 11월 매매, 44.5%가 신고가">
    <h3>화성 동탄 11월 아파트 매매 (18일까지 신고분)</h3>
    <h4>신고가 비율</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">44.5%</span>
      <span class="desc">매매 211건 가운데 94건이 종전 최고가를 넘었다.</span></div>
    <h4>신고된 매매</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">211건</span>
      <span class="desc">11월 1일~18일 계약 가운데 신고가 끝난 것.</span></div>
    <p class="cap">서울경제가 국토교통부 실거래가 공개시스템을 집계한 수치입니다. 실거래 신고 기한이 계약 뒤 30일이라 11월 거래는 앞으로 더 늘어납니다.</p>
  </div>
  <p>동탄은 11월 매매의 절반 가까이가 신고가였습니다. 211건 가운데 94건이니 거래 두 건 중 한 건꼴로 최고가를 다시 쓴 셈입니다. 거래가 줄어든 시장에서는 보통 급매가 먼저 팔리면서 가격이 내려가는데, 동탄은 반대로 움직였습니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 211건은 11월 거래 전체가 아니라 18일까지 신고가 끝난 거래입니다. 실거래 신고는 계약 뒤 30일 안에 하면 되니 11월 숫자는 12월 중순까지 계속 늘어납니다. 비율이 지금과 같게 유지될지는 그때 다시 봐야 합니다.</p>
  <p>신고가 거래가 나중에 취소되는 경우도 있습니다. 실거래가 공개시스템은 계약이 등록됐다가 취소된 내역도 함께 보여 줍니다. 관심 있는 단지가 있다면 신고가 거래 옆에 취소 표시가 붙었는지 직접 확인해 보는 게 좋습니다.</p>
  <p>신고가라는 말도 자주 오해를 삽니다. 여기서 신고가는 같은 단지, 같은 면적에서 지금까지 나온 가장 높은 값을 넘었다는 뜻입니다. 동탄 전체 최고가라는 뜻도, 모든 층이 그 값이라는 뜻도 아닙니다. 같은 반도체벨트라도 영통과 기흥의 신고가 비율은 기사에 나오지 않아, 이 글에서는 동탄 숫자만 다룹니다.</p>

  <h3>동탄 신고가 사례, 반도유보라 아이비파크8.0</h3>
  <div class="chart" data-img="카드뉴스 4번 · 동탄역 반도유보라 아이비파크8.0, 8,800만원 올랐다">
    <h3>동탄역 반도유보라 아이비파크8.0 73.6㎡ (원)</h3>
    <div class="bar"><label>11월 거래</label>
      <div class="rail"><div class="fill" style="width:100%">15억5,800만</div></div></div>
    <div class="bar"><label>직전 신고가</label>
      <div class="rail"><div class="fill gray" style="width:94.4%">14억7,000만</div></div></div>
    <p class="cap">서울경제 보도(2026년 11월 18일) 기준입니다. 층과 동은 보도에 없어 국토교통부 실거래가 공개시스템에서 확인해야 합니다. 막대 길이는 15억5,800만원을 기준으로 맞췄습니다.</p>
  </div>
  <p>대표 사례는 동탄역 반도유보라 아이비파크8.0입니다. 전용 73.6㎡가 이달 15억5,800만원에 거래됐습니다. 직전 신고가 14억7,000만원보다 8,800만원 높은 값입니다. 비율로 따지면 6% 정도 오른 셈입니다.</p>
  <p>숫자로 감을 잡아 보면 이렇습니다. 같은 면적을 직전 신고가에 산 사람과 이번에 산 사람의 차이가 8,800만원입니다. 대출 금리 연 4%로 이 금액을 빌린다고 가정하면 이자만 한 해 약 352만원, 한 달 약 29만원이 더 듭니다. 같은 집에 매달 그만큼을 더 내고 들어가는 셈입니다.</p>
  <p>이번 거래가 15억원을 넘었다는 점도 볼 만합니다. 아래에서 다루겠지만 대출 한도가 15억원에서 한 번 꺾이기 때문입니다. 동탄의 신고가 행진이 15억원 선을 넘어서도 이어질지가 다음 관심사입니다.</p>

  <h3>15억 아래는 대출 6억, 그래서 갈렸다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 15억 아래는 대출 6억, 그래서 갈렸다">
    <h3>집값 구간별 주택담보대출 한도 (10·15 대책)</h3>
    <h4>15억원 이하</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">6억</span>
      <span class="desc">동탄 대부분 단지가 여기에 든다.</span></div>
    <h4>15억~25억원</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4억</span>
      <span class="desc">한강벨트 84㎡ 상당수가 여기다.</span></div>
    <h4>25억원 초과</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2억</span>
      <span class="desc">강남3구 대표 단지 대부분.</span></div>
    <p class="cap">10·15 대책의 주택담보대출 한도 기준(보도 기준)입니다. 지역과 대출 종류에 따라 LTV 등 다른 조건이 함께 붙으니 은행에서 확인하십시오.</p>
  </div>
  <p>두 지역을 가른 이유로 가장 많이 꼽히는 건 대출 한도입니다. 집값 15억원 이하는 주택담보대출이 6억원까지, 15억원에서 25억원은 4억원, 25억원을 넘으면 2억원까지만 나옵니다. 같은 돈을 들고 있어도 어느 구간의 집을 사느냐에 따라 빌릴 수 있는 돈이 세 배까지 차이 납니다.</p>
  <p>예시로 계산해 보면 차이가 분명해집니다. 14억원짜리 집은 대출 6억원을 받으면 현금 8억원이 필요합니다. 20억원짜리 집은 대출이 4억원이라 현금 16억원이 있어야 합니다. 집값은 1.4배인데 필요한 현금은 두 배입니다. 한강벨트 84㎡ 상당수가 15억원을 넘는다는 점을 생각하면 매수자가 줄어든 이유가 보입니다.</p>
  <p>화성은 규제지역에서 빠져 있다는 점도 함께 거론됩니다. 서울 전역은 토지거래허가구역이라 실거주 요건이 붙지만 동탄은 그렇지 않습니다. 기사는 여기에 반도체 업황 호조로 성과급과 사내대출을 쓸 수 있는 맞벌이 고소득층이 수요를 받친다고 진단했습니다. 다만 이건 기사의 해석이고, 개인 대출 가능액은 소득과 보유 주택에 따라 달라집니다.</p>
  <p>15억원 선이 얼마나 큰지는 오늘 사례로 바로 계산됩니다. 반도유보라 아이비파크8.0 73.6㎡가 직전 신고가 14억7,000만원이었을 때는 대출 6억원을 받으면 현금 8억7,000만원이 필요했습니다. 이번 거래가 15억5,800만원으로 15억원을 넘으면서 대출이 4억원으로 줄고, 필요한 현금은 11억5,800만원이 됩니다. 집값은 8,800만원 올랐는데 들고 있어야 할 현금은 2억8,800만원 늘어난 셈입니다.</p>

  <h3>동탄 신고가, 사기 전에 볼 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 동탄 신고가, 사기 전에 볼 3가지 (체크리스트)">
    <img class="card-art" data-file="dth-06-check.png" src="../images/cards/report/dth-06-check.png" alt="체크포인트 카드 · 1. 거래 취소 여부, 2. 15억 선과 대출 한도, 3. 같은 단지 층·동 비교" loading="lazy" width="1080" height="1080">
    <figcaption>동탄 신고가, 계약 전에 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>거래 취소 여부</strong>. 신고가 거래 옆에 취소 표시가 붙었는지 실거래가 공개시스템에서 봅니다.</li>
    <li><strong>15억 선과 대출 한도</strong>. 15억원을 넘는 순간 대출이 6억원에서 4억원으로 줄어듭니다.</li>
    <li><strong>같은 단지 층·동 비교</strong>. 신고가 한 건이 단지 전체 시세는 아닙니다. 층과 동, 면적을 맞춰 봅니다.</li>
  </ol>
  <p>앞으로 볼 숫자도 정리해 둡니다. 11월 동탄 거래는 신고 기한이 끝나는 12월 중순에야 전체 숫자가 나옵니다. 한강벨트 11월 거래량도 그 무렵 집계됩니다. 그때 신고가 비율이 유지되는지, 한강벨트 거래가 바닥을 찍는지가 두 시장의 다음 장면입니다.</p>
  <p>서울 쪽에는 날짜가 하나 더 있습니다. 서울 토지거래허가구역 지정 기한이 12월 31일이라 연장 여부가 연말 전에 발표될 예정입니다. 실거주 요건이 그대로 이어지는지에 따라 한강벨트 거래가 다시 움직일지가 갈릴 수 있습니다.</p>

  <h3>정리</h3>
  <p><strong>동탄 신고가</strong> 거래가 11월 들어 매매 211건 중 94건, 44.5%까지 늘었습니다. 동탄역 반도유보라 아이비파크8.0 73.6㎡는 15억5,800만원으로 직전보다 8,800만원 올랐습니다. <span class="mark">같은 때 한강벨트 7개구의 10월 거래는 작년보다 73.1% 줄어 두 시장이 정반대로 움직이고 있습니다.</span> 15억원 아래 대출 6억원이라는 선이 수요를 가른 것으로 보이지만, 11월 숫자는 아직 신고가 덜 끝난 중간 집계입니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 거래량과 신고가 수치는 서울경제의 국토교통부 실거래가 공개시스템 집계(2026년 11월 18일 보도) 기준이며, 11월 거래는 신고 기한(계약 뒤 30일)이 남아 바뀔 수 있습니다. 한강벨트는 10월, 동탄은 11월 중순 집계로 기간이 다릅니다. 대출 한도는 개인 조건에 따라 다르니 금융회사에 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 서울경제 「한강벨트 거래 73% 줄어들때…동탄 2건 중 1건 신고가」(2026-11-18) · 서울경제 서울 아파트값 주간 동향(2026-11-20) · 국토교통부 실거래가 공개시스템 · 10·15 주택시장 안정화 대책 주택담보대출 한도<br>
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
for v, hh in ((770, 23.1), (2458, 73.8), (1323, 39.7)):
    assert round(v / 2865 * 86, 1) == hh, (v, round(v / 2865 * 86, 1))
assert round((2865 - 770) / 2865 * 100, 1) == 73.1 and round((2458 - 1323) / 2458 * 100, 1) == 46.2
assert round(73.1 - 19.1, 1) == 54.0
assert 2865 - 770 == 2095 and 2458 - 1323 == 1135
assert round(54.0 / 73.1 * 100, 1) == 73.9 and round(46.2 / 73.1 * 100, 1) == 63.2
assert round(94 / 211 * 100, 1) == 44.5
assert 155800 - 147000 == 8800 and round(14.7 / 15.58 * 100, 1) == 94.4
assert round(8800 * 0.04) == 352
assert 147000 - 60000 == 87000 and 155800 - 40000 == 115800 and 115800 - 87000 == 28800
KW = "동탄 신고가"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("동탄신고가")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
