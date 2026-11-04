# -*- coding: utf-8 -*-
"""리포트 #116 (2026-11-05) 서울 아파트 매물 8만건 돌파. #115를 복제해 교체한다.

메인 검색어: 서울 아파트 매물

수치와 검산
  사건일과 오늘의 간격: 아실 집계 11/4 기준 · 보도 11/4(어제) → 1일.
  아실(국민일보·여성신문·서울신문 11/4 보도): 서울 아파트 매물 8/3 60,409 → 9월 말 72,099 → 11/4 80,430 (+20,021, +33.1%)
  강남3구 22,182 → 29,802 (+34.4%) · 서초 7,630→10,502 (+2,872) · 강남 9,453→12,126 (+2,673) · 송파 5,099→7,174 (+2,075)
  성북구 증가율 61.1%(25개 구 중 최고) · 강남3구 외 22개 구 +32.4%
  서울부동산정보광장: 9월 서울 아파트 매매 3,431건(9개월 만의 최저)
  서울신문: 강남3구는 가격 낮춘 매물, 성북·서대문·노원은 상승 거래
단정하지 않은 것
  · 8·3 세제 개편안의 세부 내용과 매물 증가의 인과(보도 표현만 인용)
  · 매물 건수는 중개 플랫폼 등록 기준(실거래 아님, 중복 등록 가능)
  · 개인 세금 → 국세청·세무사 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-04-garak-woosung1.html"
SLUG, PRE = "2026-11-05-seoul-listings", "sl1105"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 116, "2026-11-05"
PREV_SLUG = "gw1104-"
BANNED = ["가락우성", "대우건설", "쌍문한양"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "서울 아파트 매물 8만건, 우리 구는 얼마나 늘었나"
DESC = ("서울 아파트 매물이 11월 4일 기준 8만430건으로 올해 가장 많습니다(아실). 8월 3일 6만409건에서 석 달 새 2만21건(33.1%) 늘었습니다. "
        "서초구가 2,872건으로 가장 많이 늘었고 증가율은 성북구가 61.1%로 가장 높았습니다. 9월 거래는 3,431건으로 9개월 만의 최저입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="석 달 새 2만건 늘어 8만430건. 서초 +2,872건, 성북 +61.1%. 팔려는 집은 늘고 거래는 줄었습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">서울 아파트 매물 8만건,<br>우리 구는 얼마나 늘었나</h1>
  <p class="sub"><strong>서울 아파트 매물</strong>이 <strong>11월 4일</strong> 기준 <strong>8만430건</strong>으로 올해 가장 많습니다. 8월 3일 세제 개편안 발표 날보다 <strong>2만21건(33.1%)</strong> 늘었습니다. <span class="mark">서초구가 건수로, 성북구가 비율로 가장 많이 늘었습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 서울 매물</div><div class="kw">8만430건</div>
      <p>11월 4일, <strong>올해 최다</strong>.</p></div>
    <div class="kcard"><div class="hot">석 달 증가</div><div class="kw">+33.1%</div>
      <p>8월 3일보다 <strong>2만21건</strong>.</p></div>
    <div class="kcard"><div class="hot">서초구</div><div class="kw">+2,872건</div>
      <p>건수로 <strong>가장 많이</strong>.</p></div>
    <div class="kcard"><div class="hot">성북구</div><div class="kw">+61.1%</div>
      <p>비율로 <strong>가장 많이</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>서울 아파트 매물 건수 추이 (건)</h3>
    <span class="badge">석 달 +2만21건</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:64.6%">60,409</div><div class="barv" style="--h:64.6%"></div></div>
      <div class="col dim"><div class="v" style="--h:77.1%">72,099</div><div class="barv" style="--h:77.1%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">80,430</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>8월 3일</span><span>9월 말</span><span>11월 4일</span></div>
    <p class="cap">부동산 빅데이터 업체 아실 집계(11월 4일 보도)입니다. 막대 높이는 최댓값 8만430건을 기준으로 맞췄습니다. 중개 플랫폼에 올라온 매물 수라 실제 거래 건수와는 다릅니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 서울 아파트 매물 8만건, 우리 구는 얼마나 늘었나"),
    ("02-trend", "서울 아파트 매물, 석 달 새 2만건 늘었다"),
    ("03-gangnam", "강남3구 매물, 서초가 가장 많이 늘었다"),
    ("04-rate", "증가율은 성북구가 1등, 61.1%"),
    ("05-deal", "매물은 늘고 거래는 9개월 만에 최저"),
    ("06-check", "서울 아파트 매물 볼 때 체크 3가지"),
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

ARTICLE = '''<article data-tags="서울아파트매물,서울아파트,아파트매물,서초구아파트,강남3구,성북구아파트,송파아파트,강남아파트,부동산세제개편,서울집값">
  <h2>서울 아파트 매물 8만건, 우리 구는 얼마나 늘었나</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 서울 아파트 매물 8만건, 우리 구는 얼마나 늘었나"></span>

  <p>서울 아파트 매물이 11월 4일 기준 8만430건으로 올해 들어 가장 많아졌습니다. 부동산 빅데이터 업체 아실 집계를 어제(11월 4일) 여러 언론이 전했습니다. <span class="mark">8월 3일 정부 세제 개편안 발표 날 6만409건이던 것이 석 달 만에 2만21건, 33.1% 늘었습니다.</span></p>

  <h3>서울 아파트 매물, 석 달 새 2만건 늘었다</h3>
  <span class="imgslot" hidden data-img="카드뉴스 2번 · 서울 아파트 매물, 석 달 새 2만건 늘었다"></span>
  <p>흐름을 보면 한 번에 뛴 것이 아니라 꾸준히 쌓였습니다. 8월 3일 6만409건, 9월 말 7만2,099건, 11월 4일 8만430건입니다. 앞의 두 달 남짓 동안 1만1,690건, 그 뒤 한 달여 동안 8,331건이 늘었습니다. 보도들은 세제 개편안 발표 뒤 집을 팔려는 사람이 늘어난 것으로 봅니다. <span class="mark">다만 매물 건수는 중개 플랫폼에 올라온 숫자라 같은 집이 여러 곳에 올라가 있을 수 있고, 실제 거래와는 다릅니다.</span></p>

  <h3>강남3구 서울 아파트 매물, 서초가 가장 많이 늘었다</h3>
  <div class="chart" data-img="카드뉴스 3번 · 강남3구 매물, 서초가 가장 많이 늘었다">
    <h3>강남3구 매물 증가 (8월 3일 → 11월 4일)</h3>
    <h4>서초구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">+2,872</span>
      <span class="desc">7,630건 → 1만502건. 25개 구 중 가장 많이 늘었다.</span></div>
    <h4>강남구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">+2,673</span>
      <span class="desc">9,453건 → 1만2,126건. 매물 수는 가장 많다.</span></div>
    <h4>송파구</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">+2,075</span>
      <span class="desc">5,099건 → 7,174건.</span></div>
    <p class="cap">아실 집계(11월 4일 보도) 기준입니다. 강남3구 합계는 2만2,182건에서 2만9,802건으로 34.4% 늘었습니다.</p>
  </div>
  <p>강남3구 매물은 2만2,182건에서 2만9,802건으로 7,620건 늘었습니다. 서울 전체 증가분(2만21건)의 38%가 세 구에서 나왔습니다. 서울신문은 강남3구에서 값을 크게 낮춘 매물이 나오고 있다고 전했습니다. <span class="mark">매물이 늘면 사는 쪽이 고를 수 있는 폭이 넓어집니다. 다만 호가가 내려간 매물이 곧 실제 거래 가격은 아닙니다.</span></p>

  <h3>증가율은 성북구가 1등, 61.1%</h3>
  <div class="chart" data-img="카드뉴스 4번 · 증가율은 성북구가 1등, 61.1%">
    <h3>8월 3일 대비 매물 증가율 (%)</h3>
    <div class="bar"><label>성북구</label>
      <div class="rail"><div class="fill" style="width:100%">61.1</div></div></div>
    <div class="bar"><label>송파구</label>
      <div class="rail"><div class="fill gray" style="width:66.6%">40.7</div></div></div>
    <div class="bar"><label>서초구</label>
      <div class="rail"><div class="fill gray" style="width:61.5%">37.6</div></div></div>
    <div class="bar"><label>나머지 22개 구</label>
      <div class="rail"><div class="fill gray" style="width:53%">32.4</div></div></div>
    <div class="bar"><label>강남구</label>
      <div class="rail"><div class="fill gray" style="width:46.3%">28.3</div></div></div>
    <p class="cap">모두 같은 기간(8월 3일 → 11월 4일) 증가율이라 한 축에 놓았습니다. 막대 길이는 성북구 61.1%를 기준으로 맞췄습니다. 송파·서초·강남은 보도된 건수로 계산했습니다.</p>
  </div>
  <p>비율로 보면 이야기가 달라집니다. 성북구 매물이 61.1% 늘어 25개 구 가운데 증가율이 가장 높았습니다. 강남3구를 뺀 22개 구도 합쳐서 32.4% 늘어 강남3구(34.4%)와 거의 같았습니다. <span class="mark">매물 증가는 강남만의 일이 아니라 서울 전역에서 함께 나타나고 있습니다.</span> 그런데 서울신문 보도로는 성북·서대문·노원구에서는 오히려 값이 오른 거래가 이어지고 있습니다. 같은 매물 증가라도 동네마다 뜻이 다를 수 있다는 얘기입니다.</p>

  <h3>매물은 늘고 거래는 9개월 만에 최저</h3>
  <div class="chart" data-img="카드뉴스 5번 · 매물은 늘고 거래는 9개월 만에 최저">
    <h3>파는 집과 팔린 집</h3>
    <h4>11월 4일 매물</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">8만430</span>
      <span class="desc">팔려고 내놓은 서울 아파트. 올해 최다.</span></div>
    <h4>9월 매매 거래</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3,431</span>
      <span class="desc">한 달 동안 실제로 팔린 건수. 9개월 만의 최저.</span></div>
    <p class="cap">매물은 한 시점의 쌓인 수, 거래는 한 달 동안의 건수라 단위가 다릅니다. 막대로 비교하지 않고 따로 적었습니다. 거래는 서울부동산정보광장 기준입니다.</p>
  </div>
  <p>내놓은 집은 늘었는데 팔린 집은 줄었습니다. 서울부동산정보광장에 따르면 9월 서울 아파트 매매는 3,431건으로 지난해 12월 이후 가장 적었습니다. 9월 거래는 신고 기한(계약 후 30일)이 지나 대부분 집계된 수치입니다. <span class="mark">파는 쪽과 사는 쪽이 가격을 두고 버티는 구간입니다.</span></p>

  <h3>서울 아파트 매물 볼 때 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 서울 아파트 매물 볼 때 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="sl1105-06-check.png" src="../images/cards/report/sl1105-06-check.png" alt="체크포인트 카드 · 1. 매물 수는 거래가 아니다, 2. 호가와 실거래가는 다르다, 3. 세금은 내 경우로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>서울 아파트 매물 상담에 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>매물 수는 거래가 아니다</strong>. 중개 플랫폼에 올라온 숫자라 같은 집이 여러 번 잡힐 수 있습니다. 흐름을 보는 지표로만 쓰십시오.</li>
    <li><strong>호가와 실거래가는 다르다</strong>. 값을 낮춘 매물이 늘어도 실제로 그 값에 팔렸는지는 국토교통부 실거래가 공개시스템에서 확인하십시오.</li>
    <li><strong>세금은 내 경우로 확인</strong>. 세제 개편안이 나에게 어떻게 적용되는지는 보유 주택 수·지역·보유 기간마다 다릅니다. 국세청 상담이나 세무사에게 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>서울 아파트 매물</strong>은 11월 4일 기준 8만430건으로 8월 3일보다 2만21건(33.1%) 늘었습니다. 서초구(+2,872건)·강남구(+2,673건)·송파구(+2,075건)가 건수로 많이 늘었고, 증가율은 성북구가 61.1%로 가장 높았습니다. 9월 거래는 3,431건으로 9개월 만의 최저입니다. <span class="mark">집을 살 사람에게는 고를 매물이 늘어난 시기지만, 실제 팔린 값은 따로 확인해야 합니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 매물 수는 아실 집계를 전한 국민일보·여성신문·서울신문(2026-11-04) 보도, 거래량은 서울부동산정보광장 기준입니다. 송파·서초·강남 증가율은 보도된 건수로 계산했습니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 국민일보 서울 아파트 매물 8만건 돌파(2026-11-04) · 여성신문 서울 아파트 매물 8만건 넘어(2026-11-04) · 서울신문 쌓이는 서울 아파트 매물 8만건(2026-11-04) · 아실 매물 집계 · 서울부동산정보광장 9월 매매 거래량<br>
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
assert 60409 + 20021 == 80430 and round(20021 / 60409 * 100, 1) == 33.1
assert 7630 + 9453 + 5099 == 22182 and 10502 + 12126 + 7174 == 29802
assert round((29802 - 22182) / 22182 * 100, 1) == 34.4
assert round(12401 / 38227 * 100, 1) == 32.4 and 80430 - 29802 - (60409 - 22182) == 12401
for a, b, r in ((7630, 10502, 37.6), (9453, 12126, 28.3), (5099, 7174, 40.7)):
    assert round((b - a) / a * 100, 1) == r
for v, h in zip((60409, 72099), (64.6, 77.1)):
    assert round(v / 80430 * 86, 1) == h
for v, w in zip((40.7, 37.6, 32.4, 28.3), (66.6, 61.5, 53.0, 46.3)):
    assert round(v / 61.1 * 100, 1) == w
assert 72099 - 60409 == 11690 and 80430 - 72099 == 8331 and round(7620 / 20021 * 100) == 38
KW = "서울 아파트 매물"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("서울아파트매물")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
