# -*- coding: utf-8 -*-
"""리포트 #133 (2026-11-21 토 오후 · 추가 발행 x1) 잠실 래미안아이파크 줍줍 신청자격. #132를 복제해 교체한다.

메인 검색어: 잠실 래미안아이파크 줍줍
요청: 대표 키워드 추가 발행(공장 블로그 요청 #5, 메모 "무순위 줍줍 신청자격"). 틀은 Q&A형.
핫이슈: 11/17 공고 뒤 뉴스핌·파이낸셜뉴스·서울경제·한국경제·뉴스1 등 보도. 청약 주 2편 상한의 핫이슈 예외.

수치와 검산
  사건일과 오늘의 간격: 공고 11/17 → 4일. 특공 접수 11/23 → D-2. 일반 11/24 → D-3.
  물량: 계약취소 3가구 · 84㎡D 신혼부부 특공 1(11/23) · 43㎡·59㎡A 일반 각 1(11/24) · 청약홈 09:00~17:30
  발표 11/27 · 서류 12/1 · 계약 12/4 · 계약금 30% · 잔금 계약 후 30일 이내(보도)
  자격: 공고일 기준 서울 거주 · 일반 무주택세대주 · 특공 혼인 7년 이내 무주택 세대구성원 · 추첨 · 실거주 2년 · 재당첨 10년
  공급가(옵션 제외, 재분양비 포함 보도): 43㎡ 11억548만4,366 · 59㎡A 15억7,939만8,680 · 84㎡D 18억5,607만144
  84㎡ 입주권 실거래 43억(7/1, 국토부 실거래가 보도) · 옵션 포함 약 18억8,000만 기준 차익 약 24억(보도)
  59㎡A 보류지 입찰 기준가 30억8,000만(2026-06 파이낸셜뉴스)
  계약금 30%: 3억3,165만 · 4억7,382만 · 5억5,682만 / 잔금 70%: 7억7,384만 · 11억558만 · 12억9,925만
  대시보드 세로 (18.5607억 → 86): 11.0548 → 51.2 · 15.7940 → 73.2
  카드4 가로 (43억 → 100): 18.56 → 43.2 · 30.8 → 71.6 · 15.79 → 36.7
  카드5 (5.5682억 → 100): 4.7382 → 85.1 · 3.3165 → 59.6

단정하지 않은 것
  · 신혼 특공 소득·자산 기준과 예비신혼부부 포함 여부: 보도에서 확인 못 함 → 공고문
  · 공고일 16일/17일 보도 엇갈림 → 공고문
  · 대출 한도·재당첨 제한 기간 중인 사람의 신청 가능 여부 → 공고문·은행
  · 43㎡ 비교 실거래: 확인 못 해 비교하지 않음
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-21-seongsu2-dl.html"
SLUG, PRE = "2026-11-21-jamsil-raemian-ipark", "jrp"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 133, "2026-11-21"
PREV_SLUG = "seongsu2-dl"
BANNED = ["성수2지구", "DL이앤씨"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "잠실 래미안아이파크 줍줍 신청자격, 23일부터 접수"
DESC = ("잠실 래미안아이파크 계약취소 3가구가 무순위(줍줍)로 나옵니다. 11월 23일 신혼부부 특별공급 84㎡, 24일 일반공급 43㎡·59㎡를 청약홈에서 받습니다. "
        "서울 거주 무주택자만 넣을 수 있고, 84㎡ 공급가 18억5,607만원에 계약금 30%가 필요합니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="계약취소 3가구, 23일 신혼 특공·24일 일반. 서울 거주 무주택자 추첨, 84㎡ 공급가 18억5,607만원 vs 입주권 43억.">
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
  <div class="eyebrow">2026 · 11월 부동산 키워드 리포트 #{NO} · 청약 특집</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">잠실 래미안아이파크<br>줍줍, 누가 넣나</h1>
  <p class="sub">송파구 <strong>잠실 래미안아이파크</strong> 계약취소 3가구가 무순위로 나옵니다. <strong>11월 23일</strong> 신혼부부 특별공급, <strong>24일</strong> 일반공급입니다. <span class="mark">공고일 기준 서울에 사는 무주택자만 넣을 수 있습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/23 접수</div><div class="kw">3가구</div>
      <p>특공 <strong>1</strong>, 일반 <strong>2</strong>.</p></div>
    <div class="kcard"><div class="hot">신청자격</div><div class="kw">서울 무주택</div>
      <p>공고일 기준, <strong>추첨</strong>.</p></div>
    <div class="kcard"><div class="hot">84㎡ 공급가</div><div class="kw">18억5,607만</div>
      <p>입주권 실거래 <strong>43억</strong>.</p></div>
    <div class="kcard"><div class="hot">계약금</div><div class="kw">30%</div>
      <p>84㎡는 <strong>5억5,682만</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>잠실 래미안아이파크 무순위 공급가 (원)</h3>
    <span class="badge">84㎡는 신혼부부 특공</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:51.2%">11.05억</div><div class="barv" style="--h:51.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:73.2%">15.79억</div><div class="barv" style="--h:73.2%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">18.56억</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>43㎡ 일반</span><span>59㎡A 일반</span><span>84㎡D 특공</span></div>
    <p class="cap">입주자모집공고 보도 기준 공급금액입니다(옵션 제외). 발코니 확장 등 이미 시공된 옵션 대금은 따로 승계해야 합니다. 막대 길이는 최댓값 18억5,607만원을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 잠실 래미안아이파크 줍줍 신청자격"),
    ("02-sched", "접수는 23일·24일, 하루씩"),
    ("03-who", "서울 사는 무주택자만, 추첨"),
    ("04-price", "84㎡ 공급가, 실거래의 절반도 안 된다"),
    ("05-cash", "당첨되면 계약금만 3억~5억대"),
    ("06-check", "넣기 전에 볼 3가지"),
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

ARTICLE = '''<article data-tags="잠실래미안아이파크줍줍,잠실래미안아이파크,무순위청약,줍줍,계약취소주택,로또청약,송파구청약,신혼부부특별공급,무주택세대주,청약홈">
  <h2>잠실 래미안아이파크 줍줍 신청자격, 23일부터 접수</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 잠실 래미안아이파크 줍줍 신청자격"></span>

  <p><strong>3줄 요약</strong><br>잠실 래미안아이파크에서 계약이 취소된 3가구가 무순위(줍줍)로 다시 나옵니다.<br>11월 23일 신혼부부 특별공급(84㎡ 1가구), 24일 일반공급(43㎡·59㎡ 각 1가구)을 청약홈에서 받고, 공고일 기준 서울에 사는 무주택자만 넣을 수 있습니다.<br>84㎡ 공급가는 18억5,607만원으로 7월 입주권 실거래 43억원보다 약 24억원 낮지만, 계약금 30%만 5억5,682만원이라 현금 준비가 먼저입니다.</p>

  <p>잠실 래미안아이파크 줍줍 신청이 모레, 11월 23일부터 시작됩니다. 송파구 신천동 잠실진주아파트를 재건축한 이 단지에서 불법전매나 공급질서 교란으로 계약이 취소된 3가구를 한국부동산원 청약홈에서 다시 공급합니다. 11월 17일 공고가 나온 뒤 파이낸셜뉴스, 서울경제, 뉴스1 등이 일제히 "20억 로또"라는 제목을 달았습니다. <span class="mark">다만 아무나 넣을 수 있는 줍줍은 아닙니다.</span> 누가, 언제, 얼마를 들고 넣을 수 있는지 사람들이 가장 많이 묻는 질문 다섯 개로 정리합니다.</p>

  <h3>잠실 래미안아이파크 줍줍, 언제 신청하나요?</h3>
  <div class="chart" data-img="카드뉴스 2번 · 접수는 23일·24일, 하루씩">
    <h3>잠실 래미안아이파크 무순위 일정 (공고 보도 기준)</h3>
    <h4>신혼부부 특별공급</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 23일</span>
      <span class="desc">84㎡D 1가구. 청약홈 접수.</span></div>
    <h4>일반공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 24일</span>
      <span class="desc">43㎡·59㎡A 각 1가구.</span></div>
    <h4>당첨 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 27일</span>
      <span class="desc">서류 접수는 12월 1일.</span></div>
    <h4>계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12월 4일</span>
      <span class="desc">계약금 30%, 잔금은 30일 안에.</span></div>
    <p class="cap">뉴스핌·서울경제·비건뉴스 등 입주자모집공고 보도 기준입니다. 정정 공고가 나올 수 있으니 청약홈 원문을 함께 확인하십시오.</p>
  </div>
  <p>답부터 말하면 접수는 이틀, 그것도 유형별로 하루씩입니다. 23일(월)에는 신혼부부 특별공급 84㎡D 1가구를, 24일(화)에는 일반공급 43㎡와 59㎡A 각 1가구를 받습니다. 접수 시간은 두 날 모두 오전 9시부터 오후 5시 30분까지이고 청약홈에서 넣습니다. 그날을 놓치면 다시 기회가 없습니다.</p>
  <p>당첨자는 27일에 발표합니다. 당첨되면 12월 1일 서류를 내고 12월 4일 계약합니다. 보도에 따르면 계약금은 공급가의 30%이고, 잔금은 계약일부터 30일 안에 치러야 합니다. 새로 짓는 단지처럼 중도금을 나눠 내며 2~3년을 기다리는 구조가 아니라, 이미 지어진 집을 한 달 남짓 사이에 사는 일정입니다.</p>
  <p>자주 헷갈리는 날짜가 하나 있습니다. 공고일을 16일로 쓴 기사와 17일로 쓴 기사가 섞여 있습니다. 거주지와 무주택 여부는 공고일을 기준으로 따지므로, 최근에 전입했거나 집을 판 분은 청약홈 공고문에 찍힌 날짜를 먼저 확인하는 게 좋습니다.</p>

  <h3>잠실 래미안아이파크 줍줍 신청자격, 통장 없어도 되나요?</h3>
  <div class="chart" data-img="카드뉴스 3번 · 서울 사는 무주택자만, 추첨">
    <h3>잠실 래미안아이파크 무순위 신청자격 (보도 기준)</h3>
    <h4>사는 곳</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">서울</span>
      <span class="desc">입주자모집공고일 기준 서울 거주.</span></div>
    <h4>집</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">무주택</span>
      <span class="desc">일반공급은 무주택 세대주.</span></div>
    <h4>뽑는 방법</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">추첨</span>
      <span class="desc">가점·통장 가입기간을 보지 않는다.</span></div>
    <p class="cap">비건뉴스·재경일보 등 공고 보도 기준입니다. 세부 요건과 예외는 청약홈 입주자모집공고문이 정본입니다.</p>
  </div>
  <p>일반공급은 청약통장이 없어도 넣을 수 있다고 보도됐습니다. 조건은 세 가지입니다. 공고일 기준 서울에 살 것, 무주택 세대주일 것, 그리고 당첨은 추첨으로 정한다는 점입니다. 가점이나 통장 가입기간을 따지지 않으니 청약 점수가 낮은 1~2인 가구도 같은 확률로 들어갑니다.</p>
  <p>예전 줍줍과는 조건이 다릅니다. 국토교통부는 2025년 2월 무순위 청약 자격을 무주택자로 좁히고, 지자체가 지역 여건에 따라 거주 요건을 붙일 수 있도록 제도를 바꿨습니다. 그 전에는 집이 있어도, 다른 지역에 살아도 넣을 수 있어 한 가구에 수많은 사람이 몰리는 일이 이어졌습니다. 이번 잠실 래미안아이파크 줍줍은 바뀐 기준을 따라 서울 거주 무주택자로 범위가 좁아졌습니다.</p>
  <p>무주택은 신청자 한 사람이 아니라 세대 전체를 보는 경우가 보통입니다. 배우자나 같은 세대원이 집을 갖고 있으면 걸릴 수 있다는 뜻입니다. 또 일반공급은 세대주 요건이 붙어 있어 부모님 집에 세대원으로 올라가 있는 분은 넣지 못할 수 있습니다. 분양권이나 입주권을 주택으로 볼지, 예전 당첨 이력이 있는 분이 넣을 수 있는지도 공고문에서 따로 확인해야 합니다.</p>
  <p>누가 가장 유리한지는 분명합니다. 서울에 살고 집이 없으며 현금이 있는 세대주입니다. 이 셋 가운데 하나라도 빠지면 당첨돼도 계약까지 가기 어렵습니다.</p>

  <h3>신혼부부 특공 84㎡는 누가 넣을 수 있나요?</h3>
  <p>84㎡D 1가구는 신혼부부 특별공급으로 나옵니다. 보도된 조건은 혼인기간 7년 이내, 무주택 세대구성원, 공고일 기준 서울 거주입니다. 일반공급과 달리 세대주가 아니어도 무주택 세대구성원이면 신청할 수 있습니다. 이 역시 추첨으로 정합니다.</p>
  <p>보도에서 확인되지 않은 부분도 있습니다. 신혼부부 특공에 보통 붙는 소득과 자산 기준이 이번 재공급에도 적용되는지, 예비신혼부부나 한부모 가구도 넣을 수 있는지는 기사마다 언급이 없었습니다. 이 부분은 청약홈 공고문의 특별공급 자격 항목을 직접 읽어 보셔야 합니다. 혼인기간은 혼인신고일을 기준으로 세는 것이 일반적입니다.</p>
  <p>84㎡가 관심의 중심인 이유는 차익이 가장 크기 때문입니다. 2024년 첫 분양 때도 특별공급에만 4만명 넘게 몰렸다는 보도가 있었습니다. 이번에는 한 가구뿐이라 경쟁은 그때보다 훨씬 치열할 수 있습니다. 다만 계약금 5억5,682만원을 혼인 7년 이내 부부가 한 달 안에 마련하기는 쉽지 않습니다.</p>

  <h3>잠실 래미안아이파크 줍줍, 얼마나 싸게 나오나요?</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡ 공급가, 실거래의 절반도 안 된다">
    <h3>공급가와 최근 거래 기준가 (원)</h3>
    <div class="bar"><label>84㎡ 입주권 실거래 (7월)</label>
      <div class="rail"><div class="fill gray" style="width:100%">43억</div></div></div>
    <div class="bar"><label>84㎡D 이번 공급가</label>
      <div class="rail"><div class="fill" style="width:43.2%">18억5,607만</div></div></div>
    <div class="bar"><label>59㎡ 보류지 기준가 (6월)</label>
      <div class="rail"><div class="fill gray" style="width:71.6%">30억8,000만</div></div></div>
    <div class="bar"><label>59㎡A 이번 공급가</label>
      <div class="rail"><div class="fill" style="width:36.7%">15억7,940만</div></div></div>
    <p class="cap">84㎡ 입주권 실거래는 국토교통부 실거래가 공개시스템 보도(2026년 7월 1일, 43억원), 59㎡ 보류지 입찰 기준가는 파이낸셜뉴스(2026년 6월) 기준입니다. 43㎡는 비교할 거래를 확인하지 못해 뺐습니다. 막대 길이는 최댓값 43억원을 기준으로 맞췄습니다.</p>
  </div>
  <p>84㎡로 보면 절반도 안 되는 값입니다. 이번 84㎡D 공급가는 18억5,607만원이고, 같은 면적 입주권은 7월 1일 43억원에 거래됐습니다. 차이는 약 24억4,000만원입니다. 발코니 확장과 유상옵션을 더한 금액(약 18억8,000만원)으로 계산해도 언론이 말하는 '24억 차익'과 거의 같습니다.</p>
  <p>59㎡A는 공급가 15억7,940만원입니다. 올해 6월 조합이 보류지를 팔 때 59㎡A 입찰 기준가를 30억8,000만원으로 정했다는 보도가 있었습니다. 이 값과 비교하면 약 15억원 낮습니다. 43㎡ 공급가는 11억548만원인데, 같은 면적의 최근 거래는 확인하지 못해 여기서는 비교하지 않았습니다.</p>
  <p>이렇게 싼 이유는 2024년 분양 당시 가격이 그대로 이어지기 때문입니다. 이 단지는 분양가상한제가 적용돼 3.3㎡당 평균 5,409만원에 분양했고, 그 뒤 잠실 시세가 크게 올랐습니다. 2024년 10월 1순위 청약에서도 평균 269대 1이 나왔습니다. 계약취소 재공급은 처음 분양가를 바탕으로 하므로 시세와 차이가 벌어질수록 '로또' 소리가 커집니다.</p>
  <p>하나 주의할 점이 있습니다. 이미 시공된 발코니 확장과 옵션은 빼고 계약할 수 없다고 보도됐습니다. 공급가만 보고 예산을 잡으면 옵션 대금만큼 모자랄 수 있습니다. 또 실거주 의무 2년이 붙어 있어 세입자 보증금으로 잔금을 치르는 방법은 쓰기 어렵습니다.</p>

  <h3>당첨되면 현금은 얼마나 있어야 하나요?</h3>
  <div class="chart" data-img="카드뉴스 5번 · 당첨되면 계약금만 3억~5억대">
    <h3>계약금 30% 예시 (공급가 기준, 옵션 제외)</h3>
    <h4>43㎡ 일반</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3억3,165만</span>
      <span class="desc">잔금 7억7,384만원.</span></div>
    <h4>59㎡A 일반</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4억7,382만</span>
      <span class="desc">잔금 11억558만원.</span></div>
    <h4>84㎡D 특공</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">5억5,682만</span>
      <span class="desc">잔금 12억9,925만원.</span></div>
    <p class="cap">보도된 공급금액에 계약금 30%를 곱해 만원 단위로 반올림한 예시입니다. 옵션 대금과 취득세는 따로입니다.</p>
  </div>
  <p>계약금만 3억원에서 5억원대입니다. 공급가의 30%를 12월 4일 계약 때 내야 하므로 43㎡는 3억3,165만원, 59㎡A는 4억7,382만원, 84㎡D는 5억5,682만원이 필요합니다. 나머지 70%인 잔금은 보도대로라면 계약일부터 30일 안에 내야 합니다. 84㎡라면 한 달 남짓 사이에 18억원이 넘는 돈을 맞춰야 하는 셈입니다.</p>
  <p>예를 들어 59㎡A에 당첨되면 12월 4일 4억7,382만원, 이듬해 1월 초까지 11억558만원을 더 내야 합니다. 여기에 옵션 대금과 취득세가 붙습니다. 잔금 일부를 주택담보대출로 채우려는 분이 많을 텐데, 서울은 집값 구간별로 대출 한도가 묶여 있고 이 단지처럼 시세와 공급가 차이가 큰 경우 은행이 한도를 어떻게 잡을지 미리 알기 어렵습니다. 신청 전에 거래 은행에 물어보는 게 순서입니다.</p>
  <p>당첨되고 계약을 포기하면 끝나는 문제도 아닙니다. 재당첨 제한 10년이 붙은 단지라 당첨 이력이 남으면 앞으로 다른 청약에 불리해질 수 있습니다. 포기했을 때 어떻게 처리되는지는 공고문의 유의사항에서 확인하십시오. 자금 계획 없이 '일단 넣고 보자'는 접근이 위험한 이유입니다.</p>

  <h3>넣기 전에 볼 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 넣기 전에 볼 3가지 (체크리스트)">
    <img class="card-art" data-file="jrp-06-check.png" src="../images/cards/report/jrp-06-check.png" alt="체크포인트 카드 · 1. 공고일 기준 서울·무주택, 2. 23일 특공·24일 일반, 3. 계약금 30% 현금" loading="lazy" width="1080" height="1080">
    <figcaption>잠실 래미안아이파크 줍줍, 넣기 전에 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>공고일 기준 서울·무주택</strong>. 세대 전체의 주택 여부와 세대주 요건을 공고문으로 확인합니다.</li>
    <li><strong>23일 특공, 24일 일반</strong>. 유형별로 하루씩만 받고 시간은 오전 9시부터 오후 5시 30분까지입니다.</li>
    <li><strong>계약금 30% 현금</strong>. 84㎡ 기준 5억5,682만원, 잔금은 30일 안이라고 보도됐습니다.</li>
  </ol>
  <p>다음 날짜는 이렇습니다. 23일과 24일 접수가 끝나면 27일 당첨자가 나오고, 12월 1일 서류 접수, 12월 4일 계약으로 이어집니다. 신청 인원과 경쟁률은 접수가 끝난 뒤 청약홈에서 공개됩니다.</p>

  <h3>정리</h3>
  <p><strong>잠실 래미안아이파크 줍줍</strong>은 계약취소 3가구를 다시 공급하는 무순위 청약으로, 11월 23일 신혼부부 특별공급 84㎡, 24일 일반공급 43㎡·59㎡를 청약홈에서 받습니다. <span class="mark">공고일 기준 서울에 사는 무주택자만 넣을 수 있고 당첨은 추첨입니다.</span> 84㎡ 공급가는 18억5,607만원으로 최근 입주권 거래보다 약 24억원 낮지만, 계약금 30%와 한 달 안의 잔금, 실거주 2년을 감당할 수 있는지부터 따져 봐야 합니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 일정·공급가·자격은 11월 17일 입주자모집공고에 대한 언론 보도 기준이며, 정본은 청약홈(applyhome.co.kr) 공고문입니다. 신혼부부 특별공급의 소득·자산 기준, 대출 가능 여부, 당첨 포기 시 불이익은 공고문과 금융기관에 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 뉴스핌·파이낸셜뉴스 잠실 래미안아이파크 3가구 무순위 공급(2026-11-17) · 한국경제·서울경제·뉴스1 계약취소 재공급·시세 차익(2026-11-18) · 비건뉴스·재경일보 접수 일정·공급금액(2026-11-18~20) · 파이낸셜뉴스 보류지 입찰 기준가(2026-06-17) · 국토교통부 실거래가 공개시스템(입주권 2026-07) · 2024년 10월 분양 보도(이투데이·SBS Biz)<br>
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
for v, hh in ((11.05484366, 51.2), (15.7939868, 73.2)):
    assert round(v / 18.56070144 * 86, 1) == hh
for v, w in ((18.56070144, 43.2), (30.8, 71.6), (15.7939868, 36.7)):
    assert round(v / 43 * 100, 1) == w
assert round(4.73819604 / 5.56821043 * 100, 1) == 85.1 and round(3.3164531 / 5.56821043 * 100, 1) == 59.6
for p, dep, bal in ((1105484366, 33165, 77384), (1579398680, 47382, 110558), (1856070144, 55682, 129925)):
    assert round(p * 0.3 / 1e4) == dep and round(p * 0.7 / 1e4) == bal
KW = "잠실 래미안아이파크 줍줍"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 2)[2].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("잠실래미안아이파크줍줍")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
