# -*- coding: utf-8 -*-
"""리포트 #120 (2026-11-09) 해링턴플레이스 용산 리버뷰 청년안심주택. #119를 복제해 교체한다.

메인 검색어: 해링턴플레이스 용산 리버뷰

수치와 검산
  사건일과 오늘의 간격: 1순위 청약 11/12(D-3, 리드) · 주간 분양 캘린더 보도 11/6(3일 전).
  단지 (한국경제·디지털타임스 9/18): 전체 988세대 중 635세대 공공지원민간임대(청년안심주택)
    특공 128 · 일반 507 · 25·35형 청년, 56·61형 신혼부부 · 보증금 비율 30~50% 선택
    보증금 6,200만~2억3,800만원 · 월 41만~121만원 · 주차 680대(지하1~4층) · 10월 준공 예정
  주간 (이투데이·파이낸셜뉴스·서울경제 11/6): 12곳 5,215가구 청약 · 경기 79% · 당첨 발표 8곳 · 계약 11곳
    견본주택 1곳(부천대장 하우스토리 디센트 548가구, 11/13) · 용산 리버뷰 12일 1순위
  대시보드(곳, 12→86): 12 86 · 11 78.8 · 8 57.3 · 1 7.2
  구성 가로(988→100): 635 64.3 · 507 51.3 · 128 13.0
  보증금(23,800→100): 6,200 26.1 · 월세(121→100): 41 33.9

단정하지 않은 것
  · 특공 접수일, 소득·자산 기준, 계약 기간·갱신 조건은 공고문 확인 필요(보도에 없음)
  · 1순위 12일은 분양 캘린더 보도 기준 · 나머지 353세대의 성격은 보도에 없어 쓰지 않음
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-08-mokdong13.html"
DST = ROOT / "posts/2026-11-09-yongsan-riverview.html"
SLUG, PRE = "2026-11-09-yongsan-riverview", "ysr"
NO, DATE = 120, "2026-11-09"
PREV_SLUG = "mk13-"
BANNED = ["목동", "삼성물산", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "해링턴플레이스 용산 리버뷰, 분양 아닌 월세 임대"
DESC = ("해링턴플레이스 용산 리버뷰가 이번 주 청약을 받습니다. 분양이 아니라 청년·신혼부부 대상 공공지원민간임대(청년안심주택) 635세대입니다. "
        "보증금 6,200만~2억3,800만원, 월 41만~121만원. 구성·일정·비용과 확인할 점을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="용산 신축이지만 내 집이 되는 청약이 아닙니다. 청년 25·35형, 신혼 56·61형, 월 41만원부터. 이번 주 전국 청약 12곳 일정도 함께 봤습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">해링턴플레이스 용산 리버뷰<br>분양 아닌 월세 임대</h1>
  <p class="sub"><strong>해링턴플레이스 용산 리버뷰</strong>가 이번 주 <strong>12일(목) 1순위</strong> 청약을 받습니다(분양 캘린더 보도 기준). 이름은 아파트 분양 같지만 <strong>청년·신혼부부용 공공지원민간임대(청년안심주택) 635세대</strong>입니다. 보증금 6,200만~2억3,800만원에 <strong>월 41만~121만원</strong>을 냅니다. <span class="mark">당첨돼도 내 집이 되는 청약이 아니라, 정해진 기간 세 들어 사는 자리입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 용산 리버뷰</div><div class="kw">11월 12일</div>
      <p><strong>1순위</strong> 청약(보도 기준).</p></div>
    <div class="kcard"><div class="hot">공급</div><div class="kw">635세대</div>
      <p>특공 <strong>128</strong> · 일반 507.</p></div>
    <div class="kcard"><div class="hot">월 임대료</div><div class="kw">41만~121만</div>
      <p>보증금 비율 <strong>30~50%</strong> 선택.</p></div>
    <div class="kcard"><div class="hot">이번 주 전국</div><div class="kw">5,215가구</div>
      <p>12곳 청약, 경기 <strong>79%</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>11월 둘째 주(9~15일) 분양 일정 (곳)</h3>
    <span class="badge">견본주택은 1곳뿐</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">12</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:78.8%">11</div><div class="barv" style="--h:78.8%"></div></div>
      <div class="col dim"><div class="v" style="--h:57.3%">8</div><div class="barv" style="--h:57.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:7.2%">1</div><div class="barv" style="--h:7.2%"></div></div>
    </div>
    <div class="collbl"><span>청약 접수</span><span>정당계약</span><span>당첨 발표</span><span>견본주택</span></div>
    <p class="cap">모두 단지 수(곳)라 한 축에 놓았습니다. 막대 길이는 최댓값 12곳을 기준으로 맞췄습니다. 리얼투데이 집계를 인용한 이투데이·파이낸셜뉴스(11월 6일) 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 해링턴플레이스 용산 리버뷰, 분양 아닌 월세 임대"),
    ("02-mix", "988세대 중 635세대가 청년·신혼 임대"),
    ("03-sched", "이번 주 목요일 1순위, 날짜는 공고문으로"),
    ("04-cost", "보증금 6,200만원부터, 월 41만원부터"),
    ("05-week", "이번 주 전국 청약 12곳, 5,215가구"),
    ("06-check", "해링턴플레이스 용산 리버뷰 체크 3가지"),
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

ARTICLE = '''<article data-tags="해링턴플레이스용산리버뷰,용산리버뷰,청년안심주택,용산청년안심주택,공공지원민간임대,용산임대주택,신혼부부임대,청년임대주택,11월청약일정,용산구">
  <h2>해링턴플레이스 용산 리버뷰, 분양 아닌 월세 임대</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 해링턴플레이스 용산 리버뷰, 분양 아닌 월세 임대"></span>

  <p>해링턴플레이스 용산 리버뷰가 이번 주 청약을 받습니다. 서울 용산구 용문동 단지로, 분양 캘린더 보도에 따르면 <strong>11월 12일(목) 1순위</strong> 청약이 잡혀 있습니다. <span class="mark">다만 이 청약은 아파트를 사는 분양이 아니라 청년·신혼부부가 월세를 내고 사는 공공지원민간임대(청년안심주택)입니다.</span></p>

  <h3>해링턴플레이스 용산 리버뷰, 988세대 중 635세대가 임대</h3>
  <div class="chart" data-img="카드뉴스 2번 · 988세대 중 635세대가 청년·신혼 임대">
    <h3>해링턴플레이스 용산 리버뷰 공급 구성 (세대)</h3>
    <div class="bar"><label>단지 전체</label>
      <div class="rail"><div class="fill gray" style="width:100%">988</div></div></div>
    <div class="bar"><label>청년안심주택</label>
      <div class="rail"><div class="fill" style="width:64.3%">635</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill gray" style="width:51.3%">507</div></div></div>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill gray" style="width:13%"></div><span class="railval">128</span></div></div>
    <p class="cap">모두 세대 수라 한 축에 놓았습니다. 막대 길이는 단지 전체 988세대를 기준으로 맞췄습니다. 청년안심주택 635세대 = 일반공급 507 + 특별공급 128입니다. 한국경제·디지털타임스(9월 18일) 보도 기준입니다.</p>
  </div>
  <p>단지 전체 988세대 가운데 이번에 모집하는 공공지원민간임대는 635세대입니다. 특별공급 128세대, 일반공급 507세대입니다. 주택형은 25·35·56·61형 네 가지이고, <strong>25형과 35형은 청년, 56형과 61형은 신혼부부</strong> 몫입니다. <span class="mark">이름에 '플레이스'와 '리버뷰'가 붙어 분양 단지로 오해하기 쉽지만, 당첨되면 받는 것은 소유권이 아니라 임대차 계약입니다.</span></p>

  <h3>이번 주 목요일 1순위, 날짜는 공고문으로</h3>
  <div class="chart" data-img="카드뉴스 3번 · 이번 주 목요일 1순위, 날짜는 공고문으로">
    <h3>해링턴플레이스 용산 리버뷰 일정</h3>
    <h4>준공</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10월</span>
      <span class="desc">준공 예정으로 보도됐다. 지어진 집에 들어가는 모집이다.</span></div>
    <h4>1순위 청약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.12</span>
      <span class="desc">분양 캘린더 보도 기준. 특별공급 날짜는 보도에 없다.</span></div>
    <h4>확인할 곳</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">공고문</span>
      <span class="desc">접수 시간·방법·서류는 모집공고와 단지 홈페이지에서.</span></div>
    <p class="cap">한국경제·디지털타임스(9월 18일), 이투데이·서울경제(11월 6일) 보도 기준입니다. 특별공급 접수일은 확인하지 못했습니다.</p>
  </div>
  <p>단지는 10월 준공 예정으로 보도됐고, 준공 뒤 임차인 모집을 하는 순서입니다. 1순위 청약일은 분양 캘린더 보도 기준 11월 12일입니다. <span class="mark">특별공급 접수일과 소득·자산 기준은 보도에서 찾지 못했습니다. 접수 전에 모집공고문을 직접 확인하십시오.</span></p>

  <h3>해링턴플레이스 용산 리버뷰 보증금·월 임대료</h3>
  <div class="chart" data-img="카드뉴스 4번 · 보증금 6,200만원부터, 월 41만원부터">
    <h3>보증금 범위 (만원)</h3>
    <div class="bar"><label>최저</label>
      <div class="rail"><div class="fill" style="width:26.1%">6,200</div></div></div>
    <div class="bar"><label>최고</label>
      <div class="rail"><div class="fill gray" style="width:100%">23,800</div></div></div>
    <h3>월 임대료 범위 (만원)</h3>
    <div class="bar"><label>최저</label>
      <div class="rail"><div class="fill" style="width:33.9%">41</div></div></div>
    <div class="bar"><label>최고</label>
      <div class="rail"><div class="fill gray" style="width:100%">121</div></div></div>
    <p class="cap">보증금과 월 임대료는 단위가 같아도 성격이 달라 축을 나눴습니다. 각 막대 길이는 최고값을 기준으로 맞췄습니다. 공급 유형·주택형·보증금 비율(30~50%)에 따라 달라집니다. 한국경제(9월 18일) 보도 기준입니다.</p>
  </div>
  <p>보증금은 6,200만~2억3,800만원, 월 임대료는 41만~121만원입니다. 보증금 비율을 30~50% 사이에서 고를 수 있어, 보증금을 많이 내면 월세가 줄어드는 구조입니다. <span class="mark">월 41만원이면 1년에 492만원, 월 121만원이면 1년에 1,452만원입니다.</span> 주차는 지하 1~4층 680대 규모이고 빌트인 가전이 들어갑니다.</p>

  <h3>이번 주 전국 청약 12곳, 5,215가구</h3>
  <div class="chart" data-img="카드뉴스 5번 · 이번 주 전국 청약 12곳, 5,215가구">
    <h3>11월 둘째 주 분양 시장</h3>
    <h4>청약 물량</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">5,215</span>
      <span class="desc">전국 12곳에서 가구 청약을 받는다.</span></div>
    <h4>경기 비중</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">79%</span>
      <span class="desc">평택·수원·시흥 등 경기 남부 중심. 광교 지분적립형도 이번 주.</span></div>
    <h4>견본주택</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.13</span>
      <span class="desc">부천대장 하우스토리 디센트 548가구, 이번 주 유일한 개관.</span></div>
    <p class="cap">리얼투데이 집계를 인용한 이투데이·파이낸셜뉴스·서울경제(11월 6일) 보도 기준입니다. 경기 물량은 매체에 따라 4,012가구 또는 4,102가구로 다르게 나옵니다.</p>
  </div>
  <p>이번 주(9~15일) 전국에서는 12곳, 5,215가구가 청약을 받습니다. 물량의 79%가 경기에 몰렸고, 서울에서는 해링턴플레이스 용산 리버뷰가 눈에 띕니다. 견본주택은 13일 문을 여는 부천대장 하우스토리 디센트(548가구) 한 곳이고, 당첨자 발표 8곳, 정당계약 11곳이 이어집니다.</p>

  <h3>해링턴플레이스 용산 리버뷰 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 해링턴플레이스 용산 리버뷰 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="ysr-06-check.png" src="../images/cards/report/ysr-06-check.png" alt="체크포인트 카드 · 1. 분양이 아닌 임대, 2. 청년은 25·35형 신혼은 56·61형, 3. 자격·날짜는 공고문" loading="lazy" width="1080" height="1080">
    <figcaption>해링턴플레이스 용산 리버뷰 신청 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>분양이 아닌 임대</strong>. 당첨되면 임대차 계약을 맺고 보증금과 월세를 냅니다. 계약 기간과 갱신 조건은 모집공고로 확인하십시오.</li>
    <li><strong>청년은 25·35형, 신혼부부는 56·61형</strong>. 내가 어느 유형인지부터 정하고 그 주택형의 보증금·월세를 봅니다.</li>
    <li><strong>자격·날짜는 공고문</strong>. 소득·자산 기준과 특별공급 접수일은 보도에 없습니다. 모집공고와 단지 홈페이지, 서울시 청년안심주택 안내에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>해링턴플레이스 용산 리버뷰</strong>는 분양이 아니라 청년·신혼부부용 청년안심주택 635세대(특공 128·일반 507)입니다. 1순위는 11월 12일(보도 기준), 보증금 6,200만~2억3,800만원, 월 41만~121만원입니다. <span class="mark">용산 신축에 살 수 있는 자리지만 내 집 마련 청약은 아닙니다. 신청 전에 모집공고문으로 자격과 날짜를 확인하십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 단지 구성·임대 조건은 한국경제·디지털타임스(2026-09-18), 청약 일정과 주간 분양 시장은 이투데이·파이낸셜뉴스·서울경제(2026-11-06) 보도 기준입니다. 최종 조건은 모집공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 한국경제 해링턴플레이스용산리버뷰 635세대 공급(2026-09-18) · 디지털타임스 해링턴플레이스용산리버뷰 10월 준공 예정(2026-09-18) · 이투데이 분양캘린더 11월 둘째 주(2026-11-06) · 파이낸셜뉴스 11월 둘째 주 12곳 5215가구(2026-11-06) · 서울경제 분양캘린더(2026-11-06)<br>
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
for v, h in zip((11, 8, 1), (78.8, 57.3, 7.2)):
    assert round(v / 12 * 86, 1) == h, (v, h)
for v, w in zip((635, 507, 128), (64.3, 51.3, 13.0)):
    assert round(v / 988 * 100, 1) == w, (v, w)
assert 507 + 128 == 635 and round(6200 / 23800 * 100, 1) == 26.1 and round(41 / 121 * 100, 1) == 33.9
assert 41 * 12 == 492 and 121 * 12 == 1452
KW = "해링턴플레이스 용산 리버뷰"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("해링턴플레이스용산리버뷰")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
