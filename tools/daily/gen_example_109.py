# -*- coding: utf-8 -*-
"""리포트 #109 (2026-10-30) 청라 아크원 푸르지오 견본주택 개관일. #108을 복제해 교체한다.

메인 검색어: 청라 아크원 푸르지오

수치와 검산
  사건일과 오늘의 간격: 견본주택 개관 10/30(오늘) → 0일. 특공 11/2(D-3).
  보도: 청라국제업무단지 M5, 아파트 868 + 주거형 오피스텔 987 = 1,855 · 지하 5층~지상 49층 6개 동
    (아시아타임즈 10/2·10/29, 시대일보 10/29) · 아파트 84㎡ 620·103㎡ 248 · 특공 514·일반 354
    · 분양가 84㎡ 8억3,780만~9억2,070만 · 103㎡ 10억8,880만~11억7,100만(하한은 출처마다 달라 공고문 확인)
    · 공고 10/22 · 견본주택 10/30 · 특공 11/2 · 1순위 11/3 · 당첨 11/10 · 계약 11/22~24
    · 분양가상한제 · 계약금 5% · 중도금 60% · 인천 거주 50% 우선
  대시보드 세로 (1,855 → 86%): 987 → 45.8 · 868 → 40.2 · 354 → 16.4
  가로 공급 (868 → 100%): 514 → 59.2 · 354 → 40.8
  가로 분양가 (11억7,100만 → 100%): 10억8,880만 → 93.0 · 9억2,070만 → 78.6 · 8억3,780만 → 71.5
  계약금 5% 계산: 8억3,780만 → 4,189만 · 9억2,070만 → 4,604만(반올림)

단정하지 않은 것
  · 전매제한·실거주 의무 기간 · 2순위 날짜 · 분양가 하한 · 중도금 대출 조건 → 입주자모집공고 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-29-sh-happyhouse.html"
SLUG, PRE = "2026-10-30-cheongna-arkone", "arw1030"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 109, "2026-10-30"
PREV_SLUG = "shh1029-"
BANNED = ["행복주택"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "청라 아크원 푸르지오 오늘 견본주택, 분양가 8억대"
DESC = ("청라 아크원 푸르지오가 오늘(10월 30일) 견본주택을 엽니다. 아파트 868가구(84㎡ 620·103㎡ 248)로 분양가상한제가 적용되며, "
        "84㎡ 분양가는 8억3,780만~9억2,070만원 선으로 보도됐습니다. 특별공급 11월 2일, 1순위 11월 3일, 당첨 발표 11월 10일입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="아파트 868가구, 특공 514·일반 354. 특공 11월 2일, 1순위 3일. 84㎡ 8억3,780만~9억2,070만원.">
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
  <div class="eyebrow">2026 · 10월 부동산 키워드 리포트 #{NO}</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">청라 아크원 푸르지오,<br>오늘 견본주택</h1>
  <p class="sub"><strong>청라 아크원 푸르지오</strong>가 <strong>10월 30일(금)</strong> 견본주택을 엽니다. 아파트 <strong>868가구</strong>에 분양가상한제가 적용됩니다. <span class="mark">특별공급은 다음 주 월요일 11월 2일, 1순위는 3일입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 오늘</div><div class="kw">10월 30일</div>
      <p><strong>견본주택</strong> 개관.</p></div>
    <div class="kcard"><div class="hot">아파트 공급</div><div class="kw">868가구</div>
      <p>일반공급 <strong>354</strong>.</p></div>
    <div class="kcard"><div class="hot">84㎡ 분양가</div><div class="kw">8억대~9억대</div>
      <p><strong>분양가상한제</strong> 적용.</p></div>
    <div class="kcard"><div class="hot">다음 단계</div><div class="kw">11월 2일</div>
      <p>특별공급, <strong>3일 1순위</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>청라 아크원 푸르지오 공급 구성 (가구·실)</h3>
    <span class="badge">10월 보도</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">1,855</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:45.8%">987</div><div class="barv" style="--h:45.8%"></div></div>
      <div class="col"><div class="v gtx" style="--h:40.2%">868</div><div class="barv" style="--h:40.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:16.4%">354</div><div class="barv" style="--h:16.4%"></div></div>
    </div>
    <div class="collbl"><span>전체</span><span>오피스텔</span><span>아파트</span><span>일반공급</span></div>
    <p class="cap">아시아타임즈(2026-10-02) 보도 수치입니다. 이번 청약은 아파트 868가구이고 오피스텔 987실은 따로 공급합니다. 막대 길이는 전체 1,855를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 청라 아크원 푸르지오, 오늘 견본주택"),
    ("02-supply", "868가구 중 일반공급은 354"),
    ("03-date", "특공 11월 2일, 당첨 11월 10일"),
    ("04-price", "84㎡ 8억3,780만~9억2,070만원"),
    ("05-cash", "계약금 5%, 인천 거주 50% 우선"),
    ("06-tips", "청라 아크원 푸르지오 청약 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="청라아크원푸르지오,아크원푸르지오,청라아크원푸르지오분양가,청라아크원푸르지오견본주택,청라국제도시,청라분양,인천분양,분양가상한제,아파트청약,11월청약">
  <h2>청라 아크원 푸르지오, 오늘 견본주택</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 청라 아크원 푸르지오, 오늘 견본주택"></span>

  <p>청라 아크원 푸르지오가 오늘(10월 30일) 견본주택을 엽니다. 대우건설이 인천 청라국제업무단지 M5블록에 짓는 단지로, 지하 5층~지상 최고 49층 6개 동에 아파트 868가구와 주거형 오피스텔 987실이 들어섭니다. <span class="mark">이번 청약은 아파트 868가구이고 분양가상한제가 적용됩니다.</span> 입주자모집공고는 10월 22일에 나왔고 특별공급은 다음 주 월요일 11월 2일입니다.</p>

  <h3>청라 아크원 푸르지오 868가구, 일반공급은 354</h3>
  <div class="chart" data-img="카드뉴스 2번 · 868가구 중 일반공급은 354">
    <h3>아파트 공급 구성 (가구)</h3>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill gray" style="width:59.2%">514</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill" style="width:40.8%">354</div></div></div>
    <p class="cap">청약 정리 자료의 공고 수치입니다. 막대 길이는 아파트 868가구를 100으로 맞췄습니다. 주택형은 84㎡ 620가구, 103㎡ 248가구입니다.</p>
  </div>
  <p>868가구 가운데 514가구가 특별공급입니다. <span class="mark">통장 가점으로 겨루는 일반공급은 354가구로, 전체의 10채 중 4채 꼴입니다.</span> 신혼부부·생애최초·다자녀 같은 특별공급 자격이 있다면 11월 2일이 첫 기회입니다. 주택형은 84㎡가 620가구로 대부분이고 103㎡가 248가구입니다.</p>

  <h3>청라 아크원 푸르지오 청약 일정: 특공 11월 2일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 특공 11월 2일, 당첨 11월 10일">
    <h3>남은 일정</h3>
    <h4>견본주택 개관</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.30</span>
      <span class="desc">오늘입니다.</span></div>
    <h4>특별공급 · 1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.2~3</span>
      <span class="desc">월요일 특공, 화요일 1순위.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.10</span>
      <span class="desc">계약은 11월 22~24일.</span></div>
    <p class="cap">아시아타임즈·시대일보(2026-10-29) 보도와 청약 정리 자료 기준입니다. 2순위 날짜와 세부 시간은 청약홈 입주자모집공고로 확인하십시오.</p>
  </div>
  <p>견본주택은 오늘부터 주말까지 사흘이 사실상 둘러볼 수 있는 시간입니다. <span class="mark">월요일에 바로 특별공급이 열리므로, 특공을 노린다면 이번 주말 안에 청약홈에서 자격과 통장 상태를 확인해 두는 편이 안전합니다.</span> 당첨자 발표는 11월 10일, 계약은 11월 22~24일입니다.</p>

  <h3>분양가, 84㎡ 8억3,780만~9억2,070만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡ 8억3,780만~9억2,070만원">
    <h3>주택형별 분양가 범위 (만원)</h3>
    <div class="bar"><label>103㎡ 최고</label>
      <div class="rail"><div class="fill gray" style="width:100%">117,100</div></div></div>
    <div class="bar"><label>103㎡ 최저</label>
      <div class="rail"><div class="fill gray" style="width:93.0%">108,880</div></div></div>
    <div class="bar"><label>84㎡ 최고</label>
      <div class="rail"><div class="fill" style="width:78.6%">92,070</div></div></div>
    <div class="bar"><label>84㎡ 최저</label>
      <div class="rail"><div class="fill" style="width:71.5%">83,780</div></div></div>
    <p class="cap">청약 정리 자료의 공고 분양가 범위입니다. 하한값은 자료마다 차이가 있어(한 자료는 최저 9억50만원으로 표기) 동·호수별 확정 금액은 입주자모집공고로 확인하십시오. 막대는 최고가 11억7,100만원을 100으로 맞췄습니다.</p>
  </div>
  <p>84㎡는 8억 중반에서 9억 초반, 103㎡는 10억 후반에서 11억 후반입니다. <span class="mark">분양가상한제가 적용된 가격이라는 점이 이 단지의 핵심이지만, 주변 청라 기존 아파트보다 비싸다는 평가도 함께 나왔습니다.</span> 층과 향에 따라 같은 84㎡라도 8천만원 넘게 차이 나므로, 견본주택에서 원하는 동의 가격표를 먼저 받아 보십시오.</p>

  <h3>청라 아크원 푸르지오 계약금 5%, 인천 거주 50% 우선</h3>
  <div class="chart" data-img="카드뉴스 5번 · 계약금 5%, 인천 거주 50% 우선">
    <h3>돈과 자격, 먼저 볼 것</h3>
    <h4>계약금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">5%</span>
      <span class="desc">84㎡면 약 4,189만~4,604만원.</span></div>
    <h4>중도금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">60%</span>
      <span class="desc">대출 조건은 공고문으로.</span></div>
    <h4>지역 우선</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">50%</span>
      <span class="desc">인천 거주자 우선, 서울·경기도 가능.</span></div>
    <p class="cap">계약금·중도금 비율과 지역 배정은 보도 기준입니다. 계약금 금액은 84㎡ 분양가 범위에 5%를 곱해 반올림한 값입니다. 전매제한·실거주 의무 기간은 입주자모집공고에서 확인하십시오.</p>
  </div>
  <p>계약금이 분양가의 5%라 84㎡ 기준 4천만원대로 계약할 수 있습니다. <span class="mark">물량의 절반은 인천 거주자에게 먼저 돌아가고, 남은 물량에서 서울·경기 거주자가 함께 경쟁합니다.</span> 분양가상한제 단지는 전매제한과 실거주 의무가 붙는 경우가 많은데, 이 단지의 기간은 보도에서 확인하지 못했으므로 공고문 해당 조항을 꼭 읽으십시오.</p>

  <h3>청라 아크원 푸르지오 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 청라 아크원 푸르지오 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="arw1030-06-tips.png" src="../images/cards/report/arw1030-06-tips.png" alt="체크포인트 카드 · 1. 특공 자격과 통장, 2. 동·호수별 분양가표, 3. 전매제한·실거주 의무 조항" loading="lazy" width="1080" height="1080">
    <figcaption>청라 아크원 푸르지오 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>특공 자격과 통장 확인</strong>. 특별공급은 11월 2일, 1순위는 3일입니다.</li>
    <li><strong>동·호수별 분양가표</strong>. 84㎡도 최저와 최고가 8천만원 넘게 차이 납니다.</li>
    <li><strong>전매제한·실거주 의무 조항</strong>. 분양가상한제 단지라 공고문에서 기간을 확인합니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>청라 아크원 푸르지오</strong>는 오늘 10월 30일 견본주택을 열고 11월 2일 특별공급, 3일 1순위 청약을 받습니다. 아파트 868가구 가운데 일반공급은 354가구이고, 84㎡ 분양가는 8억3,780만~9억2,070만원 선입니다. <span class="mark">당첨자 발표는 11월 10일, 계약은 11월 22~24일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 공급 구성과 일정은 10월 보도와 청약 정리 자료 기준이며 입주자모집공고 원문은 직접 확인하지 못했습니다. 분양가 하한, 2순위 날짜, 전매제한·실거주 의무 기간, 중도금 대출 조건은 청약홈 입주자모집공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 아시아타임즈 "청라국제업무단지에 청라 아크원 푸르지오 1855가구 공급"(2026-10-02) · 아시아타임즈 "청라 아크원 푸르지오, 30일 견본주택 개관"(2026-10-29) · 시대일보(2026-10-29) · 뉴시스(2026-10-02) · 소비자가 만드는 신문 분양현장 톺아보기 · 머니투데이 10월 마지막주 분양 일정(2026-10-25) · 청약홈<br>
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
assert 868 + 987 == 1855 and 514 + 354 == 868 and 620 + 248 == 868
assert round(987 / 1855 * 86, 1) == 45.8 and round(868 / 1855 * 86, 1) == 40.2 and round(354 / 1855 * 86, 1) == 16.4
assert round(514 / 868 * 100, 1) == 59.2 and round(354 / 868 * 100, 1) == 40.8
assert round(108880 / 117100 * 100, 1) == 93.0 and round(92070 / 117100 * 100, 1) == 78.6 and round(83780 / 117100 * 100, 1) == 71.5
assert round(83780 * 0.05) == 4189 and round(92070 * 0.05) == 4604
KW = "청라 아크원 푸르지오"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("청라아크원푸르지오")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
