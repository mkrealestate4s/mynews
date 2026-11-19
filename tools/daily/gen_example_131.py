# -*- coding: utf-8 -*-
"""리포트 #131 (2026-11-20 금) 하안주공5단지 재건축 시공사 한화 선정. #130을 복제해 교체한다.

메인 검색어: 하안주공5단지
요일 종류: 금요일 주의형 대신 재건축 해설형으로 바꿈. 이유: 주의형으로 쓸 1주일 안의 새 사건이 없고,
  하안주공5단지 시공사 선정(11/18 총회, 11/19 서울경제·한국경제·파이낸셜뉴스·이데일리 보도)이 이번 주 재건축 최대 뉴스.
  '착공은 아직 멀었다'를 한 섹션으로 둬 주의형 성격을 남긴다.
핫이슈 훑기: 잠실 래미안아이파크 줍줍(매체 5곳) → 11/22(일) D-1에 씀(달력). 반포124 일정 순연은 한국경제 1곳뿐이라 보류.

수치와 검산
  사건일과 오늘의 간격: 시공사 선정 총회 11/18 → 2일. 발표 11/19 → 1일.
  하안주공5단지: 지하 5층~지상 45층 · 2,886가구(일부 2,885) · 공사비 약 1조698억 · 사업시행자 한국자산신탁(신탁 방식)
  입찰 경과: 3월 첫 입찰 무응찰(더구루) · 7월 세 번째 공고도 무응찰(MTN 7/21) · 입찰 때 3.3㎡당 800만원(신탁사 추산, 낮다는 평가)
  하안주공 12개 단지 중 처음 시공사 선정 · 4월 설명회 SK에코플랜트·한화·대방 참석(3·4단지·5단지 언급)
  한화 올해 정비사업 누적 2조5,264억(작년의 3배 이상) · 하안5 비중 10,698/25,264 = 42.3%
  비교 공사비: 압구정3구역 5조5,610억(현대, 5월) · 목동10단지 2조6,136억(현대, 10/18 선정 공시)
  하안주공 전체 계획(2025-09 아시아경제): 정비구역 지정 → 2027 사업시행인가 → 2028 관리처분 → 2030 착공. 1·2·8단지 제외 신탁 방식
  12단지 정비구역·사업시행자 지정 고시 2025-12-10 · 8단지 추진위 승인 2025-09-17
  목동4단지 3.3㎡당 1,010만원(#128)
  대시보드 세로 (5.561조 → 86): 2.6136 → 40.4 · 1.0698 → 16.5
  카드4 가로 (25,264 → 100): 10,698 → 42.3

단정하지 않은 것
  · 가구수·층수: 계획, 인가 단계에서 바뀔 수 있음 · 공사비: 공시·보도 금액, 본계약에서 변동
  · 착공·입주 시점: 2025년 보도된 하안주공 전체 계획, 5단지 확정 일정 아님
  · 다른 단지 시공사: 정해지지 않음, '유력' 표현 안 씀
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-19-banpo124-vs-onebaily.html"
SLUG, PRE = "2026-11-20-hanan5-hanwha", "hah"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 131, "2026-11-20"
PREV_SLUG = "banpo124-vs-onebaily"
BANNED = ["원베일리", "반포124"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "하안주공5단지 재건축, 12개 단지 중 첫 시공사 한화"
DESC = ("광명 하안주공5단지 재건축 시공사로 한화 건설부문이 11월 18일 총회에서 선정됐습니다. 공사비 약 1조698억원, 지상 45층 2,886가구 계획입니다. "
        "하안주공 12개 단지 가운데 처음이고, 착공까지는 인가 단계가 남았습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="공사비 약 1조698억, 지상 45층 2,886가구 계획. 올해 무응찰이 이어진 끝에 한화 선정. 착공까지는 사업시행인가·관리처분이 남았다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">하안주공5단지,<br>시공사는 한화</h1>
  <p class="sub">광명 <strong>하안주공5단지</strong> 재건축 시공사로 한화 건설부문이 <strong>11월 18일</strong> 총회에서 선정됐습니다. 공사비는 약 1조698억원이고, 하안주공 12개 단지 가운데 처음입니다. <span class="mark">다만 시공사 선정은 출발선이고, 착공까지는 인가 단계가 남아 있습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 11/18 총회</div><div class="kw">한화</div>
      <p>하안주공5단지 <strong>시공사</strong> 선정.</p></div>
    <div class="kcard"><div class="hot">공사비</div><div class="kw">1조698억</div>
      <p>보도 기준, <strong>본계약</strong>에서 변동.</p></div>
    <div class="kcard"><div class="hot">계획 규모</div><div class="kw">2,886가구</div>
      <p>지하 5층~<strong>지상 45층</strong>.</p></div>
    <div class="kcard"><div class="hot">하안주공</div><div class="kw">12곳 중 1</div>
      <p>처음으로 <strong>시공사</strong>를 정했다.</p></div>
  </div>

  <div class="colchart">
    <h3>올해 시공사를 정한 재건축 공사비 (원)</h3>
    <span class="badge">하안주공5단지는 1조원대</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5.56조</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:40.4%">2.61조</div><div class="barv" style="--h:40.4%"></div></div>
      <div class="col"><div class="v gtx" style="--h:16.5%">1.07조</div><div class="barv" style="--h:16.5%"></div></div>
    </div>
    <div class="collbl"><span>압구정3구역</span><span>목동10단지</span><span>하안주공5단지</span></div>
    <p class="cap">압구정3구역(5월, 현대건설)·목동10단지(10월, 현대건설 공시)·하안주공5단지(11월 18일, 한화 건설부문) 보도 금액입니다. 본계약에서 바뀔 수 있습니다. 막대 길이는 최댓값 5조5,610억원을 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 하안주공5단지 시공사 한화"),
    ("02-size", "하안주공5단지, 숫자 셋으로 보면"),
    ("03-cost", "올해 대어 셋 중 하안주공5단지"),
    ("04-share", "한화 올해 수주의 42%가 이 한 곳"),
    ("05-next", "하안주공5단지, 착공은 아직"),
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

ARTICLE = '''<article data-tags="하안주공5단지,하안주공재건축,광명재건축,하안주공,한화건설,포레나,광명하안동,신탁방식재건축,재건축시공사,광명아파트">
  <h2>하안주공5단지 재건축, 12개 단지 중 첫 시공사 한화</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 하안주공5단지 시공사 한화"></span>

  <p><strong>3줄 요약</strong><br>하안주공5단지 재건축 시공사로 한화 건설부문이 11월 18일 총회에서 선정됐습니다.<br>공사비는 약 1조698억원이고, 지하 5층에서 지상 45층까지 2,886가구를 짓는 계획입니다.<br>하안주공 12개 단지 가운데 처음 시공사를 정한 곳이지만, 착공까지는 사업시행인가와 관리처분 단계가 남아 있습니다.</p>

  <p>하안주공5단지 시공사가 정해졌습니다. 경기 광명시 하안동 하안주공5단지 재건축 정비사업 시공사 선정총회가 11월 18일 열렸고, 한화 건설부문이 시공사로 뽑혔다고 다음 날 밝혔습니다. 서울경제, 한국경제, 파이낸셜뉴스, 이데일리가 같은 날 일제히 전했습니다. <span class="mark">하안주공 12개 단지 가운데 시공사를 정한 건 이번이 처음입니다.</span> 올해 입찰이 여러 번 무응찰로 끝났던 곳이라 소유자들에게는 한 고비를 넘긴 셈입니다.</p>

  <h3>하안주공5단지 시공사, 한화로 정해졌다</h3>
  <div class="chart" data-img="카드뉴스 2번 · 하안주공5단지, 숫자 셋으로 보면">
    <h3>하안주공5단지 재건축 계획 (보도 기준)</h3>
    <h4>공사비</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">1조698억</span>
      <span class="desc">본계약에서 바뀔 수 있다.</span></div>
    <h4>계획 가구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2,886</span>
      <span class="desc">일부 보도는 2,885가구. 인가 단계에서 바뀐다.</span></div>
    <h4>최고 층수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">45층</span>
      <span class="desc">지하 5층~지상 45층 계획.</span></div>
    <p class="cap">한화 건설부문 발표(2026년 11월 19일)와 서울경제·한국경제·파이낸셜뉴스 보도 기준입니다. 계획 가구수와 층수는 확정 전입니다.</p>
  </div>
  <p>결론부터 말하면 공사비 1조원대, 45층 2,886가구 계획입니다. 한화 건설부문은 지하 5층에서 지상 45층까지 아파트 2,886가구를 짓는다고 밝혔고, 공사비는 약 1조698억원입니다. 일부 매체는 가구수를 2,885가구로 적었는데, 어느 쪽이든 계획 숫자라 사업시행인가 단계에서 다시 바뀔 수 있습니다.</p>
  <p>이 단지는 조합이 아니라 신탁 방식입니다. 사업시행자는 한국자산신탁이고, 입찰 조건도 신탁사가 정했습니다. 하안주공 재건축은 1·2단지와 8단지를 빼고 대부분 신탁 방식으로 추진된다고 2025년 9월 보도됐습니다. 신탁 방식은 조합을 따로 만들지 않아 초기 절차가 빠른 대신, 신탁사에 수수료를 냅니다.</p>
  <p>시공사가 정해지기까지는 순탄하지 않았습니다. 3월 첫 입찰은 응찰한 건설사가 없어 유찰됐고, 7월 세 번째 공고도 무응찰이었습니다. 당시 신탁사가 제시한 공사비는 3.3㎡당 800만원이었는데, 건설사들 사이에서 낮다는 평가가 있었다는 보도가 나왔습니다. 그 뒤 협상 절차를 거쳐 이번 총회에서 한화가 최종 선정됐습니다.</p>
  <p>800만원이 어느 정도인지 비교해 보면 이렇습니다. 이번 주 유찰된 서울 목동4단지는 3.3㎡당 1,010만원을 내걸었습니다. 서울 대표 단지와 200만원 넘게 차이가 나니 건설사들이 망설였던 이유가 짐작됩니다. 최종 계약 단가는 아직 공개되지 않았고, 본계약에서 정해집니다.</p>
  <p>누가 영향을 받는지도 짚어 둘 만합니다. 시공사가 정해지면 설계를 구체화하고 사업시행인가 신청 준비에 들어갈 수 있습니다. 반대로 시공사 없이 시간이 흐르면 그사이 오른 공사비가 고스란히 사업비에 얹힙니다. 올해 두 차례 넘게 유찰되는 동안 소유자들이 가장 걱정한 게 이 부분이었고, 이번 선정으로 일정이 다시 움직이기 시작했습니다.</p>

  <h3>올해 시공사 정한 대어와 비교하면</h3>
  <span class="imgslot" hidden data-img="카드뉴스 3번 · 올해 대어 셋 중 하안주공5단지"></span>
  <p>서울 대어보다는 작지만 경기권에서는 큰 사업입니다. 올해 시공사를 정한 재건축 가운데 압구정3구역은 공사비 5조5,610억원으로 정비사업 사상 최대였고, 목동10단지는 10월 현대건설이 2조6,136억원에 시공권을 땄습니다. 하안주공5단지 1조698억원은 압구정3구역의 5분의 1, 목동10단지의 절반이 안 됩니다.</p>
  <p>그래도 1조원을 넘는 사업은 흔하지 않습니다. 공사비 1조원은 업계에서 '대어'로 부르는 기준선이고, 하안주공5단지는 광명 철산·하안 일대 재건축 가운데서도 큰 축에 듭니다. 광명시에는 이미 광명 푸르지오포레나, 광명 자이더샵포레나가 있어 이번 수주로 포레나 브랜드 단지가 하나 더 늘게 됐습니다.</p>
  <p>자주 헷갈리는 점이 하나 있습니다. 공사비는 건설사가 받는 돈이지 분양가가 아닙니다. 소유자가 실제로 낼 분담금은 공사비뿐 아니라 일반분양 수입, 이주비 이자, 신탁 수수료 등을 모두 따져야 나오고, 이 계산은 관리처분계획 단계에서 처음 구체적인 숫자로 나옵니다.</p>
  <p>가구당으로 나눠 보면 감이 옵니다. 공사비 1조698억원을 계획 가구수 2,886가구로 나누면 한 가구에 약 3억7,000만원꼴입니다. 이 돈이 그대로 소유자 몫이 되는 건 아닙니다. 늘어나는 가구를 일반분양으로 팔아 생기는 수입이 공사비를 덜어 주기 때문입니다. 그래서 같은 공사비라도 일반분양가가 얼마로 정해지느냐에 따라 분담금이 크게 달라집니다.</p>

  <h3>한화는 올해 수주의 42%를 여기서</h3>
  <div class="chart" data-img="카드뉴스 4번 · 한화 올해 수주의 42%가 이 한 곳">
    <h3>한화 건설부문 올해 정비사업 수주 (억원)</h3>
    <div class="bar"><label>올해 누적</label>
      <div class="rail"><div class="fill gray" style="width:100%">25,264</div></div></div>
    <div class="bar"><label>하안주공5단지</label>
      <div class="rail"><div class="fill" style="width:42.3%">10,698</div></div></div>
    <p class="cap">한화 건설부문 발표·파이낸셜뉴스(2026년 11월 19일) 기준입니다. 누적액은 매체에 따라 '2조5,000억원 돌파'로도 보도됐습니다. 막대 길이는 최댓값 2조5,264억원을 기준으로 맞췄습니다.</p>
  </div>
  <p>한화 입장에서는 올해 가장 큰 계약입니다. 이번 수주로 한화 건설부문의 올해 정비사업 누적 수주액은 2조5,264억원이 됐고, 지난해의 세 배가 넘는 역대 최대라고 회사는 밝혔습니다. 그중 42%가 하안주공5단지 한 곳에서 나왔습니다.</p>
  <p>소유자가 이 숫자를 볼 이유도 있습니다. 시공사가 사업 규모를 키우는 중이라는 건 다음 하안주공 단지 입찰에도 관심을 보일 가능성이 있다는 뜻입니다. 4월 하안주공 시공사 설명회에는 SK에코플랜트, 한화 건설부문, 대방건설이 참석했다고 보도됐습니다. 다만 다른 단지에 누가 들어올지는 입찰 결과가 나와야 알 수 있고, 지금 말할 수 있는 건 관심을 보인 건설사가 있었다는 것까지입니다.</p>
  <p>비교할 숫자가 하나 더 있습니다. 한화의 올해 수주는 지난해의 세 배가 넘는다고 했는데, 한 해 수주의 절반 가까이를 경기권 단지 한 곳에서 채웠다는 점이 눈에 띕니다. 서울 대표 단지에서는 현대건설 같은 대형사가 단독으로 들어가는 일이 잦았고, 그 사이 다른 건설사들은 수도권 대단지로 눈을 돌리는 모습입니다. 하안주공처럼 12개 단지가 줄줄이 이어지는 곳은 첫 단지를 잡으면 다음 단지 입찰에서 유리하다는 말도 나옵니다. 다만 이건 업계의 관측입니다.</p>

  <h3>하안주공5단지, 착공은 아직 멀었다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 하안주공5단지, 착공은 아직">
    <h3>하안주공 재건축 남은 단계 (2025년 보도 계획)</h3>
    <h4>사업시행인가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2027년</span>
      <span class="desc">설계·가구수가 여기서 굳는다.</span></div>
    <h4>관리처분인가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2028년</span>
      <span class="desc">분담금이 숫자로 나온다.</span></div>
    <h4>착공</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">2030년</span>
      <span class="desc">하안주공 전체 계획, 5단지 확정 일정 아님.</span></div>
    <p class="cap">아시아경제(2025년 9월) 보도의 하안주공 재건축 전체 일정 계획입니다. 단지별 실제 일정은 사업시행자와 광명시 고시로 확인하십시오.</p>
  </div>
  <p>시공사 선정은 출발선입니다. 2025년 보도된 하안주공 재건축 계획은 2027년 사업시행인가, 2028년 관리처분인가를 거쳐 2030년 착공하는 일정입니다. 이 일정은 하안주공 전체를 놓고 세운 계획이라 5단지만의 확정 일정이 아니고, 인허가와 이주가 늦어지면 뒤로 밀립니다.</p>
  <p>다른 단지는 아직 한 단계씩 앞에 있습니다. 12단지는 2025년 12월 10일 정비구역과 사업시행자 지정이 고시됐고, 8단지는 2025년 9월 조합설립추진위원회 승인을 받았습니다. 3·4단지도 시공사 선정 절차에 들어간다고 4월 보도됐습니다. 5단지가 첫 사례가 됐으니 공사비 수준과 입찰 조건이 다른 단지의 기준점이 될 가능성이 큽니다.</p>
  <p>이 단계에서 매수를 고민한다면 몇 가지를 따로 봐야 합니다. 재건축 단지의 거래 제한과 입주권 요건은 단계마다 다르고, 신탁 방식은 조합 방식과 절차가 조금 다릅니다. 일반론으로 판단하지 말고 사업시행자와 광명시 재건축 담당 부서에 직접 확인하는 게 맞습니다.</p>
  <p>앞으로 볼 날짜는 두 가지입니다. 하나는 한국자산신탁과 한화가 맺을 본계약 시점이고, 다른 하나는 사업시행인가 신청 시점입니다. 본계약에서 3.3㎡당 단가와 물가 상승분을 어떻게 반영할지가 정해지고, 사업시행인가 신청 때 가구수와 평형 구성이 처음 공식 서류로 나옵니다. 두 날짜 모두 아직 발표되지 않았으니 사업시행자 공지를 챙겨 보시면 됩니다.</p>

  <h3>하안주공 소유자가 볼 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 하안주공 소유자가 볼 3가지 (체크리스트)">
    <img class="card-art" data-file="hah-06-check.png" src="../images/cards/report/hah-06-check.png" alt="체크포인트 카드 · 1. 본계약 공사비, 2. 계획 가구수는 확정 전, 3. 다음 단계 일정" loading="lazy" width="1080" height="1080">
    <figcaption>하안주공5단지 시공사 선정 뒤, 확인할 3가지. 저장해 두고 보세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>본계약 공사비</strong>. 1조698억원은 선정 시점 금액입니다. 3.3㎡당 단가와 물가 반영 조건은 본계약에서 정해집니다.</li>
    <li><strong>계획 가구수는 확정 전</strong>. 2,886가구와 45층은 계획이고, 사업시행인가에서 바뀔 수 있습니다.</li>
    <li><strong>다음 단계 일정</strong>. 착공 2030년은 하안주공 전체 계획입니다. 단지 일정은 사업시행자 공지와 광명시 고시로 보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>하안주공5단지</strong> 재건축 시공사로 한화 건설부문이 11월 18일 선정됐습니다. 공사비 약 1조698억원, 지상 45층 2,886가구 계획이고, 하안주공 12개 단지 가운데 첫 시공사 선정입니다. <span class="mark">올해 무응찰이 이어진 끝에 정해진 만큼, 이 조건이 다른 하안주공 단지의 기준점이 될 수 있습니다.</span> 다만 착공까지는 사업시행인가와 관리처분이 남아 있고, 가구수와 공사비는 그 과정에서 바뀔 수 있습니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 공사비와 가구수·층수는 시공사 발표와 보도 기준이며 본계약과 인가 단계에서 바뀔 수 있습니다. 착공 일정은 2025년 보도된 하안주공 전체 계획으로 5단지 확정 일정이 아닙니다. 거래 제한과 입주권 요건은 사업시행자와 광명시에 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 한화 건설부문 하안주공5단지 시공사 선정 발표(2026-11-19) · 서울경제·한국경제·파이낸셜뉴스·이데일리 하안주공5단지 수주(2026-11-19) · MTN·더구루 하안주공5단지 입찰 무응찰(2026-03·07) · 아시아경제 하안주공 재건축 일정(2025-09) · 파이낸셜뉴스 목동10단지 시공사 선정(2026-10) · 광명시 하안주공12단지 정비구역 고시(2025-12)<br>
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
for v, h in ((2.6136, 40.4), (1.0698, 16.5)):
    assert round(v / 5.561 * 86, 1) == h
assert round(10698 / 25264 * 100, 1) == 42.3
assert round(10698 / 2886, 1) == 3.7
KW = "하안주공5단지"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("하안주공5단지")
slots = (art0.count('class="chart"') + art0.count('class="colchart"') + art0.count("<figure") + art0.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art0))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · 줄표 0")
