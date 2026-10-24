# -*- coding: utf-8 -*-
"""리포트 #104 (2026-10-25) 아크메르 동탄 95·99 청약. #103을 복제해 교체한다.

메인 검색어: 아크메르 동탄 청약

수치와 검산
  사건일과 오늘의 간격: 특별공급 10/26(내일, D-1) · 주간 분양 일정 보도 10/23 → 2일.
  보도: 화성 동탄구 반송동 95·99 · 지하7~지상49층 7개 동 총 1,808가구 (M1-1-2 812 · M1-2-2 996)
    · 시행 KB부동산신탁 · 시공 포스코이앤씨
    · 특공 10/26 · 1순위 10/27 · 2순위 10/28 · 당첨 95 11/3 · 99 11/4 · 계약 11/16~18
    · 84㎡ 최고 분양가 95 17억1,530만 · 99 17억1,680만 (보도)
    · 10월 다섯째 주 전국 8곳 5,555가구(오피스텔·조합원 취소분 포함, 리얼투데이)
      트리븐센텀 1,644 · 신분평 에피트 더웨이시티 992 · GD메트로타워 오피스텔 770 · 매교역 펠루시드 오피스텔 154 · 연산 센텀 월드메르디앙 144
  대시보드 세로 (5,555 → 86%): 1,808 → 28.0 · 996 → 15.4 · 812 → 12.6
  가로 (1,808 → 100%): 1,644 → 90.9 · 992 → 54.9 · 770 → 42.6 · 154 → 8.5 · 144 → 8.0
  가로 (17.168억 → 100%): 17.153 → 99.9 · 20% 3.4336 → 20.0 · 10% 1.7168 → 10.0

단정하지 않은 것
  · 블록별 812·996이 95·99 중 어느 쪽인지: 쓰지 않음
  · 계약금 비율: 10%·20%는 가정. 공고문 확인
  · 두 단지 중복 청약 가능 여부·규제지역·전매·재당첨: 공고문 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-24-dh-banpo124.html"
SLUG, PRE = "2026-10-25-acmer-dongtan", "akm1025"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 104, "2026-10-25"
PREV_SLUG = "dhb1024-"
BANNED = ["반포124", "반포주공"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "아크메르 동탄 청약 내일 특공, 국평 17억 넘었다"
DESC = ("아크메르 동탄 95·99 청약이 내일(10월 26일) 특별공급으로 시작합니다. 화성 동탄구 반송동 49층 1,808가구로, "
        "1순위는 27일입니다. 84㎡ 최고 분양가는 17억1,680만원으로 보도됐습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="특별공급 10월 26일, 1순위 27일, 2순위 28일. 당첨 발표는 95 11월 3일, 99 11월 4일. 84㎡ 최고 17억1,680만원.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">아크메르 동탄 청약,<br>내일 특별공급</h1>
  <p class="sub"><strong>아크메르 동탄 95·99</strong>가 <strong>10월 26일(월)</strong> 특별공급, 27일 1순위 청약을 받습니다. 화성 동탄구 반송동, 최고 49층 <strong>1,808가구</strong>입니다. <span class="mark">84㎡ 최고 분양가는 17억1,680만원으로 보도됐습니다. 이번 주 전국 청약 단지 중 가장 큽니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · D-1</div><div class="kw">10월 26일</div>
      <p><strong>특별공급</strong> 접수일.</p></div>
    <div class="kcard"><div class="hot">총 가구</div><div class="kw">1,808가구</div>
      <p>최고 <strong>49층</strong>, 7개 동.</p></div>
    <div class="kcard"><div class="hot">84㎡ 최고</div><div class="kw">17억</div>
      <p>99 <strong>17억1,680만원</strong>.</p></div>
    <div class="kcard"><div class="hot">1순위</div><div class="kw">10월 27일</div>
      <p>2순위 <strong>28일</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>아크메르 동탄 물량 (가구)</h3>
    <span class="badge">10월 보도 기준</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5,555</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:28%">1,808</div><div class="barv" style="--h:28%"></div></div>
      <div class="col dim"><div class="v" style="--h:15.4%">996</div><div class="barv" style="--h:15.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:12.6%">812</div><div class="barv" style="--h:12.6%"></div></div>
    </div>
    <div class="collbl"><span>이번 주 전국</span><span>아크메르 동탄</span><span>M1-2-2블록</span><span>M1-1-2블록</span></div>
    <p class="cap">이번 주 전국은 10월 26일~11월 1일 청약 8곳 합계로, 오피스텔과 조합원 취소분을 포함한 리얼투데이 집계입니다. 막대 길이는 최댓값 5,555가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 아크메르 동탄 청약, 내일 특별공급"),
    ("02-date", "특공 26일, 1순위 27일, 발표는 하루 차"),
    ("03-week", "이번 주 청약 단지 중 가장 큰 1,808가구"),
    ("04-price", "국평 17억, 계약금만 억대"),
    ("05-check", "공고문에서 확인할 것 3가지"),
    ("06-tips", "아크메르 동탄 청약 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="아크메르동탄,아크메르동탄청약,아크메르동탄분양가,동탄청약,동탄분양,화성청약,반송동,포스코이앤씨,경기청약,특별공급">
  <h2>아크메르 동탄 청약, 내일 특별공급</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 아크메르 동탄 청약, 내일 특별공급"></span>

  <p>아크메르 동탄 청약이 내일(10월 26일) 특별공급으로 시작합니다. 경기 화성시 동탄구 반송동 95·99번지 일원에 지하 7층~지상 최고 49층, 7개 동 1,808가구를 짓는 단지입니다. KB부동산신탁이 시행하고 포스코이앤씨가 시공합니다. <span class="mark">84㎡ 최고 분양가가 17억원을 넘어 "동탄 국평 17억"이라는 보도가 나왔습니다.</span></p>

  <h3>아크메르 동탄 청약 일정, 특공 26일·1순위 27일</h3>
  <div class="chart" data-img="카드뉴스 2번 · 특공 26일, 1순위 27일, 발표는 하루 차">
    <h3>청약 일정 (보도 기준)</h3>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.26</span>
      <span class="desc">95·99 두 단지 모두 같은 날입니다.</span></div>
    <h4>1순위 · 2순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.27~28</span>
      <span class="desc">1순위 27일, 2순위 28일입니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.3~4</span>
      <span class="desc">95는 3일, 99는 4일로 하루 차이가 납니다.</span></div>
    <h4>정당계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.16~18</span>
      <span class="desc">두 단지 같은 기간입니다.</span></div>
    <p class="cap">미디어펜·더비즈 등 10월 보도 기준입니다. 접수 시간과 세부 일정은 청약홈 입주자 모집공고문으로 다시 확인하십시오.</p>
  </div>
  <p>특별공급은 내일 하루, 1순위는 모레 27일입니다. 당첨자 발표는 95가 11월 3일, 99가 4일로 하루 차이가 납니다. <span class="mark">발표일이 다르면 두 단지에 함께 넣을 수 있는지, 한쪽에 당첨되면 다른 쪽은 어떻게 되는지가 달라집니다.</span> 이 부분은 기사마다 설명이 엇갈리니 공고문의 중복 청약 조항을 직접 읽고 넣으십시오.</p>

  <h3>이번 주 청약 단지 중 아크메르 동탄이 가장 크다</h3>
  <div class="chart" data-img="카드뉴스 3번 · 이번 주 청약 단지 중 가장 큰 1,808가구">
    <h3>10월 다섯째 주 청약 단지 (가구·실)</h3>
    <div class="bar"><label>아크메르 동탄 (화성)</label>
      <div class="rail"><div class="fill" style="width:100%">1,808</div></div></div>
    <div class="bar"><label>트리븐센텀 1·2단지 (부산)</label>
      <div class="rail"><div class="fill gray" style="width:90.9%">1,644</div></div></div>
    <div class="bar"><label>신분평 에피트 더웨이시티 (청주)</label>
      <div class="rail"><div class="fill gray" style="width:54.9%">992</div></div></div>
    <div class="bar"><label>GD메트로타워 (서울, 오피스텔)</label>
      <div class="rail"><div class="fill gray" style="width:42.6%">770</div></div></div>
    <div class="bar"><label>매교역 펠루시드 (수원, 오피스텔)</label>
      <div class="rail"><div class="fill gray" style="width:8.5%"></div><span class="railval">154</span></div></div>
    <div class="bar"><label>연산 센텀 월드메르디앙 (부산)</label>
      <div class="rail"><div class="fill gray" style="width:8%"></div><span class="railval">144</span></div></div>
    <p class="cap">10월 26일~11월 1일 청약 일정, 리얼투데이 집계 보도 기준입니다. 오피스텔은 실 단위입니다. 막대 길이는 최댓값 1,808가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>이번 주 전국에서 청약을 받는 곳은 8곳, 5,555가구입니다. 아크메르 동탄이 1,808가구로 가장 크고, 같은 27일에 부산 해운대 트리븐센텀 1·2단지(1,644가구)도 1순위를 받습니다. <span class="mark">수도권 아파트로 범위를 좁히면 이번 주 1,000가구가 넘는 단지는 아크메르 동탄 하나입니다.</span> 서울 대림동 GD메트로타워 770실은 오피스텔이라 아파트 청약과 규칙이 다릅니다.</p>

  <h3>아크메르 동탄 분양가, 국평 17억에 계약금만 억대</h3>
  <div class="chart" data-img="카드뉴스 4번 · 국평 17억, 계약금만 억대">
    <h3>84㎡ 최고 분양가와 계약금 (억원)</h3>
    <div class="bar"><label>99 · 84㎡ 최고</label>
      <div class="rail"><div class="fill" style="width:100%">17.17</div></div></div>
    <div class="bar"><label>95 · 84㎡ 최고</label>
      <div class="rail"><div class="fill gray" style="width:99.9%">17.15</div></div></div>
    <div class="bar"><label>계약금 20%라면</label>
      <div class="rail"><div class="fill gray" style="width:20%"></div><span class="railval">3.43</span></div></div>
    <div class="bar"><label>계약금 10%라면</label>
      <div class="rail"><div class="fill gray" style="width:10%"></div><span class="railval">1.72</span></div></div>
    <p class="cap">84㎡ 최고 분양가는 보도 수치(95 17억1,530만원, 99 17억1,680만원)입니다. 계약금은 비율을 가정해 99 최고가에 곱한 값이며 실제 비율은 공고문으로 확인하십시오. 막대 길이는 최댓값을 기준으로 맞췄습니다.</p>
  </div>
  <p>84㎡ 최고 분양가는 95가 17억1,530만원, 99가 17억1,680만원으로 보도됐습니다. "동탄 분양가 신기록"이라는 보도가 붙었습니다. <span class="mark">계약금이 10%면 1억7,000만원 남짓, 20%면 3억4,000만원 남짓을 당첨 직후 현금으로 내야 합니다.</span> 같은 84㎡라도 타입과 층에 따라 값이 달라지니 내가 넣을 타입의 금액을 공고문 표에서 확인하십시오.</p>

  <h3>공고문에서 확인할 것 3가지</h3>
  <div class="chart" data-img="카드뉴스 5번 · 공고문에서 확인할 것 3가지">
    <h3>기사로는 확인되지 않은 것</h3>
    <h4>두 단지 중복 청약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">하루 차</span>
      <span class="desc">발표일이 달라 조건을 공고문으로.</span></div>
    <h4>계약금 비율</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10~20%</span>
      <span class="desc">위 계산은 가정입니다.</span></div>
    <h4>전매·재당첨 제한</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">공고문</span>
      <span class="desc">규제 적용 여부를 직접 확인.</span></div>
    <p class="cap">청약홈(applyhome.co.kr) 입주자 모집공고문이 정본입니다. 대출 가능 금액은 은행 상담으로 확인하십시오.</p>
  </div>
  <p>기사만으로는 확인되지 않는 것이 세 가지 있습니다. 두 단지 중복 청약 조건, 계약금 비율, 전매와 재당첨 제한입니다. <span class="mark">세 가지 모두 당첨 뒤 돈과 자격에 바로 걸리는 조건이라, 내일 특별공급 전에 공고문에서 먼저 읽어 두는 편이 안전합니다.</span></p>

  <h3>아크메르 동탄 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 아크메르 동탄 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="akm1025-06-tips.png" src="../images/cards/report/akm1025-06-tips.png" alt="체크포인트 카드 · 1. 특공 26일·1순위 27일 날짜 확인, 2. 95·99 중복 청약 조건 공고문 확인, 3. 계약금 현금 계획" loading="lazy" width="1080" height="1080">
    <figcaption>아크메르 동탄 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>특공 26일·1순위 27일 날짜 확인</strong>. 2순위는 28일입니다. 청약홈 접수 시간을 미리 봐 둡니다.</li>
    <li><strong>95·99 중복 청약 조건 공고문 확인</strong>. 발표일이 하루 다릅니다. 함께 넣기 전에 공고문 조항을 읽습니다.</li>
    <li><strong>계약금 현금 계획</strong>. 84㎡ 최고가 기준 10%만 해도 1억7,000만원 남짓입니다. 대출 한도는 은행 상담으로 확인합니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>아크메르 동탄 청약</strong>은 내일 10월 26일 특별공급, 27일 1순위, 28일 2순위 순서로 진행됩니다. 화성 동탄구 반송동 최고 49층 1,808가구로 이번 주 전국 청약 단지 중 가장 큽니다. <span class="mark">84㎡ 최고 분양가는 17억1,680만원, 당첨 발표는 95가 11월 3일, 99가 4일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 일정·분양가·물량은 10월 보도(미디어펜·더비즈·SBS Biz·이투데이·브릿지경제·한국경제) 기준입니다. 계약금은 비율을 가정한 계산입니다. 중복 청약·전매·재당첨 조건과 확정 내용은 청약홈(applyhome.co.kr) 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 미디어펜 아크메르 동탄 10월 마지막 주 분양(2026-10) · 더비즈 내집마련 캘린더(2026-10) · SBS Biz "화성 동탄 국평이 17억?"(2026-10) · 이투데이·브릿지경제 10월 다섯째 주 분양(2026-10-23) · 한국경제 아크메르 동탄(2026-10)<br>
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
for v, w in ((1644, 90.9), (992, 54.9), (770, 42.6), (154, 8.5), (144, 8.0)):
    assert round(v / 1808 * 100, 1) == w, v
for v, h in ((1808, 28.0), (996, 15.4), (812, 12.6)):
    assert round(v / 5555 * 86, 1) == h, v
assert 812 + 996 == 1808
assert round(17.153 / 17.168 * 100, 1) == 99.9 and round(17.168 * 0.2, 2) == 3.43 and round(17.168 * 0.1, 2) == 1.72
KW = "아크메르 동탄"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("아크메르동탄")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
