# -*- coding: utf-8 -*-
"""리포트 #105 (2026-10-26) 트리븐센텀 1·2단지 청약. #104를 복제해 교체한다.

메인 검색어: 트리븐센텀 청약

수치와 검산
  사건일과 오늘의 간격: 특별공급 10/26(오늘, D-day) · 1순위 10/27 · 주간 분양 보도 10/23 → 3일.
  보도: 부산 해운대구 반여동 · 1단지 852 + 2단지 792 = 1,644세대 · 시공 두산에너빌리티 · 견본주택 10/16 개관
    · 특공 10/26 · 1순위 10/27 · 2순위 10/28 · 계약 11/17~19
    · 2단지 공급금액 6억9,280만~10억1,830만 · 84A 385세대 7억7,200만 · 84B 154세대 7억5,930만
    · 10월 다섯째 주 전국 8곳 5,555가구(리얼투데이) · 아크메르 동탄 1,808 · 신분평 에피트 992
  대시보드 세로 (5,555 → 86%): 1,644 → 25.5 · 852 → 13.2 · 792 → 12.3
  가로 (1,808 → 100%): 1,644 → 90.9 · 992 → 54.9 · 852 → 47.1 · 792 → 43.8
  가로 (10.183억 → 100%): 7.72 → 75.8 · 7.593 → 74.6 · 6.928 → 68.0

단정하지 않은 것
  · 당첨자 발표일: 1단지 11/4·11/5 출처 엇갈림 → "11월 4~5일, 공고문 확인"
  · 1단지 분양가: 출처 신뢰도 낮아 쓰지 않음. 84A 금액도 사이트마다 7억7,200만·7억7,970만 차이 → 확인 안내
  · 중복 청약 가능 여부·규제·전매·계약금 비율: 공고문 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-25-acmer-dongtan.html"
SLUG, PRE = "2026-10-26-trivn-centum", "trv1026"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 105, "2026-10-26"
PREV_SLUG = "akm1025-"
BANNED = ["반송동", "포스코이앤씨", "17억"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "트리븐센텀 청약 오늘 특공, 국평 7억대"
DESC = ("트리븐센텀 청약이 오늘(10월 26일) 특별공급으로 시작합니다. 부산 해운대구 반여동 1·2단지 1,644세대로, "
        "1순위는 27일입니다. 2단지 84㎡A는 7억7,200만원으로 알려졌습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="특별공급 10월 26일, 1순위 27일, 2순위 28일. 계약 11월 17~19일. 1단지 852세대, 2단지 792세대.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">트리븐센텀 청약,<br>오늘 특별공급</h1>
  <p class="sub"><strong>트리븐센텀 1·2단지</strong>가 <strong>10월 26일(월)</strong> 특별공급, 27일 1순위 청약을 받습니다. 부산 해운대구 반여동, 두 단지 합쳐 <strong>1,644세대</strong>입니다. <span class="mark">2단지 84㎡A는 7억7,200만원으로 알려졌습니다. 이번 주 부산에서 가장 큰 청약입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · D-day</div><div class="kw">10월 26일</div>
      <p><strong>특별공급</strong> 접수일.</p></div>
    <div class="kcard"><div class="hot">총 세대</div><div class="kw">1,644세대</div>
      <p>1단지 <strong>852</strong>, 2단지 <strong>792</strong>.</p></div>
    <div class="kcard"><div class="hot">2단지 84㎡A</div><div class="kw">7.7억</div>
      <p><strong>7억7,200만원</strong> (보도).</p></div>
    <div class="kcard"><div class="hot">1순위</div><div class="kw">10월 27일</div>
      <p>2순위 <strong>28일</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>트리븐센텀 물량 (세대)</h3>
    <span class="badge">10월 보도 기준</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5,555</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:25.5%">1,644</div><div class="barv" style="--h:25.5%"></div></div>
      <div class="col dim"><div class="v" style="--h:13.2%">852</div><div class="barv" style="--h:13.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:12.3%">792</div><div class="barv" style="--h:12.3%"></div></div>
    </div>
    <div class="collbl"><span>이번 주 전국</span><span>트리븐센텀</span><span>1단지</span><span>2단지</span></div>
    <p class="cap">이번 주 전국은 10월 26일~11월 1일 청약 8곳 합계로, 오피스텔과 조합원 취소분을 포함한 리얼투데이 집계입니다. 막대 길이는 최댓값 5,555가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 트리븐센텀 청약, 오늘 특별공급"),
    ("02-date", "특공 26일, 1순위 27일, 계약 11월 17일"),
    ("03-size", "1단지 852, 2단지 792, 합쳐 1,644세대"),
    ("04-price", "2단지 국평 7억대, 최고 10억"),
    ("05-check", "공고문에서 확인할 것 3가지"),
    ("06-tips", "트리븐센텀 청약 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="트리븐센텀,트리븐센텀청약,트리븐센텀분양가,해운대청약,부산청약,반여동,두산에너빌리티,부산분양,명장공원,특별공급">
  <h2>트리븐센텀 청약, 오늘 특별공급</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 트리븐센텀 청약, 오늘 특별공급"></span>

  <p>트리븐센텀 청약이 오늘(10월 26일) 특별공급으로 시작합니다. 부산 해운대구 반여동에 1단지 852세대, 2단지 792세대, 합쳐 1,644세대를 짓는 단지로 두산에너빌리티가 시공합니다. 견본주택은 10월 16일 문을 열었습니다. <span class="mark">약 78만㎡ 명장공원을 끼고 있다는 점을 내세웠고, 2단지 84㎡A 분양가는 7억7,200만원으로 알려졌습니다.</span></p>

  <h3>트리븐센텀 청약 일정, 특공 26일·1순위 27일</h3>
  <div class="chart" data-img="카드뉴스 2번 · 특공 26일, 1순위 27일, 계약 11월 17일">
    <h3>청약 일정 (보도 기준)</h3>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.26</span>
      <span class="desc">오늘입니다. 1·2단지 모두 같은 날입니다.</span></div>
    <h4>1순위 · 2순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.27~28</span>
      <span class="desc">1순위 27일, 2순위 28일입니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.4~5</span>
      <span class="desc">단지별 날짜가 자료마다 달라 공고문 확인.</span></div>
    <h4>정당계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.17~19</span>
      <span class="desc">두 단지 같은 기간으로 안내됐습니다.</span></div>
    <p class="cap">데일리안·파이낸셜뉴스 등 10월 보도와 청약 일정 안내 기준입니다. 접수 시간과 단지별 당첨 발표일은 청약홈 입주자 모집공고문으로 다시 확인하십시오.</p>
  </div>
  <p>특별공급은 오늘 하루, 1순위는 내일 27일입니다. 계약은 11월 17~19일로 안내됐습니다. <span class="mark">당첨자 발표일은 1단지가 11월 4일과 5일로 자료마다 다르게 적혀 있습니다.</span> 두 단지 발표일이 다르면 함께 넣을 수 있는지가 달라지므로, 공고문의 중복 청약 조항과 발표일을 직접 확인하고 넣으십시오.</p>

  <h3>트리븐센텀 규모, 이번 주 부산에서 가장 크다</h3>
  <div class="chart" data-img="카드뉴스 3번 · 1단지 852, 2단지 792, 합쳐 1,644세대">
    <h3>10월 다섯째 주 대단지와 트리븐센텀 (세대)</h3>
    <div class="bar"><label>아크메르 동탄 (화성)</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,808</div></div></div>
    <div class="bar"><label>트리븐센텀 합계 (부산)</label>
      <div class="rail"><div class="fill" style="width:90.9%">1,644</div></div></div>
    <div class="bar"><label>신분평 에피트 더웨이시티 (청주)</label>
      <div class="rail"><div class="fill gray" style="width:54.9%">992</div></div></div>
    <div class="bar"><label>트리븐센텀 1단지</label>
      <div class="rail"><div class="fill" style="width:47.1%">852</div></div></div>
    <div class="bar"><label>트리븐센텀 2단지</label>
      <div class="rail"><div class="fill" style="width:43.8%">792</div></div></div>
    <p class="cap">10월 26일~11월 1일 청약 일정, 리얼투데이 집계 보도와 분양 보도 기준입니다. 막대 길이는 최댓값 1,808가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>이번 주 전국 청약은 8곳, 5,555가구입니다. 트리븐센텀은 1,644세대로 화성 아크메르 동탄(1,808가구) 다음으로 크고, 부산에서는 가장 큽니다. <span class="mark">1단지와 2단지가 따로 청약을 받으므로, 어느 단지에 넣을지 먼저 정해야 합니다.</span> 2단지는 84㎡A 385세대, 84㎡B 154세대로 84㎡가 절반을 넘습니다.</p>

  <h3>트리븐센텀 분양가, 2단지 국평 7억대</h3>
  <div class="chart" data-img="카드뉴스 4번 · 2단지 국평 7억대, 최고 10억">
    <h3>2단지 공급금액 (억원)</h3>
    <div class="bar"><label>2단지 최고</label>
      <div class="rail"><div class="fill gray" style="width:100%">10.18</div></div></div>
    <div class="bar"><label>84㎡A (385세대)</label>
      <div class="rail"><div class="fill" style="width:75.8%">7.72</div></div></div>
    <div class="bar"><label>84㎡B (154세대)</label>
      <div class="rail"><div class="fill" style="width:74.6%">7.59</div></div></div>
    <div class="bar"><label>2단지 최저</label>
      <div class="rail"><div class="fill gray" style="width:68%">6.93</div></div></div>
    <p class="cap">2단지 공급금액 6억9,280만~10억1,830만원, 84㎡A 7억7,200만원, 84㎡B 7억5,930만원은 분양 정보 보도 기준입니다. 84㎡A는 7억7,970만원으로 적은 곳도 있어 공고문 확인이 필요합니다. 1단지 금액은 출처가 엇갈려 싣지 않았습니다. 막대 길이는 최댓값을 기준으로 맞췄습니다.</p>
  </div>
  <p>2단지 공급금액은 6억9,280만원에서 10억1,830만원 사이로 알려졌습니다. 84㎡A는 7억7,200만원, 84㎡B는 7억5,930만원입니다. <span class="mark">계약금이 10%라면 84㎡A 기준 7,720만원을 당첨 직후 현금으로 준비해야 합니다.</span> 계약금 비율은 가정이니 공고문 표에서 확인하십시오. 1단지는 타입별 금액이 자료마다 달라 여기 싣지 않았습니다.</p>

  <h3>공고문에서 확인할 것 3가지</h3>
  <div class="chart" data-img="카드뉴스 5번 · 공고문에서 확인할 것 3가지">
    <h3>기사로는 확인되지 않은 것</h3>
    <h4>1·2단지 중복 청약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">조항 확인</span>
      <span class="desc">발표일과 함께 공고문으로.</span></div>
    <h4>계약금 비율</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10%?</span>
      <span class="desc">위 계산은 가정입니다.</span></div>
    <h4>전매·재당첨 제한</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">공고문</span>
      <span class="desc">규제 적용 여부를 직접 확인.</span></div>
    <p class="cap">청약홈(applyhome.co.kr) 입주자 모집공고문이 정본입니다. 대출 가능 금액은 은행 상담으로 확인하십시오.</p>
  </div>
  <p>기사만으로는 확인되지 않는 것이 세 가지 있습니다. 1·2단지 중복 청약 조건, 계약금 비율, 전매와 재당첨 제한입니다. <span class="mark">세 가지 모두 당첨 뒤 돈과 자격에 바로 걸리는 조건이라, 내일 1순위 전에 공고문에서 먼저 읽어 두는 편이 안전합니다.</span></p>

  <h3>트리븐센텀 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 트리븐센텀 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="trv1026-06-tips.png" src="../images/cards/report/trv1026-06-tips.png" alt="체크포인트 카드 · 1. 특공 26일·1순위 27일 날짜 확인, 2. 1단지·2단지 중 어디에 넣을지, 3. 계약금 현금 계획" loading="lazy" width="1080" height="1080">
    <figcaption>트리븐센텀 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>특공 26일·1순위 27일 날짜 확인</strong>. 2순위는 28일입니다. 청약홈 접수 시간을 미리 봐 둡니다.</li>
    <li><strong>1단지·2단지 중 어디에 넣을지</strong>. 따로 청약을 받습니다. 중복 청약 조건과 발표일을 공고문에서 읽습니다.</li>
    <li><strong>계약금 현금 계획</strong>. 2단지 84㎡A 기준 10%만 해도 7,720만원입니다. 대출 한도는 은행 상담으로 확인합니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>트리븐센텀 청약</strong>은 오늘 10월 26일 특별공급, 27일 1순위, 28일 2순위 순서로 진행됩니다. 부산 해운대구 반여동 1단지 852세대, 2단지 792세대로 이번 주 부산에서 가장 큰 청약입니다. <span class="mark">2단지 84㎡A는 7억7,200만원, 계약은 11월 17~19일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 일정·분양가·물량은 10월 보도(데일리안·파이낸셜뉴스·대한경제·뉴스1·서울경제)와 청약 일정 안내 기준입니다. 계약금은 비율을 가정한 계산입니다. 당첨 발표일·중복 청약·전매·재당첨 조건과 확정 내용은 청약홈(applyhome.co.kr) 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 데일리안 "트리븐 센텀, 27일 1순위 청약"(2026-10) · 파이낸셜뉴스 트리븐 센텀 16일 견본주택 개관(2026-10-13) · 대한경제 트리븐 센텀 1,644세대(2026-09-28) · 뉴스1·서울경제 분양캘린더 전국 8곳 5,555가구(2026-10-23)<br>
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
for v, w in ((1644, 90.9), (992, 54.9), (852, 47.1), (792, 43.8)):
    assert round(v / 1808 * 100, 1) == w, v
for v, hh in ((1644, 25.5), (852, 13.2), (792, 12.3)):
    assert round(v / 5555 * 86, 1) == hh, v
assert 852 + 792 == 1644
for v, w in ((7.72, 75.8), (7.593, 74.6), (6.928, 68.0)):
    assert round(v / 10.183 * 100, 1) == w, v
KW = "트리븐센텀"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("트리븐센텀")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
