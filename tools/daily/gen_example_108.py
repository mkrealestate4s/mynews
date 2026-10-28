# -*- coding: utf-8 -*-
"""리포트 #108 (2026-10-29) SH 행복주택 1차 당첨자 발표 D-1. #107을 복제해 교체한다.

메인 검색어: SH 행복주택

수치와 검산
  사건일과 오늘의 간격: 당첨자 발표 10/30(내일, D-1 예정) → 1일.
  보도: SH 2026년 1차 행복주택 총 1,884세대 = 신규 단지 55 + 잔여 공가 332 + 예비입주자 1,497
    (헤럴드경제 2026-05-27 · 파이낸셜뉴스 2026-05-28) · 임대료 시세 60~80%
    · 면적별 평균: 29㎡ 이하 보증금 6,200만·월 24만 / 39㎡ 1억1,400만·43만 / 49㎡ 1억3,600만·52만 / 59㎡ 1억6,300만·62만
    · 접수 6/15~17 · 서류심사 대상 발표 6/26 · 서류 7/1~3 · 당첨 발표 10/30 예정 · 11월 계약 · 12월 이후 입주(보도)
  당첨 발표일은 블로그·정리 사이트와 보도로 본 예정일이고 SH 공식 공지는 직접 읽지 못함 → "예정"으로 쓰고 SH 청약센터 확인 안내
  대시보드 세로 (1,884 → 86%): 1,497 → 68.3 · 332 → 15.2 · 55 → 2.5
  가로 월 임대료 (62만 → 100%): 52 → 83.9 · 43 → 69.4 · 24 → 38.7

단정하지 않은 것
  · 발표 시각·조회 방법: SH 인터넷청약시스템 공지 확인
  · 단지별 임대료(평균치만 보도) · 계약 날짜 세부 · 예비 순번 운용
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-28-acmer-2nd.html"
SLUG, PRE = "2026-10-29-sh-happyhouse", "shh1029"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 108, "2026-10-29"
PREV_SLUG = "akm1028-"
BANNED = ["아크메르", "동탄"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "SH 행복주택 내일 당첨 발표, 1,884세대 결과"
DESC = ("SH 행복주택 2026년 1차 당첨자 발표가 내일(10월 30일) 예정입니다. 6월에 접수한 1,884세대(신규 55·잔여 공가 332·예비 1,497)의 결과로, "
        "임대료는 시세 60~80% 수준입니다. 발표 뒤 11월 계약, 12월 이후 입주로 보도됐습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="1,884세대 중 예비입주자 1,497. 당첨 발표 10월 30일 예정, 11월 계약. 59㎡ 평균 보증금 1억6,300만원·월 62만원.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">SH 행복주택,<br>내일 당첨 발표</h1>
  <p class="sub"><strong>SH 행복주택 2026년 1차</strong> 당첨자 발표가 <strong>10월 30일(금)</strong>로 예정돼 있습니다. 6월에 접수한 <strong>1,884세대</strong>의 결과입니다. <span class="mark">이 가운데 1,497세대는 바로 들어가는 집이 아니라 예비입주자 자리입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · D-1</div><div class="kw">10월 30일</div>
      <p><strong>당첨자 발표</strong> 예정일.</p></div>
    <div class="kcard"><div class="hot">총 모집</div><div class="kw">1,884세대</div>
      <p>예비입주자 <strong>1,497</strong>.</p></div>
    <div class="kcard"><div class="hot">임대료 수준</div><div class="kw">시세 60~80%</div>
      <p>59㎡ 평균 <strong>월 62만원</strong>.</p></div>
    <div class="kcard"><div class="hot">다음 단계</div><div class="kw">11월 계약</div>
      <p>입주는 <strong>12월 이후</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>SH 행복주택 1차 모집 구성 (세대)</h3>
    <span class="badge">5월 공고 보도</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">1,884</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:68.3%">1,497</div><div class="barv" style="--h:68.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:15.2%">332</div><div class="barv" style="--h:15.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:2.5%">55</div><div class="barv" style="--h:2.5%"></div></div>
    </div>
    <div class="collbl"><span>합계</span><span>예비입주자</span><span>잔여 공가</span><span>신규 단지</span></div>
    <p class="cap">SH 2026년 1차 행복주택 입주자 모집 보도(헤럴드경제 2026-05-27) 수치입니다. 막대 길이는 합계 1,884세대를 기준으로 맞췄습니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: SH 행복주택, 내일 당첨 발표"),
    ("02-mix", "1,884세대 중 1,497은 예비 자리"),
    ("03-date", "발표 10월 30일, 계약 11월"),
    ("04-rent", "평균 월 임대료 24만~62만원"),
    ("05-check", "발표 날 확인할 것 3가지"),
    ("06-tips", "SH 행복주택 발표 후 체크 3가지"),
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

ARTICLE = '''<article data-tags="SH행복주택,SH행복주택당첨자발표,행복주택당첨자발표,SH행복주택1차,행복주택,서울행복주택,SH청약,공공임대,청년주택,신혼부부임대">
  <h2>SH 행복주택, 내일 당첨 발표</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: SH 행복주택, 내일 당첨 발표"></span>

  <p>SH 행복주택 2026년 1차 당첨자 발표가 내일(10월 30일) 예정돼 있습니다. 서울주택도시공사(SH)가 지난 5월 공고하고 6월 15~17일 인터넷으로 접수한 1,884세대의 결과입니다. <span class="mark">접수부터 발표까지 넉 달 반이 걸린 셈이라, 넣어 놓고 잊고 있던 분도 많을 겁니다.</span> 청년·신혼부부·고령자 등이 대상이고 임대료는 시세의 60~80% 수준으로 보도됐습니다.</p>

  <h3>SH 행복주택 1,884세대, 1,497은 예비 자리</h3>
  <div class="chart" data-img="카드뉴스 2번 · 1,884세대 중 1,497은 예비 자리">
    <h3>모집 구성 (세대)</h3>
    <div class="bar"><label>예비입주자</label>
      <div class="rail"><div class="fill" style="width:79.5%">1,497</div></div></div>
    <div class="bar"><label>잔여 공가</label>
      <div class="rail"><div class="fill gray" style="width:17.6%"></div><span class="railval">332</span></div></div>
    <div class="bar"><label>신규 단지</label>
      <div class="rail"><div class="fill gray" style="width:2.9%"></div><span class="railval">55</span></div></div>
    <p class="cap">헤럴드경제(2026-05-27) 보도 수치입니다. 막대 길이는 합계 1,884세대를 100으로 맞췄습니다.</p>
  </div>
  <p>숫자를 나눠 보면 결과를 읽는 법이 달라집니다. <span class="mark">바로 들어갈 수 있는 집은 신규 단지 55세대와 기존 입주자가 나가며 빈 잔여 공가 332세대, 합쳐 387세대입니다.</span> 나머지 1,497세대는 예비입주자 모집입니다. 예비로 뽑히면 빈집이 날 때 순번대로 연락이 오므로, 당첨 문자를 받아도 입주 시점은 사람마다 다릅니다.</p>

  <h3>SH 행복주택 당첨 발표 10월 30일, 계약은 11월</h3>
  <div class="chart" data-img="카드뉴스 3번 · 발표 10월 30일, 계약 11월">
    <h3>지나온 일정과 남은 일정</h3>
    <h4>인터넷 접수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">6.15~17</span>
      <span class="desc">사흘간 받았습니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.30</span>
      <span class="desc">내일, 예정일입니다.</span></div>
    <h4>계약 · 입주</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월</span>
      <span class="desc">입주는 12월 이후로 보도.</span></div>
    <p class="cap">접수일은 공고 보도, 발표일은 공고 일정을 옮긴 정리 자료 기준입니다. 서류 제출은 7월 1~3일이었습니다. 발표 시각과 계약 날짜는 SH 인터넷청약시스템 공지로 확인하십시오.</p>
  </div>
  <p>서류심사 대상자는 6월 26일에 발표됐고 7월 1~3일에 서류를 냈습니다. 그 뒤 소득·자산 검증을 거쳐 내일 최종 결과가 나옵니다. <span class="mark">발표일은 공고에 적힌 예정일이라 바뀔 수 있습니다. 결과는 SH 인터넷청약시스템에서 본인 인증으로 조회합니다.</span></p>

  <h3>임대료, 평균 월 24만~62만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 평균 월 임대료 24만~62만원">
    <h3>면적별 평균 월 임대료 (만원)</h3>
    <div class="bar"><label>59㎡ 이하</label>
      <div class="rail"><div class="fill" style="width:100%">62</div></div></div>
    <div class="bar"><label>49㎡ 이하</label>
      <div class="rail"><div class="fill gray" style="width:83.9%">52</div></div></div>
    <div class="bar"><label>39㎡ 이하</label>
      <div class="rail"><div class="fill gray" style="width:69.4%">43</div></div></div>
    <div class="bar"><label>29㎡ 이하</label>
      <div class="rail"><div class="fill gray" style="width:38.7%">24</div></div></div>
    <p class="cap">면적별 평균치 보도(헤럴드경제 2026-05-27)입니다. 평균 보증금은 29㎡ 6,200만원, 39㎡ 1억1,400만원, 49㎡ 1억3,600만원, 59㎡ 1억6,300만원입니다. 단지별 금액은 공고문으로 확인하십시오.</p>
  </div>
  <p>당첨되면 가장 먼저 필요한 건 보증금입니다. <span class="mark">59㎡ 평균으로 보증금 1억6,300만원에 월 62만원, 가장 작은 29㎡도 보증금 6,200만원에 월 24만원입니다.</span> 다만 이건 전체 평균이라 내가 넣은 단지 금액과 다를 수 있습니다. 보증금과 월 임대료를 서로 바꾸는 전환 조건도 단지 공고문에서 봅니다.</p>

  <h3>SH 행복주택 발표 날 확인할 것 3가지</h3>
  <div class="chart" data-img="카드뉴스 5번 · 발표 날 확인할 것 3가지">
    <h3>발표 날 볼 것</h3>
    <h4>당첨인지, 예비인지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">순번</span>
      <span class="desc">예비면 번호를 적어 둡니다.</span></div>
    <h4>계약 날짜와 장소</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월</span>
      <span class="desc">세부 날짜는 SH 공지로.</span></div>
    <h4>보증금 준비</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">1억대</span>
      <span class="desc">39㎡ 이상 평균 기준.</span></div>
    <p class="cap">SH 인터넷청약시스템 공지와 입주자 모집공고문이 정본입니다. 문의는 SH 콜센터(1600-3456).</p>
  </div>
  <p>결과 화면에서 먼저 볼 것은 당첨인지 예비인지입니다. 예비라면 순번이 곧 입주 가능성이니 적어 두십시오. <span class="mark">당첨이라면 계약일에 보증금 일부를 바로 내야 하므로, 전세대출이나 버팀목대출을 쓸 계획이면 지금 은행 상담부터 잡는 편이 안전합니다.</span> 계약을 하지 않으면 당첨 기록이 남아 다음 공공임대 신청에 불리할 수 있으니 공고문의 제한 조항도 함께 읽으십시오.</p>

  <h3>SH 행복주택 발표 후 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · SH 행복주택 발표 후 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="shh1029-06-tips.png" src="../images/cards/report/shh1029-06-tips.png" alt="체크포인트 카드 · 1. 당첨인지 예비인지와 순번, 2. 계약 날짜 SH 공지 확인, 3. 보증금과 대출 계획" loading="lazy" width="1080" height="1080">
    <figcaption>SH 행복주택 발표 뒤에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>당첨인지 예비인지 확인</strong>. 예비면 순번을 적어 둡니다.</li>
    <li><strong>계약 날짜 확인</strong>. 11월 계약으로 보도됐고 세부 날짜는 SH 공지로 봅니다.</li>
    <li><strong>보증금과 대출 계획</strong>. 59㎡ 평균 보증금은 1억6,300만원입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>SH 행복주택</strong> 2026년 1차 당첨자 발표는 내일 10월 30일 예정입니다. 1,884세대 가운데 바로 들어갈 수 있는 집은 신규 55세대와 잔여 공가 332세대이고 1,497세대는 예비입주자 자리입니다. <span class="mark">발표 뒤 11월 계약, 12월 이후 입주로 보도됐습니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 모집 물량과 평균 임대료는 5월 공고 보도(헤럴드경제 2026-05-27) 기준입니다. 당첨자 발표일은 공고 일정을 옮긴 정리 자료에서 확인한 예정일이며 SH 공식 공지는 직접 확인하지 못했습니다. 발표 시각, 단지별 임대료, 계약 일정은 SH 인터넷청약시스템과 공고문으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 헤럴드경제 "SH, 행복주택 1884세대 청약 접수…시세 60~80% 임대료"(2026-05-27) · 파이낸셜뉴스 SH 행복주택 모집(2026-05-28) · 파이낸셜뉴스 SH 행복주택 접수(2026-06-10) · 고방 SH 행복주택 1,884호 모집 정리(2026-06) · SH 인터넷청약시스템<br>
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
assert 55 + 332 + 1497 == 1884
assert round(1497 / 1884 * 86, 1) == 68.3 and round(332 / 1884 * 86, 1) == 15.2 and round(55 / 1884 * 86, 1) == 2.5
assert round(1497 / 1884 * 100, 1) == 79.5 and round(332 / 1884 * 100, 1) == 17.6 and round(55 / 1884 * 100, 1) == 2.9
assert round(52 / 62 * 100, 1) == 83.9 and round(43 / 62 * 100, 1) == 69.4 and round(24 / 62 * 100, 1) == 38.7
KW = "SH 행복주택"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("SH행복주택")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
