# -*- coding: utf-8 -*-
"""리포트 #126 (2026-11-15) 경희궁 에피트. #125를 복제해 교체한다.

메인 검색어: 경희궁 에피트

수치와 검산
  사건일과 오늘의 간격: 대한경제 11/11 '11월 분양' 보도(4일 전) · 청약 정보 사이트 모집공고 11/13(2일 전) · 특공 11/25(10일 뒤, 공고문 확인 필요).
  단지 (파이낸셜뉴스 10/15 · 한국금융신문 10/23 · 대한경제 11/11): 종로구 교남동 돈의문2구역 · 지하6층~지상21층 2개동 · 39·59·84㎡ 228가구 · 일반분양 135
    시공 HL디앤아이한라 · 견본주택 은평구 증산동(11월 개관 예정) · 입주 2030년 8월(청약 정보 사이트)
  분양가 최고(만원, 당근부동산 청약정보): 39 118,241 · 59 189,843 · 84B 251,744 · 84A 257,484
  스트레이트뉴스: 3.3㎡당 7,450만원 · 84㎡ 평균 247,751 · 최고 257,484 · 사전 거론 7,600만원(머니투데이 10/6)
  일정(청약 정보 사이트, 확인 필요): 공고 11/13 · 특공 11/25 · 1순위 해당 11/26 · 기타 11/27 · 발표 12/4 · 계약 12/16~18
  대시보드(257,484→86): 118,241 39.5 · 189,843 63.4 · 251,744 84.1
  가구(228→100): 135 59.2 · 93 40.8
  84㎡(257,484→100): 251,744 97.8 · 247,751 96.2

단정하지 않은 것
  · 일정은 공식 공고문 대조 전이라 '청약 정보 사이트 안내' 로만 쓴다(한 차례 연기 이력)
  · 93가구를 조합원분이라 단정하지 않는다('일반분양 외')
  · 계약금 비율·중도금·대출·전매제한은 보도에서 확인 못 함 → 공고문 확인
  · 분상제 미적용·투기과열지구는 보도·청약 정보 사이트 표현으로 인용
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-14-toheo-oct.html"
DST = ROOT / "posts/2026-11-15-gyeonghuigung-epit.html"
SLUG, PRE = "2026-11-15-gyeonghuigung-epit", "ghe"
NO, DATE = 126, "2026-11-15"
PREV_SLUG = "th10-"
BANNED = ["토지거래허가 신청", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "경희궁 에피트 84㎡ 25억대, 분상제 아닙니다"
DESC = ("경희궁 에피트는 종로구 교남동 돈의문2구역 228가구(일반분양 135가구) 단지입니다. "
        "전용 84㎡ 최고 분양가 25억7,484만원, 3.3㎡당 7,450만원으로 보도됐고 분양가상한제가 적용되지 않습니다. 분양가·일정·확인할 점을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="4대문 안 돈의문2구역 228가구. 일반분양 135가구, 84㎡ 최고 25억7,484만원. 특공 11월 25일 안내, 공고문 확인 필요.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">경희궁 에피트<br>84㎡ 25억대, 분상제 아닙니다</h1>
  <p class="sub"><strong>경희궁 에피트</strong>는 종로구 교남동 돈의문2구역에 들어서는 <strong>228가구</strong> 단지로, 이 가운데 <strong>135가구</strong>가 일반분양입니다. 전용 84㎡ 최고 분양가는 <strong>25억7,484만원</strong>, 3.3㎡당 7,450만원으로 보도됐습니다. <span class="mark">분양가상한제가 적용되지 않는 단지라 주변 시세보다 싸게 나오는 '로또 청약'으로 보면 안 됩니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 경희궁 에피트</div><div class="kw">228가구</div>
      <p>일반분양 <strong>135가구</strong>.</p></div>
    <div class="kcard"><div class="hot">84㎡ 최고가</div><div class="kw">25억7,484만</div>
      <p>3.3㎡당 <strong>7,450만원</strong> 보도.</p></div>
    <div class="kcard"><div class="hot">특별공급</div><div class="kw">11월 25일</div>
      <p>1순위 <strong>11/26</strong> 안내. 공고문 확인.</p></div>
    <div class="kcard"><div class="hot">분양가상한제</div><div class="kw">미적용</div>
      <p>투기과열지구 · 입주 <strong>2030년 8월</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>경희궁 에피트 타입별 최고 분양가 (만원)</h3>
    <span class="badge">39㎡도 11억대</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:39.5%">118,241</div><div class="barv" style="--h:39.5%"></div></div>
      <div class="col dim"><div class="v" style="--h:63.4%">189,843</div><div class="barv" style="--h:63.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:84.1%">251,744</div><div class="barv" style="--h:84.1%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">257,484</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>39㎡</span><span>59㎡</span><span>84B</span><span>84A</span></div>
    <p class="cap">모두 타입별 최고 분양가(만원)라 한 축에 놓았습니다. 막대 길이는 최댓값 257,484만원을 기준으로 맞췄습니다. 청약 정보 사이트(당근부동산)의 모집공고 정리 기준이며 확정 금액은 입주자모집공고문으로 확인하십시오.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 경희궁 에피트 84㎡ 25억대, 분상제 아닙니다"),
    ("02-mix", "228가구 중 일반분양 135가구"),
    ("03-sched", "특공 11월 25일, 1순위 26일 안내"),
    ("04-price", "84㎡는 24억7,751만원이 평균"),
    ("05-site", "4대문 안 21층 2개 동, 입주 2030년"),
    ("06-check", "경희궁 에피트 체크 3가지"),
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

ARTICLE = '''<article data-tags="경희궁에피트,경희궁에피트분양가,돈의문2구역,종로아파트분양,교남동,서울청약,11월청약일정,HL디앤아이한라,분양가상한제,투기과열지구">
  <h2>경희궁 에피트 84㎡ 25억대, 분상제 아닙니다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 경희궁 에피트 84㎡ 25억대, 분상제 아닙니다"></span>

  <p>경희궁 에피트가 11월 분양에 들어갑니다. 서울 종로구 교남동 돈의문2구역을 재개발해 짓는 228가구 단지로, 경희궁자이 바로 옆 4대문 안 신축입니다. 청약 정보 사이트에는 11월 13일 모집공고, <strong>25일 특별공급, 26일 1순위</strong>로 안내돼 있습니다. <span class="mark">다만 이 단지는 분양가상한제를 적용받지 않아 전용 84㎡ 최고가가 25억원을 넘습니다.</span></p>

  <h3>경희궁 에피트, 228가구 중 일반분양 135가구</h3>
  <div class="chart" data-img="카드뉴스 2번 · 228가구 중 일반분양 135가구">
    <h3>경희궁 에피트 공급 구성 (가구)</h3>
    <div class="bar"><label>전체</label>
      <div class="rail"><div class="fill gray" style="width:100%">228</div></div></div>
    <div class="bar"><label>일반분양</label>
      <div class="rail"><div class="fill" style="width:59.2%">135</div></div></div>
    <div class="bar"><label>그 외</label>
      <div class="rail"><div class="fill gray" style="width:40.8%">93</div></div></div>
    <p class="cap">모두 가구 수라 한 축에 놓았습니다. 막대 길이는 전체 228가구를 기준으로 맞췄습니다. '그 외'는 전체에서 일반분양을 뺀 값입니다. 파이낸셜뉴스(10월 15일)·한국금융신문(10월 23일) 보도 기준입니다.</p>
  </div>
  <p>전용 39·59·84㎡ 세 가지 면적으로 모두 228가구이고, 청약으로 나오는 일반분양은 135가구입니다. 나머지 93가구가 어떻게 배정되는지는 보도에 나오지 않았습니다. <span class="mark">물량이 작아 타입별로 나누면 한 타입에 수십 가구 안팎이 됩니다. 타입별 가구 수는 모집공고문에서 확인하십시오.</span></p>

  <h3>특공 11월 25일, 1순위 26일 안내</h3>
  <div class="chart" data-img="카드뉴스 3번 · 특공 11월 25일, 1순위 26일 안내">
    <h3>경희궁 에피트 청약 일정 (안내 기준)</h3>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.25</span>
      <span class="desc">수요일. 청약홈에서 접수한다.</span></div>
    <h4>1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.26</span>
      <span class="desc">해당지역. 기타지역은 27일로 안내돼 있다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12.4</span>
      <span class="desc">계약은 12월 16~18일로 안내돼 있다.</span></div>
    <p class="cap">청약 정보 사이트(당근부동산)의 모집공고 정리 기준입니다. 이 단지는 10월에 한 차례 일정이 미뤄졌으므로(경제시그널) 청약홈 공고문으로 다시 확인하십시오.</p>
  </div>
  <p>청약 정보 사이트에 올라온 일정은 특별공급 11월 25일, 1순위 해당지역 26일·기타지역 27일, 당첨자 발표 12월 4일, 계약 12월 16~18일입니다. 처음에는 10월 공고가 예정됐다가 11월로 미뤄진 이력이 있습니다. <span class="mark">날짜는 청약홈의 입주자모집공고문이 정본입니다. 넣기 전에 한 번 더 대조하십시오.</span></p>

  <h3>경희궁 에피트 분양가, 84㎡는 평균 24억대</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡는 24억7,751만원이 평균">
    <h3>경희궁 에피트 전용 84㎡ 분양가 (만원)</h3>
    <div class="bar"><label>84A 최고</label>
      <div class="rail"><div class="fill" style="width:100%">257,484</div></div></div>
    <div class="bar"><label>84B 최고</label>
      <div class="rail"><div class="fill gray" style="width:97.8%">251,744</div></div></div>
    <div class="bar"><label>84 평균</label>
      <div class="rail"><div class="fill gray" style="width:96.2%">247,751</div></div></div>
    <p class="cap">막대 길이는 최댓값 257,484만원을 기준으로 맞췄습니다. 평균은 스트레이트뉴스, 타입별 최고가는 청약 정보 사이트 기준입니다. 3.3㎡당 7,450만원 보도이며 확정 금액은 공고문으로 확인하십시오.</p>
  </div>
  <p>전용 84㎡는 평균 24억7,751만원, 최고가는 84A 25억7,484만원으로 보도됐습니다. 3.3㎡당으로는 7,450만원입니다. 분양 전에는 3.3㎡당 7,600만원대까지 거론됐습니다(머니투데이). 작은 면적도 싸지 않습니다. 59㎡ 최고가가 18억9,843만원, 39㎡도 11억8,241만원입니다. <span class="mark">계약금·중도금 비율과 대출 조건은 아직 보도로 확인되지 않았습니다. 현금 계획은 공고문을 보고 세우십시오.</span></p>

  <h3>4대문 안 21층 2개 동, 입주 2030년</h3>
  <div class="chart" data-img="카드뉴스 5번 · 4대문 안 21층 2개 동, 입주 2030년">
    <h3>경희궁 에피트 단지 개요</h3>
    <h4>규모</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">21층</span>
      <span class="desc">지하 6층~지상 21층 2개 동. 시공은 HL디앤아이한라.</span></div>
    <h4>입주 예정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2030.8</span>
      <span class="desc">당첨부터 입주까지 4년 가까이 걸린다.</span></div>
    <h4>견본주택</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">증산동</span>
      <span class="desc">은평구에 연다. 종로 현장이 아니다.</span></div>
    <p class="cap">규모·시공·견본주택은 파이낸셜뉴스·한국금융신문·대한경제(10~11월) 보도, 입주 예정은 청약 정보 사이트 기준입니다.</p>
  </div>
  <p>단지는 지하 6층~지상 21층 2개 동으로, 돈의문 재개발의 마지막 단지로 소개됩니다. 시공은 HL디앤아이한라이고 견본주택은 종로가 아니라 은평구 증산동에 엽니다. 입주 예정은 2030년 8월로 안내돼 있어 당첨 뒤 4년 가까이 기다려야 합니다.</p>

  <h3>경희궁 에피트 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 경희궁 에피트 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="ghe-06-check.png" src="../images/cards/report/ghe-06-check.png" alt="체크포인트 카드 · 1. 분상제 미적용 시세 비교, 2. 일정은 공고문으로, 3. 투기과열지구 1순위 조건" loading="lazy" width="1080" height="1080">
    <figcaption>경희궁 에피트 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>분상제 미적용, 시세와 비교부터</strong>. 상한제가 없어 시세 차익을 전제로 넣으면 안 됩니다. 옆 단지 실거래가와 직접 비교해 보십시오.</li>
    <li><strong>일정은 공고문으로</strong>. 이미 한 차례 미뤄졌습니다. 특공 25일·1순위 26일 안내는 청약홈 공고문과 대조하십시오.</li>
    <li><strong>투기과열지구 1순위 조건</strong>. 통장 가입 기간·예치금·세대주 요건, 재당첨 제한은 내 청약통장 순위(가입)확인서와 공고문으로 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>경희궁 에피트</strong>는 종로구 교남동 돈의문2구역 228가구(일반분양 135가구) 단지로, 전용 84㎡ 최고 분양가가 25억7,484만원(3.3㎡당 7,450만원)으로 보도됐습니다. 특공 25일·1순위 26일로 안내돼 있지만 일정은 공고문으로 확인해야 합니다. <span class="mark">분양가상한제 단지가 아니므로 '당첨=시세 차익'으로 보지 말고 자금 계획부터 세우십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 단지 개요는 파이낸셜뉴스(2026-10-15)·한국금융신문(2026-10-23)·대한경제(2026-11-11), 84㎡ 평균 분양가는 스트레이트뉴스, 타입별 최고가·일정은 청약 정보 사이트(당근부동산) 정리 기준입니다. 최종 조건은 입주자모집공고문과 청약홈으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 파이낸셜뉴스 서울 4대문 안 마지막 퍼즐 경희궁 에피트 11월 분양(2026-10-15) · 한국금융신문 돈의문2구역 경희궁 에피트 11월 분양(2026-10-23) · 대한경제 경희궁자이 잇는 돈의문 새 주거지(2026-11-11) · 스트레이트뉴스 [새집] 서울 등 전국 11곳 5000가구 · 머니투데이 청약 기다렸는데 분양가도 껑충(2026-10-06) · 경제시그널 돈의문 재개발 마지막 단지 · 당근부동산 경희궁 에피트 청약 정보<br>
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
for v, h in zip((118241, 189843, 251744), (39.5, 63.4, 84.1)):
    assert round(v / 257484 * 86, 1) == h, (v, h)
for v, w in zip((135, 93), (59.2, 40.8)):
    assert round(v / 228 * 100, 1) == w, (v, w)
assert 135 + 93 == 228
for v, w in zip((251744, 247751), (97.8, 96.2)):
    assert round(v / 257484 * 100, 1) == w, (v, w)
KW = "경희궁 에피트"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("경희궁에피트")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
