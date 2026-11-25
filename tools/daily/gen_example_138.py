# -*- coding: utf-8 -*-
"""리포트 #138 (2026-11-25 수 오후 · 특집 · 추가 발행 x1) 위반건축물 양성화 12월 17일 시행. #137을 복제해 교체한다.

메인 검색어: 위반건축물 양성화
요청: 사용자 지시 특집("위반건축물 양성화 관련 내용 특집으로 오늘 하나 더"). 마감·시행일이 걸린 글이라 실행 가이드로 쓴다(일정 → 대상 → 절차 → 함정 → 체크).

수치와 검산
  사건일과 오늘의 간격: 시행 12/17 → D-22. 시행령 입법예고 마감 11/9 → 16일 전.
  법: 특정건축물 정리에 관한 특별조치법 · 본회의 재석 158 찬성 155(이투데이) · 공포 6/16 · 시행 12/17(공포 후 6개월, 건축사신문)
  신고 기간 18개월 2026-12-17 ~ 2028-06-16(전북도 발표, 뉴스1) · 시행령 제정안 입법예고 9/30~11/9(국토부)
  대상: 2023-12-31 이전 사실상 완공 소규모 주거용 · 단독 165㎡ · 다가구 660㎡(당정 1월 보도, 한국경제·뉴스1) · 다세대 세대당 85㎡(해설 자료, 시행령 확인)
  제외: 개발제한구역 · 군사시설 보호구역 · 정비구역 · 보전산지 · 투기성·고의성
  절차: 건축사 설계도서·현장조사서 → 시·군·구 신고 → 심의 → 과태료 납부 뒤 사용승인(전북도: 신고 후 30일 안 심의·승인)
  규모(국토부 2025-10-01 발표, 경향신문·뉴시스): 위반건축물 14.8만동 · 주거용 8.3만 · 소규모 주택 4.6만(54.7%) · 양성화 범위 약 4만동
  대시보드 세로 (14.8 → 86): 8.3 → 48.2 · 4.6 → 26.7 · 4.0 → 23.2
  비율: 4.6/8.3 = 55.4%(보도 54.7%는 원자료 반올림 차이라 보도값을 쓴다) · 4/14.8 = 27%

단정하지 않은 것
  · 과태료 수준: 법안소위 대안에 '이행강제금 5회분' 보도. 최종 법·시행령 금액은 구청 확인
  · 근생빌라 포함 여부·조건: 전북도 안내는 포함, 해설 자료는 세대 수 늘린 경우 제외. 확인 필요
  · 시행령 확정 공포: 검색에서 확인 못 함
  · 다세대 85㎡ 기준은 해설 자료 기준
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-25-jongbu-nonresident.html"
SLUG, PRE = "2026-11-25-violation-building", "vbl"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 138, "2026-11-25"
PREV_SLUG = "jongbu-nonresident"
BANNED = ["종부세", "jbs-", "공정시장가액"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "위반건축물 양성화 12월 17일 시행, 우리 집 해당될까"
DESC = ("위반건축물 양성화 특별법(특정건축물 정리에 관한 특별조치법)이 12월 17일 시행됩니다. 2023년 12월 31일 이전에 지은 소규모 주거용 건물이 대상이고 "
        "신고 기간은 2028년 6월 16일까지 18개월입니다. 대상, 신고 절차, 빠지는 경우, 비용을 실행 순서대로 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="12월 17일부터 18개월. 2023년 말 이전 소규모 주거용 위반건축물, 구청 신고 뒤 사용승인. 대상·절차·제외 정리.">
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
  <div class="eyebrow">2026 · 11월 부동산 키워드 리포트 #{NO} · 특집</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">위반건축물 양성화,<br>12월 17일 시작</h1>
  <p class="sub">소규모 주거용 위반건축물을 한시적으로 합법화하는 특별법이 <strong>12월 17일</strong> 시행됩니다. 신고 기간은 <strong>2028년 6월 16일까지 18개월</strong>입니다. <span class="mark">2014년 이후 약 10년 만에 다시 열리는 길입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 시행일</div><div class="kw">12월 17일</div>
      <p>오늘부터 <strong>22일</strong> 남았다.</p></div>
    <div class="kcard"><div class="hot">신고 기간</div><div class="kw">18개월</div>
      <p><strong>2028년 6월 16일</strong>까지.</p></div>
    <div class="kcard"><div class="hot">대상 건물</div><div class="kw">2023년 말</div>
      <p>이전에 <strong>사실상 완공</strong>된 곳.</p></div>
    <div class="kcard"><div class="hot">예상 범위</div><div class="kw">약 4만동</div>
      <p>국토부 <strong>추정</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>전국 위반건축물 규모 (만 동)</h3>
    <span class="badge">양성화 범위는 약 4만동</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">14.8만</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:48.2%">8.3만</div><div class="barv" style="--h:48.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:26.7%">4.6만</div><div class="barv" style="--h:26.7%"></div></div>
      <div class="col"><div class="v gtx" style="--h:23.2%">약 4만</div><div class="barv" style="--h:23.2%"></div></div>
    </div>
    <div class="collbl"><span>전체</span><span>주거용</span><span>소규모 주택</span><span>양성화 예상</span></div>
    <p class="cap">국토교통부 2025년 10월 1일 '위반건축물 합리적 관리방안' 발표 보도 기준입니다. 소규모 주택은 단독·다가구·다세대이고, 양성화 예상 범위는 국토부 추정입니다. 막대 길이는 14.8만동을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 위반건축물 양성화, 12월 17일 시작"),
    ("02-scale", "주거용 위반건축물, 약 4만동이 대상"),
    ("03-when", "언제부터 언제까지"),
    ("04-who", "우리 집이 대상인지"),
    ("05-how", "신고에서 사용승인까지"),
    ("06-check", "위반건축물 양성화 체크 3가지"),
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

ARTICLE = '''<article data-tags="위반건축물양성화,위반건축물,불법건축물양성화,특정건축물정리특별조치법,근생빌라,이행강제금,사용승인,다가구주택,빌라,건축물대장">
  <h2>위반건축물 양성화 12월 17일 시행, 우리 집 해당될까</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 위반건축물 양성화, 12월 17일 시작"></span>

  <p><strong>3줄 요약</strong><br>위반건축물 양성화 특별법이 12월 17일 시행되고, 신고는 2028년 6월 16일까지 18개월 동안 받습니다.<br>2023년 12월 31일 이전에 사실상 다 지은 단독·다가구·다세대 같은 소규모 주거용 건물이 대상입니다.<br>건축사 도면을 갖춰 구청에 신고하고 과태료를 내면 사용승인을 받을 수 있지만, 금액과 세부 기준은 시행령과 구청 안내로 확인해야 합니다.</p>

  <p>위반건축물 양성화가 약 10년 만에 다시 열립니다. 정식 이름은 「특정건축물 정리에 관한 특별조치법」입니다. 국회 본회의에서 재석 158명 가운데 155명 찬성으로 통과했고, 6월 16일 공포돼 6개월 뒤인 12월 17일부터 시행됩니다. 베란다를 넓히거나 옥상에 방을 들인 빌라, 허가 없이 증축한 단독주택처럼 건축물대장에 '위반건축물' 딱지가 붙은 집이 대상입니다. 시행이 3주 남은 지금, 우리 집이 해당하는지와 무엇을 준비해야 하는지 순서대로 정리했습니다.</p>

  <h3>위반건축물 양성화, 왜 다시 하나요?</h3>
  <span class="imgslot" hidden data-img="카드뉴스 2번 · 주거용 위반건축물, 약 4만동이 대상"></span>
  <p>위반건축물이 너무 많고, 사는 사람이 피해를 보기 때문입니다. 국토교통부가 2025년 10월 1일 내놓은 관리방안을 보면 전국 위반건축물은 약 14만8천동이고, 그 가운데 주거용이 약 8만3천동입니다. 주거용의 54.7%인 4만6천동이 단독·다가구·다세대 같은 소규모 주택입니다. 국토부는 이번 양성화 범위에 약 4만동이 들어갈 것으로 봤습니다.</p>
  <p>위반건축물이 되면 사는 사람에게 실제 손해가 생깁니다. 시정할 때까지 이행강제금이 해마다 붙고, 전세대출이나 전세보증보험 가입이 막히는 경우가 있습니다. 그래서 세입자를 구하기 어렵고 집을 팔 때도 값이 깎입니다. 위반 사실을 모르고 산 사람도 같은 처지가 된다는 점이 이번 법을 만든 이유로 꼽힙니다.</p>
  <p>이행강제금 부담이 커진 배경도 있습니다. 예전에는 같은 위반에 이행강제금을 매기는 횟수가 5회로 묶여 있었지만, 2019년 건축법 개정으로 이 제한이 없어졌습니다. 그래서 시정하지 않으면 해마다 계속 내야 하는 구조가 됐고, 오래된 위반건축물을 가진 집주인일수록 누적 부담이 커졌습니다. 양성화는 이 고리를 한 번에 끊는 방법입니다.</p>
  <p>이런 한시 양성화는 처음이 아닙니다. 2014년에도 같은 이름의 특별조치법으로 한 차례 길이 열렸고, 이번이 그 뒤 약 10년 만입니다. 반대로 정부는 양성화 기간이 끝나면 이행강제금을 시정 때까지 반복해서 매기고, 임대처럼 돈을 버는 목적의 위반은 더 무겁게 매기는 쪽으로 단속을 강화하겠다고 밝혔습니다. 이번 기회를 놓치면 다음은 더 어렵다는 뜻입니다.</p>

  <h3>위반건축물 양성화, 언제부터 언제까지인가요?</h3>
  <div class="chart" data-img="카드뉴스 3번 · 언제부터 언제까지">
    <h3>위반건축물 양성화 일정</h3>
    <h4>법 공포</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">6월 16일</span>
      <span class="desc">특정건축물 정리에 관한 특별조치법.</span></div>
    <h4>시행령 입법예고</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 9일</span>
      <span class="desc">9월 30일부터 의견 접수, 마감.</span></div>
    <h4>시행 · 신고 시작</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">12월 17일</span>
      <span class="desc">오늘부터 22일 뒤.</span></div>
    <h4>신고 마감</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2028년 6월</span>
      <span class="desc">16일까지, 18개월.</span></div>
    <p class="cap">건축사신문, 국토교통부 입법예고, 전북도 발표(뉴스1) 기준입니다. 시행령은 입법예고 단계까지 확인했으며 최종 공포본에서 세부 내용이 달라질 수 있습니다.</p>
  </div>
  <p>12월 17일부터 2028년 6월 16일까지 18개월입니다. 법은 6월 16일 공포됐고 부칙에서 공포 6개월 뒤 시행으로 정했습니다. 세부 기준을 담은 시행령 제정안은 9월 30일부터 11월 9일까지 입법예고를 거쳤습니다. 전북도는 이미 이 18개월 일정으로 양성화를 시행한다고 밝혔습니다.</p>
  <p>18개월이 길어 보이지만 서두를 이유가 있습니다. 신고하려면 건축사가 그린 도면과 현장조사서가 필요한데, 시행 초기에 신청이 몰리면 건축사 일정을 잡는 것부터 늦어질 수 있습니다. 서울 종로구처럼 '특정건축물 지원센터'를 열어 신고 접수와 상담을 한곳에서 받겠다는 자치구도 있으니, 내 구청이 창구를 따로 여는지부터 보는 게 좋습니다.</p>
  <p>신고는 건축주나 소유자가 합니다. 세입자가 대신 신청하는 구조가 아니므로, 위반 표시가 걸린 집에 세 들어 사는 분이라면 집주인에게 양성화 계획을 물어보는 것이 할 수 있는 일입니다. 다가구·다세대처럼 소유자가 여럿인 건물은 누가 비용을 나눠 낼지부터 정해야 해서 준비가 더 오래 걸립니다.</p>

  <h3>우리 집이 위반건축물 양성화 대상인가요?</h3>
  <div class="chart" data-img="카드뉴스 4번 · 우리 집이 대상인지">
    <h3>대상 기준 (보도·해설 기준)</h3>
    <h4>완공 시점</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">2023년 말</span>
      <span class="desc">12월 31일 이전 사실상 완공.</span></div>
    <h4>단독주택 · 연면적</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">165㎡</span>
      <span class="desc">당정 협의 보도 기준.</span></div>
    <h4>다가구주택 · 연면적</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">660㎡</span>
      <span class="desc">당정 협의 보도 기준.</span></div>
    <h4>다세대주택 · 세대당 전용</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">85㎡</span>
      <span class="desc">해설 자료 기준, 시행령 확인.</span></div>
    <p class="cap">단독·다가구 면적은 2026년 1월 당정 협의 보도(한국경제·뉴스1), 다세대는 해설 자료 기준입니다. 기준이 연면적과 세대당 전용면적으로 달라 한 축에 놓지 않았습니다. 이하·미만 구분과 조례 위임 범위는 시행령과 구청에서 확인이 필요합니다.</p>
  </div>
  <p>2023년 12월 31일 이전에 사실상 다 지은 소규모 주거용 건물이면 대상일 가능성이 큽니다. 보도와 해설 자료를 종합하면 단독주택은 연면적 165㎡, 다가구주택은 660㎡, 다세대주택은 세대당 전용 85㎡ 안팎이 기준으로 알려져 있습니다. 2024년 이후에 새로 생긴 위반은 이번 양성화로 구제받지 못합니다. 같은 건물이라도 2023년 이전에 늘린 부분은 대상이 되고 그 뒤에 늘린 부분은 빠질 수 있으니, 공사 시점을 보여 줄 사진이나 계약서가 있다면 미리 챙겨 두는 게 좋습니다.</p>
  <p>근생빌라는 자주 헷갈리는 대목입니다. 근린생활시설로 허가받고 실제로는 주택으로 쓰는 건물인데, 전북도 안내에는 대상에 들어가 있고 안전·주차 기준을 맞추면 포함될 수 있다는 보도도 있습니다. 반면 세대 수를 늘린 경우는 빠진다는 해설도 있어 아직 한 문장으로 정리하기 어렵습니다. 근생빌라라면 시행령 공포본과 구청 건축과 안내를 꼭 맞춰 보는 게 안전합니다.</p>
  <p>빠지는 경우도 정해져 있습니다. 개발제한구역, 군사시설 보호구역, 정비구역, 보전산지처럼 공익을 해칠 우려가 있는 곳의 건물은 대상이 아닙니다. 투기 목적이거나 일부러 위반한 것으로 보이는 건물도 제외됩니다. 재개발·재건축 정비구역 안의 빌라라면 이번 양성화가 아니라 정비사업 절차를 따라야 한다는 뜻입니다.</p>

  <h3>위반건축물 양성화 신고는 어떻게 하나요?</h3>
  <div class="chart" data-img="카드뉴스 5번 · 신고에서 사용승인까지">
    <h3>신고에서 사용승인까지</h3>
    <h4>1단계</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">도면</span>
      <span class="desc">건축사가 설계도서·현장조사서 작성.</span></div>
    <h4>2단계</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">신고</span>
      <span class="desc">시·군·구청 건축 부서에 접수.</span></div>
    <h4>3단계</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">심의</span>
      <span class="desc">안전·주차 등 기준 검토.</span></div>
    <h4>4단계</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">사용승인</span>
      <span class="desc">과태료 낸 뒤 대장 정리.</span></div>
    <p class="cap">전북도 발표(뉴스1)와 법안 보도 기준입니다. 전북도는 신고 뒤 30일 안에 심의와 사용승인을 진행한다고 안내했습니다. 지자체마다 처리 방식이 다를 수 있습니다.</p>
  </div>
  <p>순서는 도면, 신고, 심의, 사용승인입니다. 건축주나 소유자가 건축사에게 설계도서와 현장조사서를 받아 관할 시·군·구청에 신고하면, 지자체가 안전과 주차 기준 등을 심의한 뒤 사용승인을 내줍니다. 전북도는 신고 뒤 30일 안에 심의와 사용승인을 마치겠다고 안내했습니다. 서류가 갖춰져 있다면 생각보다 빨리 끝날 수 있다는 뜻입니다. 사용승인이 나면 건축물대장에서 위반건축물 표시가 정리되는 구조입니다.</p>
  <p>돈은 두 갈래로 듭니다. 하나는 건축사 도면과 현장조사 비용이고, 다른 하나는 양성화의 대가로 내는 과태료입니다. 과태료는 국회 법안소위 단계에서 '이행강제금 5회분 수준'으로 논의됐다는 보도가 있지만, 최종 금액 산식은 시행령과 구청 안내로 확인해야 합니다. 이미 밀린 이행강제금이 있으면 1년 안에 내는 조건으로 승인받을 수 있다는 보도도 있습니다.</p>
  <p>예외도 하나 있습니다. 전세사기 피해자가 경매 등으로 떠안은 위반건축물은 과태료와 주차장 설치 의무를 면제하는 특례가 들어갔습니다. 전세사기 피해 주택을 낙찰받은 분이라면 이 특례를 먼저 확인하는 게 좋습니다.</p>

  <h3>위반건축물 양성화 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 위반건축물 양성화 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="vbl-06-check.png" src="../images/cards/report/vbl-06-check.png" alt="체크포인트 카드 · 1. 건축물대장부터 떼 보기, 2. 근생빌라는 구청 확인, 3. 마감 전 건축사 일정" loading="lazy" width="1080" height="1080">
    <figcaption>위반건축물 양성화를 앞두고 챙길 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>건축물대장부터 떼 보기</strong>. 정부24에서 무료로 떼면 '위반건축물' 표시와 위반 내용이 나옵니다.</li>
    <li><strong>근생빌라는 구청 확인</strong>. 포함 여부와 조건이 자료마다 달라 시행령 공포본과 구청 안내를 함께 봅니다.</li>
    <li><strong>마감 전 건축사 일정</strong>. 2028년 6월 16일 마감이지만 도면 준비에 시간이 걸립니다.</li>
  </ol>
  <p>집을 사거나 전세를 구하는 쪽이라면 순서가 반대입니다. 계약 전에 건축물대장을 떼서 위반 표시가 있는지 보고, 있다면 매도인이 양성화를 신청할 계획인지, 비용은 누가 낼지를 계약서 특약에 적어 두는 게 안전합니다. 위반 표시가 남은 집은 전세대출이 막힐 수 있다는 점도 함께 따져 봐야 합니다.</p>

  <h3>정리</h3>
  <p><strong>위반건축물 양성화</strong>는 12월 17일 시행돼 2028년 6월 16일까지 18개월 동안 신고를 받습니다. 2023년 12월 31일 이전에 사실상 다 지은 단독·다가구·다세대 같은 소규모 주거용 건물이 대상이고, 개발제한구역·정비구역이나 투기성 위반은 빠집니다. 건축사 도면으로 구청에 신고하고 과태료를 내면 사용승인을 받는 구조입니다. <span class="mark">과태료 금액과 근생빌라 기준은 시행령과 구청 안내로 확인하고, 건축물대장부터 떼 보는 게 첫 단계입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 법률·건축 자문이 아닙니다. 대상 면적·과태료·근생빌라 기준은 법안·시행령 입법예고와 보도, 해설 자료 기준이며 시행령 공포본에서 달라질 수 있습니다. 개별 건물의 대상 여부는 관할 시·군·구청 건축 부서와 건축사에게 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 건축사신문 위반건축물 양성화 12월 17일 전면 시행 · 국토교통부 「특정건축물 정리에 관한 특별조치법 시행령」 제정안 입법예고(2026-09-30~11-09) · 이투데이 불법건축물 한시적 양성화법 국회 본회의 통과 · 뉴스1 전북도 위반건축물 양성화 특별조치 18개월 · 한국경제 165㎡ 미만 불법 단독주택(2026-01) · 뉴스1 당정 불법건축물 양성화 기준 · 경향신문·뉴시스 국토부 소규모 주거용 위반건축물 한시 양성화(2025-10-01) · 서울신문 종로구 특정건축물 지원센터(2026-07-20) · 헤럴드경제 불법건축물 양성화법 국토위 법안소위 통과<br>
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
assert round(8.3 / 14.8 * 86, 1) == 48.2 and round(4.6 / 14.8 * 86, 1) == 26.7 and round(4.0 / 14.8 * 86, 1) == 23.2
KW = "위반건축물 양성화"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("위반건축물양성화")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
assert out.count("· 특집") == 1
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
