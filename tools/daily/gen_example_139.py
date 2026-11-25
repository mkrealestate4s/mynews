# -*- coding: utf-8 -*-
"""리포트 #139 (2026-11-26 목 · 비교형) 잠실 래미안아이파크 줍줍 경쟁률. #138 을 복제해 교체한다.

메인 검색어: 잠실 래미안아이파크 줍줍
핫이슈 훑기: 잠실 래미안아이파크 줍줍 결과(11/24 접수 마감) · 이데일리·한국경제(2건)·헤럴드경제 11/24~25 → 오늘 씀.
  #133(11/21) 과 같은 단지지만 2주 규칙의 예외 조건('결과: 경쟁률' 새 숫자)에 해당. 청약 주 2편 상한의 핫이슈 예외.
  목요일 종류(청약 단지 한 곳 깊게, 비교형)와도 맞는다.

수치와 검산
  사건일과 오늘의 간격: 일반 접수 11/24 → 2일. 특공 11/23 → 3일. 당첨 발표 11/27 → D-1.
  신청자(청약홈 집계 보도): 59㎡A 3만3,125 · 43㎡ 2만322 → 일반 2가구 5만3,447(평균 2만6,723.5대 1) · 84㎡D 신혼 특공 1만503 → 합 6만3,950
  2024년 10월 첫 분양: 일반 1순위 307가구 8만2,487명(268.69대 1) · 특공 282가구 3만9,478명 · 59㎡A 24가구 1만4,190명(591.2대 1)
  3만3,125 / 591.2 = 약 56배
  공급가(옵션 제외): 43㎡ 11억548만 · 59㎡A 15억7,940만 · 84㎡D 18억5,607만 (#133 과 같음)
  84㎡ 입주권 실거래 43억(7/1) · 59㎡A 보류지 기준가 30억8,000만(2026-06)
  계약금 30%: 3억3,165만 · 4억7,382만 · 5억5,682만 / 잔금 70%: 7억7,384만 · 11억558만 · 12억9,925만
  대시보드 세로 (3만3,125 → 86): 2만322 → 52.8 · 1만503 → 27.3
  카드2 가로 (3만3,125 → 100): 61.3 · 31.7
  카드3 가로 (43억 → 100): 43.2 · 71.6 · 36.7

단정하지 않은 것
  · 당첨 포기 시 불이익의 범위 → 공고문
  · 다른 단지 줍줍(문정·철산) 신청자 수는 접수일을 확인 못 해 비교에 쓰지 않음
  · 43㎡ 비교 실거래: 확인 못 함
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-25-violation-building.html"
SLUG, PRE = "2026-11-26-jamsil-raemian-result", "jrr"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 139, "2026-11-26"
PREV_SLUG = "violation-building"
BANNED = ["위반건축물", "양성화"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "잠실 래미안아이파크 줍줍, 3가구에 6만명 몰렸다"
DESC = ("잠실 래미안아이파크 계약취소 3가구 무순위(줍줍)에 6만3,950명이 신청했습니다. 59㎡ 한 가구에 3만3,125명, 43㎡ 2만322명, 신혼부부 특공 84㎡ 1만503명입니다. "
        "당첨 발표는 11월 27일, 계약은 12월 4일입니다. 공급가와 최근 실거래, 2024년 첫 분양 경쟁률을 나란히 비교합니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="일반 2가구 5만3,447명, 신혼 특공 1가구 1만503명. 84㎡ 공급가 18억5,607만원 vs 입주권 43억. 발표 11월 27일.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">잠실 래미안아이파크<br>줍줍, 6만명 몰렸다</h1>
  <p class="sub">송파구 <strong>잠실 래미안아이파크</strong> 계약취소 3가구에 <strong>6만3,950명</strong>이 신청했습니다. 59㎡ 한 가구에만 3만3,125명입니다. <span class="mark">당첨 발표는 내일, 11월 27일입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 신청자</div><div class="kw">6만3,950명</div>
      <p>3가구, 특공 <strong>1</strong>·일반 <strong>2</strong>.</p></div>
    <div class="kcard"><div class="hot">일반 평균</div><div class="kw">2만6,723대 1</div>
      <p>2가구에 <strong>5만3,447명</strong>.</p></div>
    <div class="kcard"><div class="hot">84㎡ 공급가</div><div class="kw">18억5,607만</div>
      <p>입주권 실거래 <strong>43억</strong>.</p></div>
    <div class="kcard"><div class="hot">당첨 발표</div><div class="kw">11월 27일</div>
      <p>계약은 <strong>12월 4일</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>잠실 래미안아이파크 줍줍 유형별 신청자 (명)</h3>
    <span class="badge">유형마다 1가구</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:52.8%">2만322</div><div class="barv" style="--h:52.8%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">3만3,125</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:27.3%">1만503</div><div class="barv" style="--h:27.3%"></div></div>
    </div>
    <div class="collbl"><span>43㎡ 일반</span><span>59㎡A 일반</span><span>84㎡D 신혼 특공</span></div>
    <p class="cap">한국부동산원 청약홈 집계 보도(2026-11-24~25) 기준입니다. 특공은 11월 23일, 일반은 24일에 받았습니다. 막대 길이는 최댓값 3만3,125명을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 잠실 래미안아이파크 줍줍 경쟁률"),
    ("02-people", "59㎡ 한 집에 3만3,125명"),
    ("03-price", "84㎡, 실거래의 절반도 안 된다"),
    ("04-vs2024", "2년 전 59㎡는 591대 1이었다"),
    ("05-next", "내일 발표, 계약은 12월 4일"),
    ("06-check", "발표 전에 볼 3가지"),
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

ARTICLE = '''<article data-tags="잠실래미안아이파크줍줍,잠실래미안아이파크,줍줍경쟁률,무순위청약,로또청약,계약취소주택,송파구청약,신혼부부특별공급,당첨자발표,청약홈">
  <h2>잠실 래미안아이파크 줍줍, 3가구에 6만명 몰렸다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 잠실 래미안아이파크 줍줍 경쟁률"></span>

  <p><strong>3줄 요약</strong><br>잠실 래미안아이파크 계약취소 3가구 무순위(줍줍)에 모두 6만3,950명이 신청했습니다.<br>일반공급 2가구에 5만3,447명(평균 2만6,723.5대 1), 신혼부부 특별공급 84㎡ 1가구에 1만503명이 넣었습니다.<br>당첨 발표는 내일 11월 27일이고, 당첨되면 12월 4일 계약금 30%를 내야 하니 현금 계획부터 다시 보셔야 합니다.</p>

  <p>잠실 래미안아이파크 줍줍 접수가 끝났고, 숫자가 나왔습니다. 11월 23일 신혼부부 특별공급과 24일 일반공급을 합쳐 3가구에 6만3,950명이 몰렸습니다. 이데일리, 한국경제, 헤럴드경제가 24일과 25일 연달아 "5만명", "6만명"을 제목에 올렸습니다. <span class="mark">한 가구로 치면 2만명이 넘게 붙은 셈입니다.</span> 오늘은 이 경쟁률을 공급가, 최근 실거래, 2년 전 첫 분양과 나란히 놓고 왜 이렇게 몰렸는지, 당첨되면 무엇이 이어지는지 비교해 봅니다.</p>

  <h3>잠실 래미안아이파크 줍줍 경쟁률, 유형별로 보면</h3>
  <div class="chart" data-img="카드뉴스 2번 · 59㎡ 한 집에 3만3,125명">
    <h3>유형별 신청자 (각 1가구, 명)</h3>
    <div class="bar"><label>59㎡A 일반 (11월 24일)</label>
      <div class="rail"><div class="fill" style="width:100%">3만3,125명</div></div></div>
    <div class="bar"><label>43㎡ 일반 (11월 24일)</label>
      <div class="rail"><div class="fill gray" style="width:61.3%">2만322명</div></div></div>
    <div class="bar"><label>84㎡D 신혼부부 특공 (11월 23일)</label>
      <div class="rail"><div class="fill gray" style="width:31.7%">1만503명</div></div></div>
    <p class="cap">한국부동산원 청약홈 집계를 인용한 이데일리·한국경제 보도(2026-11-24~25) 기준입니다. 막대 길이는 최댓값 3만3,125명을 기준으로 맞췄습니다.</p>
  </div>
  <p>가장 많이 몰린 곳은 59㎡A입니다. 한 가구에 3만3,125명이 신청했습니다. 43㎡에는 2만322명이 넣어 일반공급 2가구에 모두 5만3,447명, 평균 경쟁률은 2만6,723.5대 1입니다. 하루 전 신혼부부 특별공급 84㎡D 1가구에는 1만503명이 신청했습니다.</p>
  <p>확률로 바꾸면 이렇습니다. 59㎡A는 3만3,125명 가운데 한 명을 추첨으로 뽑습니다. 10만명이 넣으면 3명꼴로 당첨되는 확률입니다. 43㎡는 2만명 가운데 한 명, 84㎡는 1만명 가운데 한 명입니다. 가점이나 통장 가입기간을 보지 않는 추첨이라 누구에게나 같은 확률이 적용됩니다.</p>
  <p>84㎡ 신청자가 오히려 적은 이유도 숫자에 있습니다. 84㎡는 혼인 7년 이내 신혼부부만 넣을 수 있었고, 계약금만 5억5,682만원이 필요했습니다. 넣을 수 있는 사람의 범위가 좁았던 셈입니다. 59㎡A는 서울에 사는 무주택 세대주라면 통장이 없어도 넣을 수 있었고, 계약금도 4억7,382만원으로 한 단계 낮았습니다.</p>

  <h3>잠실 래미안아이파크 줍줍 공급가와 실거래 비교</h3>
  <div class="chart" data-img="카드뉴스 3번 · 84㎡, 실거래의 절반도 안 된다">
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
  <p>몰린 이유는 가격 차이 하나로 설명됩니다. 84㎡D 공급가는 18억5,607만원이고, 같은 면적 입주권은 7월 1일 43억원에 거래됐습니다. 차이는 약 24억4,000만원입니다. 59㎡A 공급가 15억7,940만원은 올해 6월 조합이 정한 보류지 입찰 기준가 30억8,000만원보다 약 15억원 낮습니다.</p>
  <p>비율로 보면 더 분명합니다. 84㎡ 공급가는 최근 거래가의 43% 수준이고, 59㎡A는 보류지 기준가의 51% 수준입니다. 시세의 절반 안팎에 새 아파트를 사는 기회라서 서울 무주택자 수만명이 한꺼번에 움직였습니다. 43㎡ 공급가는 11억548만원인데, 같은 면적의 최근 거래는 확인하지 못해 비교하지 않았습니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 언론이 쓰는 '17억 차익', '24억 로또'는 기사마다 기준이 다릅니다. 어떤 기사는 59㎡를, 어떤 기사는 84㎡를, 어떤 기사는 옵션을 더한 금액을 기준으로 계산했습니다. 차익은 팔았을 때의 이야기이고, 실거주 2년 의무가 붙어 있어 당장 손에 쥐는 돈이 아니라는 점도 같이 봐야 합니다.</p>
  <p>공급가가 이렇게 낮게 남은 이유는 분양가상한제입니다. 이 단지는 2024년 10월 상한제를 적용받아 3.3㎡당 평균 5,409만원에 분양했습니다. 계약취소 재공급은 처음 분양가를 바탕으로 하므로, 그 뒤 2년 동안 오른 잠실 시세는 공급가에 반영되지 않습니다. 시세가 오를수록 줍줍의 '로또' 소리가 커지는 구조입니다.</p>

  <h3>2년 전 첫 분양 경쟁률과 비교하면</h3>
  <div class="chart" data-img="카드뉴스 4번 · 2년 전 59㎡는 591대 1이었다">
    <h3>같은 단지 경쟁률 · 2024년 10월 vs 이번</h3>
    <h4>2024 일반 1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">268.7대 1</span>
      <span class="desc">307가구에 8만2,487명.</span></div>
    <h4>2024 59㎡A</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">591.2대 1</span>
      <span class="desc">24가구에 1만4,190명.</span></div>
    <h4>이번 59㎡A</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">3만3,125대 1</span>
      <span class="desc">1가구, 약 56배.</span></div>
    <p class="cap">2024년 10월 분양 당시 보도(SBS Biz·시대일보 등)와 이번 청약홈 집계 보도 기준입니다. 막대 대신 숫자로 적은 이유는 두 값의 차이가 100배를 넘어 한 축에 그리면 작은 값이 보이지 않기 때문입니다.</p>
  </div>
  <p>같은 단지, 같은 59㎡A인데 경쟁률은 약 56배가 됐습니다. 2024년 10월 첫 분양 때 59㎡A는 24가구에 1만4,190명이 신청해 591.2대 1이었습니다. 일반 1순위 전체로는 307가구에 8만2,487명, 평균 268.7대 1이었고, 특별공급 282가구에도 3만9,478명이 몰렸습니다.</p>
  <p>이번에는 가구 수가 1가구라 경쟁률이 크게 보이는 면이 있습니다. 신청자 수 자체로 보면 59㎡A는 2년 전 1만4,190명에서 3만3,125명으로 2.3배 정도 늘었습니다. 그사이 무순위 자격이 서울 거주 무주택자로 좁아졌는데도 사람이 더 몰렸다는 점이 눈에 띕니다. 분양가는 2024년 그대로인데 잠실 시세만 올라 차이가 벌어진 결과입니다.</p>
  <p>자격이 좁아진 배경도 짚어 둘 만합니다. 국토교통부는 2025년 2월 무순위 청약 자격을 무주택자로 좁히고, 지자체가 거주 요건을 붙일 수 있도록 제도를 바꿨습니다. 그 전에는 집이 있어도, 다른 지역에 살아도 넣을 수 있어 한 가구에 수십만명이 몰린 사례도 있었습니다. 이번 신청자 6만3,950명은 모두 서울에 사는 무주택자라는 점에서, 서울 안의 실수요가 그만큼 두껍다는 신호로 읽힙니다.</p>

  <h3>내일 당첨 발표, 그다음 일정</h3>
  <div class="chart" data-img="카드뉴스 5번 · 내일 발표, 계약은 12월 4일">
    <h3>당첨 뒤 일정과 현금 (공고 보도 기준)</h3>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 27일</span>
      <span class="desc">청약홈에서 조회.</span></div>
    <h4>서류 접수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12월 1일</span>
      <span class="desc">자격 검증.</span></div>
    <h4>계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12월 4일</span>
      <span class="desc">계약금 30%, 84㎡는 5억5,682만원.</span></div>
    <p class="cap">보도된 공급금액에 30%를 곱해 만원 단위로 반올림한 값입니다. 옵션 대금과 취득세는 따로입니다.</p>
  </div>
  <p>당첨자는 내일 11월 27일 청약홈에서 발표합니다. 당첨되면 12월 1일 서류를 내고 12월 4일 계약합니다. 계약금은 공급가의 30%로 43㎡ 3억3,165만원, 59㎡A 4억7,382만원, 84㎡D 5억5,682만원입니다. 나머지 70%는 보도대로라면 계약일부터 30일 안에 내야 합니다.</p>
  <p>예를 들어 59㎡A에 당첨되면 12월 4일 4억7,382만원, 이듬해 1월 초까지 11억558만원을 더 내야 합니다. 84㎡라면 잔금만 12억9,925만원입니다. 여기에 이미 시공된 발코니 확장 같은 옵션 대금과 취득세가 붙습니다. 서류 단계에서 거주지나 무주택 요건이 맞지 않으면 당첨이 취소되고, 그 물량은 예비 순번이나 다음 공급으로 넘어갑니다.</p>
  <p>같은 주에 서울 청약이 하나 더 있습니다. 종로구 경희궁 에피트가 오늘 11월 26일 1순위를 받습니다. 이 단지는 분양가상한제를 적용받지 않아 84㎡ 최고 분양가가 25억원대로, 잠실 줍줍과 달리 시세와 공급가 차이가 크지 않다는 평가가 나옵니다. 같은 서울 청약이라도 분양가가 어떻게 정해졌는지에 따라 경쟁률이 크게 갈린다는 점을 비교해 볼 만합니다.</p>
  <p>다음으로 볼 서울 청약은 서초구 디에이치 반포124입니다. 원래 11월 27일 공고를 계획했지만 분양가 심의가 보류돼 12월 4일 재심의가 예정돼 있다는 보도가 나왔습니다. 심의 결과에 따라 공고와 접수 일정이 뒤로 밀릴 수 있습니다. 이 단지도 분양가상한제 지역이라, 확정 분양가가 나오면 주변 실거래와 이 글과 같은 방식으로 다시 비교해 보겠습니다.</p>

  <h3>발표 전에 볼 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 발표 전에 볼 3가지 (체크리스트)">
    <img class="card-art" data-file="jrr-06-check.png" src="../images/cards/report/jrr-06-check.png" alt="체크포인트 카드 · 1. 27일 청약홈 당첨 조회, 2. 계약금 30% 현금, 3. 실거주 2년·재당첨 10년" loading="lazy" width="1080" height="1080">
    <figcaption>잠실 래미안아이파크 줍줍, 발표 전에 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>27일 청약홈 당첨 조회</strong>. 서류 접수는 12월 1일 하루입니다.</li>
    <li><strong>계약금 30% 현금</strong>. 84㎡ 기준 5억5,682만원, 잔금은 30일 안이라고 보도됐습니다.</li>
    <li><strong>실거주 2년 · 재당첨 10년</strong>. 당첨 뒤 포기해도 이력이 남을 수 있으니 공고문 유의사항을 봅니다.</li>
  </ol>
  <p>당첨되고 계약을 포기하면 끝나는 문제도 아닙니다. 재당첨 제한 10년이 붙은 단지라 당첨 이력이 앞으로의 청약에 영향을 줄 수 있습니다. 잔금 일부를 대출로 채울 생각이라면 발표 전에 거래 은행에 한도를 물어보는 게 순서입니다.</p>

  <h3>정리</h3>
  <p><strong>잠실 래미안아이파크 줍줍</strong>에는 계약취소 3가구에 6만3,950명이 신청했고, 59㎡A 한 가구에만 3만3,125명이 몰렸습니다. <span class="mark">84㎡ 공급가가 최근 거래가의 43% 수준이라는 가격 차이가 이 경쟁률을 만들었습니다.</span> 당첨 발표는 11월 27일, 계약은 12월 4일이며, 계약금 30%와 한 달 안의 잔금, 실거주 2년을 감당할 수 있는지가 당첨 뒤의 관건입니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 신청자 수는 청약홈 집계를 인용한 언론 보도 기준이며, 일정·공급가는 11월 17일 입주자모집공고 보도 기준입니다. 정본은 청약홈(applyhome.co.kr) 공고문입니다. 당첨 포기 시 불이익과 대출 가능 여부는 공고문과 금융기관에 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 이데일리 잠래아 줍줍 5.3만명(2026-11-24) · 한국경제 줍줍 신청자·주간이집(2026-11-24) · 헤럴드경제 잠래아 줍줍 현금(2026-11-25) · 파이낸셜뉴스 3가구 무순위 공급(2026-11-17) · 파이낸셜뉴스 보류지 입찰 기준가(2026-06) · 국토교통부 실거래가 공개시스템(입주권 2026-07) · 2024년 10월 분양 경쟁률 보도(SBS Biz·시대일보)<br>
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
assert 33125 + 20322 == 53447 and 53447 + 10503 == 63950 and 53447 / 2 == 26723.5
assert round(20322 / 33125 * 100, 1) == 61.3 and round(10503 / 33125 * 100, 1) == 31.7
assert round(33125 / 591.2) == 56
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
