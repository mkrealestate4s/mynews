# -*- coding: utf-8 -*-
"""리포트 #123 (2026-11-12) 재건축 용적률 1.2배 특례. #122를 복제해 교체한다.

메인 검색어: 재건축 용적률 1.2배

수치와 검산
  사건일과 오늘의 간격: 국토부 비공개 국무회의 보고 보도 11/10~11(서울경제, 1~2일 전, 리드) · 뉴스핌 연내 법제화 불투명 11/6(6일 전).
  방안(서울경제 11/10~11): 민간 재건축·재개발 용적률 법적 상한의 1.2배 · 특례 여부는 중앙도시계획위원회가 먼저 판단 → 지방도시계획위원회 세부 심의
    3년 한시 · 강남·서초·송파·용산 제외 방침 · 여당은 국회 계류 도정법 개정안에 수정안 반영 검토 · 국민의힘은 공공과 같은 1.3배 주장
  9/1 여당 국토위, 야당에 민간 정비사업 1.2배 제안(네이트·뉴스1)
  법적 상한(국토계획법 시행령 제85조): 1종 200 · 2종 250 · 3종 300 · 준주거 500 → 1.2배 240 · 300 · 360 · 600
    대시보드 컬럼(600→86): 34.4 43 51.6 86
    카드2 가로(360→100): 250 69.4 · 300 83.3 · 360 100
    카드4 가로(390→100): 300 76.9 · 360 92.3 · 390 100

단정하지 않은 것
  · 법 개정 전 방안. 국회 통과·시행일 미정 · 1.2배와 1.3배 중 어느 쪽인지 미정
  · 우리 단지 적용 여부는 중도위 판단이라 일반론으로 답하지 않는다 · 서울시 조례 용적률은 법적 상한보다 낮다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-11-eunma-jaechohwan.html"
DST = ROOT / "posts/2026-11-12-floor-ratio-12.html"
SLUG, PRE = "2026-11-12-floor-ratio-12", "far"
NO, DATE = 123, "2026-11-12"
PREV_SLUG = "emj-"
BANNED = ["은마", "재초환", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "재건축 용적률 1.2배, 강남3구·용산은 빠진다"
DESC = ("재건축 용적률 1.2배 특례 방안이 국무회의에 보고됐다는 보도가 나왔습니다. "
        "민간 재건축·재개발 용적률을 법적 상한의 1.2배까지, 3년 한시로 풀되 강남·서초·송파·용산은 뺀다는 내용입니다. "
        "용도지역별 숫자, 1.3배 주장과의 차이, 아직 확정 아닌 부분을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="3종 주거 법적 상한 300%가 1.2배면 360%. 3년 한시, 중앙도시계획위원회가 먼저 판단. 국회 통과 전 방안입니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">재건축 용적률 1.2배<br>강남3구·용산은 빠진다</h1>
  <p class="sub"><strong>재건축 용적률 1.2배</strong> 특례 방안이 국무회의에 보고됐다는 보도가 나왔습니다. 민간 재건축·재개발 용적률을 <strong>법적 상한의 1.2배</strong>까지 3년 동안 풀어 주되, 강남·서초·송파·용산은 빼는 방향입니다. <span class="mark">다만 아직 국회를 통과하지 않은 방안이고, 단지마다 중앙도시계획위원회가 먼저 적용 여부를 판단합니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 용적률 특례</div><div class="kw">1.2배</div>
      <p>법적 상한의 <strong>1.2배</strong>까지 (방안).</p></div>
    <div class="kcard"><div class="hot">3종 주거</div><div class="kw">360%</div>
      <p>법적 상한 <strong>300%</strong>의 1.2배.</p></div>
    <div class="kcard"><div class="hot">기간</div><div class="kw">3년 한시</div>
      <p>시행 뒤 <strong>3년</strong>만 적용.</p></div>
    <div class="kcard"><div class="hot">제외 지역</div><div class="kw">4개 구</div>
      <p>강남·서초·송파·<strong>용산</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>1.2배를 적용하면, 용도지역별 용적률 (%)</h3>
    <span class="badge">준주거는 600%까지</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:34.4%">240</div><div class="barv" style="--h:34.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:43%">300</div><div class="barv" style="--h:43%"></div></div>
      <div class="col"><div class="v gtx" style="--h:51.6%">360</div><div class="barv" style="--h:51.6%"></div></div>
      <div class="col dim"><div class="v" style="--h:86%">600</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>1종 일반</span><span>2종 일반</span><span>3종 일반</span><span>준주거</span></div>
    <p class="cap">국토계획법 시행령의 용도지역별 용적률 상한(1종 200%, 2종 250%, 3종 300%, 준주거 500%)에 1.2를 곱한 값입니다. 재건축 아파트가 가장 많은 3종 일반주거를 강조했습니다. 막대 길이는 최댓값 600%를 기준으로 맞췄습니다. 서울시 조례 용적률은 이보다 낮습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 재건축 용적률 1.2배, 강남3구·용산은 빠진다"),
    ("02-zone", "3종 주거는 300%에서 360%로"),
    ("03-rule", "누가 받나: 3년, 4개 구 제외, 중도위 판단"),
    ("04-gap", "1.2배냐 1.3배냐, 아직 안 정해졌다"),
    ("05-when", "보고는 됐지만 법은 아직"),
    ("06-check", "재건축 용적률 1.2배 체크 3가지"),
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

ARTICLE = '''<article data-tags="재건축용적률1.2배,재건축용적률,용적률특례,재개발용적률,도정법개정안,정비사업,재건축,강북재건축,중앙도시계획위원회,용적률완화">
  <h2>재건축 용적률 1.2배, 강남3구·용산은 빠진다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 재건축 용적률 1.2배, 강남3구·용산은 빠진다"></span>

  <p>재건축 용적률 1.2배 특례 방안이 국무회의에 보고됐다는 보도가 이번 주 나왔습니다. 서울경제에 따르면 국토교통부는 비공개 국무회의에서 민간 재건축·재개발 용적률을 법적 상한의 1.2배까지 높이고, 적용 여부는 중앙도시계획위원회가 먼저 정하는 방안을 보고했습니다. 특례는 3년 한시이고 강남·서초·송파·용산은 빠질 방침입니다. <span class="mark">아직 법이 바뀐 것이 아니라, 국회에 걸려 있는 도시정비법 개정안에 넣을 수정안 단계입니다.</span></p>

  <h3>재건축 용적률 1.2배, 숫자로 보면</h3>
  <div class="chart" data-img="카드뉴스 2번 · 3종 주거는 300%에서 360%로">
    <h3>법적 상한과 1.2배 적용 후 용적률 (%)</h3>
    <div class="bar"><label>2종 지금</label>
      <div class="rail"><div class="fill gray" style="width:69.4%">250</div></div></div>
    <div class="bar"><label>2종 1.2배</label>
      <div class="rail"><div class="fill gray" style="width:83.3%">300</div></div></div>
    <div class="bar"><label>3종 지금</label>
      <div class="rail"><div class="fill gray" style="width:83.3%">300</div></div></div>
    <div class="bar"><label>3종 1.2배</label>
      <div class="rail"><div class="fill" style="width:100%">360</div></div></div>
    <p class="cap">국토계획법 시행령의 법적 상한 기준입니다. 막대 길이는 최댓값 360%를 기준으로 맞췄습니다. 실제 단지별 용적률은 정비계획과 심의에서 정해집니다.</p>
  </div>
  <p>용적률은 땅 넓이 대비 지을 수 있는 건물 바닥면적 합계입니다. 3종 일반주거지역의 법적 상한은 300%이고, 1.2배면 360%가 됩니다. 같은 땅에 지을 수 있는 연면적이 20% 늘어난다는 뜻입니다. <span class="mark">늘어난 면적은 일반분양 물량으로 돌릴 수 있어 사업성이 낮은 단지일수록 효과가 큽니다.</span> 다만 서울은 조례로 정한 기준 용적률이 법적 상한보다 낮아, 단지마다 출발점이 다릅니다.</p>

  <h3>재건축 용적률 1.2배, 누가 받나</h3>
  <div class="chart" data-img="카드뉴스 3번 · 누가 받나: 3년, 4개 구 제외, 중도위 판단">
    <h3>보도된 특례 조건</h3>
    <h4>적용 기간</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3년</span>
      <span class="desc">시행 뒤 3년 동안만 적용하는 한시 특례.</span></div>
    <h4>제외 지역</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4개 구</span>
      <span class="desc">강남·서초·송파·용산은 대상에서 빠질 방침.</span></div>
    <h4>판단 순서</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">중도위</span>
      <span class="desc">구청 입안 → 중앙도시계획위원회 판단 → 지방위원회 세부 심의.</span></div>
    <p class="cap">서울경제(11월 10~11일) 보도 기준이며 법 개정 전 방침입니다.</p>
  </div>
  <p>특례를 받으려면 구청이 정비계획을 입안한 뒤 국토부 중앙도시계획위원회가 먼저 적용 여부를 판단하고, 그다음 서울시 같은 지방도시계획위원회가 세부 계획을 심의하는 구조로 보도됐습니다. 이를 두고 심의가 한 단계 더 늘어난다는 지적도 나왔습니다. <span class="mark">강남3구와 용산이 빠지면 서울에서는 노원·도봉·성북 같은 강북권 노후 단지가 주로 대상이 됩니다.</span> 다만 개별 단지가 실제로 받을지는 위원회 판단이라 지금 단정할 수 없습니다.</p>

  <h3>1.2배냐 1.3배냐, 아직 안 정해졌다</h3>
  <div class="chart" data-img="카드뉴스 4번 · 1.2배냐 1.3배냐, 아직 안 정해졌다">
    <h3>3종 일반주거 기준, 안별 용적률 (%)</h3>
    <div class="bar"><label>지금 법적 상한</label>
      <div class="rail"><div class="fill gray" style="width:76.9%">300</div></div></div>
    <div class="bar"><label>정부·여당 1.2배</label>
      <div class="rail"><div class="fill" style="width:92.3%">360</div></div></div>
    <div class="bar"><label>국민의힘 1.3배</label>
      <div class="rail"><div class="fill gray" style="width:100%">390</div></div></div>
    <p class="cap">국민의힘은 공공 정비사업과 같은 1.3배를 주장해 왔다고 보도됐습니다. 막대 길이는 최댓값 390%를 기준으로 맞췄습니다.</p>
  </div>
  <p>정부·여당은 1.2배, 국민의힘은 공공 정비사업과 같은 1.3배를 주장해 와서 국회 논의가 남아 있습니다. 3종 기준으로 두 안의 차이는 30%p입니다. 여당 안에서도 민간 정비사업 용적률 완화에 신중해야 한다는 목소리가 있다고 전해졌습니다.</p>

  <h3>보고는 됐지만 법은 아직</h3>
  <div class="chart" data-img="카드뉴스 5번 · 보고는 됐지만 법은 아직">
    <h3>재건축 용적률 1.2배, 지금까지 흐름</h3>
    <h4>여당 제안</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9월 1일</span>
      <span class="desc">여당 국토위가 야당에 민간 정비사업 1.2배를 제안.</span></div>
    <h4>법제화 전망</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월 6일</span>
      <span class="desc">연내 법 개정 통과가 불투명하다는 보도.</span></div>
    <h4>국무회의 보고</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">이번 주</span>
      <span class="desc">국토부 방안 보고 보도. 도정법 수정안 반영 검토.</span></div>
    <p class="cap">뉴스1(9월 1일), 뉴스핌(11월 6일), 서울경제(11월 10~11일) 보도 기준입니다. 시행일은 정해지지 않았습니다.</p>
  </div>
  <p>뉴스핌은 11월 6일 민간 정비사업 용적률 1.2배 방향은 잡혔지만 연내 법 개정 통과는 불투명하다고 전했습니다. 법이 통과돼도 시행령과 심의 기준이 나와야 실제 신청이 가능합니다. <span class="mark">지금 조합 단계에서 할 일은 정비계획 일정표에 특례를 반영할 여지가 있는지 확인하는 정도입니다.</span></p>

  <h3>재건축 용적률 1.2배 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 재건축 용적률 1.2배 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="far-06-check.png" src="../images/cards/report/far-06-check.png" alt="체크포인트 카드 · 1. 국회 통과 전 방안, 2. 강남3구·용산 제외, 3. 우리 단지는 중도위 판단" loading="lazy" width="1080" height="1080">
    <figcaption>재건축 용적률 1.2배 기사를 보고 확인할 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>국회 통과 전 방안</strong>. 국무회의 보고와 수정안 검토 단계입니다. 배수(1.2배·1.3배)와 시행일 모두 미정입니다.</li>
    <li><strong>강남3구·용산 제외</strong>. 보도된 방침대로면 강남·서초·송파·용산 단지는 대상이 아닙니다.</li>
    <li><strong>우리 단지는 위원회 판단</strong>. 같은 구라도 중앙도시계획위원회 판단을 거쳐야 합니다. 진행 상황은 조합·구청·정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>재건축 용적률 1.2배</strong> 특례는 민간 재건축·재개발 용적률을 법적 상한의 1.2배까지, 3년 동안 풀어 주는 방안입니다. 3종 주거라면 300%가 360%가 됩니다. 강남·서초·송파·용산은 빠지고, 단지별로 중앙도시계획위원회가 먼저 판단합니다. <span class="mark">아직 국회를 통과하지 않았으니 지금은 확정이 아니라 방향으로 읽으십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 특례 방안은 서울경제(2026-11-10~11) 보도, 법제화 전망은 뉴스핌(2026-11-06), 용도지역별 상한은 국토계획법 시행령 기준입니다. 법 개정 전 방안이므로 확정 내용은 국토교통부 발표와 국회 의결로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 서울경제 용적률 1.2배 높인다면서…정부 심의 또 받으라는 국토부(2026-11) · 서울경제 재개발 용적률 1.2배 높인다더니…'옥상옥 심사기구'(2026-11) · 뉴스핌 정비사업 용적률 1.2배 허용한다더니…연내 법제화 '안갯속'(2026-11-06) · 뉴스1 與 국토위, 野에 '민간 정비사업 용적률 1.2배' 제안(2026-09-01) · 국토의 계획 및 이용에 관한 법률 시행령 제85조<br>
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
for v, h in zip((240, 300, 360, 600), (34.4, 43, 51.6, 86)):
    assert round(v / 600 * 86, 1) == h, (v, h)
for v, w in zip((250, 300, 360), (69.4, 83.3, 100)):
    assert round(v / 360 * 100, 1) == w, (v, w)
for v, w in zip((300, 360, 390), (76.9, 92.3, 100)):
    assert round(v / 390 * 100, 1) == w, (v, w)
KW = "재건축 용적률 1.2배"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("재건축용적률1.2배")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
