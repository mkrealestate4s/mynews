# -*- coding: utf-8 -*-
"""리포트 #117 (2026-11-06) 재건축 통합지원센터 이달 말 출범. #116을 복제해 교체한다.

메인 검색어: 재건축 통합지원센터

수치와 검산
  사건일과 오늘의 간격: 김이탁 국토부 1차관 발언 11/5 (MTN 도시정비포럼) → 1일.
  MTN(11/5): 국토부 인허가 지원 기능 + 금융위 금융지원센터를 합친 인허가·금융 통합지원센터 이달 말 출범.
    수도권 주요 정비사업장 전담 관리, 금감원 직원 1명이 약 20개 사업장 담당.
    서울 재건축·재개발 매년 평균 3만호 이상 착공 계획.
  뉴스핌·이투데이(10/16 정례브리핑): '연내' 출범 예정, 지자체 간 법령 해석 차이·갈등 조정, 이주비 한도 확대 언급.
  한국경제(10/13): 송파한양1차 조합설립인가 접수 사흘 만(법정 처리기한 30일).
    개포주공6·7단지 관리처분계획 인가, 1,960가구 → 최고 35층 2,698가구(+738, +37.7%).
단정하지 않은 것
  · 출범일(이달 말 vs 연내 보도 엇갈림) · 센터 이름(보도마다 다름)
  · 이주비 한도 확대의 구체 수치(검색으로 못 읽음) · 개별 사업장 지정 여부
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-05-seoul-listings.html"
SLUG, PRE = "2026-11-06-redev-center", "rc1106"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 117, "2026-11-06"
PREV_SLUG = "sl1105-"
BANNED = ["아실", "8만430", "서울부동산정보광장"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "재건축 통합지원센터 이달 말 출범, 뭐가 빨라지나"
DESC = ("재건축 통합지원센터가 이달 말 문을 엽니다. 김이탁 국토교통부 1차관이 11월 5일 밝혔습니다. 국토부 인허가 지원과 금융위원회 금융지원센터를 합쳐 "
        "수도권 주요 정비사업장을 전담 관리하고, 금융감독원 직원 1명이 약 20개 사업장을 맡습니다. 정부는 서울 재건축·재개발을 매년 3만호 이상 착공하겠다고 했습니다.")
HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="인허가와 돈 문제를 한 창구에서. 감독원 직원 1명이 사업장 20곳을 맡고, 서울 재건축·재개발은 매년 3만호 착공이 목표입니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">재건축 통합지원센터<br>이달 말 출범, 뭐가 빨라지나</h1>
  <p class="sub"><strong>재건축 통합지원센터</strong>가 <strong>이달 말</strong> 문을 엽니다. 김이탁 국토교통부 1차관이 <strong>11월 5일</strong> 도시정비포럼에서 밝혔습니다. 인허가와 금융 문제를 한 창구에서 다루고, <strong>감독원 직원 1명이 사업장 20곳</strong>을 맡습니다. <span class="mark">정부 목표는 서울 재건축·재개발 매년 3만호 착공입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 통합지원센터</div><div class="kw">이달 말</div>
      <p>출범 예고, <strong>11월 5일 발언</strong>.</p></div>
    <div class="kcard"><div class="hot">전담 관리</div><div class="kw">1명당 20곳</div>
      <p>감독원 직원이 <strong>사업장 약 20개</strong>.</p></div>
    <div class="kcard"><div class="hot">서울 착공 목표</div><div class="kw">매년 3만호</div>
      <p>재건축·재개발 <strong>평균 3만호 이상</strong>.</p></div>
    <div class="kcard"><div class="hot">구청 속도</div><div class="kw">3일</div>
      <p>송파한양1차 조합설립인가, <strong>법정 30일</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>개포주공6·7단지 가구 수 (가구)</h3>
    <span class="badge">+738가구</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:62.5%">1,960</div><div class="barv" style="--h:62.5%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">2,698</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>지금</span><span>재건축 후</span></div>
    <p class="cap">강남구가 관리처분계획을 인가한 개포주공6·7단지 사례입니다(한국경제 10월 13일 보도, 최고 35층). 막대 높이는 2,698가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 재건축 통합지원센터 이달 말 출범, 뭐가 빨라지나"),
    ("02-what", "재건축 통합지원센터, 두 창구를 하나로"),
    ("03-speed", "구청 인가는 이미 빨라졌다, 30일이 3일로"),
    ("04-when", "출범 시점, 연내에서 이달 말로"),
    ("05-gaepo", "개포주공6·7단지, 1,960가구가 2,698가구로"),
    ("06-check", "재건축 통합지원센터 볼 때 체크 3가지"),
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

ARTICLE = '''<article data-tags="재건축통합지원센터,재건축,재개발,정비사업,재건축인허가,개포주공,송파한양1차,서울재건축,정비사업금융,주택공급">
  <h2>재건축 통합지원센터 이달 말 출범, 뭐가 빨라지나</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 재건축 통합지원센터 이달 말 출범, 뭐가 빨라지나"></span>

  <p>재건축 통합지원센터가 이달 말 문을 엽니다. 김이탁 국토교통부 제1차관이 어제(11월 5일) 머니투데이방송 도시정비포럼 축사에서 밝혔습니다. <span class="mark">재건축·재개발 사업장이 인허가와 돈 문제로 멈추지 않게, 정부가 한 창구에서 붙잡고 관리하겠다는 내용입니다.</span></p>

  <h3>재건축 통합지원센터, 두 창구를 하나로</h3>
  <div class="chart" data-img="카드뉴스 2번 · 재건축 통합지원센터, 두 창구를 하나로">
    <h3>무엇을 합치나</h3>
    <h4>국토교통부</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">인허가</span>
      <span class="desc">심의·인가가 늦어지는 사업장 지원. 지자체 간 법령 해석 차이도 조정.</span></div>
    <h4>금융위원회</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">금융</span>
      <span class="desc">사업비·이주비 대출과 보증 문제를 풀던 금융지원센터.</span></div>
    <h4>전담 관리</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">1명 20곳</span>
      <span class="desc">금융감독원 직원 1명이 수도권 주요 사업장 약 20개를 맡는다.</span></div>
    <p class="cap">머니투데이방송(11월 5일)·뉴스핌(10월 16일) 보도 기준입니다. 센터의 정식 이름은 보도마다 조금씩 달라 확정 전입니다.</p>
  </div>
  <p>지금까지 인허가는 국토부, 돈 문제는 금융위원회가 따로 지원했습니다. 조합 입장에서는 심의가 막히면 구청과 국토부를, 사업비 대출이 막히면 금융기관과 금융위를 따로 찾아야 했습니다. 통합지원센터는 이 둘을 합쳐 사업장별 담당자를 정해 둡니다. <span class="mark">금융감독원 직원 1명이 사업장 약 20곳을 맡는 전담 방식입니다.</span> 정부는 이 센터로 서울 재건축·재개발을 매년 평균 3만호 이상 착공하겠다고 했습니다.</p>

  <h3>구청 인가는 이미 빨라졌다, 30일이 3일로</h3>
  <div class="chart" data-img="카드뉴스 3번 · 구청 인가는 이미 빨라졌다, 30일이 3일로">
    <h3>조합설립인가 처리 기간 (일)</h3>
    <div class="bar"><label>법정 처리기한</label>
      <div class="rail"><div class="fill gray" style="width:100%">30</div></div></div>
    <div class="bar"><label>송파한양1차</label>
      <div class="rail"><div class="fill" style="width:10%"></div><span class="railval">3</span></div></div>
    <p class="cap">한국경제(10월 13일) 보도 기준입니다. 송파구는 송파한양1차 조합설립인가를 접수 사흘 만에 내줬습니다. 막대 길이는 법정 기한 30일을 기준으로 맞췄습니다.</p>
  </div>
  <p>속도전은 자치구에서 먼저 시작됐습니다. 송파구는 송파한양1차 재건축 조합설립인가를 접수 사흘 만에 내줬습니다. 법정 처리기한은 30일입니다. <span class="mark">구청 단계가 빨라져도 그 뒤 심의·이주·착공 단계에서 돈과 해석 문제로 멈추는 일이 많았고, 통합지원센터는 그 구간을 겨냥합니다.</span></p>

  <h3>재건축 통합지원센터 출범 시점, 연내에서 이달 말로</h3>
  <div class="chart" data-img="카드뉴스 4번 · 출범 시점, 연내에서 이달 말로">
    <h3>발표 흐름</h3>
    <h4>10월 16일</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">연내</span>
      <span class="desc">국토부 정례브리핑. 통합 지원센터로 일원화, 연내 출범 예정.</span></div>
    <h4>11월 5일</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">이달 말</span>
      <span class="desc">김이탁 1차관 도시정비포럼 축사. 출범 시점을 앞당겨 예고.</span></div>
    <p class="cap">정확한 출범일과 지원 대상 사업장 명단은 아직 발표되지 않았습니다. 국토교통부 보도자료로 확인해야 합니다.</p>
  </div>
  <p>지난달 16일 국토부 정례브리핑에서는 '연내 출범'이었는데, 이번에는 '이달 말'로 시점이 당겨졌습니다. 다만 정확한 날짜와 어느 사업장이 전담 관리 대상이 되는지는 아직 나오지 않았습니다. <span class="mark">우리 단지가 대상인지는 공식 발표가 난 뒤 조합이나 구청에 물어보는 것이 정확합니다.</span></p>

  <h3>개포주공6·7단지, 1,960가구가 2,698가구로</h3>
  <span class="imgslot" hidden data-img="카드뉴스 5번 · 개포주공6·7단지, 1,960가구가 2,698가구로"></span>
  <p>재건축이 공급에 왜 중요한지 보여 주는 사례가 개포주공6·7단지입니다. 강남구가 관리처분계획을 인가했고, 지금 1,960가구가 최고 35층 2,698가구로 바뀝니다. 738가구(37.7%)가 늘어납니다. <span class="mark">서울은 새 땅이 거의 없어서 이렇게 낡은 단지를 다시 지을 때 늘어나는 가구가 사실상 새 공급입니다.</span> 정부가 착공 속도에 매달리는 이유입니다.</p>

  <h3>재건축 통합지원센터 볼 때 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 재건축 통합지원센터 볼 때 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="rc1106-06-check.png" src="../images/cards/report/rc1106-06-check.png" alt="체크포인트 카드 · 1. 출범일은 공식 발표로, 2. 우리 단지가 대상인지, 3. 계획 가구 수는 확정 전" loading="lazy" width="1080" height="1080">
    <figcaption>재건축 통합지원센터 소식을 볼 때 확인할 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>출범일은 공식 발표로</strong>. '이달 말'은 차관 발언이고 '연내'는 지난달 브리핑입니다. 국토교통부 보도자료가 나오면 그 날짜를 따르십시오.</li>
    <li><strong>우리 단지가 대상인지</strong>. 전담 관리는 수도권 주요 사업장이 대상이라고만 나왔습니다. 조합·구청, 정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
    <li><strong>계획 가구 수는 확정 전</strong>. 심의와 인가 단계마다 가구 수와 층수가 바뀝니다. 기사 속 숫자는 그 시점 계획입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>재건축 통합지원센터</strong>는 국토부 인허가 지원과 금융위원회 금융지원센터를 합친 창구로, 이달 말 출범이 예고됐습니다(11월 5일 김이탁 1차관). 금융감독원 직원 1명이 수도권 사업장 약 20곳을 맡고, 정부는 서울 재건축·재개발을 매년 3만호 이상 착공하겠다는 목표를 내놨습니다. 송파구는 이미 조합설립인가를 사흘 만에 내주고 있습니다. <span class="mark">정확한 출범일과 대상 사업장은 공식 발표를 기다려야 합니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 센터 내용은 머니투데이방송(2026-11-05)·뉴스핌·이투데이(2026-10-16) 보도, 자치구 사례는 한국경제(2026-10-13) 보도 기준입니다. 개포주공6·7단지 증가율은 보도된 가구 수로 계산했습니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 머니투데이방송 김이탁 1차관 인허가·금융 통합지원센터 출범(2026-11-05) · 뉴스핌 정비사업 이주비 한도 확대·인허가 지원 강화(2026-10-16) · 이투데이 금융위 정비사업 금융·보증 지원 강화(2026-10-16) · 한국경제 자치구 재건축 인허가 속도전(2026-10-13)<br>
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
assert 1960 + 738 == 2698 and round(738 / 1960 * 100, 1) == 37.7
assert round(1960 / 2698 * 86, 1) == 62.5
assert round(3 / 30 * 100) == 10
KW = "재건축 통합지원센터"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("재건축통합지원센터")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
