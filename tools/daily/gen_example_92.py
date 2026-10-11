# -*- coding: utf-8 -*-
"""리포트 #92 (2026-10-11) 이번 주 청약 일정 (10/12~10/16). #91을 복제해 교체한다.

메인 검색어: 이번 주 청약 일정
일요일. 월요일(10/12)은 #83에서 약속한 SH 매입임대 D-1 글이라 오늘은 주간 달력으로 미리 묶는다.

수치와 검산
  사건일과 오늘의 간격: 모두 앞으로 1~5일 안의 일정.
  10/12(월) 향남역 그로브 스위첸 특별공급 (#91)
  10/13(화) 향남 1순위 · 쌍용 더 플래티넘 한강 1순위 333가구 (#91)
            SH 신혼·신생아 매입임대Ⅰ 서울 347호 접수 10/13 10시~10/15 17시 (#83, SH 공고 9/30) · Ⅱ도 같은 기간, 중복 신청 결격
            세종 4-2생활권 M3 신혼희망타운 행복주택 예비입주자 129명(55㎡) 10/13~15 (LH청약플러스·정리 자료)
            인천계양 A17 신혼희망타운 전시관 개관(부천 오정동, LH 9/30 보도) · 일반 접수 10/26~27
  10/14(수) 향남 2순위 · 청담르엘 장기전세(SH 51차) 서류심사 대상자 발표 → 서류 우편 10/19~21 · 당첨 2027-03-05 (#74)
  10/15(목) SH 매입임대 접수 마감 17시 · 인천석남 어울림센터 행복주택 최초모집 마감 (LH청약플러스 목록)
  다음 주: 10/19 매입임대Ⅱ 서류심사 대상 발표 · 10/20 향남 당첨자 발표
  요일별 건수 (위 목록 기준): 월 1 · 화 5 · 수 2 · 목 2
  막대 환산: 대시보드 세로 (건, 최댓값 5 → 86%): 1 → 17.2 · 2 → 34.4

단정하지 않은 것
  · 세종 M3·인천석남은 정리 자료·목록 기준이라 공고문 확인 안내를 붙였다.
  · 각 공고의 자격은 요약만 하고 공고문으로 넘긴다.
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-10-hyangnam.html"
DST = ROOT / "posts/2026-10-11-weekcal.html"
SLUG, PRE = "2026-10-11-weekcal", "wk1011"
NO, DATE = 92, "2026-10-11"
PREV_SLUG = "hng1010-"
BANNED = ["5억5천만원", "계약금 5%", "2,750만원"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "이번 주 청약 일정, SH 신혼 매입임대부터 향남까지"
DESC = ("10월 12일부터 16일까지 이번 주 청약 일정을 요일별로 정리했습니다. 화요일 SH 신혼·신생아 매입임대 서울 347호 접수가 시작되고, "
        "같은 날 향남역 그로브 스위첸·쌍용 더 플래티넘 한강 1순위가 겹칩니다. 수요일에는 청담르엘 장기전세 서류심사 대상자가 발표됩니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="이번 주 청약 일정, SH 신혼 매입임대부터 향남까지">
<meta property="og:description" content="월 향남 특공, 화 SH 매입임대·1순위 2곳, 수 청담르엘 서류심사 발표, 목 마감. 요일별로 놓치지 않게 정리했습니다.">
<meta property="og:type" content="article">
<meta property="og:image" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:url" content="{URL}">
<link rel="canonical" href="{URL}">
<link rel="alternate" type="application/rss+xml" title="부동산 인사이트 RSS" href="../feed.xml">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"NewsArticle",
 "headline":"이번 주 청약 일정, SH 신혼 매입임대부터 향남까지",
 "description":"10월 12일부터 16일까지의 청약 일정입니다. 12일 향남역 그로브 스위첸 특별공급, 13일 향남·양평 쌍용 더 플래티넘 한강 1순위와 SH 신혼·신생아 매입임대Ⅰ 서울 347호 접수 시작(15일 마감), 14일 청담르엘 장기전세 서류심사 대상자 발표가 이어집니다. 매입임대Ⅰ과 Ⅱ는 중복 신청하면 모두 결격입니다.",
 "image":"{OG}",
 "datePublished":"{DATE}","dateModified":"{DATE}",
 "author":{{"@type":"Organization","name":"부동산 인사이트"}},
 "publisher":{{"@type":"Organization","name":"부동산 인사이트"}},
 "mainEntityOfPage":"{URL}","inLanguage":"ko"}}
</script>'''

HEADER = f'''<header>
  <div class="eyebrow">2026 · 10월 부동산 키워드 리포트 #{NO}</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">이번 주 청약 일정,<br>화요일이 몰렸다</h1>
  <p class="sub">10월 12일부터 16일까지 <strong>이번 주 청약 일정</strong>입니다. <strong>화요일(13일)</strong>에 SH 신혼·신생아 매입임대 접수와 향남·양평 1순위가 겹칩니다. <strong>수요일(14일)</strong>에는 청담르엘 장기전세 서류심사 대상자가 발표됩니다. <span class="mark">SH 매입임대는 목요일(15일) 오후 5시에 닫힙니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>이번 주 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 화</div><div class="kw">10월 13일</div>
      <p>SH 매입임대 <strong>접수 시작</strong>.</p></div>
    <div class="kcard"><div class="hot">서울</div><div class="kw">347호</div>
      <p>신혼·신생아 <strong>매입임대Ⅰ</strong>.</p></div>
    <div class="kcard"><div class="hot">발표</div><div class="kw">10월 14일</div>
      <p>청담르엘 <strong>서류심사</strong>.</p></div>
    <div class="kcard"><div class="hot">마감</div><div class="kw">15일 17시</div>
      <p>SH 매입임대 <strong>접수 마감</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>이번 주 요일별 청약·발표 일정 (건)</h3>
    <span class="badge">10월 12~15일</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:17.2%">1</div><div class="barv" style="--h:17.2%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">5</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:34.4%">2</div><div class="barv" style="--h:34.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:34.4%">2</div><div class="barv" style="--h:34.4%"></div></div>
    </div>
    <div class="collbl"><span>12일 월</span><span>13일 화</span><span>14일 수</span><span>15일 목</span></div>
    <p class="cap">모두 같은 항목(이 글에서 정리한 접수·발표·마감 일정 수, 건)이라 한 축에 놓았습니다. 막대 길이는 최댓값 5건을 기준으로 맞췄습니다. 이 리포트가 다룬 일정만 센 것이며 전국 전체 일정 수가 아닙니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 이번 주 청약 일정, SH 신혼 매입임대부터 향남까지"),
    ("02-week", "이번 주 청약 일정 요일별"),
    ("03-sh", "SH 신혼·신생아 매입임대 서울 347호"),
    ("04-cheongdam", "수요일, 청담르엘 장기전세 서류심사 발표"),
    ("05-public", "LH 공공임대·신혼희망타운 일정"),
    ("06-check", "이번 주 청약 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="이번주청약일정,청약일정,SH신혼매입임대,신혼신생아매입임대,향남역그로브스위첸,청담르엘장기전세,신혼희망타운,행복주택,10월청약,내집마련">
  <h2>이번 주 청약, 요일별로 정리</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 이번 주 청약 일정, SH 신혼 매입임대부터 향남까지"></span>

  <p>이번 주 청약 일정은 <strong>화요일(13일)</strong>에 몰려 있습니다. SH 신혼·신생아 매입임대 서울 347호 접수가 시작되고, 같은 날 향남역 그로브 스위첸과 양평 쌍용 더 플래티넘 한강이 1순위를 받습니다. 수요일에는 청담르엘 장기전세 서류심사 대상자가 발표됩니다. <span class="mark">공공임대와 민간 분양이 한 주에 겹치니 내 일정부터 골라 두십시오.</span></p>

  <h3>이번 주 청약 일정 요일별</h3>
  <div class="chart" data-img="카드뉴스 2번 · 이번 주 청약 일정 요일별">
    <h3>10월 12~15일 청약·발표 일정</h3>
    <h4>12일 월</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">특공</span>
      <span class="desc">향남역 그로브 스위첸 특별공급 접수.</span></div>
    <h4>13일 화</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">5건</span>
      <span class="desc">SH 매입임대Ⅰ·Ⅱ 접수 시작, 향남·양평 1순위, 세종 신희타 행복주택 접수, 인천계양 A17 전시관 개관.</span></div>
    <h4>14일 수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">발표</span>
      <span class="desc">청담르엘 장기전세 서류심사 대상자 발표, 향남 2순위.</span></div>
    <h4>15일 목</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">마감</span>
      <span class="desc">SH 매입임대 오후 5시 마감, 인천석남 행복주택 마감.</span></div>
    <p class="cap">10월 4일·5일·10일 리포트와 SH·LH 공고 정리 자료 기준입니다. 각 일정은 청약홈·SH 인터넷청약시스템·LH청약플러스 공고문으로 다시 확인하십시오.</p>
  </div>
  <p>월요일은 향남역 그로브 스위첸 특별공급 하나뿐입니다. 화요일에 일정이 다섯 건 겹치고, 수요일과 목요일은 발표와 마감입니다. <span class="mark">이번 주 청약 일정에서 가장 놓치기 쉬운 것은 목요일 오후 5시 SH 매입임대 마감입니다.</span> 다음 주에는 19일 매입임대Ⅱ 서류심사 대상 발표, 20일 향남 당첨자 발표가 이어집니다.</p>

  <h3>SH 신혼·신생아 매입임대 서울 347호</h3>
  <div class="chart" data-img="카드뉴스 3번 · SH 신혼·신생아 매입임대 서울 347호">
    <h3>SH 신혼·신생아 매입임대주택Ⅰ (9월 30일 공고)</h3>
    <h4>접수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">13~15일</span>
      <span class="desc">13일 오전 10시부터 15일 오후 5시까지.</span></div>
    <h4>1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">신생아</span>
      <span class="desc">2년 안 출산·입양(임신 포함), 지원대상 한부모가족.</span></div>
    <h4>임대료</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">30~50%</span>
      <span class="desc">주변 시세 대비. 최장 20년 거주.</span></div>
    <p class="cap">SH 2026년 하반기 신혼·신생아 매입임대주택Ⅰ 모집공고 요약(10월 4일 리포트) 기준입니다. 소득 70%(맞벌이 90%) 이하, 총자산 3억4,500만원 이하이며 가구원수별 금액은 공고문 표로 확인하십시오.</p>
  </div>
  <p>이번 주 가장 큰 공공임대는 <strong>SH 신혼·신생아 매입임대Ⅰ 서울 347호</strong>입니다. 신생아 가구와 한부모가족이 1순위입니다. <span class="mark">같은 날 공고된 매입임대Ⅱ와 함께 넣으면 둘 다 결격입니다.</span> 자격은 공고일인 9월 30일 기준으로 봅니다. 접수 전날인 월요일에 다시 정리해 드리겠습니다.</p>

  <h3>수요일, 청담르엘 장기전세 서류심사 발표</h3>
  <div class="chart" data-img="카드뉴스 4번 · 수요일, 청담르엘 장기전세 서류심사 발표">
    <h3>SH 제51차 장기전세 (청담르엘 포함) 이후 일정</h3>
    <h4>서류심사 대상 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">14일</span>
      <span class="desc">SH 인터넷청약시스템에서 확인.</span></div>
    <h4>서류 제출</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">19~21일</span>
      <span class="desc">우편 접수. 기한을 넘기면 탈락할 수 있습니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2027년</span>
      <span class="desc">3월 5일.</span></div>
    <p class="cap">SH 제51차 장기전세주택 모집공고(8월 31일)와 9월 26일 리포트 기준입니다. 제출 서류 목록은 공고문과 발표 안내에서 확인하십시오.</p>
  </div>
  <p>9월에 접수한 SH 제51차 장기전세(청담르엘 포함) 신청자는 <strong>수요일(14일)</strong>에 서류심사 대상인지 확인해야 합니다. 대상자는 <strong>19일부터 21일</strong>까지 서류를 우편으로 냅니다. <span class="mark">발표 확인을 놓치면 서류 제출 기간도 놓칩니다.</span> 당첨자 발표는 2027년 3월 5일입니다.</p>

  <h3>이번 주 청약 일정, LH 공공임대·신혼희망타운</h3>
  <span class="imgslot" hidden data-img="카드뉴스 5번 · LH 공공임대·신혼희망타운 일정"></span>
  <p>LH 쪽도 이번 주에 일정이 있습니다. <strong>세종 4-2생활권 M3 신혼희망타운 행복주택</strong>은 13일부터 15일까지 전용 55㎡ 예비입주자 129명을 모집합니다. <strong>인천석남 어울림센터 행복주택</strong> 최초모집은 15일 마감입니다. 26~27일 일반 접수를 앞둔 <strong>인천계양 A17 신혼희망타운</strong>(309가구)은 부천 오정동 전시관을 13일 엽니다. <span class="mark">세 곳 모두 LH청약플러스 목록과 정리 자료 기준이니 공고문으로 다시 확인하십시오.</span></p>

  <h3>이번 주 청약 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 이번 주 청약 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="wk1011-06-check.png" src="../images/cards/report/wk1011-06-check.png" alt="체크포인트 카드 · 1. SH 매입임대Ⅰ과 Ⅱ는 하나만, 2. 청담르엘 신청자는 14일 발표 확인, 3. 마감 시각까지 공고문으로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>이번 주 청약 상담에 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>SH 매입임대Ⅰ과 Ⅱ는 하나만</strong>. 둘 다 넣으면 모두 결격입니다. 신생아 가구라면 Ⅰ의 1순위인지부터 보십시오.</li>
    <li><strong>청담르엘 신청자는 14일 발표 확인</strong>. 서류심사 대상이면 19~21일 우편 제출입니다. 서류는 미리 떼어 두십시오.</li>
    <li><strong>마감 시각까지 공고문으로 확인</strong>. SH 매입임대는 15일 오후 5시에 닫힙니다. 정확한 일정과 자격은 청약홈·SH·LH 공고문이 기준입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>이번 주 청약 일정</strong>은 화요일(13일)에 몰렸습니다. SH 신혼·신생아 매입임대 서울 347호 접수(15일 오후 5시 마감), 향남역 그로브 스위첸·쌍용 더 플래티넘 한강 1순위가 같은 날입니다. 수요일(14일)에는 청담르엘 장기전세 서류심사 대상자가 발표됩니다. <span class="mark">매입임대는 Ⅰ과 Ⅱ 중 하나만 넣으십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 청약 권유가 아닙니다. 일정은 SH 신혼·신생아 매입임대주택Ⅰ 모집공고(9월 30일)·SH 제51차 장기전세 모집공고(8월 31일)·분양 일정 보도(10월 8~9일)·LH청약플러스 목록과 정리 자료 기준입니다. 정확한 일정과 자격은 각 공고문에서 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: SH 2026년 하반기 신혼·신생아 매입임대주택Ⅰ·Ⅱ 모집공고(2026-09-30) · SH 제51차 장기전세주택 모집공고(2026-08-31) · 분양 일정 보도(서울경제·파이낸셜뉴스 2026-10-08~09) · LH청약플러스 공고 목록 · LH 인천계양 A17 보도(2026-09-30)<br>
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
assert round(1 / 5 * 86, 1) == 17.2 and round(2 / 5 * 86, 1) == 34.4 and 1 + 5 + 2 + 2 == 10
assert "공고문" in out and "결격" in out
KW = "이번 주 청약 일정"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("이번주청약일정")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
