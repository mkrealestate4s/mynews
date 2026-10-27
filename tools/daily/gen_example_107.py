# -*- coding: utf-8 -*-
"""리포트 #107 (2026-10-28) 아크메르 동탄 2순위 D-day. #106을 복제해 교체한다.

메인 검색어: 아크메르 동탄

수치와 검산
  사건일과 오늘의 간격: 2순위 접수 10/28(오늘, D-day) · 특공 결과 보도 10/27 → 1일.
  보도: 특별공급 95·99 726가구 모집에 269건 접수, 평균 0.37 대 1 (메트로신문 10/27, 청약홈 기준)
    · 95블록 84㎡C 특공 마감 (스트레이트뉴스 제목)
    · 1순위 10/27 · 2순위 10/28 · 당첨 95 11/3 · 99 11/4 · 계약 11/16~18 · 총 1,808가구 · 최고 49층
    · 84㎡ 최고 분양가 95 17억1,530만 · 99 17억1,680만 (#104 보도)
  1순위 공식 경쟁률: 보도로 확인 못 함 → 쓰지 않고 청약홈 경쟁률 조회로 안내
  대시보드 세로 (1,808 → 86%): 726 → 34.5 · 269 → 12.8
  가로 (726 → 100%): 269 → 37.1
  가로 (17.168억 → 100%): 17.153 → 99.9 · 20% 3.4336 → 20.0 · 10% 1.7168 → 10.0

단정하지 않은 것
  · 1순위 경쟁률·미달 여부: 청약홈 확인
  · 2순위 자격 세부·계약금 비율·전매·재당첨: 공고문 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-27-gyeyang-deadline.html"
SLUG, PRE = "2026-10-28-acmer-2nd", "akm1028"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 107, "2026-10-28"
PREV_SLUG = "gyd1027-"
BANNED = ["계양", "신혼희망"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "아크메르 동탄 오늘 2순위, 특공은 미달이었다"
DESC = ("아크메르 동탄 청약이 오늘(10월 28일) 2순위 접수를 받습니다. 앞서 특별공급은 726가구 모집에 269건이 접수돼 "
        "평균 0.37 대 1로 미달이었습니다. 당첨 발표는 95가 11월 3일, 99가 11월 4일입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="특별공급 726가구에 269건, 평균 0.37 대 1. 2순위 10월 28일, 당첨 발표 11월 3~4일, 계약 11월 16~18일.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">아크메르 동탄,<br>오늘 2순위 접수</h1>
  <p class="sub"><strong>아크메르 동탄 95·99</strong>가 <strong>10월 28일(수)</strong> 2순위 청약을 받습니다. 앞서 특별공급은 <strong>726가구 모집에 269건</strong>이 들어와 <span class="mark">평균 0.37 대 1, 미달이었습니다. 남은 물량이 일반공급으로 넘어갑니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · D-day</div><div class="kw">10월 28일</div>
      <p><strong>2순위</strong> 접수일.</p></div>
    <div class="kcard"><div class="hot">특공 경쟁률</div><div class="kw">0.37 대 1</div>
      <p>726가구에 <strong>269건</strong>.</p></div>
    <div class="kcard"><div class="hot">당첨 발표</div><div class="kw">11월 3일</div>
      <p>99는 <strong>4일</strong>.</p></div>
    <div class="kcard"><div class="hot">총 가구</div><div class="kw">1,808가구</div>
      <p>최고 <strong>49층</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>아크메르 동탄 특별공급 (가구·건)</h3>
    <span class="badge">10월 27일 보도</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">1,808</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:34.5%">726</div><div class="barv" style="--h:34.5%"></div></div>
      <div class="col dim"><div class="v" style="--h:12.8%">269</div><div class="barv" style="--h:12.8%"></div></div>
    </div>
    <div class="collbl"><span>총 가구</span><span>특공 모집</span><span>특공 접수</span></div>
    <p class="cap">특별공급 모집·접수는 한국부동산원 청약홈 기준 보도 수치입니다. 막대 길이는 총 1,808가구를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 아크메르 동탄, 오늘 2순위 접수"),
    ("02-special", "특공 726가구에 269건, 0.37 대 1"),
    ("03-date", "2순위 오늘, 발표는 11월 3~4일"),
    ("04-price", "국평 17억, 계약금만 억대"),
    ("05-check", "2순위 넣기 전 확인할 것 3가지"),
    ("06-tips", "아크메르 동탄 2순위 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="아크메르동탄,아크메르동탄청약,아크메르동탄2순위,아크메르동탄경쟁률,동탄청약,동탄분양,화성청약,포스코이앤씨,경기청약,2순위청약">
  <h2>아크메르 동탄, 오늘 2순위 접수</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 아크메르 동탄, 오늘 2순위 접수"></span>

  <p>아크메르 동탄이 오늘(10월 28일) 2순위 청약을 받습니다. 경기 화성시 동탄구 반송동 95·99번지 일원, 최고 49층 1,808가구 단지입니다. <span class="mark">앞서 26일 특별공급은 726가구 모집에 269건만 들어와 평균 0.37 대 1로 미달이었습니다.</span> 84㎡ 최고 분양가가 17억원을 넘는 단지라 결과에 관심이 쏠렸습니다.</p>

  <h3>아크메르 동탄 특별공급, 726가구에 269건</h3>
  <div class="chart" data-img="카드뉴스 2번 · 특공 726가구에 269건, 0.37 대 1">
    <h3>특별공급 모집과 접수 (95·99 합계)</h3>
    <div class="bar"><label>모집 가구</label>
      <div class="rail"><div class="fill" style="width:100%">726</div></div></div>
    <div class="bar"><label>접수 건수</label>
      <div class="rail"><div class="fill gray" style="width:37.1%">269</div></div></div>
    <p class="cap">한국부동산원 청약홈 기준 보도(메트로신문, 2026-10-27) 수치입니다. 막대 길이는 모집 726가구를 기준으로 맞췄습니다.</p>
  </div>
  <p>특별공급 평균 경쟁률은 0.37 대 1입니다. 100가구를 뽑는데 37명 정도가 신청한 셈입니다. <span class="mark">다만 단지 전체가 고르게 비었다는 뜻은 아닙니다. 95블록 84㎡C 타입은 특공에서 마감됐다는 보도도 나왔습니다.</span> 특공에서 남은 물량은 일반공급으로 넘어가 1·2순위 신청자에게 돌아갑니다.</p>

  <h3>아크메르 동탄 2순위 오늘, 발표는 11월 3~4일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 2순위 오늘, 발표는 11월 3~4일">
    <h3>남은 일정 (보도 기준)</h3>
    <h4>2순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.28</span>
      <span class="desc">오늘 하루, 95·99 같은 날입니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.3~4</span>
      <span class="desc">95는 3일, 99는 4일입니다.</span></div>
    <h4>정당계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.16~18</span>
      <span class="desc">두 단지 같은 기간입니다.</span></div>
    <p class="cap">10월 보도 기준입니다. 접수 시간과 세부 일정은 청약홈 입주자 모집공고문으로 다시 확인하십시오.</p>
  </div>
  <p>어제(27일) 1순위 접수가 끝났고 오늘이 2순위입니다. 1순위 공식 경쟁률은 아직 보도로 확인되지 않았습니다. <span class="mark">타입별로 1순위에서 마감됐는지는 청약홈 '청약 경쟁률' 조회에서 바로 볼 수 있으니, 2순위로 넣기 전에 내가 고른 타입부터 확인하십시오.</span> 1순위에서 마감된 타입은 2순위 접수를 받지 않습니다.</p>

  <h3>분양가, 국평 17억에 계약금만 억대</h3>
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
    <p class="cap">84㎡ 최고 분양가는 보도 수치(95 17억1,530만원, 99 17억1,680만원)입니다. 계약금은 비율을 가정해 99 최고가에 곱한 값이며 실제 비율은 공고문으로 확인하십시오.</p>
  </div>
  <p>특공이 미달된 이유로는 높은 분양가가 먼저 꼽힙니다. 84㎡ 최고 분양가는 95가 17억1,530만원, 99가 17억1,680만원으로 보도됐습니다. <span class="mark">계약금이 10%면 1억7,000만원 남짓, 20%면 3억4,000만원 남짓을 당첨 직후 현금으로 내야 합니다.</span> 2순위는 경쟁이 덜할 수 있지만 당첨되면 이 돈은 똑같이 듭니다.</p>

  <h3>아크메르 동탄 2순위 넣기 전 확인할 것 3가지</h3>
  <div class="chart" data-img="카드뉴스 5번 · 2순위 넣기 전 확인할 것 3가지">
    <h3>기사로는 확인되지 않은 것</h3>
    <h4>내 타입 1순위 마감 여부</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">청약홈</span>
      <span class="desc">마감 타입은 2순위가 없습니다.</span></div>
    <h4>2순위 자격</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">공고문</span>
      <span class="desc">통장 요건을 직접 확인.</span></div>
    <h4>계약금·전매 조건</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10~20%</span>
      <span class="desc">비율과 제한은 공고문으로.</span></div>
    <p class="cap">청약홈(applyhome.co.kr) 입주자 모집공고문이 정본입니다. 대출 가능 금액은 은행 상담으로 확인하십시오.</p>
  </div>
  <p>2순위는 보통 1순위 요건(가입 기간·예치금)을 채우지 못한 청약통장 가입자가 넣는 순서입니다. 세부 자격은 단지 공고문이 정하니 직접 확인하십시오. <span class="mark">당첨되면 2순위라도 당첨 기록이 남습니다. 계약을 포기할 생각이라면 넣기 전에 재당첨 제한 조항을 먼저 읽는 편이 안전합니다.</span></p>

  <h3>아크메르 동탄 2순위 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 아크메르 동탄 2순위 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="akm1028-06-tips.png" src="../images/cards/report/akm1028-06-tips.png" alt="체크포인트 카드 · 1. 내 타입 1순위 마감 여부 청약홈 확인, 2. 2순위 자격 공고문 확인, 3. 계약금 현금 계획" loading="lazy" width="1080" height="1080">
    <figcaption>아크메르 동탄 2순위 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>내 타입 1순위 마감 여부 확인</strong>. 청약홈 경쟁률 조회에서 타입별로 봅니다.</li>
    <li><strong>2순위 자격 공고문 확인</strong>. 통장 요건과 거주 요건을 공고문 표로 봅니다.</li>
    <li><strong>계약금 현금 계획</strong>. 84㎡ 최고가 기준 10%만 해도 1억7,000만원 남짓입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>아크메르 동탄</strong>은 오늘 10월 28일 2순위 접수를 받습니다. 특별공급은 726가구에 269건, 평균 0.37 대 1로 미달이었고 남은 물량은 일반공급으로 넘어갔습니다. <span class="mark">당첨 발표는 95가 11월 3일, 99가 4일이고 계약은 11월 16~18일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 특별공급 결과는 청약홈 기준 보도(메트로신문 2026-10-27), 일정·분양가는 10월 보도 기준입니다. 1순위 경쟁률은 보도로 확인하지 못해 싣지 않았습니다. 계약금은 비율을 가정한 계산입니다. 자격·전매·재당첨 조건은 청약홈(applyhome.co.kr) 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 메트로신문 "아크메르 동탄, 특공 미달, 평균 경쟁률 0.37대 1"(2026-10-27) · 스트레이트뉴스 아크메르 동탄 95블록 84㎡C 특공 마감(2026-10) · 리얼캐스트 아크메르 동탄 27일 1순위·28일 2순위(2026-10) · 파이낸셜뉴스 동탄1신도시 1808가구(2026-10-26) · SBS Biz "화성 동탄 국평이 17억?"(2026-10)<br>
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
assert round(269 / 726, 2) == 0.37
assert round(726 / 1808 * 86, 1) == 34.5 and round(269 / 1808 * 86, 1) == 12.8
assert round(269 / 726 * 100, 1) == 37.1
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
