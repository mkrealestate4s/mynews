# -*- coding: utf-8 -*-
"""리포트 #121 (2026-11-10) 한화포레나 지제역 1순위. #120을 복제해 교체한다.

메인 검색어: 한화포레나 지제역

수치와 검산
  사건일과 오늘의 간격: 1순위 청약 11/10(D-day, 리드) · 특공 11/9(1일 전) · 견본주택 개관 11/6(4일 전).
  단지 (헤럴드경제·리얼캐스트·KCE뉴스 11/4~6): 평택시 세교동 · 1,098가구 · 특공 528 · 일반 570
    특공: 신혼 141 · 다자녀 106 · 신생아 93 · 기관추천 93 · 생애최초 64 · 노부모 31 (합 528)
    일정: 특공 11/9 · 1순위 11/10 · 2순위 11/11 · 당첨 11/18 · 계약 11/29~12/1 · 입주 2029년 말
    1순위: 통장 12개월 + 예치금 · 세대원·유주택자 가능 · 동일 순위 경쟁 시 평택 6개월 이상 거주자 우선
    분양가(만원): 84A 64,875~70,875 · 84B 62,695~70,095 · 84C 64,850~72,450 · 84D 66,150~72,350
    계약금 10%(1차 1,000만원, 30일 안에 잔액) · 중도금 60% 이자후불제
  대시보드 특공(141→86): 141 86 · 106 64.7 · 93 56.7 · 93 56.7 · 64 39.0 · 31 18.9
  공급 가로(1098→100): 570 51.9 · 528 48.1
  최저 분양가(66,150→100): 62,695 94.8 · 64,850 98.0 · 64,875 98.1 · 66,150 100

단정하지 않은 것
  · 예치금 액수·전매제한·재당첨 제한은 모집공고 확인 필요 · '실거주 의무 없음'은 보도(위키트리) 표현으로만 인용
  · 59·74㎡ 분양가는 보도에서 확인 못 함, 84㎡만 쓴다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-09-yongsan-riverview.html"
DST = ROOT / "posts/2026-11-10-forena-jijeyeok.html"
SLUG, PRE = "2026-11-10-forena-jijeyeok", "fjj"
NO, DATE = 121, "2026-11-10"
PREV_SLUG = "ysr-"
BANNED = ["용산", "해링턴", "청년안심", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "한화포레나 지제역 오늘 1순위, 84㎡ 6억대부터"
DESC = ("한화포레나 지제역이 오늘(11월 10일) 1순위 청약을 받습니다. 평택 세교동 1,098가구, 특별공급 528·일반 570가구. "
        "전용 84㎡ 분양가 6억2,695만~7억2,450만원, 계약금 10%. 일정·분양가·자격과 확인할 점을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="평택지제역 1,098가구 대단지. 오늘 1순위, 내일 2순위, 18일 당첨 발표. 84㎡ 6억대부터, 평택 6개월 거주자 우선.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">한화포레나 지제역<br>오늘 1순위, 84㎡ 6억대부터</h1>
  <p class="sub"><strong>한화포레나 지제역</strong>이 오늘 <strong>11월 10일(화) 1순위</strong> 청약을 받습니다. 경기 평택시 세교동 <strong>1,098가구</strong> 대단지로, 어제 특별공급(528가구)에 이어 오늘 일반공급 570가구 1순위 접수입니다. 전용 84㎡ 분양가는 <strong>6억2,695만~7억2,450만원</strong>입니다. <span class="mark">같은 순위 안에서 경쟁하면 평택시 6개월 이상 거주자가 먼저입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 포레나 지제역</div><div class="kw">11월 10일</div>
      <p>오늘 <strong>1순위</strong>, 내일 2순위.</p></div>
    <div class="kcard"><div class="hot">공급</div><div class="kw">1,098가구</div>
      <p>특공 <strong>528</strong> · 일반 570.</p></div>
    <div class="kcard"><div class="hot">84㎡ 분양가</div><div class="kw">6억대부터</div>
      <p>최저 <strong>6억2,695만</strong> · 최고 7억2,450만.</p></div>
    <div class="kcard"><div class="hot">당첨 발표</div><div class="kw">11월 18일</div>
      <p>계약 <strong>11/29~12/1</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>한화포레나 지제역 특별공급 528가구 (가구)</h3>
    <span class="badge">신혼부부가 가장 많다</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">141</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:64.7%">106</div><div class="barv" style="--h:64.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:56.7%">93</div><div class="barv" style="--h:56.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:56.7%">93</div><div class="barv" style="--h:56.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:39%">64</div><div class="barv" style="--h:39%"></div></div>
      <div class="col dim"><div class="v" style="--h:18.9%">31</div><div class="barv" style="--h:18.9%"></div></div>
    </div>
    <div class="collbl"><span>신혼</span><span>다자녀</span><span>신생아</span><span>기관</span><span>생초</span><span>노부모</span></div>
    <p class="cap">모두 가구 수라 한 축에 놓았습니다. 막대 길이는 최댓값 141가구를 기준으로 맞췄습니다. 기관은 기관추천, 생초는 생애최초입니다. 헤럴드경제·리얼캐스트(11월 4~6일) 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 한화포레나 지제역 오늘 1순위, 84㎡ 6억대부터"),
    ("02-mix", "1,098가구 중 일반공급 570가구"),
    ("03-sched", "오늘 1순위, 18일 당첨 발표"),
    ("04-price", "84㎡ 최저가 6억2,695만원부터"),
    ("05-pay", "계약금은 10%, 먼저 1,000만원"),
    ("06-check", "한화포레나 지제역 체크 3가지"),
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

ARTICLE = '''<article data-tags="한화포레나지제역,포레나지제역,평택지제역,평택청약,평택아파트분양,세교동,11월청약일정,1순위청약,경기분양,삼성평택캠퍼스">
  <h2>한화포레나 지제역 오늘 1순위, 84㎡ 6억대부터</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 한화포레나 지제역 오늘 1순위, 84㎡ 6억대부터"></span>

  <p>한화포레나 지제역이 오늘(11월 10일) 1순위 청약을 받습니다. 경기 평택시 세교동, 평택지제역 생활권에 들어서는 1,098가구 단지입니다. 어제 특별공급을 받았고 <strong>오늘 1순위, 내일(11일) 2순위</strong> 순서입니다. <span class="mark">청약통장 가입 12개월 이상이고 예치금을 채웠다면 세대원과 유주택자도 1순위로 넣을 수 있다고 보도됐습니다.</span></p>

  <h3>한화포레나 지제역, 1,098가구 중 일반공급 570가구</h3>
  <div class="chart" data-img="카드뉴스 2번 · 1,098가구 중 일반공급 570가구">
    <h3>한화포레나 지제역 공급 구성 (가구)</h3>
    <div class="bar"><label>전체</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,098</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill" style="width:51.9%">570</div></div></div>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill gray" style="width:48.1%">528</div></div></div>
    <p class="cap">모두 가구 수라 한 축에 놓았습니다. 막대 길이는 전체 1,098가구를 기준으로 맞췄습니다. 헤럴드경제·KCE뉴스(11월 4~6일) 보도 기준입니다.</p>
  </div>
  <p>전체 1,098가구 가운데 특별공급이 528가구, 오늘 1순위로 나오는 일반공급이 570가구입니다. 특별공급은 신혼부부 141, 다자녀 106, 신생아 93, 기관추천 93, 생애최초 64, 노부모부양 31가구로 나뉩니다. <span class="mark">어제 특별공급에서 떨어졌더라도 오늘 일반공급 1순위에 다시 넣을 수 있는지는 모집공고의 중복 청약 규정으로 확인하십시오.</span></p>

  <h3>오늘 1순위, 18일 당첨 발표</h3>
  <div class="chart" data-img="카드뉴스 3번 · 오늘 1순위, 18일 당첨 발표">
    <h3>한화포레나 지제역 일정</h3>
    <h4>1순위 청약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.10</span>
      <span class="desc">오늘. 2순위는 내일 11일. 청약홈에서 접수한다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.18</span>
      <span class="desc">다음 주 수요일. 청약홈에서 확인한다.</span></div>
    <h4>정당계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.29</span>
      <span class="desc">12월 1일까지 3일. 입주는 2029년 말 예정.</span></div>
    <p class="cap">헤럴드경제·KCE뉴스(11월 4~6일) 보도 기준입니다. 접수 시간과 방법은 청약홈 모집공고로 확인하십시오.</p>
  </div>
  <p>1순위는 오늘, 2순위는 내일 받고 당첨자는 18일 발표합니다. 정당계약은 11월 29일부터 12월 1일까지 3일간이고 입주는 2029년 말 예정입니다. <span class="mark">같은 순위 안에서 경쟁이 붙으면 평택시에 6개월 이상 산 사람이 먼저 공급받습니다.</span></p>

  <h3>한화포레나 지제역 분양가, 84㎡ 타입별</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡ 최저가 6억2,695만원부터">
    <h3>전용 84㎡ 타입별 최저 분양가 (만원)</h3>
    <div class="bar"><label>84B</label>
      <div class="rail"><div class="fill" style="width:94.8%">62,695</div></div></div>
    <div class="bar"><label>84C</label>
      <div class="rail"><div class="fill gray" style="width:98%">64,850</div></div></div>
    <div class="bar"><label>84A</label>
      <div class="rail"><div class="fill gray" style="width:98.1%">64,875</div></div></div>
    <div class="bar"><label>84D</label>
      <div class="rail"><div class="fill gray" style="width:100%">66,150</div></div></div>
    <p class="cap">타입별 가장 낮은 층의 분양가입니다. 막대 길이는 네 값 중 최댓값 66,150만원을 기준으로 맞췄습니다. 최고층은 7억95만~7억2,450만원입니다. 리얼캐스트·위키트리 보도 기준이며 59·74㎡ 분양가는 확인하지 못했습니다.</p>
  </div>
  <p>주력인 84A는 1층 6억4,875만원부터 최고층 7억875만원으로, 같은 타입 안에서 층에 따라 6,000만원 차이가 납니다. 84B는 6억2,695만~7억95만원, 84C는 6억4,850만~7억2,450만원, 84D는 6억6,150만~7억2,350만원입니다. 네 타입 모두 6억 초중반에서 7억 초반 사이입니다.</p>

  <h3>계약금은 10%, 먼저 1,000만원</h3>
  <div class="chart" data-img="카드뉴스 5번 · 계약금은 10%, 먼저 1,000만원">
    <h3>한화포레나 지제역 납부 조건</h3>
    <h4>계약금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10%</span>
      <span class="desc">계약 때 1,000만원, 30일 안에 나머지를 낸다.</span></div>
    <h4>중도금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">60%</span>
      <span class="desc">이자후불제. 이자는 입주 때 한꺼번에 낸다.</span></div>
    <h4>84A 1층 계약금</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">약 6,490만</span>
      <span class="desc">6억4,875만원의 10%. 1,000만원을 빼면 약 5,490만원.</span></div>
    <p class="cap">리얼캐스트·위키트리 보도 기준입니다. 84A 1층 계약금은 분양가 × 10%로 직접 계산해 만원 단위에서 반올림했습니다.</p>
  </div>
  <p>계약금은 분양가의 10%로, 계약할 때 1,000만원을 먼저 내고 30일 안에 나머지를 냅니다. 84A 1층이면 계약금이 약 6,490만원이고, 첫날 1,000만원을 낸 뒤 한 달 안에 약 5,490만원을 더 마련해야 합니다. 중도금 60%는 이자후불제입니다. <span class="mark">당첨 발표(18일)부터 계약(29일)까지 열흘 남짓이니 계약금은 지금 확인해 두는 편이 낫습니다.</span></p>

  <h3>한화포레나 지제역 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 한화포레나 지제역 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="fjj-06-check.png" src="../images/cards/report/fjj-06-check.png" alt="체크포인트 카드 · 1. 평택 6개월 거주자 우선, 2. 오늘 1순위 내일 2순위, 3. 계약금 10%는 30일 안에" loading="lazy" width="1080" height="1080">
    <figcaption>한화포레나 지제역 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>평택 6개월 거주자 우선</strong>. 같은 순위 안에서 경쟁하면 평택시 6개월 이상 거주자가 먼저입니다. 다른 지역이면 남는 물량을 노리는 구조입니다.</li>
    <li><strong>오늘 1순위, 내일 2순위</strong>. 1순위는 통장 12개월 이상 + 예치금입니다. 내 통장의 지역별 예치금 기준은 청약홈과 모집공고에서 확인하십시오.</li>
    <li><strong>계약금 10%는 30일 안에</strong>. 84㎡면 6천만원 대가 필요합니다. 전매 제한과 재당첨 제한은 모집공고로 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>한화포레나 지제역</strong>은 평택 세교동 1,098가구(특공 528·일반 570) 단지로 오늘 1순위, 내일 2순위 청약을 받고 18일 당첨자를 발표합니다. 전용 84㎡ 분양가는 6억2,695만~7억2,450만원, 계약금 10%에 중도금 60% 이자후불제입니다. <span class="mark">넣기 전에 평택 거주 기간과 계약금 마련 계획부터 확인하십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 공급 구성·일정은 헤럴드경제·KCE뉴스(2026-11-04~06), 분양가·납부 조건은 리얼캐스트·위키트리 보도 기준입니다. 최종 조건은 입주자모집공고문과 청약홈으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 헤럴드경제 삼성 평택캠퍼스 인근 1098가구 한화포레나 지제역 분양(2026-11) · KCE뉴스 한화포레나 지제역 분양 돌입 9일 특별공급(2026-11) · 리얼캐스트 분양단지 톺아보기 한화포레나 지제역 · 위키트리 한화포레나 지제역 분양가 · 파이낸셜뉴스 11월 둘째 주 12곳 5215가구(2026-11-06)<br>
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
for v, h in zip((106, 93, 93, 64, 31), (64.7, 56.7, 56.7, 39.0, 18.9)):
    assert round(v / 141 * 86, 1) == h, (v, h)
assert 141 + 106 + 93 + 64 + 31 + 93 == 528 and 528 + 570 == 1098
for v, w in zip((570, 528), (51.9, 48.1)):
    assert round(v / 1098 * 100, 1) == w, (v, w)
for v, w in zip((62695, 64850, 64875), (94.8, 98.0, 98.1)):
    assert round(v / 66150 * 100, 1) == w, (v, w)
assert 70875 - 64875 == 6000
KW = "한화포레나 지제역"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("한화포레나지제역")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
