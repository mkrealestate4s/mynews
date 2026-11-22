# -*- coding: utf-8 -*-
"""리포트 #135 (2026-11-23 월) 11월 넷째 주 청약 일정 · 서울 4곳 묶음. #134를 복제해 교체한다.

메인 검색어: 11월 넷째 주 청약
요일 종류: 월요일 이번 주 청약·분양 일정 묶음(일정형).
핫이슈 훑기: 6검색 결과 최근 48시간 새 핫이슈 없음. 잠실 래미안아이파크 줍줍은 #133 으로 썼고 오늘 접수 시작이라 묶음 한 섹션으로만 둔다.

수치와 검산
  사건일과 오늘의 간격: 주간 분양캘린더(리얼투데이) 11/21 보도 → 2일. 접수 11/23~27 → 오늘부터.
  전국 15곳 6,295가구(오피스텔 포함) · 전주 1,681 · 수도권 8곳 2,904 · 지방 7곳 3,391 (뉴스1·이투데이·데일리안 11/21)
  해링턴 플레이스 문래: 218가구 전부 84㎡ · 특공 11/23 · 1순위 해당 11/24 · 기타 11/25 · 2순위 11/26 · 발표 12/2 · 계약 12/14~16
    · 최고 분양가 84A 18억2,700만(110) · 84B 17억8,500만(54) · 84C 17억7,500만(54) · 입주 2030년 3월 (비즈워치·이코노미스트 11/18~19)
  경희궁 에피트: 228가구(일반 135, 일부 보도 134) · 특공 11/25 · 1순위 11/26 · 발표 12/4 · 84㎡ 최고 25억7,484만 (#126)
  잠실 래미안아이파크 줍줍: 특공 11/23 · 일반 11/24 · 발표 11/27 · 84㎡D 18억5,607만 · 59㎡A 15억7,940만 · 43㎡ 11억548만 · 계약금 30% (#133)
  디에이치 반포124: 공고 11/27 예정(10월 보도 계획, 확인 필요) · 특공 12/7 · 1순위 12/8 (#130)
  대시보드 세로 (6,295 → 86): 2,904 → 39.7 · 3,391 → 46.3 · 1,681 → 23.0
  카드4 가로 (25억7,484만 → 100): 18억5,607만 → 72.1 · 18억2,700만 → 71.0

단정하지 않은 것
  · 디에이치 반포124 공고일: 10월 보도 기준 계획. 청약홈 공고로 확인
  · 분양가는 최고가 기준 보도. 타입별 최저가·계약금 비율(해링턴·에피트)은 공고문 확인
  · 시흥 거모 아테라 신혼희망타운은 보도마다 가구수·일정이 달라 뺐다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-22-dongtan-high.html"
SLUG, PRE = "2026-11-23-nov-week4-seoul", "nw4"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 135, "2026-11-23"
PREV_SLUG = "dongtan-high"
BANNED = ["반도유보라", "dth-"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "11월 넷째 주 청약 일정, 서울 4곳 날짜순 정리"
DESC = ("11월 넷째 주 청약은 전국 15곳 6,295가구로 전주의 3.7배입니다. 서울에서는 잠실 래미안아이파크 줍줍(23·24일), 해링턴 플레이스 문래(24일 1순위), "
        "경희궁 에피트(26일 1순위)가 접수를 받고 디에이치 반포124 공고가 27일 예정돼 있습니다. 날짜순으로 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="23일 래미안아이파크 줍줍, 24일 해링턴 플레이스 문래, 26일 경희궁 에피트, 27일 반포124 공고 예정. 전국 6,295가구.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">11월 넷째 주 청약,<br>서울 4곳 날짜순</h1>
  <p class="sub">이번 주 청약은 전국 <strong>15곳 6,295가구</strong>로 전주의 3.7배입니다. 서울은 잠실 래미안아이파크 줍줍, 해링턴 플레이스 문래, 경희궁 에피트가 접수를 받고 <strong>디에이치 반포124</strong> 공고가 27일 예정돼 있습니다. <span class="mark">84㎡ 분양가는 18억에서 25억까지 벌어집니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/23~27</div><div class="kw">6,295가구</div>
      <p>전국 <strong>15곳</strong> 청약 접수.</p></div>
    <div class="kcard"><div class="hot">전주 대비</div><div class="kw">3.7배</div>
      <p>전주 <strong>1,681가구</strong>에서 늘었다.</p></div>
    <div class="kcard"><div class="hot">서울 1순위</div><div class="kw">2곳</div>
      <p>문래 <strong>24일</strong>, 경희궁 <strong>26일</strong>.</p></div>
    <div class="kcard"><div class="hot">공고 예정</div><div class="kw">27일</div>
      <p>디에이치 반포124, <strong>확인 필요</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>11월 넷째 주 청약 물량 (가구)</h3>
    <span class="badge">전주의 3.7배</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">6,295</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:39.7%">2,904</div><div class="barv" style="--h:39.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:46.3%">3,391</div><div class="barv" style="--h:46.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:23%">1,681</div><div class="barv" style="--h:23%"></div></div>
    </div>
    <div class="collbl"><span>이번 주 전국</span><span>수도권</span><span>지방</span><span>전주 전국</span></div>
    <p class="cap">리얼투데이 집계(뉴스1·이투데이 11월 21일 보도) 기준이며 오피스텔을 포함합니다. 수도권 8곳, 지방 7곳입니다. 막대 길이는 최댓값 6,295가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 11월 넷째 주 청약, 서울 4곳"),
    ("02-cal", "이번 주 서울 청약 달력"),
    ("03-zup", "잠실 래미안아이파크 줍줍 3가구"),
    ("04-price", "84㎡ 분양가, 세 곳 비교"),
    ("05-week", "이번 주 물량, 전주의 3.7배"),
    ("06-check", "이번 주 청약 넣기 전 3가지"),
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

ARTICLE = '''<article data-tags="11월넷째주청약,이번주청약일정,해링턴플레이스문래,경희궁에피트,잠실래미안아이파크,디에이치반포124,서울청약,무순위청약,청약일정,분양캘린더">
  <h2>11월 넷째 주 청약 일정, 서울 4곳 날짜순 정리</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 11월 넷째 주 청약, 서울 4곳"></span>

  <p><strong>3줄 요약</strong><br>11월 넷째 주 청약은 전국 15곳 6,295가구로, 전주 1,681가구의 3.7배입니다.<br>서울은 23·24일 잠실 래미안아이파크 줍줍, 24일 해링턴 플레이스 문래 1순위, 26일 경희궁 에피트 1순위가 차례로 열립니다.<br>84㎡ 기준 분양가는 문래 18억2,700만원부터 경희궁 25억7,484만원까지 7억원 넘게 차이가 나니 자금 계획부터 맞춰 보는 게 먼저입니다.</p>

  <p>11월 넷째 주 청약 일정이 오늘부터 시작됩니다. 부동산 정보업체 리얼투데이 집계로 이번 주 전국 15곳에서 6,295가구가 청약 접수를 받습니다. 수도권이 8곳 2,904가구, 지방이 7곳 3,391가구입니다. 서울만 보면 무순위 한 곳, 1순위 두 곳, 공고 예정 한 곳이 날짜를 나눠 잡고 있어 하루씩 겹치지 않게 따라가면 됩니다. 오늘은 서울 네 곳을 날짜순으로 정리합니다.</p>

  <h3>11월 넷째 주 청약 일정, 날짜순 달력</h3>
  <div class="chart" data-img="카드뉴스 2번 · 이번 주 서울 청약 달력">
    <h3>이번 주 서울 청약 (2026년 11월 23~27일)</h3>
    <h4>잠실 래미안아이파크 줍줍 · 해링턴 플레이스 문래 특공</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">23일</span>
      <span class="desc">래미안아이파크 신혼 특공 1가구, 문래 특별공급.</span></div>
    <h4>잠실 래미안아이파크 일반 · 해링턴 플레이스 문래 1순위</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">24일</span>
      <span class="desc">래미안아이파크 일반 2가구, 문래 1순위 해당지역.</span></div>
    <h4>경희궁 에피트 특공</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">25일</span>
      <span class="desc">특별공급 접수. 문래는 1순위 기타지역.</span></div>
    <h4>경희궁 에피트 1순위</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">26일</span>
      <span class="desc">1순위 접수. 문래는 2순위.</span></div>
    <h4>디에이치 반포124 공고 예정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">27일</span>
      <span class="desc">10월 보도 기준 계획. 래미안아이파크 당첨 발표.</span></div>
    <p class="cap">각 단지 분양 일정 보도와 리얼투데이 주간 분양캘린더 기준입니다. 디에이치 반포124 공고일은 계획이라 청약홈 공고로 확인해야 합니다.</p>
  </div>
  <p>달력으로 보면 이번 주는 24일과 26일이 고비입니다. 24일에는 잠실 래미안아이파크 일반공급과 해링턴 플레이스 문래 1순위 해당지역 접수가 같은 날 열립니다. 26일에는 경희궁 에피트 1순위가 있습니다. 같은 날 두 곳에 넣을 수 있는지는 단지와 공급 유형마다 달라 청약홈에서 확인하고 넣어야 합니다.</p>
  <p>왜 이번 주에 물량이 몰렸는지도 볼 만합니다. 전주 전국 물량은 1,681가구에 그쳤는데 이번 주는 6,295가구로 늘었습니다. 연말 전에 분양을 마치려는 단지들이 11월 말과 12월 초에 일정을 잡는 일이 매년 반복됩니다. 견본주택은 6곳이 새로 문을 열고, 당첨자 발표는 8곳, 정당계약은 10곳에서 진행됩니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 무순위(줍줍)는 청약통장이 필요 없지만 1순위 청약은 통장 가입 기간과 납입 횟수를 채워야 합니다. 같은 주에 열린다고 같은 조건으로 넣을 수 있는 게 아닙니다.</p>

  <h3>23·24일 잠실 래미안아이파크 줍줍</h3>
  <div class="chart" data-img="카드뉴스 3번 · 잠실 래미안아이파크 줍줍 3가구">
    <h3>잠실 래미안아이파크 계약취소 재공급 (공급가)</h3>
    <h4>84㎡D · 신혼 특공 · 23일</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">18억5,607만</span>
      <span class="desc">1가구.</span></div>
    <h4>59㎡A · 일반 · 24일</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">15억7,940만</span>
      <span class="desc">1가구.</span></div>
    <h4>43㎡ · 일반 · 24일</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11억548만</span>
      <span class="desc">1가구.</span></div>
    <p class="cap">입주자모집공고(11월 17일) 보도 기준입니다. 서울 거주 무주택 세대 구성원만 신청할 수 있고 계약금은 공급가의 30%입니다.</p>
  </div>
  <p>이번 주 첫날은 잠실 래미안아이파크 계약취소분 3가구입니다. 23일 신혼부부 특별공급으로 84㎡D 1가구, 24일 일반공급으로 43㎡와 59㎡A 각 1가구를 받습니다. 당첨 발표는 27일, 계약은 12월 4일입니다. 이미 지어져 입주가 2027년 1월로 잡힌 단지라 계약 뒤 잔금까지 시간이 짧습니다.</p>
  <p>공급가가 몇 년 전 분양가 그대로라 시세와 차이가 큽니다. 84㎡ 입주권은 7월에 43억원(28층)에 거래됐다는 보도가 있었는데, 공급가 18억5,607만원과 비교하면 24억원 넘게 차이가 납니다. 그래서 기사마다 '20억 로또'라는 말이 붙었습니다.</p>
  <p>다만 돈이 먼저 필요합니다. 계약금 30%면 84㎡는 약 5억5,682만원을 12월 4일에 내야 합니다. 실거주 2년 의무와 재당첨 제한 10년도 붙습니다. 자격과 일정은 지난 글에서 자세히 다뤘으니 여기서는 날짜만 챙기시면 됩니다.</p>

  <h3>24일 해링턴 플레이스 문래 1순위</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡ 분양가, 세 곳 비교">
    <h3>이번 주 서울 84㎡ 분양가 (최고가 기준)</h3>
    <div class="bar"><label>경희궁 에피트</label>
      <div class="rail"><div class="fill" style="width:100%">25억7,484만</div></div></div>
    <div class="bar"><label>래미안아이파크 줍줍</label>
      <div class="rail"><div class="fill gray" style="width:72.1%">18억5,607만</div></div></div>
    <div class="bar"><label>해링턴 플레이스 문래</label>
      <div class="rail"><div class="fill gray" style="width:71%">18억2,700만</div></div></div>
    <p class="cap">각 단지 입주자모집공고 보도의 84㎡ 최고 분양가 기준입니다. 래미안아이파크는 계약취소분 공급가입니다. 막대 길이는 최댓값 25억7,484만원을 기준으로 맞췄습니다.</p>
  </div>
  <p>영등포구 문래동 해링턴 플레이스 문래는 23일 특별공급을 시작으로 24일 1순위 해당지역, 25일 기타지역, 26일 2순위를 받습니다. 지하 3층에서 지상 29층, 218가구 규모이고 모든 가구가 전용 84㎡ 한 가지 면적입니다. 당첨자 발표는 12월 2일, 정당계약은 12월 14일부터 16일까지이고 입주는 2030년 3월 예정입니다.</p>
  <p>분양가는 84㎡A 최고 18억2,700만원(110가구), 84㎡B 17억8,500만원(54가구), 84㎡C 17억7,500만원(54가구)으로 보도됐습니다. 이번 주 서울 84㎡ 가운데 가장 낮은 축이지만 18억원 안팎이면 대출만으로 맞추기 어려운 금액입니다. 타입별 최저가와 계약금 비율은 공고문에서 확인해야 합니다.</p>
  <p>같은 84㎡라도 이번 주 세 곳의 차이는 큽니다. 경희궁 에피트 최고가와 문래 최고가는 7억4,784만원 차이입니다. 입지와 분양가상한제 적용 여부, 준공 시점이 다 다르니 금액만 놓고 고르기보다 내 자금이 어느 선까지 되는지부터 정해 두는 게 순서입니다.</p>
  <p>대출로 예시를 들면 차이가 더 분명해집니다. 10·15 대책의 주택담보대출 한도는 집값 15억원 이하 6억원, 15억~25억원 4억원, 25억원 초과 2억원입니다. 이 기준을 그대로 대면 문래 84㎡A 18억2,700만원은 최대 4억원이라 14억2,700만원을 다른 돈으로 채워야 하고, 경희궁 에피트 25억7,484만원은 최대 2억원이라 23억원 넘게 필요합니다. 다만 새 아파트 잔금대출은 입주 시점의 규정과 시세로 정해지니 실제 한도는 은행에 따로 물어봐야 합니다.</p>

  <h3>26일 경희궁 에피트 1순위</h3>
  <p>종로구 교남동 경희궁 에피트는 25일 특별공급, 26일 1순위 접수를 받고 12월 4일 당첨자를 발표합니다. 계약은 12월 16일부터 18일까지로 안내됐습니다. 전체 228가구 가운데 일반분양은 135가구입니다(일부 보도 134가구).</p>
  <p>이 단지는 분양가상한제 적용 단지가 아닙니다. 그래서 84㎡ 최고 분양가가 25억7,484만원까지 올라갔습니다. '서울 새 아파트는 다 로또'라는 생각으로 넣었다가 시세와 차이가 크지 않아 당황하는 경우가 생길 수 있습니다. 주변 실거래가와 비교한 내용은 앞서 다룬 글을 참고하시면 됩니다.</p>
  <p>시흥 거모 아테라 신혼희망타운도 같은 26일 1순위로 보도됐지만 기사마다 공급 가구수와 접수 기간이 달라 이 글에서는 뺐습니다. 신혼희망타운을 노리는 분이라면 LH 청약플러스 공고문을 직접 보시는 게 정확합니다.</p>

  <h3>11월 넷째 주 청약, 전국 물량은</h3>
  <span class="imgslot" hidden data-img="카드뉴스 5번 · 이번 주 물량, 전주의 3.7배"></span>
  <p>서울 밖에서는 지방 물량이 더 많습니다. 지방 7곳 3,391가구 가운데 울산 동구 화정1지구 아르엘이 802가구로 가장 크고, 충남 논산 엘리프 논산 디에디션 499가구, 전북 익산 두산위브 트레지움 익산 251가구, 부산 동구 호반써밋 초량 236가구가 뒤를 잇습니다. 수도권은 8곳 2,904가구입니다.</p>
  <p>숫자로 비교하면 이번 주 물량은 전주보다 4,614가구 많습니다. 다만 집계에는 오피스텔이 섞여 있어 아파트만 세면 이보다 적습니다. 매체마다 '6,200여 가구', '15개 단지'처럼 표기도 조금씩 달라 단지별 일정은 청약홈에서 다시 보는 게 안전합니다.</p>

  <h3>27일 디에이치 반포124 공고 예정</h3>
  <p>이번 주 마지막 날짜는 디에이치 반포124입니다. 10월 보도로는 11월 27일 입주자모집공고, 12월 7일 특별공급, 12월 8일 1순위 일정이 계획돼 있었습니다. 일반분양 1,832가구 중 84㎡가 1,358가구로 강남권에서 보기 드문 물량입니다. <span class="mark">다만 공고일은 계획이라 실제 공고가 청약홈에 올라와야 확정됩니다.</span> 공고가 나오면 확정 분양가로 다시 정리하겠습니다.</p>

  <h3>이번 주 청약 넣기 전 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 이번 주 청약 넣기 전 3가지 (체크리스트)">
    <img class="card-art" data-file="nw4-06-check.png" src="../images/cards/report/nw4-06-check.png" alt="체크포인트 카드 · 1. 날짜별 자격, 2. 계약금 마련 시점, 3. 공고일 확인" loading="lazy" width="1080" height="1080">
    <figcaption>이번 주 청약 넣기 전에 볼 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>날짜별 자격</strong>. 무순위는 통장 없이, 1순위는 통장 조건이 필요합니다. 거주지 요건도 단지마다 다릅니다.</li>
    <li><strong>계약금 마련 시점</strong>. 래미안아이파크는 12월 4일, 문래는 12월 14일부터 계약입니다.</li>
    <li><strong>공고일 확인</strong>. 디에이치 반포124 공고는 계획입니다. 청약홈에서 실제 공고를 확인하십시오.</li>
  </ol>
  <p>다음 주 날짜도 미리 적어 둡니다. 27일 래미안아이파크 당첨 발표, 12월 2일 문래 당첨 발표, 12월 4일 경희궁 에피트 당첨 발표와 래미안아이파크 계약이 이어집니다. 반포124 공고가 예정대로 나오면 12월 첫 주에 특별공급과 1순위가 몰립니다.</p>

  <h3>정리</h3>
  <p><strong>11월 넷째 주 청약</strong>은 전국 15곳 6,295가구로 전주의 3.7배입니다. 서울은 23·24일 잠실 래미안아이파크 줍줍, 24일 해링턴 플레이스 문래 1순위, 26일 경희궁 에피트 1순위가 열리고 27일 디에이치 반포124 공고가 예정돼 있습니다. <span class="mark">84㎡ 분양가가 18억원대에서 25억원대까지 벌어지니 넣기 전에 계약금과 잔금 계획부터 맞춰 보시기 바랍니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 물량은 리얼투데이 집계(오피스텔 포함) 보도 기준이고, 분양가는 각 단지 입주자모집공고 보도의 최고가 기준입니다. 디에이치 반포124 공고일은 계획이며 바뀔 수 있습니다. 청약 자격과 일정은 청약홈 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 뉴스1·이투데이·데일리안 11월 넷째 주 분양캘린더(리얼투데이 집계, 2026-11-21) · 비즈워치·이코노미스트 해링턴 플레이스 문래 분양(2026-11-18~19) · 파이낸셜뉴스·서울경제·뉴스1 잠실 래미안아이파크 무순위 공고(2026-11-17~18) · 대한경제 경희궁 에피트 분양(2026-11-11) · 디에이치 반포124 분양 일정 보도(2026-10)<br>
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
for v, hh in ((2904, 39.7), (3391, 46.3), (1681, 23.0)):
    assert round(v / 6295 * 86, 1) == hh
assert 2904 + 3391 == 6295 and round(6295 / 1681, 1) == 3.7 and 6295 - 1681 == 4614
assert round(185607 / 257484 * 100, 1) == 72.1 and round(182700 / 257484 * 100, 1) == 71.0
assert 182700 - 40000 == 142700 and 257484 - 20000 > 230000
assert 257484 - 182700 == 74784 and round(185607 * 0.3) == 55682 and 430000 - 185607 > 240000
KW = "11월 넷째 주 청약"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("11월넷째주청약")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
