# -*- coding: utf-8 -*-
"""리포트 #98 (2026-10-19) 목동10단지 재건축 시공사 현대건설 선정. #97을 복제해 교체한다.

메인 검색어: 목동10단지 재건축

수치와 검산
  사건일과 오늘의 간격: 10/18(일) 제3차 토지등소유자 전체회의 → 오늘 10/19, 1일. 현대건설 DART 공시 10/19.
  표결 (디벨로퍼뉴스 10/18): 사업시행자 지정 동의 토지등소유자 1,960명 · 참여 1,624명 · 찬성 1,557명 = 95.9%
        참여율 1,624/1,960 = 82.9% · 찬성/전체 동의자 1,557/1,960 = 79.4%
  규모 (MTN 10/18·10/6): 최고 15층 2,160가구 → 최고 40층 4,248가구 (+2,088, 1.97배). 통합심의 전 계획.
  공사비: 예정공사비 약 2조6,135억원 (3.3㎡당 약 990만원, 디벨로퍼뉴스·MTN) · DART 계약금액 약 2조6,136억원(VAT 별도, 리드경제)
          가구당 단순 나눗셈 2조6,135억 / 4,248 = 약 6억1,523만원
  현대건설 제안 (MTN 10/18): 디에이치 목동 에세르 · 커뮤니티 가구당 3.22평 · 공사비 인상분 12개월 현대 부담 ·
          입찰보증금 금리 CD+0% · 이주비 LTV 100% (제안)
  경과 (디벨로퍼뉴스): 1차 현설 6개사(현대·대우·포스코이앤씨 등) → 입찰 현대 단독 → 2차 현설 현대 단독 → 2회 유찰 → 우협 → 선정
  목동 단지별 (MTN 10/6·10/8, 헤럴드 6/28, 서플 10/5, 파이낸셜 9/27):
    6단지 DL이앤씨 6/27 선정 86.2% · 2,184가구 49층 · 1조2,868억
    10단지 현대 4,248 · 990만원
    12단지 GS 2,810가구 43층 · 1조7,888억 · 980만원 · 총회 11월 목표
    13단지 삼성물산 3,852가구 49층 · 2조3,762억 · 980만원 · 홍보관 10월 마지막 주 · 총회 11월 중순 · 우협 9/29
    8단지 대우 1,881가구 49층 · 1조1,119억 · 965만원 · 총회 12월 중순 목표
    4단지 2,436가구 49층 · 1조6,389억 · 1,010만원 · 입찰 마감 11/16 예정
    7단지 입찰공고 11월 중순 예정
  대시보드 세로 (계획 가구, 최댓값 4,248 → 86%): 3,852 → 78.0 · 2,810 → 56.9 · 2,436 → 49.3 · 2,184 → 44.2 · 1,881 → 38.1
  표결 가로 (명, 1,960 → 100%): 1,624 → 82.9 · 1,557 → 79.4
  3.3㎡당 공사비 가로 (만원, 1,010 → 100%): 990 → 98.0 · 980 → 97.0 · 965 → 95.5
  같은 주말: 여의도 시범 10/16 삼성물산 선정 2조2,685억원 (세계일보 10/19)

단정하지 않은 것
  · 4,248가구·40층은 통합심의 전 계획 → 확정 전
  · 이주비 LTV 100%는 제안 조건. 실제 대출 한도는 본계약·대출 규제에 따라 달라질 수 있음
  · 12·13·8단지 총회 시기는 보도된 목표·예정
  · 조합원 지위 양도·거래 제한은 양천구청·정비사업 정보몽땅으로 넘김
"""
import pathlib
import re

ROOT = pathlib.Path("/home/claude/mynews")
SRC = ROOT / "posts/2026-10-16-jamsil5.html"
DST = ROOT / "posts/2026-10-19-mokdong10.html"
SLUG, PRE = "2026-10-19-mokdong10", "mkd1019"
NO, DATE = 98, "2026-10-19"
PREV_SLUG = "jsl1016-"
BANNED = ["잠실주공5단지", "수영장", "정구장"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "목동10단지 재건축 현대건설 확정, 단독 입찰에 96% 찬성"
DESC = ("목동10단지 재건축 시공사로 현대건설이 10월 18일 선정됐습니다. 투표 1,624명 중 1,557명(95.9%)이 찬성했습니다. "
        "최고 15층 2,160가구를 최고 40층 4,248가구로 짓는 계획이고 예정공사비는 약 2조6,135억원(3.3㎡당 약 990만원)입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="목동 재건축 첫 현대건설 수주. 단지명 디에이치 목동 에세르, 4,248가구 계획. 12·13·8·4단지 시공사 선정 일정까지 정리했습니다.">
<meta property="og:type" content="article">
<meta property="og:image" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:url" content="{URL}">
<link rel="canonical" href="{URL}">
<link rel="alternate" type="application/rss+xml" title="부동산 인사이트 RSS" href="../feed.xml">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"NewsArticle",
 "headline":"{TITLE}",
 "description":"목동10단지 재건축 시공사로 현대건설이 10월 18일 토지등소유자 전체회의에서 선정됐습니다. 투표 1,624명 중 1,557명(95.9%)이 찬성했습니다. 최고 40층 4,248가구 계획, 예정공사비 약 2조6,135억원이며 제안 단지명은 디에이치 목동 에세르입니다. 목동 12·13단지는 11월, 8단지는 12월 시공사 선정이 예정돼 있습니다.",
 "image":"{OG}",
 "datePublished":"{DATE}","dateModified":"{DATE}",
 "author":{{"@type":"Organization","name":"부동산 인사이트"}},
 "publisher":{{"@type":"Organization","name":"부동산 인사이트"}},
 "mainEntityOfPage":"{URL}","inLanguage":"ko"}}
</script>'''

HEADER = f'''<header>
  <div class="eyebrow">2026 · 10월 부동산 키워드 리포트 #{NO}</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">목동10단지 재건축,<br>현대건설 96% 찬성</h1>
  <p class="sub"><strong>목동10단지 재건축</strong> 시공사가 어제(<strong>10월 18일</strong>) <strong>현대건설</strong>로 정해졌습니다. 투표한 1,624명 중 <strong>1,557명(95.9%)</strong>이 찬성했습니다. 경쟁사 없이 단독으로 들어온 입찰이었습니다. <span class="mark">목동 14개 단지 중 시공사가 확정된 곳은 6단지에 이어 두 번째입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 선정</div><div class="kw">95.9%</div>
      <p>1,624명 중 <strong>1,557명 찬성</strong>.</p></div>
    <div class="kcard"><div class="hot">계획</div><div class="kw">4,248가구</div>
      <p>2,160가구에서 <strong>최고 40층</strong>.</p></div>
    <div class="kcard"><div class="hot">공사비</div><div class="kw">2조6,135억</div>
      <p>3.3㎡당 <strong>약 990만원</strong>.</p></div>
    <div class="kcard"><div class="hot">다음</div><div class="kw">11월</div>
      <p>12·13단지 <strong>시공사 총회</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>목동 재건축 단지별 계획 가구수 (가구 · 아래 숫자는 단지)</h3>
    <span class="badge">시공사 선정 단계 6곳</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">4,248</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:78%">3,852</div><div class="barv" style="--h:78%"></div></div>
      <div class="col dim"><div class="v" style="--h:56.9%">2,810</div><div class="barv" style="--h:56.9%"></div></div>
      <div class="col dim"><div class="v" style="--h:49.3%">2,436</div><div class="barv" style="--h:49.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:44.2%">2,184</div><div class="barv" style="--h:44.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:38.1%">1,881</div><div class="barv" style="--h:38.1%"></div></div>
    </div>
    <div class="collbl"><span>10</span><span>13</span><span>12</span><span>4</span><span>6</span><span>8</span></div>
    <p class="cap">모두 같은 항목(재건축 후 계획 가구수)이라 한 축에 놓았습니다. 막대 길이는 최댓값 4,248가구를 기준으로 맞췄습니다. 머니투데이방송(10월 6·8·18일)·헤럴드경제(6월 28일)·머니투데이(10월 5일) 보도 기준이며 심의 단계에서 바뀔 수 있는 계획 수치입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 목동10단지 재건축 현대건설 확정, 단독 입찰에 96% 찬성"),
    ("02-vote", "목동10단지 재건축 시공사 표결 1,557명 찬성"),
    ("03-scale", "2,160가구가 4,248가구로, 최고 40층"),
    ("04-cost", "3.3㎡당 공사비, 목동 단지별 비교"),
    ("05-next", "목동 재건축 다음 시공사 선정 일정"),
    ("06-check", "목동10단지 재건축 체크 3가지"),
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

ARTICLE = '''<article data-tags="목동10단지재건축,목동10단지,디에이치목동에세르,목동재건축,현대건설,목동신시가지,양천구재건축,재건축시공사선정,목동12단지,목동13단지">
  <h2>목동10단지 재건축, 현대건설 96% 찬성</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 목동10단지 재건축 현대건설 확정, 단독 입찰에 96% 찬성"></span>

  <p>목동10단지 재건축 시공사로 <strong>현대건설</strong>이 선정됐습니다. 어제(10월 18일) 동양미래대학교에서 열린 2026년 제3차 토지등소유자 전체회의 결과입니다. 현대건설은 오늘(19일) 전자공시로 계약금액 약 2조6,136억원(부가세 별도)을 알렸습니다. <span class="mark">현대건설이 목동 재건축에서 시공권을 따낸 것은 이번이 처음입니다.</span></p>

  <h3>목동10단지 재건축 시공사 표결, 1,557명 찬성</h3>
  <div class="chart" data-img="카드뉴스 2번 · 목동10단지 재건축 시공사 표결 1,557명 찬성">
    <h3>10월 18일 시공자 선정 안건 (명)</h3>
    <div class="bar"><label>동의자</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,960명</div></div></div>
    <div class="bar"><label>투표</label>
      <div class="rail"><div class="fill gray" style="width:82.9%">1,624명</div></div></div>
    <div class="bar"><label>찬성</label>
      <div class="rail"><div class="fill" style="width:79.4%">1,557명</div></div></div>
    <p class="cap">모두 같은 항목(사람 수, 명)이라 한 축에 놓았습니다. 막대 길이는 사업시행자 지정에 동의한 토지등소유자 1,960명을 기준으로 맞췄습니다. 투표 1,624명은 현장·온라인·서면결의를 합친 수입니다. 디벨로퍼뉴스·머니투데이방송(10월 18일) 보도 기준입니다.</p>
  </div>
  <p>사업시행자 지정에 동의한 토지등소유자 1,960명 중 1,624명(82.9%)이 투표했고, 그중 <strong>1,557명(95.9%)</strong>이 현대건설에 찬성했습니다. 목동10단지는 한국토지신탁이 사업시행자인 신탁 방식이라 '조합 총회'가 아니라 '토지등소유자 전체회의'로 의결합니다. 경쟁은 없었습니다. 1차 현장설명회에는 현대건설·대우건설·포스코이앤씨 등 6개사가 왔지만 입찰서는 현대건설만 냈고, 2차 현장설명회에는 현대건설만 참석했습니다. <span class="mark">두 차례 유찰 뒤 우선협상대상자로 지정돼 이번에 확정됐습니다.</span></p>

  <h3>목동10단지 재건축 규모, 2,160가구에서 4,248가구로</h3>
  <div class="chart" data-img="카드뉴스 3번 · 2,160가구가 4,248가구로, 최고 40층">
    <h3>목동10단지 지금과 계획</h3>
    <h4>지금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2,160</span>
      <span class="desc">가구 · 최고 15층.</span></div>
    <h4>계획</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4,248</span>
      <span class="desc">가구 · 최고 40층. 약 1.97배.</span></div>
    <h4>예정공사비</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2.6조</span>
      <span class="desc">약 2조6,135억원. 가구당 단순 계산 약 6억1,500만원.</span></div>
    <p class="cap">머니투데이방송·디벨로퍼뉴스(10월 18일) 보도 기준입니다. 가구당 금액은 예정공사비를 계획 가구수로 나눈 단순 계산이며 분담금이 아닙니다. 가구수·층수는 통합심의 전 계획이라 바뀔 수 있습니다.</p>
  </div>
  <p>서울 양천구 신정동 311번지 일대, 구역면적 19만4,686㎡입니다. 지하철 2호선 양천구청역과 가깝고 계남초·신서중·목동고가 주변에 있습니다. 계획은 <strong>최고 40층 4,248가구</strong>로 지금보다 2,088가구가 늘어납니다. <span class="mark">남은 절차는 통합심의와 사업시행계획인가라서 가구수와 층수는 아직 확정 전입니다.</span></p>

  <h3>3.3㎡당 990만원, 목동 단지별 공사비 비교</h3>
  <div class="chart" data-img="카드뉴스 4번 · 3.3㎡당 공사비, 목동 단지별 비교">
    <h3>목동 재건축 3.3㎡당 예정공사비 (만원)</h3>
    <div class="bar"><label>4단지</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,010</div></div></div>
    <div class="bar"><label>10단지</label>
      <div class="rail"><div class="fill" style="width:98%">990</div></div></div>
    <div class="bar"><label>12단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>13단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>8단지</label>
      <div class="rail"><div class="fill gray" style="width:95.5%">965</div></div></div>
    <p class="cap">모두 같은 항목(3.3㎡당 예정공사비, 만원)이라 한 축에 놓았습니다. 막대 길이는 최댓값 1,010만원을 기준으로 맞췄습니다. 머니투데이방송(10월 6·8일)·머니투데이(10월 5일) 보도 기준이며, 6단지는 같은 기준 수치가 보도되지 않아 뺐습니다.</p>
  </div>
  <p>목동10단지의 3.3㎡당 예정공사비는 약 <strong>990만원</strong>입니다. 목동 다른 단지들도 965만~1,010만원으로 거의 같은 선입니다. 차이는 공사비보다 <strong>제안 조건</strong>에서 났습니다. 현대건설은 단지명 <strong>디에이치 목동 에세르</strong>, 가구당 3.22평의 커뮤니티 시설, <strong>공사비 인상분 12개월 현대건설 부담</strong>, 입찰보증금 금리 CD+0%, 이주비 LTV 100%를 제안했습니다. <span class="mark">이주비 LTV 100%는 제안 조건이며, 실제 대출 한도는 본계약 내용과 대출 규제에 따라 달라질 수 있습니다.</span></p>

  <h3>목동 재건축 다음 시공사 선정, 11월에 몰린다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 목동 재건축 다음 시공사 선정 일정">
    <h3>목동 단지별 시공사 선정 일정</h3>
    <h4>6단지 · DL이앤씨</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">6월</span>
      <span class="desc">선정 완료(86.2% 찬성). 2,184가구.</span></div>
    <h4>10단지 · 현대건설</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.18</span>
      <span class="desc">선정 완료(95.9% 찬성). 4,248가구.</span></div>
    <h4>12단지 · 13단지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월</span>
      <span class="desc">GS건설, 삼성물산 선정 총회 목표.</span></div>
    <h4>4단지 · 7단지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월</span>
      <span class="desc">4단지 입찰 마감 16일, 7단지 입찰공고 중순.</span></div>
    <h4>8단지 · 대우건설</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12월</span>
      <span class="desc">중순 선정 총회 목표.</span></div>
    <p class="cap">머니투데이방송(10월 6·8일)·머니투데이(10월 5일)·헤럴드경제(6월 28일) 보도 기준입니다. 11월·12월 일정은 보도된 목표와 예정이며 각 단지 공고로 확인하십시오.</p>
  </div>
  <p>이번 달 안에는 <strong>목동13단지</strong> 삼성물산 홍보관이 10월 마지막 주 문을 엽니다(제안 단지명 래미안 모브13, 3,852가구). 11월에는 <strong>목동12단지</strong> GS건설(2,810가구)과 13단지 삼성물산의 선정 총회가 목표로 잡혀 있고, <strong>목동4단지</strong>는 16일 입찰을 마감합니다. 4단지 현장설명회에는 현대건설·포스코이앤씨 등 4개사가 왔습니다. <span class="mark">지금까지 목동은 단독 응찰이 이어졌습니다. 4단지와 7단지가 첫 경쟁입찰이 될지가 다음 관전 포인트입니다.</span> 같은 주말(16일) 여의도 시범아파트는 삼성물산을 시공사로 정했습니다(공사비 약 2조2,685억원).</p>

  <h3>목동10단지 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 목동10단지 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="mkd1019-06-check.png" src="../images/cards/report/mkd1019-06-check.png" alt="체크포인트 카드 · 1. 확정된 것은 시공사, 2. 이주비 LTV 100%는 제안, 3. 거래 전 지위 양도 확인" loading="lazy" width="1080" height="1080">
    <figcaption>목동10단지 재건축 상담에 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>확정된 것은 시공사</strong>. 4,248가구·최고 40층은 통합심의 전 계획입니다. 심의 단계마다 바뀔 수 있습니다.</li>
    <li><strong>이주비 LTV 100%는 제안</strong>. 본계약 조건과 그때의 대출 규제를 보고 판단하십시오. 개인별 한도는 사업시행자 안내로 확인합니다.</li>
    <li><strong>거래 전 지위 양도 확인</strong>. 토지등소유자 지위 승계와 거래 제한은 단계마다 다릅니다. 양천구청·정비사업 정보몽땅(cleanup.seoul.go.kr)으로 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>목동10단지 재건축</strong> 시공사는 현대건설입니다. 10월 18일 투표 1,624명 중 1,557명(95.9%)이 찬성했고, 단지명은 디에이치 목동 에세르로 제안됐습니다. 최고 40층 4,248가구, 예정공사비 약 2조6,135억원(3.3㎡당 약 990만원) 계획입니다. <span class="mark">목동은 11월 12·13단지 총회와 4단지 입찰 마감이 이어집니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 수치는 디벨로퍼뉴스·머니투데이방송(2026-10-18), 리드경제(2026-10-19, 현대건설 공시), 머니투데이방송(2026-10-06·08), 머니투데이(2026-10-05), 헤럴드경제(2026-06-28), 세계일보(2026-10-19) 보도 기준입니다. 계획 가구수·층수·공사비는 확정 전이며 사업시행자(한국토지신탁) 공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 디벨로퍼뉴스 목동10단지 시공사 선정(2026-10-18) · 머니투데이방송 목동10단지 현대건설 수주(2026-10-18) · 리드경제 현대건설 공시(2026-10-19) · 머니투데이방송 목동 수주 홍보관·13단지(2026-10-06·08) · 머니투데이 목동 재건축 경쟁입찰(2026-10-05) · 헤럴드경제 목동6단지 DL이앤씨(2026-06-28) · 세계일보 여의도 시범 삼성물산(2026-10-19)<br>
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
# 검산
assert round(1557 / 1624 * 100, 1) == 95.9 and round(1624 / 1960 * 100, 1) == 82.9 and round(1557 / 1960 * 100, 1) == 79.4
assert 4248 - 2160 == 2088 and round(4248 / 2160, 2) == 1.97
assert round(26135e8 / 4248 / 1e4) == 61523
for v, h in ((3852, 78.0), (2810, 56.9), (2436, 49.3), (2184, 44.2), (1881, 38.1)):
    assert round(v / 4248 * 86, 1) == h, (v, h)
for v, w in ((990, 98.0), (980, 97.0), (965, 95.5)):
    assert round(v / 1010 * 100, 1) == w, (v, w)
KW = "목동10단지 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("목동10단지재건축")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
