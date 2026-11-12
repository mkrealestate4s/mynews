# -*- coding: utf-8 -*-
"""리포트 #124 (2026-11-13) 목동4단지 재건축 시공사 입찰 마감 D-3. #123을 복제해 교체한다.

메인 검색어: 목동4단지 재건축

수치와 검산
  사건일과 오늘의 간격: 입찰 마감 11/16(월) 14시, 오늘에서 3일 뒤(리드) · 현설 9/30(배경) · 단독 응찰 관측 보도 9/30~10월.
  4단지: 1986년 준공 1,382가구 → 최고 49층 2,436가구(공공 293) · 용적률 299.94% (머니투데이방송·뉴시스)
  입찰: 공고 9/21 · 현설 9/30 현대·포스코이앤씨·HDC현산·제일건설 4개사 · 마감 11/16 14시 · 개봉 15시 · 보증금 600억(현금 300+보증보험 300)
  공사비 1조6,389억4,000만원 · 3.3㎡당 1,010만원(목동 첫 1천만원대). 비교 10단지 990 · 12·13단지 980 · 8단지 965 (#98 출처)
  목동 선정: 6단지 DL 86.2% · 10단지 현대 1,624명 중 1,557 95.9% · 13단지 삼성 1,884명 중 1,803 95.7%
    대시보드 컬럼(2436→86): 1382 48.8 · 2436 86 · 1054 37.2 · 293 10.3
    카드3 가로(1010→100): 990 98.0 · 980 97.0 · 965 95.5

단정하지 않은 것
  · 현대건설 단독 응찰은 관측(제안서 착수 보도)이지 결과가 아니다 · 계획 가구수·층수는 확정 전
  · 단독이면 유찰 뒤 재입찰·수의계약 경로는 10단지 사례로만 설명 · 8단지 진행은 보도가 엇갈려 쓰지 않는다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-12-floor-ratio-12.html"
DST = ROOT / "posts/2026-11-13-mokdong4.html"
SLUG, PRE = "2026-11-13-mokdong4", "mk4"
NO, DATE = 124, "2026-11-13"
PREV_SLUG = "far-"
BANNED = ["1.2배", "중도위", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "목동4단지 재건축, 16일 입찰 마감 경쟁 붙을까"
DESC = ("목동4단지 재건축 시공사 입찰이 11월 16일(월) 오후 2시 마감됩니다. "
        "3.3㎡당 1,010만원, 공사비 1조6,389억원으로 목동에서 가장 높은 조건입니다. "
        "일정, 공사비 비교, 현설 4개사와 단독 응찰 관측, 목동 다른 단지 결과를 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="11월 16일 14시 마감, 15시 개봉. 1,382가구가 최고 49층 2,436가구로. 3.3㎡당 1,010만원은 목동 최고입니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">목동4단지 재건축<br>16일 입찰 마감, 경쟁 붙을까</h1>
  <p class="sub"><strong>목동4단지 재건축</strong> 시공사 입찰이 <strong>11월 16일(월) 오후 2시</strong>에 마감됩니다. 3.3㎡당 1,010만원, 목동에서 처음 1천만원을 넘긴 공사비입니다. <span class="mark">현장설명회에는 4개사가 왔지만, 실제 입찰서가 몇 장 들어올지는 마감 날 확인됩니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 입찰 마감</div><div class="kw">11/16</div>
      <p>월요일 <strong>오후 2시</strong>, 3시 개봉.</p></div>
    <div class="kcard"><div class="hot">3.3㎡당 공사비</div><div class="kw">1,010만</div>
      <p>목동 재건축 중 <strong>가장 높다</strong>.</p></div>
    <div class="kcard"><div class="hot">예정 공사비</div><div class="kw">1.64조</div>
      <p>약 <strong>1조6,389억원</strong>.</p></div>
    <div class="kcard"><div class="hot">계획 가구</div><div class="kw">2,436</div>
      <p>지금 1,382가구, <strong>최고 49층</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>목동4단지 재건축, 지금과 계획 (가구)</h3>
    <span class="badge">1,054가구 늘어난다</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:48.8%">1,382</div><div class="barv" style="--h:48.8%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">2,436</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:37.2%">1,054</div><div class="barv" style="--h:37.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:10.3%">293</div><div class="barv" style="--h:10.3%"></div></div>
    </div>
    <div class="collbl"><span>지금</span><span>계획</span><span>늘어나는 수</span><span>그중 공공</span></div>
    <p class="cap">머니투데이방송·뉴시스 보도 기준입니다. 1986년 준공한 1,382가구를 용적률 299.94%, 최고 49층 2,436가구(공공 293가구 포함)로 짓는 계획입니다. 막대 길이는 최댓값 2,436가구를 기준으로 맞췄습니다. 가구수·층수는 심의 단계마다 바뀔 수 있어 확정 전입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 목동4단지 재건축, 16일 입찰 마감 경쟁 붙을까"),
    ("02-when", "목동4단지 재건축 입찰, 16일 오후 2시 마감"),
    ("03-cost", "3.3㎡당 1,010만원, 목동에서 가장 높다"),
    ("04-bid", "현설은 4곳, 입찰은 몇 곳?"),
    ("05-vote", "목동 앞선 단지들, 찬성률 86~96%"),
    ("06-check", "목동4단지 재건축 체크 3가지"),
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

ARTICLE = '''<article data-tags="목동4단지재건축,목동4단지,목동재건축,목동시공사선정,양천구재건축,현대건설,목동신시가지,재건축시공사,재건축입찰,목동아파트">
  <h2>목동4단지 재건축, 16일 입찰 마감 경쟁 붙을까</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 목동4단지 재건축, 16일 입찰 마감 경쟁 붙을까"></span>

  <p>목동4단지 재건축 시공사 입찰이 다음 주 월요일(11월 16일) 오후 2시에 마감됩니다. 조합은 같은 날 오후 3시에 제안서를 엽니다. 예정 공사비는 약 1조6,389억원, 3.3㎡당 1,010만원으로 목동 재건축 가운데 처음으로 1천만원을 넘겼습니다. <span class="mark">목동은 지금까지 시공사 선정이 단독 응찰로 이어져 왔고, 4단지가 첫 경쟁입찰이 될지가 이번 마감의 관전 포인트입니다.</span></p>

  <h3>목동4단지 재건축 입찰, 16일 오후 2시 마감</h3>
  <div class="chart" data-img="카드뉴스 2번 · 목동4단지 재건축 입찰, 16일 오후 2시 마감">
    <h3>목동4단지 시공사 입찰 일정</h3>
    <h4>입찰 공고</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9월 21일</span>
      <span class="desc">조합 시공사 입찰 공고. 보증금 600억원.</span></div>
    <h4>현장설명회</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9월 30일</span>
      <span class="desc">현대건설·포스코이앤씨·HDC현대산업개발·제일건설 4개사 참석.</span></div>
    <h4>입찰 마감</h4>
    <div class="statrow"><span class="big gtx" style="white-space:nowrap">11월 16일</span>
      <span class="desc">오후 2시 마감, 오후 3시 제안서 개봉.</span></div>
    <p class="cap">머니투데이방송(9월 21·30일) 보도 기준입니다. 입찰보증금 600억원은 현금 300억원과 보증보험증권 300억원으로 나뉩니다.</p>
  </div>
  <p>입찰보증금은 600억원입니다. 현금 300억원과 보증보험증권 300억원으로 나눠 내는 조건입니다. 정비사업 입찰은 보통 현장설명회 참석을 입찰 조건으로 둡니다. 이번에도 그렇다면 후보는 현설 4개사입니다. 마감 뒤 몇 곳이 냈는지는 개봉 당일 조합 공지와 보도로 확인됩니다.</p>

  <h3>목동4단지 재건축 공사비, 목동에서 가장 높다</h3>
  <div class="chart" data-img="카드뉴스 3번 · 3.3㎡당 1,010만원, 목동에서 가장 높다">
    <h3>목동 단지별 3.3㎡당 예정 공사비 (만원)</h3>
    <div class="bar"><label>4단지</label>
      <div class="rail"><div class="fill" style="width:100%">1,010</div></div></div>
    <div class="bar"><label>10단지</label>
      <div class="rail"><div class="fill gray" style="width:98%">990</div></div></div>
    <div class="bar"><label>12·13단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>8단지</label>
      <div class="rail"><div class="fill gray" style="width:95.5%">965</div></div></div>
    <p class="cap">모두 같은 항목(3.3㎡당 예정 공사비, 만원)이라 한 축에 놓았습니다. 막대 길이는 최댓값 1,010만원을 기준으로 맞췄습니다. 머니투데이방송·머니투데이(9~10월) 보도 기준입니다.</p>
  </div>
  <p>목동 단지들의 3.3㎡당 예정 공사비는 965만~1,010만원으로 거의 같은 선입니다. 4단지가 그중 가장 높고, 차이는 45만원 안쪽입니다. <span class="mark">공사비 조건만 보면 4단지가 건설사에 가장 나은 조건이라는 뜻입니다.</span> 그런데도 경쟁이 붙을지는 아직 장담할 수 없습니다.</p>

  <h3>현설은 4곳, 입찰은 몇 곳?</h3>
  <div class="chart" data-img="카드뉴스 4번 · 현설은 4곳, 입찰은 몇 곳?">
    <h3>목동4단지 입찰 전 상황</h3>
    <h4>현장설명회 참석</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4개사</span>
      <span class="desc">현대·포스코이앤씨·HDC현산·제일건설.</span></div>
    <h4>제안서 착수 보도</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">1곳</span>
      <span class="desc">현대건설만 제안서 작업에 착수했다는 업계 관측.</span></div>
    <h4>한 곳만 내면</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">유찰</span>
      <span class="desc">재입찰 뒤에도 단독이면 수의계약으로 갈 수 있다.</span></div>
    <p class="cap">머니투데이방송(9월 30일) 등 업계 관측 보도 기준이며 입찰 결과가 아닙니다.</p>
  </div>
  <p>현장설명회 직후 보도는 현대건설만 제안서 작업에 착수했다고 전했고, 포스코이앤씨는 다른 단지로 눈을 돌리고 있다는 관측도 나왔습니다. <span class="mark">이건 관측이지 입찰 결과가 아닙니다.</span> 한 곳만 입찰하면 유찰되고, 재입찰에서도 단독이면 조합이 수의계약으로 갈 수 있습니다. 목동10단지가 이 경로를 밟아 두 차례 유찰 뒤 현대건설을 우선협상대상자로 정했습니다.</p>

  <h3>목동 앞선 단지들, 찬성률 86~96%</h3>
  <div class="chart" data-img="카드뉴스 5번 · 목동 앞선 단지들, 찬성률 86~96%">
    <h3>목동 시공사 선정 찬성률 (%)</h3>
    <div class="bar"><label>6단지 DL이앤씨</label>
      <div class="rail"><div class="fill gray" style="width:86.2%">86.2</div></div></div>
    <div class="bar"><label>13단지 삼성물산</label>
      <div class="rail"><div class="fill gray" style="width:95.7%">95.7</div></div></div>
    <div class="bar"><label>10단지 현대건설</label>
      <div class="rail"><div class="fill" style="width:95.9%">95.9</div></div></div>
    <p class="cap">투표자 대비 찬성 비율입니다. 10단지는 1,624명 중 1,557명, 13단지는 1,884명 중 1,803명입니다. 막대 길이는 100%를 기준으로 맞췄습니다. 헤럴드경제(6월)·머니투데이방송(10월 18일·11월 7일) 보도 기준입니다.</p>
  </div>
  <p>목동에서 시공사가 정해진 곳은 6단지(DL이앤씨, 6월), 10단지(현대건설, 10월 18일), 13단지(삼성물산, 11월 7일)입니다. 세 곳 모두 찬성률이 86~96%로 높았습니다. 12단지(GS건설)도 선정 절차가 진행 중입니다. <span class="mark">4단지는 현대건설이 목동에서 두 번째 시공권을 가져갈지, 다른 회사가 들어와 첫 경쟁이 될지가 갈림길입니다.</span></p>

  <h3>목동4단지 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 목동4단지 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="mk4-06-check.png" src="../images/cards/report/mk4-06-check.png" alt="체크포인트 카드 · 1. 16일 개봉 결과, 2. 단독 응찰은 관측, 3. 가구수는 확정 전" loading="lazy" width="1080" height="1080">
    <figcaption>목동4단지 재건축 입찰 마감을 앞두고 확인할 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>16일 오후 3시 개봉 결과</strong>. 몇 곳이 입찰서를 냈는지가 이번 주 핵심입니다. 조합 공지로 확인하십시오.</li>
    <li><strong>단독 응찰은 관측</strong>. "현대건설 단독"은 업계 관측입니다. 유찰되면 재입찰 일정이 새로 잡힙니다.</li>
    <li><strong>2,436가구는 확정 전</strong>. 계획 가구수·층수는 심의 단계마다 바뀔 수 있습니다. 조합원 지위 양도와 거래 제한은 조합·양천구청·정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>목동4단지 재건축</strong> 시공사 입찰은 11월 16일 오후 2시에 마감하고 오후 3시에 제안서를 엽니다. 예정 공사비 약 1조6,389억원, 3.3㎡당 1,010만원으로 목동에서 가장 높은 조건이고, 1,382가구를 최고 49층 2,436가구로 다시 짓는 계획입니다. <span class="mark">현설 4개사 중 몇 곳이 실제로 입찰하는지가 목동 첫 경쟁입찰 여부를 가릅니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 입찰 일정·공사비는 머니투데이방송(2026-09-21·30)·뉴시스(2026-09-14) 보도, 단지별 찬성률은 헤럴드경제(2026-06-28)·머니투데이방송(2026-10-18·11-07) 보도 기준입니다. 입찰 결과와 계획 가구수는 확정 전이며 조합 공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 머니투데이방송 '공사비 1.6조' 목동4단지 시공사 찾는다(2026-09-21) · 머니투데이방송 목동4단지 현설에 현대·포스코 등 4개사(2026-09-30) · 뉴시스 목동 재건축 공사비도 '평당 1000만원' 시대(2026-09-14) · 머니투데이방송 목동10단지 시공사 선정(2026-10-18) · 머니투데이방송 목동13단지 시공사 선정(2026-11-07) · 헤럴드경제 목동6단지 시공사 선정(2026-06-28)<br>
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
for v, h in zip((1382, 2436, 1054, 293), (48.8, 86, 37.2, 10.3)):
    assert round(v / 2436 * 86, 1) == h, (v, h)
for v, w in zip((1010, 990, 980, 965), (100, 98.0, 97.0, 95.5)):
    assert round(v / 1010 * 100, 1) == w, (v, w)
assert 2436 - 1382 == 1054
assert round(1557 / 1624 * 100, 1) == 95.9 and round(1803 / 1884 * 100, 1) == 95.7
KW = "목동4단지 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("목동4단지재건축")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
