# -*- coding: utf-8 -*-
"""리포트 #115 (2026-11-04) 가락우성1차 재건축 2차 현설도 대우건설 단독. #114를 복제해 교체한다.

메인 검색어: 가락우성1차 재건축

수치와 검산
  사건일과 오늘의 간격: 가락우성1차 2차 현설 11/3(어제) → 1일. 쌍문한양1차 2차 입찰공고 11/3(어제) · 2차 현설 11/11(D-7).
  가락우성1차 (위클리한국주택경제 11/3 · 파이낸셜뉴스 10/20 보도):
    송파구 가락동 96-1 일대 3만5,043.70㎡ · 계획 967가구 · 예정 공사비 5,019억9,500만원 · 3.3㎡당 985만원
    1차 입찰 대우건설 단독 참여로 유찰 · 2차 현설 11/3 대우건설 단독 · 조합이 하이엔드 브랜드 적용을 참여 조건으로
    대우는 '써밋' 제안 예정(보도) · 총회 이르면 2027년 2월 말(보도, 예정)
  쌍문한양1차 (위클리한국주택경제 11/3): 도봉구 · 2차 입찰공고 11/3 · 1차 현설 10/30 DL이앤씨 단독
    · 일반경쟁입찰 · 입찰보증금 200억원 · 지하4~지상38층 1,166세대 · 2차 현설 11/11
  목동 3.3㎡당 공사비(만원, #98·#112): 4단지 1,010 · 10단지 990 · 9단지 980 · 8단지 965
  목동 시공사 정해진 5곳 모두 단독 응찰(#112, 뉴시스 10/20 · 서울경제TV 10/28)
  대시보드 세로 (1,010 → 86%): 990 84.3 · 985 83.9 · 980 83.4 · 965 82.2
  카드3 가로 (1,010 → 100): 98.0 · 97.5 · 97.0 · 95.5
  카드4 가로 (1,166 → 100): 967 → 82.9 · 차이 199세대

단정하지 않은 것
  · 967가구·1,166세대·38층은 계획(확정 전) · 대우건설·DL이앤씨 선정은 결과가 아님(관측)
  · 두 번 유찰 뒤 수의계약 전환은 '가능'이지 자동이 아님(총회 의결 필요). 조합 공지로 확인
  · 조합원 지위 양도 제한 → 조합·구청·정비사업 정보몽땅 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-03-nov-cheongyak.html"
SLUG, PRE = "2026-11-04-garak-woosung1", "gw1104"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 115, "2026-11-04"
PREV_SLUG = "nov1103-"
BANNED = ["한화포레나", "견본주택 5곳", "4,216가구"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "가락우성1차 재건축, 두 번 다 대우건설 혼자 왔다"
DESC = ("가락우성1차 재건축 시공사 2차 현장설명회(11월 3일)에도 대우건설만 참석했습니다. 1차 입찰은 대우건설 단독 참여로 유찰됐습니다. "
        "송파구 가락동 계획 967가구, 예정 공사비 5,019억원, 3.3㎡당 985만원입니다. 같은 날 도봉구 쌍문한양1차도 DL이앤씨 단독으로 2차 입찰공고를 냈습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="2차 현설도 대우건설 단독. 공사비 5,019억원, 3.3㎡당 985만원. 두 번 유찰되면 수의계약으로 갈 수 있습니다. 쌍문한양1차까지 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">가락우성1차 재건축,<br>두 번 다 대우건설 혼자</h1>
  <p class="sub"><strong>가락우성1차 재건축</strong> 시공사 2차 현장설명회가 <strong>어제(11월 3일)</strong> 열렸고 이번에도 <strong>대우건설만</strong> 왔습니다. 계획 967가구, 예정 공사비 <strong>5,019억원</strong>(3.3㎡당 985만원)입니다. <span class="mark">같은 날 도봉구 쌍문한양1차도 DL이앤씨 단독 참석 뒤 2차 입찰공고를 냈습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 가락우성1차</div><div class="kw">11월 3일</div>
      <p>2차 현설도 <strong>대우 단독</strong>.</p></div>
    <div class="kcard"><div class="hot">예정 공사비</div><div class="kw">5,019억</div>
      <p>3.3㎡당 <strong>985만원</strong>.</p></div>
    <div class="kcard"><div class="hot">계획 규모</div><div class="kw">967가구</div>
      <p>송파구 가락동, <strong>확정 전</strong>.</p></div>
    <div class="kcard"><div class="hot">쌍문한양1차</div><div class="kw">11월 11일</div>
      <p>2차 현설. <strong>1차는 DL 단독</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>3.3㎡당 예정공사비 비교 (만원)</h3>
    <span class="badge">가락우성1차 985</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">1,010</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:84.3%">990</div><div class="barv" style="--h:84.3%"></div></div>
      <div class="col"><div class="v gtx" style="--h:83.9%">985</div><div class="barv" style="--h:83.9%"></div></div>
      <div class="col dim"><div class="v" style="--h:83.4%">980</div><div class="barv" style="--h:83.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:82.2%">965</div><div class="barv" style="--h:82.2%"></div></div>
    </div>
    <div class="collbl"><span>목동4</span><span>목동10</span><span>가락우성1차</span><span>목동9</span><span>목동8</span></div>
    <p class="cap">모두 3.3㎡당 예정공사비(만원)라 한 축에 놓았습니다. 막대 높이는 최댓값 1,010만원을 기준으로 맞췄습니다. 가락우성1차는 파이낸셜뉴스(10월 20일), 목동은 머니투데이방송(10월 6~23일) 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 가락우성1차 재건축, 두 번 다 대우건설 혼자"),
    ("02-sched", "가락우성1차 시공사 선정, 어디까지 왔나"),
    ("03-cost", "3.3㎡당 985만원, 목동과 같은 선"),
    ("04-ssang", "쌍문한양1차도 DL이앤씨 혼자, 11일 2차 현설"),
    ("05-rule", "두 번 유찰되면 수의계약으로 갈 수 있다"),
    ("06-check", "가락우성1차 재건축 체크 3가지"),
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

ARTICLE = '''<article data-tags="가락우성1차재건축,가락우성1차,송파재건축,가락동재건축,대우건설,써밋,쌍문한양1차,도봉구재건축,시공사선정,수의계약">
  <h2>가락우성1차 재건축, 두 번 다 대우건설 혼자 왔다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 가락우성1차 재건축, 두 번 다 대우건설 혼자"></span>

  <p>가락우성1차 재건축 시공사 2차 현장설명회가 어제(11월 3일) 열렸고, 이번에도 대우건설 한 곳만 참석했습니다. 앞선 1차 입찰은 대우건설 단독 참여로 유찰됐습니다. <span class="mark">경쟁 없이 같은 회사만 두 번 온 셈입니다.</span></p>

  <h3>가락우성1차 재건축 시공사 선정 일정</h3>
  <div class="chart" data-img="카드뉴스 2번 · 가락우성1차 시공사 선정, 어디까지 왔나">
    <h3>가락우성1차 시공사 선정 진행</h3>
    <h4>1차 입찰</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">유찰</span>
      <span class="desc">대우건설 단독 참여로 경쟁 성립 안 됨.</span></div>
    <h4>2차 현장설명회</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.3</span>
      <span class="desc">어제. 이번에도 대우건설만 참석.</span></div>
    <h4>시공사 선정 총회</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2월 말</span>
      <span class="desc">2027년, 이르면. 보도된 예정이며 확정 일정 아님.</span></div>
    <p class="cap">위클리한국주택경제(11월 3일)·파이낸셜뉴스(10월 20일) 보도 기준입니다. 2차 입찰 마감일은 조합 공고로 확인하십시오.</p>
  </div>
  <p>조합은 시공사의 하이엔드 브랜드 적용을 입찰 참여 조건으로 걸었고, 대우건설은 하이엔드 브랜드 ‘써밋’을 제안할 것으로 전해집니다. 업계에서는 대우건설을 유력 후보로 봅니다. <span class="mark">다만 이건 관측이고, 시공사는 총회 의결로 정해집니다.</span></p>

  <h3>가락우성1차 재건축 공사비, 3.3㎡당 985만원</h3>
  <span class="imgslot" hidden data-img="카드뉴스 3번 · 3.3㎡당 985만원, 목동과 같은 선"></span>
  <p>가락우성1차는 송파구 가락동 96-1번지 일대 3만5,043.70㎡에 공동주택 967가구와 부대시설을 짓는 계획입니다. 예정 공사비는 5,019억9,500만원, 3.3㎡당 985만원입니다. 목동 재건축 단지들(965만~1,010만원)과 거의 같은 선입니다. <span class="mark">공사비가 낮아서 안 온 것이라고 보기는 어렵습니다. 대형사들이 고를 수 있는 사업장이 많아 확실히 이길 곳에만 들어가는 흐름으로 읽힙니다.</span> 목동에서 시공사가 정해진 5곳도 모두 단독 응찰이었습니다.</p>

  <h3>쌍문한양1차도 DL이앤씨 혼자, 11일 2차 현설</h3>
  <div class="chart" data-img="카드뉴스 4번 · 쌍문한양1차도 DL이앤씨 혼자, 11일 2차 현설">
    <h3>두 단지 재건축 후 계획 세대수 (세대)</h3>
    <div class="bar"><label>쌍문한양1차</label>
      <div class="rail"><div class="fill" style="width:100%">1,166</div></div></div>
    <div class="bar"><label>가락우성1차</label>
      <div class="rail"><div class="fill gray" style="width:82.9%">967</div></div></div>
    <p class="cap">두 단지 모두 재건축 후 계획 세대수라 한 축에 놓았습니다. 막대 길이는 1,166세대를 기준으로 맞췄습니다. 심의 단계에서 바뀔 수 있는 계획 수치입니다. 위클리한국주택경제·파이낸셜뉴스 보도 기준입니다.</p>
  </div>
  <p>같은 날 강북에서도 같은 장면이 나왔습니다. 도봉구 쌍문한양1차 재건축조합은 11월 3일 시공자 선정 2차 입찰공고를 냈습니다. 10월 30일 1차 현장설명회에 DL이앤씨만 참석해 경쟁이 성립하지 않았기 때문입니다. 지하 4층~지상 38층 1,166세대 계획이고 일반경쟁입찰, 입찰보증금은 200억원입니다. <span class="mark">2차 현장설명회는 11월 11일입니다.</span></p>

  <h3>두 번 유찰되면 수의계약으로 갈 수 있다</h3>
  <div class="chart" data-img="카드뉴스 5번 · 두 번 유찰되면 수의계약으로 갈 수 있다">
    <h3>단독 응찰이 이어지면 어떻게 되나</h3>
    <h4>1회</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">유찰</span>
      <span class="desc">한 곳만 오면 경쟁입찰이 성립하지 않는다.</span></div>
    <h4>재공고</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2차</span>
      <span class="desc">다시 공고하고 현장설명회를 연다.</span></div>
    <h4>2회 유찰 뒤</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">수의계약</span>
      <span class="desc">총회 의결을 거쳐 그 회사와 계약할 수 있다.</span></div>
    <p class="cap">도시정비법 시행령의 계약 방법 규정에 따른 일반적인 흐름입니다. 단지별 진행은 조합 공고가 정본입니다.</p>
  </div>
  <p>경쟁입찰이 두 번 이상 유찰되면 조합은 총회 의결을 거쳐 수의계약으로 시공사를 정할 수 있습니다. 가락우성1차도 2차 입찰에서 대우건설 한 곳만 입찰서를 내면 이 경로로 넘어갈 가능성이 큽니다. <span class="mark">가능하다는 뜻이지 자동으로 그렇게 된다는 뜻은 아닙니다.</span> 수의계약이 되면 공사비·이주비 같은 조건을 비교할 상대가 없어, 조합원 입장에서는 계약 조건을 더 꼼꼼히 봐야 합니다.</p>

  <h3>가락우성1차 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 가락우성1차 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="gw1104-06-check.png" src="../images/cards/report/gw1104-06-check.png" alt="체크포인트 카드 · 1. 유력은 결과가 아니다, 2. 967가구는 계획 수치, 3. 조합원 지위는 따로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>가락우성1차 재건축 상담에 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>유력은 결과가 아니다</strong>. 대우건설이 두 번 왔다는 것과 시공사로 정해졌다는 것은 다릅니다. 선정은 총회 의결로 끝납니다.</li>
    <li><strong>967가구는 계획 수치</strong>. 심의와 인가 단계에서 바뀔 수 있습니다. 쌍문한양1차 1,166세대·38층도 마찬가지입니다.</li>
    <li><strong>조합원 지위는 따로 확인</strong>. 송파구는 토지거래허가구역이고 재건축 조합원 지위 양도 제한도 단계마다 다릅니다. 조합·송파구청·정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>가락우성1차 재건축</strong>은 1차 입찰 유찰에 이어 11월 3일 2차 현장설명회에도 대우건설만 왔습니다. 계획 967가구, 예정 공사비 5,019억원(3.3㎡당 985만원)이고 총회는 이르면 2027년 2월 말로 전해집니다. 도봉구 쌍문한양1차도 DL이앤씨 단독으로 2차 입찰을 진행하며 11월 11일 현장설명회를 엽니다. <span class="mark">서울 재건축에서 단독 응찰이 흔해지고 있습니다. 두 번 유찰되면 수의계약으로 갈 수 있다는 점을 알고 조합 공고를 보십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 가락우성1차·쌍문한양1차는 위클리한국주택경제(2026-11-03)·파이낸셜뉴스(2026-10-20), 목동 공사비·수주 현황은 머니투데이방송(2026-10-06~23)·뉴시스(2026-10-20)·서울경제TV(2026-10-28) 보도 기준입니다. 계획 세대수·층수는 확정 전이며 조합 공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 위클리한국주택경제 가락우성1차 시공자 2차 현설도 대우건설만(2026-11-03) · 위클리한국주택경제 쌍문한양1차 시공자 재공고(2026-11-03) · 파이낸셜뉴스 가락우성1차 재건축(2026-10-20) · 머니투데이방송 목동 단지별 공사비(2026-10-06~23) · 뉴시스 목동 시공사 현황(2026-10-20) · 서울경제TV 목동 5곳 단독응찰(2026-10-28)<br>
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
for v, h in zip((990, 985, 980, 965), (84.3, 83.9, 83.4, 82.2)):
    assert round(v / 1010 * 86, 1) == h, (v, h)
for v, w in zip((990, 985, 980, 965), (98.0, 97.5, 97.0, 95.5)):
    assert round(v / 1010 * 100, 1) == w, (v, w)
assert round(967 / 1166 * 100, 1) == 82.9 and 1166 - 967 == 199
KW = "가락우성1차 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("가락우성1차재건축")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
