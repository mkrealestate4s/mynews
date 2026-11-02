# -*- coding: utf-8 -*-
"""리포트 #114 (2026-11-03) 11월 청약 일정, 이번 주 견본주택 5곳. #113을 복제해 교체한다.

메인 검색어: 11월 청약 일정

수치와 검산
  사건일과 오늘의 간격: 주간 분양 보도 11/2(어제) → 1일. 견본주택 개관 11/6 → D-3. 특공 11/9 · 1순위 11/10.
  보도(파이낸셜뉴스·리얼캐스트 11/2, 부동산인포 집계): 11월 첫째 주 전국 5곳 견본주택 · 4,216가구(일반·공공분양 3,049)
    · 리얼투데이 집계는 오피스텔·조합원 취소분 포함 4,928가구
    · 한화포레나 지제역(평택 세교동) 84·116㎡ 1,098 · 엘리프 시흥 더프라임(시흥거모 B-5) 84㎡ 338 중 일반 304
    · 시흥 거모 아테라(시흥거모 A6) 55·59㎡ 720 중 신혼희망타운 480 · 더샵 천안라크원 84~118㎡ 1,290 중 일반 1,032
    · 형곡 센트럴 아테라(구미 형곡3주공 재건축) 59㎡ 일반 135
    · 대부분 특공 11/9 · 1순위 11/10 · 2순위 11/11 · 당첨 11/17~18 (단지별 공고 확인)
  이번 주 접수(지난 글): 계양 카이브 유보라 1순위 11/3 · 2순위 11/4 (#113) · 고덕강일3단지 일반 1순위 11/4 · 발표 11/26 (#110)
  대시보드 세로 (1,290 → 86%): 1,098 → 73.2 · 720 → 48.0 · 338 → 22.5
  가로 규모 (1,290 → 100%): 1,098 → 85.1 · 720 → 55.8 · 338 → 26.2
  가로 비율: 1,032/1,290 → 80.0 · 304/338 → 89.9 · 480/720 → 66.7

단정하지 않은 것
  · 분양가 · 단지별 정확한 접수일 · 형곡 센트럴 아테라 전체 세대수 · 규제 여부·전매제한 → 각 입주자모집공고 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-02-gyeyang-caive.html"
SLUG, PRE = "2026-11-03-nov-cheongyak", "nov1103"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 114, "2026-11-03"
PREV_SLUG = "gcv1102-"
BANNED = ["반도건설", "AC3블록"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "11월 청약 일정, 이번 주 견본주택 5곳 연다"
DESC = ("11월 청약 일정 첫 주에 전국 5곳이 견본주택 문을 엽니다. 평택 한화포레나 지제역, 천안 더샵 천안라크원, 시흥 거모지구 두 곳, 구미 형곡 센트럴 아테라이며 "
        "부동산인포 집계 4,216가구입니다. 대부분 11월 9일 특별공급, 10일 1순위로 이어집니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="11월 첫째 주 견본주택 5곳, 4,216가구. 대부분 9일 특공, 10일 1순위. 이번 주 접수 단지까지 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">11월 청약 일정,<br>견본주택 5곳 연다</h1>
  <p class="sub"><strong>11월 청약 일정</strong> 첫 주에 전국 <strong>5곳</strong>이 견본주택을 엽니다. 부동산인포 집계 <strong>4,216가구</strong>이고 개관은 대부분 <strong>11월 6일(금)</strong>입니다. <span class="mark">청약은 대부분 9일 특별공급, 10일 1순위입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 이번 주</div><div class="kw">5곳</div>
      <p>견본주택 <strong>개관</strong>.</p></div>
    <div class="kcard"><div class="hot">총 공급</div><div class="kw">4,216가구</div>
      <p>부동산인포 <strong>집계</strong>.</p></div>
    <div class="kcard"><div class="hot">개관</div><div class="kw">11월 6일</div>
      <p>대부분 <strong>금요일</strong> 개관.</p></div>
    <div class="kcard"><div class="hot">다음 단계</div><div class="kw">11월 10일</div>
      <p><strong>1순위</strong>, 9일 특공.</p></div>
  </div>

  <div class="colchart">
    <h3>11월 첫째 주 견본주택 단지별 규모 (가구)</h3>
    <span class="badge">11월 2일 보도</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">1,290</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:73.2%">1,098</div><div class="barv" style="--h:73.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:48.0%">720</div><div class="barv" style="--h:48.0%"></div></div>
      <div class="col dim"><div class="v" style="--h:22.5%">338</div><div class="barv" style="--h:22.5%"></div></div>
    </div>
    <div class="collbl"><span>천안라크원</span><span>지제역</span><span>거모 아테라</span><span>엘리프 시흥</span></div>
    <p class="cap">파이낸셜뉴스·리얼캐스트(2026-11-02) 보도의 단지 전체 가구수입니다. 구미 형곡 센트럴 아테라는 일반분양 135가구만 보도돼 막대에서 뺐습니다. 막대 길이는 최댓값 1,290가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 11월 청약 일정, 견본주택 5곳 연다"),
    ("02-size", "가장 큰 곳은 천안 1,290가구"),
    ("03-date", "6일 개관, 9일 특공, 10일 1순위"),
    ("04-thisweek", "이번 주 접수: 오늘 계양, 4일 고덕강일"),
    ("05-share", "일반분양 몫, 단지마다 다르다"),
    ("06-tips", "11월 청약 일정 체크 3가지"),
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

ARTICLE = '''<article data-tags="11월청약일정,11월분양일정,이번주견본주택,한화포레나지제역,더샵천안라크원,엘리프시흥더프라임,시흥거모아테라,형곡센트럴아테라,아파트청약,청약일정">
  <h2>11월 청약 일정, 이번 주 견본주택 5곳 연다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 11월 청약 일정, 견본주택 5곳 연다"></span>

  <p>11월 청약 일정 첫 주에 전국 5곳이 견본주택을 엽니다. 경기 평택 한화포레나 지제역, 충남 더샵 천안라크원, 경기 시흥 거모지구의 엘리프 시흥 더프라임과 시흥 거모 아테라, 경북 구미 형곡 센트럴 아테라입니다. <span class="mark">부동산인포 집계로 4,216가구이고, 개관일은 대부분 11월 6일 금요일입니다.</span> 오피스텔과 조합원 취소분까지 넣은 리얼투데이 집계는 4,928가구로 조금 더 많습니다.</p>

  <h3>11월 청약 일정 첫 주, 단지별 규모</h3>
  <div class="chart" data-img="카드뉴스 2번 · 가장 큰 곳은 천안 1,290가구">
    <h3>단지 전체 가구수</h3>
    <div class="bar"><label>더샵 천안라크원</label>
      <div class="rail"><div class="fill" style="width:100%">1,290</div></div></div>
    <div class="bar"><label>한화포레나 지제역</label>
      <div class="rail"><div class="fill gray" style="width:85.1%">1,098</div></div></div>
    <div class="bar"><label>시흥 거모 아테라</label>
      <div class="rail"><div class="fill gray" style="width:55.8%">720</div></div></div>
    <div class="bar"><label>엘리프 시흥 더프라임</label>
      <div class="rail"><div class="fill gray" style="width:26.2%">338</div></div></div>
    <p class="cap">파이낸셜뉴스·리얼캐스트(2026-11-02) 보도 기준입니다. 막대 길이는 1,290가구를 100으로 맞췄습니다. 형곡 센트럴 아테라는 일반분양 135가구(59㎡)만 보도돼 같은 축에 넣지 않았습니다.</p>
  </div>
  <p>가장 큰 곳은 포스코이앤씨의 더샵 천안라크원으로 1,290가구(84~118㎡)입니다. 한화 건설부문의 한화포레나 지제역은 평택 세교동에 1,098가구(84·116㎡)를 짓습니다. <span class="mark">시흥 거모지구 두 곳은 같은 공공주택지구 안에서 B-5블록(엘리프, 84㎡ 338가구)과 A6블록(아테라, 55·59㎡ 720가구)으로 나뉩니다.</span> 구미 형곡 센트럴 아테라는 형곡3주공 재건축 단지로 59㎡ 135가구가 일반분양됩니다.</p>

  <h3>11월 청약 일정: 9일 특공, 10일 1순위</h3>
  <div class="chart" data-img="카드뉴스 3번 · 6일 개관, 9일 특공, 10일 1순위">
    <h3>견본주택 5곳 공통 일정 (대부분)</h3>
    <h4>견본주택 개관</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.6</span>
      <span class="desc">금요일, 대부분 이날 엽니다.</span></div>
    <h4>특별공급 · 1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.9~10</span>
      <span class="desc">2순위는 11일입니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.17~18</span>
      <span class="desc">단지별로 하루씩 다릅니다.</span></div>
    <p class="cap">파이낸셜뉴스(2026-11-02) 보도 기준으로 "대부분 단지"의 일정입니다. 단지마다 하루씩 다를 수 있고 정당계약 기간도 기사마다 다르므로 청약홈 입주자모집공고로 확인하십시오.</p>
  </div>
  <p>다섯 곳은 개관 뒤 사흘 만에 청약으로 넘어갑니다. <span class="mark">주말에 견본주택을 보고 월요일 9일 특별공급, 화요일 10일 1순위, 수요일 11일 2순위 순서입니다.</span> 발표는 17~18일입니다. 발표일이 같은 단지끼리는 한 곳에만 넣어야 하는 경우가 많으므로 공고문의 중복 청약 조항을 먼저 보십시오.</p>

  <h3>이번 주 접수: 오늘 계양, 4일 고덕강일</h3>
  <div class="chart" data-img="카드뉴스 4번 · 이번 주 접수: 오늘 계양, 4일 고덕강일">
    <h3>견본주택보다 먼저 받는 곳</h3>
    <h4>계양 카이브 유보라</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.3~4</span>
      <span class="desc">오늘 1순위, 내일 2순위.</span></div>
    <h4>고덕강일3단지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.4</span>
      <span class="desc">일반 1순위, 발표 26일.</span></div>
    <p class="cap">계양 카이브 유보라는 지난 리포트 #113, 고덕강일3단지 토지임대부 분양주택은 #110에서 정리한 보도 기준입니다. SR타임스 11월 첫째 주 분양동향도 두 단지를 이번 주 청약으로 꼽았습니다.</p>
  </div>
  <p>견본주택 5곳보다 먼저 이번 주에 접수를 받는 곳도 있습니다. <span class="mark">인천 계양신도시 첫 민간분양인 계양 카이브 유보라는 오늘 1순위, 서울 강동 고덕강일3단지는 내일 4일 일반 1순위입니다.</span> 두 단지의 분양가와 자격은 지난 글에 정리해 두었습니다. 이번 주 통장을 쓰면 다음 주 단지에는 넣을 수 없는지 미리 따져 보십시오.</p>

  <h3>일반분양 몫, 단지마다 다르다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 일반분양 몫, 단지마다 다르다">
    <h3>전체 중 일반·공공분양 비율 (%)</h3>
    <div class="bar"><label>엘리프 시흥(일반)</label>
      <div class="rail"><div class="fill" style="width:89.9%">89.9</div></div></div>
    <div class="bar"><label>천안라크원(일반)</label>
      <div class="rail"><div class="fill" style="width:80%">80.0</div></div></div>
    <div class="bar"><label>거모 아테라(신희타)</label>
      <div class="rail"><div class="fill gray" style="width:66.7%">66.7</div></div></div>
    <p class="cap">엘리프 시흥 304/338, 천안라크원 1,032/1,290, 시흥 거모 아테라 신혼희망타운 480/720로 계산했습니다. 보도의 '일반분양'은 조합원·임대 등을 뺀 분양 물량이며 특별공급이 포함될 수 있습니다. 한화포레나 지제역은 구분 수치가 보도되지 않았습니다.</p>
  </div>
  <p>같은 견본주택이라도 청약으로 나오는 몫은 다릅니다. <span class="mark">시흥 거모 아테라는 720가구 중 480가구가 신혼희망타운 공공분양이라 신혼부부·한부모 가구 자격이 먼저 맞아야 합니다.</span> 천안라크원은 1,290가구 중 1,032가구가 일반분양으로 나옵니다. 내 자격으로 넣을 수 있는 칸이 몇 가구인지가 실제 경쟁률을 좌우합니다.</p>

  <h3>11월 청약 일정 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 11월 청약 일정 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="nov1103-06-tips.png" src="../images/cards/report/nov1103-06-tips.png" alt="체크포인트 카드 · 1. 단지별 접수일, 2. 발표일 겹침, 3. 분양가와 전매 조건" loading="lazy" width="1080" height="1080">
    <figcaption>11월 청약 일정 첫 주에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>단지별 접수일</strong>. "대부분 9일 특공"이지만 하루씩 다른 곳이 있어 청약홈 공고로 확인합니다.</li>
    <li><strong>발표일 겹침</strong>. 17~18일 발표가 같은 단지끼리는 중복 청약이 안 되는 경우가 많습니다.</li>
    <li><strong>분양가와 전매 조건</strong>. 보도에 분양가가 아직 없으니 모집공고의 분양가표와 전매제한 조항을 봅니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>11월 청약 일정</strong> 첫 주에는 견본주택 5곳, 4,216가구가 문을 엽니다. 천안라크원 1,290가구, 한화포레나 지제역 1,098가구가 크고 시흥 거모지구 두 곳과 구미 형곡이 뒤를 잇습니다. <span class="mark">개관은 6일, 청약은 대부분 9일 특공·10일 1순위·11일 2순위, 발표는 17~18일입니다.</span> 그 전에 오늘 계양 카이브 유보라 1순위, 내일 고덕강일3단지 일반 1순위가 있습니다.</p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 단지 규모와 일정은 11월 2일 주간 분양 보도 기준이며 입주자모집공고 원문은 직접 확인하지 못했습니다. 분양가, 단지별 정확한 접수일, 규제지역 여부와 전매제한, 중복 청약 허용 범위는 청약홈 입주자모집공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 파이낸셜뉴스 "11월 첫째 주 전국 5곳 견본주택 개관…4216가구 공급"(2026-11-02) · 리얼캐스트 "11월 첫째 주 '한화포레나 지제역' 등 전국 5곳 견본주택 개관" · 포인트데일리 · SR타임스 11월 첫째주 분양동향 · 핀포인트뉴스 이번주 청약 길잡이 · 부동산인포 · 리얼투데이 · 청약홈<br>
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
assert round(1098 / 1290 * 86, 1) == 73.2 and round(720 / 1290 * 86, 1) == 48.0 and round(338 / 1290 * 86, 1) == 22.5
assert round(1098 / 1290 * 100, 1) == 85.1 and round(720 / 1290 * 100, 1) == 55.8 and round(338 / 1290 * 100, 1) == 26.2
assert round(1032 / 1290 * 100, 1) == 80.0 and round(304 / 338 * 100, 1) == 89.9 and round(480 / 720 * 100, 1) == 66.7
KW = "11월 청약 일정"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("11월청약일정")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
