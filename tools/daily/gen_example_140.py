# -*- coding: utf-8 -*-
"""리포트 #140 (2026-11-27 금) 하안주공6·7단지 재건축 시공사 IPARK현대산업개발. #139를 복제해 교체한다.

메인 검색어: 하안주공6·7단지
요일 종류: 금요일 주의형 대신 재건축 해설형으로 바꿈. 이유: 주의형으로 쓸 1주일 안의 새 사건이 없고,
  하안주공6·7단지 시공사 선정(11/24 한국경제·헤럴드경제 보도)이 이번 주 재건축 뉴스. '착공·가구수 확정 아님'을 한 섹션으로 둬 주의형 성격을 남긴다.
핫이슈 훑기: 잠실 래미안아이파크 줍줍 당첨 발표 11/27(아시아경제·한국경제·파이낸셜뉴스) → #133·#139 로 이미 2편, 2주 규칙으로 제외.
  경희궁 에피트 1순위는 공식 경쟁률 미확인(블로그 집계뿐)이라 보류.

수치와 검산
  사건일과 오늘의 간격: 선정 보도 11/24 → 3일.
  하안주공6·7단지: 총회 찬성 1,813표 / 2,092명 = 86.7% (헤럴드경제·한국경제 11/24)
  예정 공사비 1조1,549억(한국토지신탁 추산, MTN 9/18) · 보도마다 '1.1조'
  기존 2,603가구 → 3,240가구(MTN) · 일부 자료 3,263가구, 지하 3층~최고 44층 20개 동
  9월 1차 입찰 단독 응찰(MTN 9/18) · 겐슬러 협업 대안설계(머니투데이·아시아경제 7/9)
  하안주공5단지(#131): 한화 11/18 · 1조698억 · 2,886가구 45층
  목동12단지(#136): GS건설 1조7,887억 · 압구정3구역 5조5,610억
  대시보드 세로 (5.561조 → 86): 1.7887 → 27.7 · 1.1549 → 17.9 · 1.0698 → 16.5
  카드3 가로 (3,240 → 100): 2,603 → 80.3 · 늘어나는 637가구(+24.5%)
  카드4 가로 (2,092 → 100): 1,813 → 86.7
  가구당 공사비 11,549억 / 3,240 = 약 3억5,600만원

단정하지 않은 것
  · 가구수·층수: 계획(3,240 vs 3,263), 인가 단계에서 바뀔 수 있음 · 공사비: 예정 금액, 본계약에서 변동
  · 착공·입주 시점: 2025년 보도된 하안주공 전체 계획
  · 다른 단지 시공사: 정해지지 않음
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-26-jamsil-raemian-result.html"
SLUG, PRE = "2026-11-27-hanan67-ipark", "h67"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 140, "2026-11-27"
PREV_SLUG = "jamsil-raemian-result"
BANNED = ["래미안아이파크", "줍줍"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "하안주공6·7단지 재건축, 시공사 IPARK현산 찬성 87%"
DESC = ("광명 하안주공6·7단지 통합 재건축 시공사로 IPARK현대산업개발이 선정됐습니다. 총회에서 2,092명 중 1,813표, 86.7%가 찬성했습니다. "
        "예정 공사비 약 1조1,549억원, 3,240가구 계획이고 착공까지는 인가 단계가 남았습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="2,092명 중 1,813표 찬성. 예정 공사비 약 1조1,549억, 2,603가구를 3,240가구로. 하안주공5단지에 이어 두 번째 시공사 선정.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">하안주공6·7단지,<br>시공사는 IPARK현산</h1>
  <p class="sub">광명 <strong>하안주공6·7단지</strong> 통합 재건축 시공사로 IPARK현대산업개발이 선정됐습니다. 총회에서 <strong>2,092명 중 1,813표</strong>가 찬성했습니다. <span class="mark">5단지에 이어 하안주공에서 두 번째 시공사지만, 착공까지는 인가 단계가 남아 있습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/24 보도</div><div class="kw">IPARK현산</div>
      <p>하안주공6·7단지 <strong>시공사</strong> 선정.</p></div>
    <div class="kcard"><div class="hot">총회 찬성</div><div class="kw">86.7%</div>
      <p>2,092명 중 <strong>1,813표</strong>.</p></div>
    <div class="kcard"><div class="hot">예정 공사비</div><div class="kw">1조1,549억</div>
      <p>신탁사 추산, <strong>본계약</strong>에서 변동.</p></div>
    <div class="kcard"><div class="hot">계획 규모</div><div class="kw">3,240가구</div>
      <p>지금 2,603가구에서 <strong>637가구</strong> 늘어난다.</p></div>
  </div>

  <div class="colchart">
    <h3>올해 시공사를 정한 재건축 공사비 (원)</h3>
    <span class="badge">하안주공6·7단지는 1조원대</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5.56조</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:27.7%">1.79조</div><div class="barv" style="--h:27.7%"></div></div>
      <div class="col"><div class="v gtx" style="--h:17.9%">1.15조</div><div class="barv" style="--h:17.9%"></div></div>
      <div class="col dim"><div class="v" style="--h:16.5%">1.07조</div><div class="barv" style="--h:16.5%"></div></div>
    </div>
    <div class="collbl"><span>압구정3구역</span><span>목동12단지</span><span>하안주공6·7</span><span>하안주공5</span></div>
    <p class="cap">압구정3구역(5월, 현대건설)·목동12단지(11월, GS건설)·하안주공6·7단지(예정 공사비, 한국토지신탁 추산)·하안주공5단지(11월 18일, 한화 건설부문) 보도 금액입니다. 본계약에서 바뀔 수 있습니다. 막대 길이는 최댓값 5조5,610억원을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 하안주공6·7단지 시공사 IPARK현산"),
    ("02-size", "하안주공6·7단지, 숫자 셋으로 보면"),
    ("03-homes", "2,603가구가 3,240가구로"),
    ("04-vote", "2,092명 중 1,813명이 찬성"),
    ("05-next", "하안주공6·7단지, 착공은 아직"),
    ("06-check", "하안주공 소유자가 볼 3가지"),
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

ARTICLE = '''<article data-tags="하안주공6·7단지,하안주공재건축,광명재건축,하안주공,IPARK현대산업개발,아이파크,광명하안동,신탁방식재건축,재건축시공사,광명아파트">
  <h2>하안주공6·7단지 재건축, 시공사 IPARK현산 찬성 87%</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 하안주공6·7단지 시공사 IPARK현산"></span>

  <p><strong>3줄 요약</strong><br>하안주공6·7단지 통합 재건축 시공사로 IPARK현대산업개발이 선정됐고, 총회에서 2,092명 중 1,813표가 찬성했습니다.<br>예정 공사비는 약 1조1,549억원이고, 지금 2,603가구를 3,240가구로 다시 짓는 계획입니다.<br>지난주 5단지에 이어 하안주공에서 두 번째 시공사 선정이지만, 착공까지는 사업시행인가와 관리처분 단계가 남아 있습니다.</p>

  <p>하안주공6·7단지 시공사가 정해졌습니다. 경기 광명시 하안동 하안주공6·7단지 통합 재건축 시공사로 IPARK현대산업개발이 선정됐다고 한국경제와 헤럴드경제가 11월 24일 전했습니다. 총회에서 2,092명 가운데 1,813명이 찬성표를 던졌습니다. <span class="mark">지난 18일 한화 건설부문을 고른 5단지에 이어, 일주일 사이 하안주공에서 두 번째로 시공사가 정해졌습니다.</span></p>

  <h3>하안주공6·7단지 시공사, IPARK현산으로 정해졌다</h3>
  <div class="chart" data-img="카드뉴스 2번 · 하안주공6·7단지, 숫자 셋으로 보면">
    <h3>하안주공6·7단지 재건축 계획 (보도 기준)</h3>
    <h4>예정 공사비</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">1조1,549억</span>
      <span class="desc">신탁사 추산, 본계약에서 바뀔 수 있다.</span></div>
    <h4>계획 가구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3,240</span>
      <span class="desc">일부 자료는 3,263가구. 인가 단계에서 바뀐다.</span></div>
    <h4>최고 층수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">44층</span>
      <span class="desc">지하 3층~지상 44층, 20개 동 계획.</span></div>
    <p class="cap">MTN(2026년 9월 18일)·한국경제·헤럴드경제(11월 24일) 보도 기준입니다. 계획 가구수와 층수는 확정 전입니다.</p>
  </div>
  <p>결론부터 말하면 공사비 1조원대, 44층 3,240가구 계획입니다. 신탁사인 한국토지신탁이 추산한 예정 공사비는 1조1,549억원이고, 매체들은 '1조1,000억원 규모'로 전했습니다. 가구수는 3,240가구라는 보도와 3,263가구라는 자료가 함께 있는데, 어느 쪽이든 계획 숫자라 사업시행인가 단계에서 다시 바뀔 수 있습니다.</p>
  <p>두 단지를 하나로 묶어 짓는 통합 재건축이라는 점이 5단지와 다릅니다. IPARK현대산업개발은 미국 설계사 겐슬러와 손잡고 두 단지 사이 경계를 없앤 대안설계를 내놨다고 7월 보도됐습니다. 단지가 둘이면 동 배치와 커뮤니티 시설을 나누는 문제가 생기는데, 이를 한 단지처럼 그리겠다는 구상입니다.</p>
  <p>이 단지도 조합이 아니라 신탁 방식입니다. 예정 공사비를 한국토지신탁이 추산한 것도 그래서입니다. 하안주공 재건축은 1·2단지와 8단지를 빼고 대부분 신탁 방식으로 추진된다고 2025년 9월 보도됐습니다. 신탁 방식은 조합을 따로 만들지 않아 초기 절차가 빠른 대신 신탁사에 수수료를 냅니다. 소유자 입장에서는 이 수수료도 나중에 분담금 계산에 들어가는 비용이라는 점을 기억해 둘 만합니다.</p>
  <p>이곳도 입찰이 매끄럽지는 않았습니다. 9월 1차 입찰에는 IPARK현대산업개발 한 곳만 들어와 유찰됐고, 2차 입찰을 거쳐 수의계약 수순을 밟았습니다. 경쟁 입찰이 두 번 성립하지 않으면 단독 응찰한 건설사와 협상할 수 있는데, 서울 압구정3구역과 목동12단지도 같은 길을 걸었습니다.</p>
  <p>누가 영향을 받는지도 짚어 둘 만합니다. 시공사가 정해지면 설계를 구체화하고 사업시행인가 신청을 준비할 수 있습니다. 반대로 시공사 없이 시간이 흐르면 그사이 오른 공사비가 사업비에 그대로 얹힙니다. 하안주공 소유자 입장에서는 일정이 다시 움직이기 시작했다는 뜻입니다.</p>

  <h3>2,603가구가 3,240가구로</h3>
  <div class="chart" data-img="카드뉴스 3번 · 2,603가구가 3,240가구로">
    <h3>하안주공6·7단지 가구수 (지금 vs 계획)</h3>
    <div class="bar"><label>계획</label>
      <div class="rail"><div class="fill" style="width:100%">3,240</div></div></div>
    <div class="bar"><label>지금</label>
      <div class="rail"><div class="fill gray" style="width:80.3%">2,603</div></div></div>
    <p class="cap">MTN(2026년 9월 18일) 보도 기준입니다. 계획 가구수는 인가 단계에서 바뀔 수 있습니다. 막대 길이는 최댓값 3,240가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>늘어나는 가구는 637가구, 지금보다 24.5% 많습니다. 이 늘어난 몫이 일반분양과 임대주택으로 나가고, 일반분양 수입이 공사비 부담을 덜어 줍니다. 그래서 같은 공사비라도 일반분양 물량과 분양가가 얼마로 정해지느냐에 따라 소유자가 낼 돈이 크게 달라집니다.</p>
  <p>가구당으로 나눠 보면 감이 옵니다. 예정 공사비 1조1,549억원을 계획 가구수 3,240가구로 나누면 한 가구에 약 3억5,600만원꼴입니다. 지난주 5단지는 1조698억원에 2,886가구, 한 가구에 약 3억7,000만원꼴이었으니 비슷한 수준입니다. 이 돈이 그대로 소유자 몫이 되는 건 아닙니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 공사비는 건설사가 받는 돈이지 분양가가 아닙니다. 소유자가 실제로 낼 분담금은 공사비뿐 아니라 일반분양 수입, 이주비 이자, 신탁 수수료를 모두 따져야 나오고, 이 계산은 관리처분계획 단계에서 처음 구체적인 숫자로 나옵니다.</p>
  <p>규모로 보면 서울 대어보다는 작고, 경기권에서는 큰 편입니다. 올해 시공사를 정한 재건축 가운데 압구정3구역은 공사비 5조5,610억원, 목동12단지는 1조7,887억원이었습니다. 하안주공6·7단지는 목동12단지의 3분의 2쯤 되고, 이웃한 5단지보다는 조금 큽니다.</p>

  <h3>하안주공6·7단지 총회, 찬성 86.7%</h3>
  <div class="chart" data-img="카드뉴스 4번 · 2,092명 중 1,813명이 찬성">
    <h3>시공사 선정 총회 찬성 (명)</h3>
    <div class="bar"><label>참석·투표</label>
      <div class="rail"><div class="fill gray" style="width:100%">2,092</div></div></div>
    <div class="bar"><label>찬성</label>
      <div class="rail"><div class="fill" style="width:86.7%">1,813</div></div></div>
    <p class="cap">헤럴드경제·한국경제(2026년 11월 24일) 보도 기준입니다. 막대 길이는 최댓값 2,092명을 기준으로 맞췄습니다.</p>
  </div>
  <p>찬성 비율은 86.7%입니다. 단독 응찰로 수의계약을 맺는 경우 소유자들 사이에서 "경쟁이 없어 조건이 불리하다"는 말이 나오기 쉬운데, 이번 총회에서는 열에 아홉 가까이가 찬성했습니다. 기존 2,603가구 가운데 2,092명이 표를 냈으니 참여도 많았던 셈입니다.</p>
  <p>찬성률이 높다고 조건이 확정된 건 아닙니다. 공사비 단가와 물가 상승분을 어떻게 반영할지, 공사 기간은 얼마로 할지는 본계약에서 정해집니다. 총회는 이 건설사와 협상을 시작하겠다는 결정에 가깝고, 실제 계약 조건은 그 뒤에 나옵니다.</p>
  <p>비교할 숫자가 하나 더 있습니다. 하안주공5단지는 올해 입찰이 여러 번 무응찰로 끝난 뒤에야 시공사를 정했고, 당시 신탁사가 제시한 공사비는 3.3㎡당 800만원이었습니다. 6·7단지는 첫 입찰부터 응찰한 건설사가 있었다는 점이 다릅니다. 다만 6·7단지의 3.3㎡당 단가는 아직 보도되지 않았습니다.</p>

  <h3>하안주공6·7단지, 착공은 아직 멀었다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 하안주공6·7단지, 착공은 아직">
    <h3>하안주공 재건축 남은 단계 (2025년 보도 계획)</h3>
    <h4>사업시행인가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2027년</span>
      <span class="desc">설계·가구수가 여기서 굳는다.</span></div>
    <h4>관리처분인가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2028년</span>
      <span class="desc">분담금이 숫자로 나온다.</span></div>
    <h4>착공</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">2030년</span>
      <span class="desc">하안주공 전체 계획, 6·7단지 확정 일정 아님.</span></div>
    <p class="cap">아시아경제(2025년 9월) 보도의 하안주공 재건축 전체 일정 계획입니다. 단지별 실제 일정은 사업시행자와 광명시 고시로 확인하십시오.</p>
  </div>
  <p>시공사 선정은 출발선입니다. 2025년 보도된 하안주공 재건축 계획은 2027년 사업시행인가, 2028년 관리처분인가를 거쳐 2030년 착공하는 일정입니다. 이 일정은 하안주공 전체를 놓고 세운 계획이라 6·7단지만의 확정 일정이 아니고, 인허가와 이주가 늦어지면 뒤로 밀립니다.</p>
  <p>다른 단지는 아직 한 단계씩 앞에 있습니다. 하안주공 12개 단지 가운데 시공사를 정한 곳은 5단지와 6·7단지 두 곳입니다. 12단지는 2025년 12월 정비구역과 사업시행자 지정이 고시됐고, 8단지는 2025년 9월 조합설립추진위원회 승인을 받았습니다. 먼저 정해진 두 곳의 공사비 수준과 계약 조건이 다른 단지의 기준점이 될 가능성이 큽니다.</p>
  <p>이 단계에서 매수를 고민한다면 따로 봐야 할 것이 있습니다. 재건축 단지의 거래 제한과 입주권 요건은 단계마다 다르고, 신탁 방식은 조합 방식과 절차가 조금 다릅니다. 일반론으로 판단하지 말고 사업시행자와 광명시 재건축 담당 부서에 직접 확인하는 게 맞습니다.</p>
  <p>앞으로 볼 날짜는 두 가지입니다. 하나는 신탁사와 IPARK현대산업개발이 맺을 본계약 시점이고, 다른 하나는 사업시행인가 신청 시점입니다. 본계약에서 3.3㎡당 단가와 물가 반영 조건이 정해지고, 사업시행인가 신청 때 가구수와 평형 구성이 처음 공식 서류로 나옵니다. 두 날짜 모두 아직 발표되지 않았습니다.</p>

  <h3>하안주공 소유자가 볼 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 하안주공 소유자가 볼 3가지 (체크리스트)">
    <img class="card-art" data-file="h67-06-check.png" src="../images/cards/report/h67-06-check.png" alt="체크포인트 카드 · 1. 본계약 공사비, 2. 계획 가구수는 확정 전, 3. 다음 단계 일정" loading="lazy" width="1080" height="1080">
    <figcaption>하안주공6·7단지 시공사 선정 뒤, 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>본계약 공사비</strong>. 1조1,549억원은 신탁사가 추산한 예정 금액입니다. 3.3㎡당 단가와 물가 반영 조건은 본계약에서 정해집니다.</li>
    <li><strong>계획 가구수는 확정 전</strong>. 3,240가구와 44층은 계획이고, 사업시행인가에서 바뀔 수 있습니다.</li>
    <li><strong>다음 단계 일정</strong>. 착공 2030년은 하안주공 전체 계획입니다. 단지 일정은 사업시행자 공지와 광명시 고시로 보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>하안주공6·7단지</strong> 통합 재건축 시공사로 IPARK현대산업개발이 선정됐습니다. 총회에서 2,092명 중 1,813명이 찬성했고, 예정 공사비 약 1조1,549억원에 2,603가구를 3,240가구로 다시 짓는 계획입니다. <span class="mark">5단지에 이어 일주일 사이 두 번째 시공사가 정해지면서 하안주공 재건축이 속도를 내는 모습입니다.</span> 다만 착공까지는 사업시행인가와 관리처분이 남아 있고, 가구수와 공사비는 그 과정에서 바뀔 수 있습니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 공사비와 가구수·층수는 보도 기준이며 본계약과 인가 단계에서 바뀔 수 있습니다. 착공 일정은 2025년 보도된 하안주공 전체 계획으로 6·7단지 확정 일정이 아닙니다. 거래 제한과 입주권 요건은 사업시행자와 광명시에 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 한국경제·헤럴드경제 하안주공6·7단지 시공사 선정(2026-11-24) · MTN·아이뉴스24 하안주공6·7단지 단독 응찰(2026-09-18) · 머니투데이·아시아경제 겐슬러 협업 설계(2026-07-09) · 서울경제 하안주공5단지·목동12단지 시공사 선정(2026-11) · 아시아경제 하안주공 재건축 일정(2025-09) · 광명시 하안주공12단지 정비구역 고시(2025-12)<br>
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
for v, h in ((1.7887, 27.7), (1.1549, 17.9), (1.0698, 16.5)):
    assert round(v / 5.561 * 86, 1) == h
assert round(1813 / 2092 * 100, 1) == 86.7 and round(2603 / 3240 * 100, 1) == 80.3
assert round((3240 - 2603) / 2603 * 100, 1) == 24.5
KW = "하안주공6·7단지"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("하안주공6·7단지")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
