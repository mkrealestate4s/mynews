# -*- coding: utf-8 -*-
"""리포트 #113 (2026-11-02) 계양 카이브 유보라 특별공급 접수일. #112를 복제해 교체한다.

메인 검색어: 계양 카이브 유보라

수치와 검산
  사건일과 오늘의 간격: 특별공급 11/2(오늘) → 0일. 1순위 11/3(D-1).
  보도: 반도건설 · 인천 계양신도시 AC3 614 + AC4 496 = 1,110가구 · 전용 84·92·93㎡
    · 특공 AC3 353·AC4 285 = 638, 일반 AC3 261·AC4 211 = 472 (청약 정리 자료, 공고문 대조 필요)
    · 특공 11/2 · 1순위 11/3 · 2순위 11/4 · 당첨 AC3 11/10 · AC4 11/11 · 계약 11/23~25 · 입주 2029년 8월
    · 분양가상한제 · 3.3㎡당 2,400만원 · 84㎡ 7억3,100만~8억1,850만(아시아타임즈) · 정리 자료 최고 9억1,200만(당근부동산)
    · 비규제지역, 수도권 거주 만 19세 이상 1순위 가능 · 계약금 5% · 두 블록 발표일이 달라 중복 청약 가능(보도)
  대시보드 세로 (1,110 → 86%): 614 → 47.6 · 496 → 38.4 · 472 → 36.6
  가로 공급 (1,110 → 100%): 638 → 57.5 · 472 → 42.5
  가로 분양가 (9억1,200만 → 100%): 8억1,850만 → 89.7 · 7억3,100만 → 80.2
  계약금 5%: 7억3,100만 → 3,655만 · 8억1,850만 → 4,092.5만 (본문은 약 3,660만~4,090만원)

단정하지 않은 것
  · 타입별 세대수·분양가 하한 · 전매제한·실거주 의무 · 중복 청약 허용 여부 · 중도금 조건 → 입주자모집공고 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-01-mokdong9.html"
SLUG, PRE = "2026-11-02-gyeyang-caive", "gcv1102"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 113, "2026-11-02"
PREV_SLUG = "mk9-"
BANNED = ["목동"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "계양 카이브 유보라 오늘 특공, 84㎡ 7억대"
DESC = ("계양 카이브 유보라가 오늘(11월 2일) 특별공급 접수를 받습니다. 인천 계양신도시 첫 민간분양으로 AC3·AC4 두 블록 1,110가구이며 "
        "분양가상한제가 적용돼 84㎡가 7억3,100만~8억1,850만원 선으로 보도됐습니다. 1순위는 11월 3일, 당첨 발표는 10일(AC3)·11일(AC4)입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="계양신도시 첫 민간분양 1,110가구. 특공 11월 2일, 1순위 3일. 84㎡ 7억3,100만~8억1,850만원.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">계양 카이브 유보라,<br>오늘 특별공급</h1>
  <p class="sub"><strong>계양 카이브 유보라</strong>가 <strong>오늘(11월 2일)</strong> 특별공급 접수를 받습니다. 인천 계양신도시 첫 민간분양으로 <strong>1,110가구</strong>, 분양가상한제 단지입니다. <span class="mark">1순위는 내일 11월 3일입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 오늘</div><div class="kw">11월 2일</div>
      <p><strong>특별공급</strong> 접수.</p></div>
    <div class="kcard"><div class="hot">총 공급</div><div class="kw">1,110가구</div>
      <p>AC3 <strong>614</strong> · AC4 <strong>496</strong>.</p></div>
    <div class="kcard"><div class="hot">84㎡ 분양가</div><div class="kw">7억대~8억대</div>
      <p><strong>분양가상한제</strong> 적용.</p></div>
    <div class="kcard"><div class="hot">다음 단계</div><div class="kw">11월 3일</div>
      <p><strong>1순위</strong>, 4일 2순위.</p></div>
  </div>

  <div class="colchart">
    <h3>계양 카이브 유보라 공급 구성 (가구)</h3>
    <span class="badge">10월 보도</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">1,110</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:47.6%">614</div><div class="barv" style="--h:47.6%"></div></div>
      <div class="col dim"><div class="v" style="--h:38.4%">496</div><div class="barv" style="--h:38.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:36.6%">472</div><div class="barv" style="--h:36.6%"></div></div>
    </div>
    <div class="collbl"><span>전체</span><span>AC3블록</span><span>AC4블록</span><span>일반공급</span></div>
    <p class="cap">서울경제·헤럴드경제(2026-10월) 보도와 청약 정리 자료 수치입니다. 일반공급 472가구는 AC3 261, AC4 211을 더한 값입니다. 막대 길이는 전체 1,110가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 계양 카이브 유보라, 오늘 특별공급"),
    ("02-supply", "1,110가구 중 일반공급은 472"),
    ("03-date", "특공 11월 2일, 1순위 3일"),
    ("04-price", "84㎡ 7억3,100만~8억1,850만원"),
    ("05-rule", "수도권 누구나 1순위, 계약금 5%"),
    ("06-tips", "계양 카이브 유보라 청약 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="계양카이브유보라,카이브유보라,계양신도시카이브유보라,계양카이브유보라분양가,계양신도시,계양신도시분양,인천분양,분양가상한제,아파트청약,11월청약">
  <h2>계양 카이브 유보라, 오늘 특별공급</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 계양 카이브 유보라, 오늘 특별공급"></span>

  <p>계양 카이브 유보라가 오늘(11월 2일) 특별공급 접수를 받습니다. 반도건설이 인천 계양신도시 AC3·AC4 두 블록에 짓는 단지로, 계양신도시에서 처음 나오는 민간분양 아파트입니다. <span class="mark">AC3 614가구, AC4 496가구를 합쳐 1,110가구이고 분양가상한제가 적용됩니다.</span> 전용면적은 84·92·93㎡로 중대형 위주입니다. 1순위는 내일 11월 3일입니다.</p>

  <h3>계양 카이브 유보라 1,110가구, 일반공급은 472</h3>
  <div class="chart" data-img="카드뉴스 2번 · 1,110가구 중 일반공급은 472">
    <h3>공급 구성 (가구)</h3>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill gray" style="width:57.5%">638</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill" style="width:42.5%">472</div></div></div>
    <p class="cap">청약 정리 자료의 블록별 수치(AC3 특공 353·일반 261, AC4 특공 285·일반 211)를 더한 값입니다. 막대 길이는 1,110가구를 100으로 맞췄습니다. 타입별 세대수는 입주자모집공고로 확인하십시오.</p>
  </div>
  <p>1,110가구 가운데 638가구가 특별공급입니다. <span class="mark">통장 가점과 추첨으로 겨루는 일반공급은 472가구로, 10채 중 4채 꼴입니다.</span> 신혼부부·생애최초·다자녀 같은 특별공급 자격이 있다면 오늘이 기회입니다. 블록별로는 AC3에서 일반 261가구, AC4에서 일반 211가구가 나옵니다.</p>

  <h3>계양 카이브 유보라 청약 일정: 1순위 11월 3일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 특공 11월 2일, 1순위 3일">
    <h3>남은 일정</h3>
    <h4>특별공급 · 1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.2~3</span>
      <span class="desc">오늘 특공, 내일 1순위.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.10~11</span>
      <span class="desc">AC3 10일, AC4 11일.</span></div>
    <h4>계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.23~25</span>
      <span class="desc">입주는 2029년 8월 예정.</span></div>
    <p class="cap">파이낸셜뉴스(2026-10-30)·월요신문 보도와 청약 정리 자료 기준입니다. 2순위는 11월 4일입니다. 세부 시간은 청약홈 입주자모집공고로 확인하십시오.</p>
  </div>
  <p>특별공급은 오늘 하루, 1순위는 내일, 2순위는 11월 4일입니다. <span class="mark">두 블록의 당첨자 발표일이 하루 차이(10일·11일)라 AC3와 AC4에 함께 청약할 수 있다고 보도됐습니다.</span> 다만 특별공급 일부 유형(기관추천 등)은 블록 간 중복 신청이 안 된다는 안내도 있으므로, 내 유형의 중복 허용 여부는 공고문에서 확인하십시오.</p>

  <h3>분양가, 84㎡ 7억3,100만~8억1,850만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡ 7억3,100만~8억1,850만원">
    <h3>분양가 범위 (만원)</h3>
    <div class="bar"><label>정리 자료 최고</label>
      <div class="rail"><div class="fill gray" style="width:100%">91,200</div></div></div>
    <div class="bar"><label>84㎡ 최고</label>
      <div class="rail"><div class="fill" style="width:89.7%">81,850</div></div></div>
    <div class="bar"><label>84㎡ 최저</label>
      <div class="rail"><div class="fill" style="width:80.2%">73,100</div></div></div>
    <p class="cap">84㎡ 범위는 아시아타임즈(2026-10-22) 보도, 최고 9억1,200만원은 당근부동산 청약 정보 표기입니다. 자료마다 하한·상한이 조금씩 달라 동·호수별 확정 금액은 입주자모집공고로 확인하십시오. 막대는 9억1,200만원을 100으로 맞췄습니다.</p>
  </div>
  <p>3.3㎡당 분양가는 2,400만원 선으로 보도됐습니다. <span class="mark">84㎡는 7억 초중반에서 8억 초반, 92·93㎡를 포함하면 최고 9억 초반까지 올라갑니다.</span> 분양가상한제가 적용된 가격이지만 계양구 기존 아파트 시세와는 직접 비교해 보는 편이 좋습니다. 같은 84㎡라도 층과 향에 따라 8천만원 넘게 차이 납니다.</p>

  <h3>계양 카이브 유보라 1순위 자격, 수도권 누구나</h3>
  <div class="chart" data-img="카드뉴스 5번 · 수도권 누구나 1순위, 계약금 5%">
    <h3>자격과 돈, 먼저 볼 것</h3>
    <h4>1순위 지역</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">수도권</span>
      <span class="desc">비규제지역, 만 19세 이상.</span></div>
    <h4>계약금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">5%</span>
      <span class="desc">84㎡면 약 3,660만~4,090만원.</span></div>
    <h4>입주</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2029.8</span>
      <span class="desc">예정 시점입니다.</span></div>
    <p class="cap">1순위 자격·계약금 비율은 보도 기준입니다. 계약금은 84㎡ 분양가 범위에 5%를 곱해 반올림한 값입니다. 해당 지역 거주자 우선 배정 비율, 전매제한·실거주 의무 기간은 입주자모집공고에서 확인하십시오.</p>
  </div>
  <p>계양구는 비규제지역이라 청약 요건을 갖춘 수도권 거주 만 19세 이상이면 1순위로 청약할 수 있다고 보도됐습니다. <span class="mark">계약금이 분양가의 5%라 84㎡ 기준 3천만원대 후반에서 4천만원 정도로 계약할 수 있습니다.</span> 인천 거주자 우선 배정 비율과 분양가상한제에 따르는 전매제한·실거주 의무 기간은 보도에서 확인하지 못했으므로 공고문 해당 조항을 꼭 읽으십시오.</p>

  <h3>계양 카이브 유보라 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 계양 카이브 유보라 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="gcv1102-06-tips.png" src="../images/cards/report/gcv1102-06-tips.png" alt="체크포인트 카드 · 1. 블록 중복 청약 가능 여부, 2. 동·호수별 분양가표, 3. 전매제한·실거주 의무 조항" loading="lazy" width="1080" height="1080">
    <figcaption>계양 카이브 유보라 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>AC3·AC4 중복 청약 가능 여부</strong>. 발표일이 다르지만 내 유형의 허용 여부를 공고문으로 확인합니다.</li>
    <li><strong>동·호수별 분양가표</strong>. 84㎡도 최저와 최고가 8천만원 넘게 차이 납니다.</li>
    <li><strong>전매제한·실거주 의무 조항</strong>. 분양가상한제 단지라 공고문에서 기간을 확인합니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>계양 카이브 유보라</strong>는 오늘 11월 2일 특별공급, 내일 3일 1순위, 4일 2순위 청약을 받습니다. 계양신도시 첫 민간분양으로 1,110가구이고, 84㎡ 분양가는 7억3,100만~8억1,850만원 선입니다. <span class="mark">당첨자 발표는 AC3 11월 10일, AC4 11일, 계약은 11월 23~25일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 공급 구성과 일정은 10월 보도와 청약 정리 자료 기준이며 입주자모집공고 원문은 직접 확인하지 못했습니다. 타입별 세대수, 분양가 하한, 블록 간 중복 청약 허용 범위, 전매제한·실거주 의무 기간, 중도금 대출 조건은 청약홈 입주자모집공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 파이낸셜뉴스 "계양신도시 카이브 유보라, 전용 84~93㎡ 중대형 공급… 2일 특공 접수"(2026-10-30) · 아시아타임즈 "계양신도시 민간분양 본격화"(2026-10-22) · 월요신문 · 서울경제 · 헤럴드경제 · 딜사이트 · 당근부동산 청약 정보 · 이투데이·뉴스1 11월 첫째 주 분양캘린더 · 청약홈<br>
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
assert 614 + 496 == 1110 and 353 + 285 == 638 and 261 + 211 == 472 and 638 + 472 == 1110
assert round(614 / 1110 * 86, 1) == 47.6 and round(496 / 1110 * 86, 1) == 38.4 and round(472 / 1110 * 86, 1) == 36.6
assert round(638 / 1110 * 100, 1) == 57.5 and round(472 / 1110 * 100, 1) == 42.5
assert round(81850 / 91200 * 100, 1) == 89.7 and round(73100 / 91200 * 100, 1) == 80.2
assert round(73100 * 0.05) == 3655
KW = "계양 카이브 유보라"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("계양카이브유보라")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
