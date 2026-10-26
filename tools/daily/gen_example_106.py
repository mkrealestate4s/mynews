# -*- coding: utf-8 -*-
"""리포트 #106 (2026-10-27) 인천계양 A17 신혼희망타운 본청약 일반 접수 마감일. #105를 복제해 교체한다.

메인 검색어: 계양 신혼희망타운

수치와 검산
  사건일과 오늘의 간격: 일반 접수 10/26(월)~27(화) → 오늘이 마감일(D-day). 리드는 마감, 공고(9/30)는 배경.
  #102(10/23, D-3 글)와 같은 공고라 수치는 그대로 쓰고, 이번 글은 '오늘 마감 + 마감 뒤 일정'으로 각도를 바꿨다.
  LH 공고 보도(9/30): 전체 463 · 행복주택 154 · 공공분양 309 · 사전청약 133 → 일반 176 · 전용 55㎡
    · 평균 약 5억400만 · 범위 4억7,673만~5억844만(청약 정보 사이트) · 당첨 11/5 · 계약 2027년 2월 · 입주 2029년 11월
    · 전매 3년 · 실거주 의무 없음 · 전용 모기지 연 1.3% 고정
  가로 (309 → 100%): 176 → 57.0 · 133 → 43.0 ; (50,844 → 100%): 50,400 → 99.1 · 47,673 → 93.8
  대시보드 세로 (463 → 86%): 309 → 57.4 · 176 → 32.7 · 133 → 24.7

단정하지 않은 것
  · 접수 마감 시각: 검색으로 확인 못 함 → "LH 청약플러스 공고문의 접수 시간 확인"
  · 소득·자산 기준 금액, 타입별 분양가, 모기지 의무 조건 문구: 공고문 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-26-trivn-centum.html"
SLUG, PRE = "2026-10-27-gyeyang-deadline", "gyd1027"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 106, "2026-10-27"
PREV_SLUG = "trv1026-"
BANNED = ["트리븐", "반여동", "두산에너빌리티"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "계양 신혼희망타운 오늘 마감, 일반 176가구"
DESC = ("인천계양 A17블록 신혼희망타운 본청약 일반 접수가 오늘(10월 27일) 마감됩니다. 공공분양 309가구 중 "
        "176가구를 새로 뽑고, 전용 55㎡ 평균 분양가는 약 5억400만원입니다. 당첨 발표는 11월 5일입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="10월 27일 접수 마감, 11월 5일 당첨 발표, 2027년 2월 계약. 전용 55㎡ 평균 5억400만원, 전매제한 3년.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">계양 신혼희망타운,<br>오늘 접수 마감</h1>
  <p class="sub"><strong>인천계양 A17블록 신혼희망타운</strong> 본청약 일반 접수가 <strong>오늘(10월 27일, 화)</strong> 끝납니다. 새로 뽑는 물량은 <strong>176가구</strong>, 전용 55㎡ 하나입니다. <span class="mark">어제 못 넣었다면 오늘이 마지막 날입니다. 당첨 발표는 11월 5일입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 마감일</div><div class="kw">10월 27일</div>
      <p>일반 접수 <strong>마지막 날</strong>.</p></div>
    <div class="kcard"><div class="hot">일반공급</div><div class="kw">176가구</div>
      <p>공공분양 <strong>309가구</strong> 중.</p></div>
    <div class="kcard"><div class="hot">평균 분양가</div><div class="kw">5억400만</div>
      <p>전용 <strong>55㎡</strong> 단일 평형.</p></div>
    <div class="kcard"><div class="hot">당첨 발표</div><div class="kw">11월 5일</div>
      <p>마감 <strong>9일 뒤</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>계양 신혼희망타운 A17블록 물량 (가구)</h3>
    <span class="badge">9월 30일 공고</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">463</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:57.4%">309</div><div class="barv" style="--h:57.4%"></div></div>
      <div class="col"><div class="v gtx" style="--h:32.7%">176</div><div class="barv" style="--h:32.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:24.7%">133</div><div class="barv" style="--h:24.7%"></div></div>
    </div>
    <div class="collbl"><span>단지 전체</span><span>공공분양</span><span>일반공급</span><span>사전청약 당첨</span></div>
    <p class="cap">단지 전체 463가구 중 행복주택 154가구는 따로 모집합니다. 막대 길이는 최댓값 463가구를 기준으로 맞췄습니다. LH 공고(9월 30일)를 다룬 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 계양 신혼희망타운 오늘 마감"),
    ("02-date", "오늘 마감, 발표는 11월 5일"),
    ("03-supply", "309가구 중 새로 뽑는 건 176가구"),
    ("04-price", "전용 55㎡ 평균 5억400만원"),
    ("05-after", "마감 뒤 일정: 발표, 계약, 입주"),
    ("06-tips", "계양 신혼희망타운 마감 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="계양신혼희망타운,인천계양A17,신혼희망타운,신혼희망타운본청약,LH청약,계양신도시,3기신도시,신혼부부청약,공공분양,인천청약">
  <h2>계양 신혼희망타운, 오늘 접수 마감</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 계양 신혼희망타운 오늘 마감"></span>

  <p>계양 신혼희망타운 본청약 일반 접수가 오늘(10월 27일) 마감됩니다. LH가 9월 30일 공고한 인천계양 A17블록(인천 계양구 박촌동 일대) 공공분양으로, 어제(26일)부터 이틀만 받습니다. 대상은 예비신혼부부·신혼부부·한부모가족입니다. <span class="mark">새로 뽑는 물량은 176가구이고, 오늘을 넘기면 이번 회차는 끝입니다.</span></p>

  <h3>계양 신혼희망타운 접수, 오늘이 마지막 날</h3>
  <div class="chart" data-img="카드뉴스 2번 · 오늘 마감, 발표는 11월 5일">
    <h3>접수와 발표 (LH 공고 보도 기준)</h3>
    <h4>일반 접수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.26~27</span>
      <span class="desc">오늘 화요일이 마감입니다. 마감 시각은 공고문 확인.</span></div>
    <h4>사전청약 당첨자</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.19~20</span>
      <span class="desc">이미 끝났습니다. 이번 접수와 따로 받았습니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.5</span>
      <span class="desc">마감 9일 뒤, 목요일입니다.</span></div>
    <p class="cap">LH 인천계양 A17블록 신혼희망타운 입주자모집공고(9월 30일)를 다룬 보도 기준입니다. 오늘 접수 마감 시각과 신청 방법은 LH 청약플러스(apply.lh.or.kr) 공고문으로 확인하십시오.</p>
  </div>
  <p>접수는 어제와 오늘 이틀뿐이었습니다. <span class="mark">마감 시각은 이 글에서 확인하지 못했으니, 퇴근 뒤로 미루지 말고 LH 청약플러스 공고문의 접수 시간을 먼저 보십시오.</span> 결과는 11월 5일에 나옵니다.</p>

  <h3>계양 신혼희망타운 일반공급 176가구</h3>
  <div class="chart" data-img="카드뉴스 3번 · 309가구 중 새로 뽑는 건 176가구">
    <h3>공공분양 309가구 나눔 (가구)</h3>
    <div class="bar"><label>공공분양 전체</label>
      <div class="rail"><div class="fill gray" style="width:100%">309</div></div></div>
    <div class="bar"><label>이번 일반공급</label>
      <div class="rail"><div class="fill" style="width:57%">176</div></div></div>
    <div class="bar"><label>사전청약 당첨</label>
      <div class="rail"><div class="fill gray" style="width:43%">133</div></div></div>
    <p class="cap">단지 전체는 463가구이고, 그중 행복주택 154가구는 따로 모집합니다. 막대 길이는 최댓값 309가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>공공분양 309가구 가운데 133가구는 사전청약 당첨자 몫입니다. 남은 176가구를 이번 접수로 뽑습니다. <span class="mark">평형은 전용 55㎡ 하나이고 A·B·C 세 타입으로 나뉘므로, 오늘 신청할 때 타입을 고르게 됩니다.</span> 타입별 물량은 공고문 표로 확인하십시오.</p>

  <h3>전용 55㎡ 평균 5억400만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 전용 55㎡ 평균 5억400만원">
    <h3>분양가 (만원)</h3>
    <div class="bar"><label>가장 높은 값</label>
      <div class="rail"><div class="fill gray" style="width:100%">50,844</div></div></div>
    <div class="bar"><label>평균</label>
      <div class="rail"><div class="fill" style="width:99.1%">50,400</div></div></div>
    <div class="bar"><label>가장 낮은 값</label>
      <div class="rail"><div class="fill gray" style="width:93.8%">47,673</div></div></div>
    <p class="cap">평균은 보도 기준, 최고·최저는 타입·층별 분양가를 정리한 청약 정보 사이트 기준입니다. 막대 길이는 최댓값 5억844만원을 기준으로 맞췄습니다. 본인이 넣을 타입의 정확한 금액은 공고문으로 확인하십시오.</p>
  </div>
  <p>평균 분양가는 약 5억400만원입니다. 타입과 층에 따라 4억7,673만원에서 5억844만원 사이로 정리돼 있습니다. <span class="mark">분양가가 총자산 기준을 넘는 집이라 신혼희망타운 전용 모기지(연 1.3% 고정) 가입이 조건으로 붙습니다.</span> 금리는 낮지만 팔 때 차익 일부를 나누는 구조이니 정산 조건까지 읽고 넣으십시오.</p>

  <h3>마감 뒤 일정: 발표, 계약, 입주</h3>
  <div class="chart" data-img="카드뉴스 5번 · 마감 뒤 일정: 발표, 계약, 입주">
    <h3>접수 다음 단계 (보도 기준)</h3>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.5</span>
      <span class="desc">LH 청약플러스에서 확인합니다.</span></div>
    <h4>계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2027.2</span>
      <span class="desc">발표 뒤 약 석 달. 계약금을 이때 준비합니다.</span></div>
    <h4>입주</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2029.11</span>
      <span class="desc">예정입니다. 전매제한은 3년, 실거주 의무는 없다고 보도됐습니다.</span></div>
    <p class="cap">LH 공고를 다룬 보도 기준입니다. 계약 일자와 계약금 비율, 서류 제출 일정은 공고문으로 확인하십시오.</p>
  </div>
  <p>오늘 접수를 마치면 11월 5일 발표, 2027년 2월 계약, 2029년 11월 입주 순서로 갑니다. <span class="mark">당첨부터 입주까지 4년 가까이 걸리므로 지금 사는 집의 계약 만기와 어떻게 이어 붙일지 같이 계획해야 합니다.</span> 전매제한은 3년이고 실거주 의무는 붙지 않는다고 보도됐습니다.</p>

  <h3>계양 신혼희망타운 마감 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 계양 신혼희망타운 마감 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="gyd1027-06-tips.png" src="../images/cards/report/gyd1027-06-tips.png" alt="체크포인트 카드 · 1. 오늘 마감 시각 확인, 2. 소득·자산 기준은 공고문 표로, 3. 타입 고르고 모기지 조건 읽기" loading="lazy" width="1080" height="1080">
    <figcaption>계양 신혼희망타운 마감 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>오늘 마감 시각 확인</strong>. LH 청약플러스 공고문에서 접수 시간을 보고 그 전에 신청을 끝냅니다.</li>
    <li><strong>소득·자산 기준은 공고문 표로</strong>. 가구원 수별 금액은 이 글에서 확인하지 못했습니다. 예비신혼부부는 두 사람 소득·자산을 합쳐 봅니다.</li>
    <li><strong>타입 고르고 모기지 조건 읽기</strong>. 55㎡ A·B·C 중 하나를 고릅니다. 전용 모기지는 연 1.3% 고정이지만 팔 때 차익을 나눕니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>계양 신혼희망타운</strong>(인천계양 A17블록) 본청약 일반 접수는 오늘 10월 27일 마감됩니다. 공공분양 309가구 중 176가구를 새로 뽑고, 전용 55㎡ 평균 분양가는 약 5억400만원입니다. <span class="mark">당첨자 발표는 11월 5일, 계약은 2027년 2월, 입주는 2029년 11월 예정입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 물량·분양가·일정·조건은 LH 인천계양 A17블록 신혼희망타운 입주자모집공고(9월 30일)를 다룬 보도(아시아투데이·뉴스1·비즈니스플러스·핀포인트뉴스·비즈니스코리아)와 청약 정보 사이트 정리 기준입니다. 접수 마감 시각, 소득·자산 기준 금액, 타입별 분양가는 확인하지 못해 적지 않았거나 범위로만 적었습니다. LH 청약플러스(apply.lh.or.kr) 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 아시아투데이·뉴스1·비즈니스플러스·핀포인트뉴스·비즈니스코리아 LH 인천계양 A17블록 신혼희망타운 309가구 본청약(2026-09-30) · 청약 정보 사이트 인천계양 A17 분양가·일정 정리(2026-10)<br>
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
for v, w in ((176, 57.0), (133, 43.0)):
    assert round(v / 309 * 100, 1) == w, v
for v, w in ((50400, 99.1), (47673, 93.8)):
    assert round(v / 50844 * 100, 1) == w, v
for v, hh in ((309, 57.4), (176, 32.7), (133, 24.7)):
    assert round(v / 463 * 86, 1) == hh, v
assert 176 + 133 == 309 and 309 + 154 == 463
KW = "계양 신혼희망타운"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("계양신혼희망타운")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
