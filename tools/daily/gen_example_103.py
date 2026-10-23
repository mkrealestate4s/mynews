# -*- coding: utf-8 -*-
"""리포트 #103 (2026-10-24) 디에이치 반포124 일반분양 구성·예상 분양가. #102를 복제해 교체한다.

메인 검색어: 디에이치 반포124

수치와 검산
  사건일과 오늘의 간격: 일반분양 구성·일정 보도 10/19(아시아타임즈)~10/22(한국경제) → 2~5일.
    리드는 '공고 11/27 예정 · 분양가는 아직 추정'이다. 단지명 변경(10/13, #94)은 배경.
  보도: 총 5,007가구 · 일반분양 1,832 (59㎡ 281 · 80㎡ 23 · 84㎡ 1,358 · 99㎡ 82 · 114㎡ 44 · 130㎡ 44, 합 1,832)
    · 한 매체는 특공 930 + 일반 871 = 1,801 (31가구 차) · 3.3㎡당 8,000만~1억 거론, 9,000만 안팎 예상
    · 9,000만 가정 59㎡ 22억5,000 · 84㎡ 30억6,000 / 1억 가정 25억 · 34억
    · 모집공고 11/27 예정 · 특공 12/7 · 1순위 12/8 · 특공 당첨 12/16 (계획) · 2027년 말 입주 목표
  대시보드 세로 (5,007 → 86%): 1,832 → 31.5 · 1,358 → 23.3 · 281 → 4.8
  가로 (1,358 → 100%): 281 → 20.7 · 82 → 6.0 · 44 → 3.2 · 23 → 1.7
  가로 (34억 → 100%): 30.6 → 90.0 · 25 → 73.5 · 22.5 → 66.2

단정하지 않은 것
  · 분양가: 업계 추정. 공고 전 확정값 없음
  · 일반분양 1,832 vs 1,801: 최종 공고 확인
  · 청약 날짜: 계획 단계 보도. 대출 한도·자금조달 규제는 공고·은행 확인
  · 시세차익(20~40억): 관측이지 확정 이익이 아님
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-23-gyeyang-a17.html"
SLUG, PRE = "2026-10-24-dh-banpo124", "dhb1024"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 103, "2026-10-24"
PREV_SLUG = "gya1023-"
BANNED = ["신혼희망타운", "계양"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "디에이치 반포124 분양가 30억, 아직 확정 아닙니다"
DESC = ("디에이치 반포124(반포주공1단지 1·2·4주구) 일반분양 1,832가구 구성이 보도됐습니다. 84㎡가 1,358가구로 가장 많고, "
        "분양가는 3.3㎡당 9,000만원 안팎이라는 업계 추정만 있습니다. 모집공고는 11월 27일 예정입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="일반분양 1,832가구 중 84㎡ 1,358가구. 84㎡ 30억6,000만원은 3.3㎡당 9,000만원 가정치. 공고 11월 27일 예정, 특별공급 12월 7일 계획.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">디에이치 반포124,<br>분양가는 아직 추정</h1>
  <p class="sub"><strong>디에이치 반포124</strong>(반포주공1단지 1·2·4주구) 일반분양 <strong>1,832가구</strong>의 평형 구성이 보도됐습니다. 84㎡가 1,358가구로 넷 중 세 집꼴입니다. <span class="mark">84㎡ 30억원은 3.3㎡당 9,000만원을 가정한 계산이고, 확정 분양가는 11월 27일 예정인 모집공고에서 나옵니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 공고 예정</div><div class="kw">11월 27일</div>
      <p>입주자 <strong>모집공고</strong> 예정일.</p></div>
    <div class="kcard"><div class="hot">일반분양</div><div class="kw">1,832가구</div>
      <p>전체 <strong>5,007가구</strong> 중.</p></div>
    <div class="kcard"><div class="hot">84㎡ 물량</div><div class="kw">1,358가구</div>
      <p>일반분양의 <strong>74%</strong>.</p></div>
    <div class="kcard"><div class="hot">3.3㎡당 추정</div><div class="kw">9,000만</div>
      <p>업계 <strong>추정</strong>, 확정 전.</p></div>
  </div>

  <div class="colchart">
    <h3>디에이치 반포124 물량 (가구)</h3>
    <span class="badge">10월 보도 기준</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5,007</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:31.5%">1,832</div><div class="barv" style="--h:31.5%"></div></div>
      <div class="col dim"><div class="v" style="--h:23.3%">1,358</div><div class="barv" style="--h:23.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:4.8%">281</div><div class="barv" style="--h:4.8%"></div></div>
    </div>
    <div class="collbl"><span>단지 전체</span><span>일반분양</span><span>그중 84㎡</span><span>그중 59㎡</span></div>
    <p class="cap">막대 길이는 최댓값 5,007가구를 기준으로 맞췄습니다. 일반분양은 1,801가구로 보도한 매체도 있어(31가구 차) 최종 공고로 확인해야 합니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 디에이치 반포124 분양가는 아직 추정"),
    ("02-date", "공고 11월 27일, 특별공급 12월 7일 예정"),
    ("03-size", "일반분양 1,832가구, 84㎡가 1,358"),
    ("04-price", "84㎡ 30억은 9,000만원 가정치"),
    ("05-unsure", "아직 확정 아닌 것 3가지"),
    ("06-tips", "디에이치 반포124 청약 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="디에이치반포124,반포주공1단지,반포청약,디에이치반포124분양가,서초청약,강남청약,로또청약,현대건설,반포재건축,서울청약">
  <h2>디에이치 반포124, 분양가는 아직 추정</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 디에이치 반포124 분양가는 아직 추정"></span>

  <p>디에이치 반포124 일반분양 물량과 평형 구성이 이번 주 잇따라 보도됐습니다. 반포주공1단지 1·2·4주구를 다시 지은 5,007가구 단지로, 지난 13일 '디에이치 클래스트'에서 지금 이름으로 바뀌었습니다. 한국경제는 강남권에서 39년 만에 가장 큰 분양이라고 전했습니다. <span class="mark">다만 "84㎡ 30억원"은 업계 추정을 곱한 값이고, 확정 분양가는 아직 없습니다.</span></p>

  <h3>디에이치 반포124 청약 일정, 공고는 11월 27일 예정</h3>
  <div class="chart" data-img="카드뉴스 2번 · 공고 11월 27일, 특별공급 12월 7일 예정">
    <h3>예정 일정 (10월 보도 기준)</h3>
    <h4>입주자 모집공고</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.27</span>
      <span class="desc">분양가·평형별 물량·자격이 이날 확정됩니다.</span></div>
    <h4>특별공급 · 1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12.7~8</span>
      <span class="desc">특별공급 7일, 1순위 8일로 계획돼 있다고 보도됐습니다.</span></div>
    <h4>특별공급 당첨 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">12.16</span>
      <span class="desc">입주는 2027년 말 목표입니다.</span></div>
    <p class="cap">뉴스스페이스·한국경제 등 10월 19~22일 보도 기준 계획 일정입니다. 공고 전이라 바뀔 수 있으니 청약홈 공고문으로 다시 확인하십시오.</p>
  </div>
  <p>모집공고는 11월 27일, 특별공급 접수는 12월 7일, 1순위는 8일로 계획돼 있다고 보도됐습니다. 공고에서 접수까지 열흘 남짓입니다. <span class="mark">청약통장 순위와 거주 요건은 공고일 기준으로 따지므로, 지금 미리 청약홈에서 본인 순위를 확인해 두는 편이 낫습니다.</span></p>

  <h3>디에이치 반포124 일반분양 1,832가구, 84㎡가 1,358</h3>
  <div class="chart" data-img="카드뉴스 3번 · 일반분양 1,832가구, 84㎡가 1,358">
    <h3>평형별 일반분양 (가구)</h3>
    <div class="bar"><label>84㎡</label>
      <div class="rail"><div class="fill" style="width:100%">1,358</div></div></div>
    <div class="bar"><label>59㎡</label>
      <div class="rail"><div class="fill gray" style="width:20.7%"></div><span class="railval">281</span></div></div>
    <div class="bar"><label>99㎡</label>
      <div class="rail"><div class="fill gray" style="width:6%"></div><span class="railval">82</span></div></div>
    <div class="bar"><label>114㎡ · 130㎡</label>
      <div class="rail"><div class="fill gray" style="width:3.2%"></div><span class="railval">각 44</span></div></div>
    <div class="bar"><label>80㎡</label>
      <div class="rail"><div class="fill gray" style="width:1.7%"></div><span class="railval">23</span></div></div>
    <p class="cap">전용면적 기준, 10월 보도 수치입니다(합계 1,832가구). 막대 길이는 최댓값 1,358가구를 기준으로 맞췄습니다. 계획 물량이라 공고에서 바뀔 수 있습니다.</p>
  </div>
  <p>일반분양 1,832가구 가운데 84㎡가 1,358가구로 74%를 차지합니다. 59㎡는 281가구, 99㎡ 이상 큰 평형은 모두 합쳐 170가구입니다. <span class="mark">한 매체는 특별공급 930가구와 일반공급 871가구를 더한 1,801가구로 보도해 31가구 차이가 납니다.</span> 정확한 숫자는 공고문 표가 정본입니다.</p>

  <h3>84㎡ 30억은 9,000만원 가정치</h3>
  <div class="chart" data-img="카드뉴스 4번 · 84㎡ 30억은 9,000만원 가정치">
    <h3>예상 분양가 (억원, 업계 추정 계산)</h3>
    <div class="bar"><label>84㎡ · 3.3㎡당 1억</label>
      <div class="rail"><div class="fill gray" style="width:100%">34</div></div></div>
    <div class="bar"><label>84㎡ · 3.3㎡당 9,000만</label>
      <div class="rail"><div class="fill" style="width:90%">30.6</div></div></div>
    <div class="bar"><label>59㎡ · 3.3㎡당 1억</label>
      <div class="rail"><div class="fill gray" style="width:73.5%">25</div></div></div>
    <div class="bar"><label>59㎡ · 3.3㎡당 9,000만</label>
      <div class="rail"><div class="fill gray" style="width:66.2%">22.5</div></div></div>
    <p class="cap">3.3㎡당 분양가를 가정해 곱한 보도 계산값입니다(업계 거론 범위 8,000만~1억원). 막대 길이는 최댓값 34억원을 기준으로 맞췄습니다. 확정 분양가가 아닙니다.</p>
  </div>
  <p>업계는 3.3㎡당 9,000만원 안팎을 예상하고, 8,000만원대에서 1억원까지 거론합니다. 9,000만원이면 84㎡가 30억6,000만원, 1억원이면 34억원입니다. <span class="mark">가정 하나에 84㎡ 값이 3억원 넘게 움직이므로, 지금 숫자로 자금 계획을 굳히지 마십시오.</span> 주변 시세와 비교한 '20~40억 차익'도 관측이지 확정된 이익이 아닙니다.</p>

  <h3>디에이치 반포124, 아직 확정 아닌 것 3가지</h3>
  <div class="chart" data-img="카드뉴스 5번 · 아직 확정 아닌 것 3가지">
    <h3>공고 전이라 확정되지 않은 것</h3>
    <h4>분양가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">추정</span>
      <span class="desc">3.3㎡당 8,000만~1억원 거론.</span></div>
    <h4>일반분양 물량</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">31가구</span>
      <span class="desc">매체마다 1,832와 1,801로 다릅니다.</span></div>
    <h4>청약 날짜</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">계획</span>
      <span class="desc">공고 11월 27일 예정, 그 뒤 확정.</span></div>
    <p class="cap">모두 입주자 모집공고 전 보도 기준입니다. 대출 가능 금액과 자금조달 조건은 공고문과 은행 상담으로 확인하십시오.</p>
  </div>
  <p>지금 나온 숫자는 전부 공고 전 수치입니다. 분양가는 업계 추정, 물량은 매체마다 31가구 차이, 날짜는 계획입니다. <span class="mark">보도들이 공통으로 짚는 변수는 현금 조달입니다.</span> 분양가가 30억원 안팎이면 대출로 채울 수 있는 몫이 작아, 계약금과 중도금을 어떻게 마련할지가 청약 여부를 가릅니다.</p>

  <h3>디에이치 반포124 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 디에이치 반포124 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="dhb1024-06-tips.png" src="../images/cards/report/dhb1024-06-tips.png" alt="체크포인트 카드 · 1. 공고 11월 27일 예정, 확정 분양가 확인, 2. 청약홈에서 내 순위 미리 확인, 3. 계약금·중도금 현금 계획" loading="lazy" width="1080" height="1080">
    <figcaption>디에이치 반포124 청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>공고 11월 27일 예정, 확정 분양가 확인</strong>. 지금 30억원은 가정치입니다. 평형별 금액은 공고문 표로 봅니다.</li>
    <li><strong>청약홈에서 내 순위 미리 확인</strong>. 순위·거주 요건은 공고일 기준입니다. 청약통장 순위(가입)확인서로 확인하십시오.</li>
    <li><strong>계약금·중도금 현금 계획</strong>. 대출 한도와 조건은 공고문과 은행 상담으로 확인합니다. 특별공급은 12월 7일 계획입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>디에이치 반포124</strong>는 5,007가구 중 1,832가구를 일반분양하고, 그중 84㎡가 1,358가구입니다. 분양가는 3.3㎡당 9,000만원 안팎이라는 업계 추정뿐이고, 84㎡ 30억6,000만원은 그 가정을 곱한 값입니다. <span class="mark">모집공고는 11월 27일 예정, 특별공급은 12월 7일, 1순위는 8일로 계획돼 있습니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 물량·예상 분양가·일정은 입주자 모집공고 전 보도(한국경제·뉴스스페이스·아시아타임즈·비즈워치·핀포인트뉴스) 기준입니다. 분양가는 업계 추정이고, 일반분양 물량은 매체마다 다르며(1,832가구 · 1,801가구), 일정은 계획입니다. 확정 내용은 청약홈(applyhome.co.kr) 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 한국경제 "강남 39년 만에 최대분양"(2026-10-22) · 비즈워치(2026-10-21) · 아시아타임즈(2026-10-19) · 뉴스스페이스·핀포인트뉴스 디에이치 반포124 일반분양·일정 보도(2026-10) · 한국경제 반포주공1단지 단지명 변경(2026-10-13)<br>
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
for v, w in ((281, 20.7), (82, 6.0), (44, 3.2), (23, 1.7)):
    assert round(v / 1358 * 100, 1) == w, v
for v, w in ((30.6, 90.0), (25, 73.5), (22.5, 66.2)):
    assert round(v / 34 * 100, 1) == w, v
for v, h in ((1832, 31.5), (1358, 23.3), (281, 4.8)):
    assert round(v / 5007 * 86, 1) == h, v
assert 281 + 23 + 1358 + 82 + 44 + 44 == 1832 and 930 + 871 == 1801 and 1832 - 1801 == 31
assert round(1358 / 1832 * 100) == 74 and 82 + 44 + 44 == 170
KW = "디에이치 반포124"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("디에이치반포124")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
