# -*- coding: utf-8 -*-
"""리포트 #118 (2026-11-07) 광교 지분적립형 특공 D-2. #117을 복제해 교체한다.

메인 검색어: 광교 지분적립형

수치와 검산
  사건일과 오늘의 간격: 특별공급 접수 11/9(월) → 2일 뒤(D-2). 공고 10/30(8일 전)은 배경.
  분당신문·아시아경제(11/4)·이투데이·경기일보(10/30): 광교 A17블록 600가구 = 59㎡ 지분적립형 240 + 84㎡ 일반 공공분양 360.
    특공 11/9 · 1순위 11/10 · 2순위 11/11 · 당첨 11/18 · 계약 2027-01-25~27 · 입주 2029년 10월. 청약홈.
    지분적립형: 분양가 25% 먼저 취득, 나머지 75% 20년에 걸쳐 단계 취득, GH 지분에 임대료(보증금) 별도.
    59㎡ 최고 공급가 6억6,790만~6억8,590만(다른 보도 하한 6억3,450만) → 25% 약 1억6,700만~1억7,150만.
    84㎡ 9억150만~9억4,930만. 거주의무 5년 · 전매제한 10년. 계약 10% · 입주 15%.
  프레시안·국토교통뉴스(7/5): 240가구 중 특공 168(70%), 청년 36 · 신생아 48. → 일반 72.
단정하지 않은 것
  · 지분 추가 취득 주기(4년 주기는 한 보도뿐) · 임대료 금액 · 분양가 하한(보도마다 다름) · 소득·자산 기준
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-06-redev-center.html"
SLUG, PRE = "2026-11-07-gwanggyo-equity", "gk1107"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 118, "2026-11-07"
PREV_SLUG = "rc1106-"
BANNED = ["통합지원센터", "개포주공", "김이탁"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "광교 지분적립형 월요일 특공, 1억7천으로 시작"
DESC = ("광교 지분적립형 분양주택 청약이 11월 9일 특별공급으로 시작합니다. 경기주택도시공사(GH)가 광교 A17블록에 내놓은 전국 첫 지분적립형 240가구(59㎡)로, "
        "분양가의 25%만 먼저 내고 나머지 75%는 20년에 걸쳐 나눠 삽니다. 59㎡ 최고 6억8,590만원 기준 첫 지분은 약 1억7,150만원입니다.")
HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="분양가 25%로 입주, 나머지는 20년에 걸쳐. 특공 11월 9일, 1순위 10일, 당첨 18일입니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">광교 지분적립형<br>월요일 특공, 1억7천으로 시작</h1>
  <p class="sub"><strong>광교 지분적립형</strong> 분양주택 청약이 <strong>11월 9일(월) 특별공급</strong>으로 시작합니다. 전국에서 처음 나오는 지분적립형 <strong>240가구(59㎡)</strong>입니다. 분양가의 <strong>25%</strong>만 먼저 사고 나머지는 20년에 걸쳐 나눠 삽니다. <span class="mark">1순위는 10일, 당첨 발표는 18일입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 특별공급</div><div class="kw">11월 9일</div>
      <p>1순위 <strong>10일</strong>, 2순위 11일.</p></div>
    <div class="kcard"><div class="hot">첫 지분</div><div class="kw">25%</div>
      <p>나머지 75%는 <strong>20년</strong>에 걸쳐.</p></div>
    <div class="kcard"><div class="hot">59㎡ 최고가 기준</div><div class="kw">1억7,150만</div>
      <p>6억8,590만원의 <strong>25%</strong>.</p></div>
    <div class="kcard"><div class="hot">당첨 발표</div><div class="kw">11월 18일</div>
      <p>계약은 <strong>2027년 1월</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>광교 A17블록 공급 구성 (가구)</h3>
    <span class="badge">총 600가구</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:40.1%">168</div><div class="barv" style="--h:40.1%"></div></div>
      <div class="col"><div class="v" style="--h:17.2%">72</div><div class="barv" style="--h:17.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:86%">360</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>지분적립형 특공</span><span>지분적립형 일반</span><span>84㎡ 일반분양</span></div>
    <p class="cap">지분적립형은 전용 59㎡ 240가구(특공 168 · 일반 72), 나머지 360가구는 전용 84㎡ 일반 공공분양입니다(경기도 7월 5일 발표, GH 공고 보도). 막대 높이는 360가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 광교 지분적립형 월요일 특공, 1억7천으로 시작"),
    ("02-how", "광교 지분적립형, 25% 먼저 사고 나머지는 20년"),
    ("03-when", "광교 지분적립형 청약 일정, 9일 특공부터"),
    ("04-price", "59㎡ 최고 6억8,590만원, 첫 지분은 1억7,150만원"),
    ("05-supply", "240가구 중 168가구가 특별공급"),
    ("06-check", "광교 지분적립형 넣기 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="광교지분적립형,지분적립형분양주택,광교A17,GH,경기주택도시공사,광교청약,공공분양,청년특별공급,신생아특별공급,수원청약">
  <h2>광교 지분적립형 월요일 특공, 1억7천으로 시작</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 광교 지분적립형 월요일 특공, 1억7천으로 시작"></span>

  <p>광교 지분적립형 분양주택 청약이 이번 주 월요일(11월 9일) 특별공급으로 시작합니다. 경기주택도시공사(GH)가 수원 광교 A17블록에 내놓은 전국 첫 지분적립형 240가구입니다. <span class="mark">집값의 25%만 먼저 내고 들어가 살면서, 나머지 75%는 20년에 걸쳐 나눠 사는 방식입니다.</span></p>

  <h3>광교 지분적립형, 25% 먼저 사고 나머지는 20년</h3>
  <div class="chart" data-img="카드뉴스 2번 · 광교 지분적립형, 25% 먼저 사고 나머지는 20년">
    <h3>지분적립형은 이렇게 산다</h3>
    <h4>입주할 때</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">25%</span>
      <span class="desc">분양가의 25% 지분을 먼저 산다. 계약 때 10%, 입주 때 15%로 나눠 낸다.</span></div>
    <h4>살면서</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">20년</span>
      <span class="desc">나머지 75%를 단계적으로 사들인다. 추가 지분 값은 최초 공급가에 기간이자를 더해 정한다.</span></div>
    <h4>그동안</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">임대료</span>
      <span class="desc">GH가 가진 지분만큼 임대보증금이나 월 임대료를 낸다.</span></div>
    <p class="cap">분당신문·이투데이·아시아경제(10월 30일~11월 4일) 보도 기준입니다. 지분을 사는 주기와 임대료 금액은 입주자모집공고문으로 확인해야 합니다.</p>
  </div>
  <p>일반 분양은 분양가 전부를 잔금 때까지 마련해야 합니다. 지분적립형은 첫 지분 25%만 있으면 입주할 수 있습니다. 대신 공공(GH)이 가진 75%에 대해 임대보증금이나 월 임대료를 내고, 정해진 시점마다 지분을 더 사서 20년 뒤 100%를 채웁니다. 보도된 기본 임대보증금은 약 3억2,900만~3억3,000만원입니다. <span class="mark">초기 목돈은 줄지만 공짜 집이 아니라 '나눠 사는 집'이라는 점을 먼저 이해해야 합니다.</span></p>

  <h3>광교 지분적립형 청약 일정, 9일 특공부터</h3>
  <div class="chart" data-img="카드뉴스 3번 · 광교 지분적립형 청약 일정, 9일 특공부터">
    <h3>날짜로 보면</h3>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 9일</span>
      <span class="desc">월요일. 청년·신생아·신혼부부 등 특공 접수, 청약홈.</span></div>
    <h4>일반공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10~11일</span>
      <span class="desc">10일 1순위, 11일 2순위.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 18일</span>
      <span class="desc">계약은 2027년 1월 25~27일, 입주는 2029년 10월 예정.</span></div>
    <p class="cap">입주자모집공고(10월 30일) 보도 기준입니다. 견본주택은 주말 동안 오후 8시까지 연장 운영한다고 GH가 밝혔습니다.</p>
  </div>
  <p>접수는 한국부동산원 청약홈에서 받습니다. 특공 다음 날 바로 1순위가 이어지므로 특공과 일반 중 무엇을 넣을지 주말에 정해 두는 편이 좋습니다. <span class="mark">당첨자 발표는 18일이고 계약은 내년 1월 말이라, 계약금 10%를 마련할 시간은 두 달 남짓 있습니다.</span></p>

  <h3>59㎡ 최고 6억8,590만원, 첫 지분은 1억7,150만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 59㎡ 최고 6억8,590만원, 첫 지분은 1억7,150만원">
    <h3>최고 공급가와 첫 지분 (만원)</h3>
    <div class="bar"><label>84㎡ 일반분양 최고</label>
      <div class="rail"><div class="fill gray" style="width:100%">94,930</div></div></div>
    <div class="bar"><label>59㎡ 지분적립형 최고</label>
      <div class="rail"><div class="fill" style="width:72.3%">68,590</div></div></div>
    <div class="bar"><label>59㎡ 첫 지분 25%</label>
      <div class="rail"><div class="fill" style="width:18.1%"></div><span class="railval">17,150</span></div></div>
    <p class="cap">공급가는 이투데이·국제뉴스 보도 기준이며, 59㎡ 하한은 보도마다 6억3,450만원과 6억6,790만원으로 다릅니다. 첫 지분은 최고가의 25%로 계산해 반올림했습니다. 막대 길이는 9억4,930만원을 기준으로 맞췄습니다.</p>
  </div>
  <p>같은 단지 84㎡ 일반 공공분양은 9억150만~9억4,930만원입니다. 59㎡ 지분적립형은 최고 6억8,590만원이고, 이 값의 25%가 약 1억7,150만원입니다. <span class="mark">광교에서 1억원대 후반으로 새 아파트에 들어갈 수 있다는 점이 이 상품의 핵심입니다.</span> 다만 거주의무 5년, 전매제한 10년이 붙습니다.</p>

  <h3>240가구 중 168가구가 특별공급</h3>
  <span class="imgslot" hidden data-img="카드뉴스 5번 · 240가구 중 168가구가 특별공급"></span>
  <p>지분적립형 240가구 중 168가구(70%)가 특별공급입니다. 경기도 건의로 청년 특별공급 36가구가 새로 생겼고 신생아 특별공급이 48가구입니다. 일반공급은 72가구뿐입니다. 청년 특공은 만 19~39세 미혼이 대상이며 신청자 본인의 무주택 여부로 판단합니다. <span class="mark">무주택 청년이라면 일반보다 특공 쪽 문이 더 넓습니다.</span></p>

  <h3>광교 지분적립형 넣기 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 광교 지분적립형 넣기 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="gk1107-06-check.png" src="../images/cards/report/gk1107-06-check.png" alt="체크포인트 카드 · 1. 임대료까지 계산했나, 2. 5년 거주·10년 전매, 3. 소득·자산 기준은 공고문으로" loading="lazy" width="1080" height="1080">
    <figcaption>광교 지분적립형 청약 전에 확인할 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>임대료까지 계산했나</strong>. 첫 지분 1억7천만원대 말고도 GH 지분에 대한 임대보증금·임대료, 그리고 앞으로 사들일 지분 값이 있습니다. 공고문의 납부 표로 20년 총액을 확인하십시오.</li>
    <li><strong>5년 거주, 10년 전매제한</strong>. 당첨되면 5년은 직접 살아야 하고 10년 동안 팔 수 없습니다.</li>
    <li><strong>소득·자산 기준은 공고문으로</strong>. 공급 유형마다 기준이 다릅니다. 청약홈의 입주자모집공고문과 GH 안내로 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>광교 지분적립형</strong> 분양주택은 광교 A17블록 59㎡ 240가구로, 11월 9일 특별공급, 10일 1순위, 11일 2순위 접수 뒤 18일 당첨자를 발표합니다. 분양가의 25%(최고가 기준 약 1억7,150만원)로 입주하고 나머지는 20년에 걸쳐 사들이며, 그동안 GH 지분에 임대료를 냅니다. 168가구가 특별공급입니다. <span class="mark">거주의무 5년, 전매제한 10년이 붙으니 오래 살 집으로 보고 넣으십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 일정·공급가는 분당신문·아시아경제(2026-11-04), 이투데이·경기일보(2026-10-30), 국제뉴스 보도, 특공 배분은 경기도 발표(프레시안·국토교통뉴스 2026-07-05) 기준입니다. 첫 지분 금액은 보도된 최고가의 25%로 계산했습니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 분당신문 광교 지분적립형 240호 11월 9일부터 청약(2026-11-04) · 아시아경제 GH 전국 최초 지분적립형 9일부터 청약(2026-11-04) · 이투데이 광교 6억대 아파트 25% 소유로 출발(2026-10-30) · 경기일보 광교 지분적립형 240호 공급(2026-10-30) · 국제뉴스 광교 분양가 · 프레시안 지분적립형 청년 특별공급 신설(2026-07-05)<br>
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
assert 240 + 360 == 600 and 168 + 72 == 240 and round(168 / 240 * 100) == 70
assert round(168 / 360 * 86, 1) == 40.1 and round(72 / 360 * 86, 1) == 17.2
assert round(68590 * 0.25, -1) == 17150 and round(66790 * 0.25 / 100) == 167
assert round(68590 / 94930 * 100, 1) == 72.3 and round(17150 / 94930 * 100, 1) == 18.1
KW = "광교 지분적립형"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("광교지분적립형")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
