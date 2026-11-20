# -*- coding: utf-8 -*-
"""리포트 #132 (2026-11-21 토) 성수2지구 시공사 선정 총회 당일 · 성수전략정비구역 1~4지구 일정 정리. #131을 복제해 교체한다.

메인 검색어: 성수2지구
요일 종류: 토요일 구 단위 동네 리포트(일정형). 성동구 성수전략정비구역 네 지구의 시공사 선정 달력.
핫이슈 훑기: 잠실 래미안아이파크 줍줍(파이낸셜뉴스·서울경제·헤럴드경제 등) → 11/22(일) D-1에 씀(달력 그대로).

수치와 검산
  사건일과 오늘의 간격: 성수2지구 시공사 선정 총회 11/21 → 0일(오늘). 결과는 총회 뒤. 결과를 단정하지 않는다.
  성수2지구: DL이앤씨 '아크로 성수' · 1차 입찰(8/31) 단독 응찰 유찰 · 2차도 단독 → 우선협상대상자 → 10/1 수의계약 제안서
    · 최고 65층 11개 동 2,381가구 · 사업비 2조137억(일부 보도 62층 9개 동 2,350가구)
  성수1지구: GS건설 4월 선정(보도). 규모는 이 글에서 다루지 않는다.
  성수3지구: 삼성물산 9/19 총회 '래미안 레비르 성수' · 최고 72층 · 2,213가구(일부 2,203) · 예정 공사비 약 1조8,275억 · 단독 응찰 수의계약
  성수4지구: 롯데건설 7/5 총회 449표(72.4%) vs 대우건설 169표(27.3%) · '성수 르엘 S70' · 최고 64층 · 1,439가구(일부 1,447) · 공사비 1조3,099억(보도별 ~1조3,628억)
    · 연내 사업시행계획 총회 계획
  대시보드 세로 (2.0137조 → 86): 1.8275 → 78.0 · 1.3099 → 55.9
  카드4 가로 (2,381 → 100): 2,213 → 92.9 · 1,439 → 60.4

단정하지 않은 것
  · 성수2지구 총회 결과: 오늘 총회에서 정한다. 선정 확정 아님
  · 가구수·층수·공사비: 제안·계획 기준, 보도마다 다르고 인가·본계약에서 바뀜
  · 거래 제한: 성수전략정비구역 토지거래허가 등은 구청 확인으로 넘긴다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-20-hanan5-hanwha.html"
SLUG, PRE = "2026-11-21-seongsu2-dl", "ssu"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 132, "2026-11-21"
PREV_SLUG = "hanan5-hanwha"
BANNED = ["하안주공", "한국자산신탁"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "성수2지구 오늘 시공사 총회, 성수 4개 지구 정리"
DESC = ("성수2지구 재개발 조합이 11월 21일 총회를 열어 DL이앤씨를 시공사로 정할지 결정합니다. 사업비 2조137억원, 최고 65층 2,381가구 제안입니다. "
        "1지구 GS건설, 3지구 삼성물산, 4지구 롯데건설에 이어 성수전략정비구역 네 지구의 시공사 달력을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="DL이앤씨 '아크로 성수' 제안, 사업비 2조137억·최고 65층 2,381가구. 1지구 GS, 3지구 삼성, 4지구 롯데에 이어 마지막 퍼즐.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">성수2지구,<br>오늘 시공사 총회</h1>
  <p class="sub">성동구 <strong>성수2지구</strong> 재개발 조합이 <strong>11월 21일</strong> 총회를 열어 DL이앤씨를 시공사로 정할지 결정합니다. 1지구 GS건설, 3지구 삼성물산, 4지구 롯데건설에 이어 네 지구 가운데 마지막입니다. <span class="mark">결과는 총회가 끝나야 나옵니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/21 총회</div><div class="kw">DL이앤씨</div>
      <p>성수2지구 <strong>단독</strong> 제안.</p></div>
    <div class="kcard"><div class="hot">사업비</div><div class="kw">2조137억</div>
      <p>보도 기준, <strong>본계약</strong>에서 변동.</p></div>
    <div class="kcard"><div class="hot">제안 규모</div><div class="kw">2,381가구</div>
      <p>최고 <strong>65층</strong> 11개 동.</p></div>
    <div class="kcard"><div class="hot">성수 4개 지구</div><div class="kw">3곳 확정</div>
      <p>남은 곳은 <strong>2지구</strong> 하나.</p></div>
  </div>

  <div class="colchart">
    <h3>성수 2·3·4지구 공사비 (원)</h3>
    <span class="badge">성수2지구가 가장 크다</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">2.01조</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:78%">1.83조</div><div class="barv" style="--h:78%"></div></div>
      <div class="col dim"><div class="v" style="--h:55.9%">1.31조</div><div class="barv" style="--h:55.9%"></div></div>
    </div>
    <div class="collbl"><span>2지구 DL</span><span>3지구 삼성</span><span>4지구 롯데</span></div>
    <p class="cap">성수2지구 사업비(DL이앤씨 제안 보도), 3지구 예정 공사비(9월 선정 보도), 4지구 공사비(7월 선정 보도) 기준입니다. 기사마다 금액이 조금씩 다르고 본계약에서 바뀔 수 있습니다. 막대 길이는 최댓값 2조137억원을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 성수2지구 오늘 시공사 총회"),
    ("02-cal", "성수 시공사 달력, 올해 네 번째"),
    ("03-today", "성수2지구, 숫자 셋으로 보면"),
    ("04-size", "성수 네 지구 중 가장 큰 곳"),
    ("05-cost", "공사비로 보면 성수2지구가 맨 위"),
    ("06-check", "성수 재개발, 지금 볼 3가지"),
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

ARTICLE = '''<article data-tags="성수2지구,성수재개발,성수전략정비구역,아크로성수,DL이앤씨,성수3지구,성수4지구,성수1지구,성동구재개발,한강변재개발">
  <h2>성수2지구 오늘 시공사 총회, 성수 4개 지구 정리</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 성수2지구 오늘 시공사 총회"></span>

  <p><strong>3줄 요약</strong><br>성수2지구 재개발 조합이 11월 21일 총회에서 DL이앤씨를 시공사로 정할지 결정합니다.<br>DL이앤씨는 '아크로 성수'라는 이름으로 사업비 2조137억원, 최고 65층 2,381가구를 제안했습니다.<br>1지구 GS건설, 3지구 삼성물산, 4지구 롯데건설이 이미 정해져 있어 오늘 총회가 끝나면 성수 한강변 네 지구의 시공사 지도가 완성됩니다.</p>

  <p>성수2지구가 오늘 시공사를 정합니다. 서울 성동구 성수전략정비구역 2지구 재개발 조합은 11월 21일 총회를 열어 DL이앤씨를 시공사로 선정할지 표결합니다. 두 차례 입찰에 DL이앤씨만 들어와 수의계약 절차로 넘어온 곳입니다. <span class="mark">다만 총회에서 안건이 통과돼야 시공사로 확정되고, 이 글을 쓰는 시점에는 결과가 나오지 않았습니다.</span> 오늘은 2지구 총회를 중심으로 성수 네 지구가 어디까지 왔는지 날짜순으로 정리합니다.</p>

  <h3>성수2지구까지, 올해 성수 시공사 달력</h3>
  <div class="chart" data-img="카드뉴스 2번 · 성수 시공사 달력, 올해 네 번째">
    <h3>성수전략정비구역 시공사 선정 (2026년 보도 기준)</h3>
    <h4>1지구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4월</span>
      <span class="desc">GS건설 선정.</span></div>
    <h4>4지구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">7월 5일</span>
      <span class="desc">롯데건설, 대우건설과 경쟁 끝에 선정.</span></div>
    <h4>3지구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9월 19일</span>
      <span class="desc">삼성물산, 단독 응찰 뒤 수의계약.</span></div>
    <h4>2지구</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 21일</span>
      <span class="desc">DL이앤씨 선정 여부를 오늘 총회에서 정한다.</span></div>
    <p class="cap">각 조합 총회와 건설사 발표 보도 기준입니다. 성수2지구는 총회 결과가 나오기 전입니다.</p>
  </div>
  <p>올해 성수는 넉 달에 한 번꼴로 시공사가 정해졌습니다. 4월 1지구가 GS건설을 골랐고, 7월 5일 4지구가 롯데건설을 택했습니다. 9월 19일에는 3지구가 삼성물산을 시공사로 뽑았습니다. 오늘 2지구 총회가 마지막 순서입니다.</p>
  <p>성수전략정비구역은 2009년 한강변 초고층 개발을 목표로 지정된 뒤 오랫동안 제자리였던 곳입니다. 네 지구가 따로 사업을 굴리면서 속도가 갈렸고, 올해 들어 시공사 선정이 한꺼번에 몰렸습니다. 네 곳 모두 한강변에 붙어 있고 계획 층수가 60층을 넘는다는 점이 같습니다.</p>
  <p>경쟁 양상은 지구마다 달랐습니다. 4지구만 두 건설사가 실제로 맞붙었고, 3지구와 2지구는 한 회사만 입찰에 들어와 수의계약으로 넘어갔습니다. 서울 대형 정비사업에서 단독 응찰이 잦아진 흐름이 성수에서도 그대로 나타난 셈입니다.</p>
  <p>네 지구가 한 해에 시공사를 정하면서 가장 먼저 달라지는 건 속도입니다. 시공사가 있어야 설계를 구체화하고 사업시행계획을 세울 수 있습니다. 4지구가 연내 사업시행계획 총회를 예고한 것도 7월에 시공사를 정했기 때문에 가능한 일정입니다. 2지구는 오늘 안건이 통과되면 4지구보다 넉 달가량 늦게 같은 출발선에 서게 됩니다.</p>

  <h3>성수2지구 오늘 총회, 무엇을 정하나</h3>
  <div class="chart" data-img="카드뉴스 3번 · 성수2지구, 숫자 셋으로 보면">
    <h3>성수2지구 DL이앤씨 제안 (보도 기준)</h3>
    <h4>사업비</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">2조137억</span>
      <span class="desc">본계약에서 바뀔 수 있다.</span></div>
    <h4>제안 가구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2,381</span>
      <span class="desc">일부 보도는 2,350가구. 인가 단계에서 바뀐다.</span></div>
    <h4>최고 층수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">65층</span>
      <span class="desc">지하 6층~지상 65층, 11개 동 제안.</span></div>
    <p class="cap">DL이앤씨 발표(2026년 10월 2일)와 이코노미스트·SBS Biz 등 보도 기준입니다. 일부 보도는 최고 62층 9개 동으로 적었습니다. 계획 가구수와 층수는 확정 전입니다.</p>
  </div>
  <p>결론부터 말하면 오늘 총회는 DL이앤씨를 시공사로 정할지 말지를 묻는 자리입니다. DL이앤씨는 10월 1일 수의계약용 입찰제안서를 냈고, 단지 이름으로 '아크로 성수'를 제안했습니다. 제안 규모는 지하 6층에서 지상 65층까지 11개 동, 2,381가구이고 사업비는 2조137억원입니다.</p>
  <p>여기까지 오는 데 입찰을 두 번 거쳤습니다. 8월 31일 마감한 1차 입찰에 DL이앤씨만 들어와 유찰됐고, 다시 연 2차 입찰에도 DL이앤씨 혼자 응찰했습니다. 정비사업 규정상 두 번 유찰되면 수의계약을 할 수 있어 조합은 DL이앤씨를 우선협상대상자로 정하고 제안 내용을 검토해 왔습니다. 현장설명회에는 HDC현대산업개발도 참석했지만 입찰서는 내지 않았습니다.</p>
  <p>숫자가 기사마다 다른 점은 짚어 둘 만합니다. 가구수는 2,381가구와 2,350가구, 층수는 65층과 62층으로 엇갈리게 보도됐습니다. 하나는 정비계획 기준, 하나는 건설사 제안 기준으로 보입니다. 어느 쪽이든 사업시행인가 단계에서 다시 정해지는 숫자라 지금 확정된 것은 아닙니다.</p>
  <p>누가 영향을 받는지도 볼 필요가 있습니다. 시공사가 정해지면 조합은 설계를 굳히고 사업시행계획 수립에 들어갈 수 있습니다. 반대로 총회에서 안건이 부결되면 입찰을 처음부터 다시 해야 하고, 그만큼 공사비가 오를 시간을 버는 셈이 됩니다. 조합원들이 오늘 표결에 신경을 곤두세우는 이유입니다.</p>

  <h3>성수 네 지구, 규모로 비교하면</h3>
  <div class="chart" data-img="카드뉴스 4번 · 성수 네 지구 중 가장 큰 곳">
    <h3>성수 2·3·4지구 계획 가구 (가구)</h3>
    <div class="bar"><label>2지구 DL이앤씨</label>
      <div class="rail"><div class="fill" style="width:100%">2,381</div></div></div>
    <div class="bar"><label>3지구 삼성물산</label>
      <div class="rail"><div class="fill gray" style="width:92.9%">2,213</div></div></div>
    <div class="bar"><label>4지구 롯데건설</label>
      <div class="rail"><div class="fill gray" style="width:60.4%">1,439</div></div></div>
    <p class="cap">각 지구 시공사 제안·선정 보도 기준입니다. 3지구는 일부 보도 2,203가구, 4지구는 1,447가구로도 적혔습니다. 1지구는 보도된 규모가 엇갈려 뺐습니다. 막대 길이는 최댓값 2,381가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>가구수로는 2지구가 가장 큽니다. 2지구 2,381가구, 3지구 2,213가구, 4지구 1,439가구 순입니다. 층수는 3지구가 최고 72층으로 가장 높고, 2지구 65층, 4지구 64층이 뒤를 잇습니다. 이름도 각각 '아크로 성수', '래미안 레비르 성수', '성수 르엘 S70'으로 제안됐습니다.</p>
  <p>4지구는 성수에서 유일하게 표 대결이 벌어진 곳입니다. 7월 5일 총회에서 롯데건설이 449표(72.4%)를 얻어 대우건설(169표, 27.3%)을 눌렀습니다. 2022년 한남2구역에서 대우건설에 졌던 롯데건설이 4년 만에 설욕했다는 평가가 나왔습니다. 4지구 조합은 연내 사업시행계획 총회를 열 계획이라고 밝혔습니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 단지 이름은 시공사가 제안한 브랜드일 뿐 확정된 아파트 이름이 아닙니다. 실제 단지명은 조합이 나중에 따로 정하고, 입주 시점에 바뀌는 경우도 많습니다. 검색할 때는 지금 쓰는 지구 이름으로 찾는 편이 정확합니다.</p>

  <h3>공사비로 보면 성수2지구가 맨 위</h3>
  <span class="imgslot" hidden data-img="카드뉴스 5번 · 공사비로 보면 성수2지구가 맨 위"></span>
  <p>돈으로 봐도 2지구가 가장 큽니다. 2지구 사업비는 2조137억원, 3지구 예정 공사비는 약 1조8,275억원, 4지구 공사비는 1조3,099억원으로 보도됐습니다. 세 곳을 더하면 5조원이 넘습니다. 이번 주 광명에서 시공사를 정한 재건축 한 곳이 1조원대였던 것과 비교하면 성수 한 지구가 그 두 배 가까운 규모입니다.</p>
  <p>가구당으로 나눠 보면 감이 옵니다. 2지구 사업비 2조137억원을 2,381가구로 나누면 한 가구에 약 8억4,600만원꼴입니다. 다만 사업비는 공사비만이 아니라 이주비, 금융비용까지 포함한 금액일 수 있어 기사마다 기준이 다릅니다. 조합원이 실제로 낼 분담금은 일반분양 수입까지 따져 관리처분계획 단계에서야 숫자로 나옵니다.</p>
  <p>3지구는 선정 총회 때부터 공사비가 높다는 지적이 있었다고 보도됐습니다. 본계약 협상에서 공사비를 얼마나 조정하느냐가 다음 관심사입니다. 2지구도 오늘 시공사가 정해지면 같은 협상이 이어집니다.</p>
  <p>예시로 계산해 보면 비교가 쉬워집니다. 2지구 사업비 2조137억원과 4지구 공사비 1조3,099억원의 차이는 약 7,000억원이고, 가구수 차이는 942가구입니다. 가구당으로 나누면 2지구는 약 8억4,600만원, 4지구는 약 9억1,000만원으로 오히려 4지구가 높게 나옵니다. 다만 한쪽은 사업비, 한쪽은 공사비로 보도돼 기준이 달라서 이 숫자만으로 어느 쪽이 비싸다고 말하기는 어렵습니다.</p>

  <h3>성수 재개발, 지금 볼 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 성수 재개발, 지금 볼 3가지 (체크리스트)">
    <img class="card-art" data-file="ssu-06-check.png" src="../images/cards/report/ssu-06-check.png" alt="체크포인트 카드 · 1. 성수2지구 총회 결과, 2. 계획 숫자는 확정 전, 3. 거래 조건은 구청에" loading="lazy" width="1080" height="1080">
    <figcaption>성수 재개발 네 지구, 지금 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>성수2지구 총회 결과</strong>. 오늘 표결로 정해집니다. 부결되면 입찰을 다시 엽니다.</li>
    <li><strong>계획 숫자는 확정 전</strong>. 가구수와 층수, 공사비는 보도마다 다르고 인가와 본계약에서 바뀝니다.</li>
    <li><strong>거래 조건은 구청에</strong>. 토지거래허가와 조합원 지위 양도는 단계마다 다릅니다. 성동구청과 정비사업 정보몽땅(cleanup.seoul.go.kr)으로 확인하십시오.</li>
  </ol>
  <p>앞으로 볼 날짜도 정리해 둡니다. 2지구는 오늘 총회 결과가 첫 번째이고, 통과되면 본계약 협상이 이어집니다. 4지구는 연내 사업시행계획 총회가 예고돼 있습니다. 1지구와 3지구는 본계약과 사업시행계획 일정이 아직 공개되지 않았으니 조합 공지를 챙겨 보시면 됩니다.</p>
  <p>성수에서 집을 알아보는 분이라면 하나 더 봐야 합니다. 재개발 구역 안의 주택은 거래 시점에 따라 입주권이 나오는지, 조합원 지위가 넘어가는지가 달라집니다. 같은 성수동이라도 지구와 단계에 따라 조건이 다르니 일반론으로 판단하지 말고 구청에 직접 물어보는 게 맞습니다.</p>

  <h3>정리</h3>
  <p><strong>성수2지구</strong> 재개발 조합이 11월 21일 총회에서 DL이앤씨를 시공사로 정할지 결정합니다. 사업비 2조137억원, 최고 65층 2,381가구 제안이고 성수 네 지구 가운데 규모가 가장 큽니다. <span class="mark">1지구 GS건설, 3지구 삼성물산, 4지구 롯데건설에 이어 오늘 안건이 통과되면 성수 한강변 네 지구의 시공사가 모두 정해집니다.</span> 다만 가구수와 공사비는 아직 계획 숫자이고, 인가와 본계약 과정에서 바뀔 수 있습니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 성수2지구 시공사 선정은 11월 21일 총회 결과에 따르며 이 글 작성 시점에는 확정 전입니다. 사업비와 가구수·층수는 건설사 제안과 보도 기준이며 인가와 본계약 단계에서 바뀔 수 있습니다. 거래 제한과 조합원 지위는 성동구청과 조합에 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: DL이앤씨 성수2지구 수의계약 제안 발표(2026-10-02) · 이코노미스트·SBS Biz·MTN 성수2지구 입찰·총회 일정(2026-08~10) · SBS Biz·MTN 성수3지구 삼성물산 선정(2026-09-21) · 더팩트·뉴시스·파이낸셜뉴스 성수4지구 롯데건설 선정(2026-07-05) · 더구루 성수 한강변 재개발 현황(2026)<br>
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
for v, hh in ((1.8275, 78.0), (1.3099, 55.9)):
    assert round(v / 2.0137 * 86, 1) == hh, (v, round(v / 2.0137 * 86, 1))
assert round(2213 / 2381 * 100, 1) == 92.9 and round(1439 / 2381 * 100, 1) == 60.4
assert round(449 / 620 * 100, 1) == 72.4
assert round(20137 / 2381, 2) == 8.46 and round(13099 / 1439, 1) == 9.1 and 2381 - 1439 == 942
KW = "성수2지구"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("성수2지구")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
