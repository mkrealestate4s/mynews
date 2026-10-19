# -*- coding: utf-8 -*-
"""리포트 #99 (2026-10-20) 향남역 그로브 스위첸 당첨자 발표. #98을 복제해 교체한다.

메인 검색어: 향남역 그로브 스위첸

수치와 검산
  사건일과 오늘의 간격: 당첨자 발표 10/20(오늘), 0일. 청약 접수 10/12~14 → 6~8일.
  특별공급 10/12: 공급 475 · 접수 139 · 0.29 대 1 (청약 집계, mhb-blog 10/12)
  1순위 10/13: 공급 795 · 접수 511 · 0.64 대 1 (청약 집계, mhb-blog 10/13)  미달 284
  2순위: 71㎡·147㎡P 2순위 마감, 나머지 미달 (신아일보 주간분양)
  일정 (파이낸셜뉴스 10/8): 발표 10/20 · 서류 10/24~28 · 정당계약 11/2~4
  분양 조건 (#91, 서울경제 등 10/8~9): 84㎡ 5억원 중반대 · 계약금 5% · 중도금 60% 무이자 · 933가구
  5억5천 예시: 5% 2,750만 · 60% 3억3,000만 · 35% 1억9,250만
  대시보드 세로 (최댓값 795 → 86%): 475 → 51.4 · 139 → 15.0 · 511 → 55.3
  공급·접수 가로 (795 → 100%): 475 → 59.7 · 139 → 17.5 · 511 → 64.3
  계약 단계 가로 (60% → 100%): 5 → 8.3 · 35 → 58.3

단정하지 않은 것
  · 경쟁률은 청약 집계 기준. 최종 수치는 청약홈
  · 미달분 추가 공급(무순위 등)은 공고가 나와야 확정
  · 84㎡ 분양가는 보도 기준 '5억원 중반대'
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-19-mokdong10.html"
DST = ROOT / "posts/2026-10-20-hyangnam-result.html"
SLUG, PRE = "2026-10-20-hyangnam-result", "hng1020"
NO, DATE = 99, "2026-10-20"
PREV_SLUG = "mkd1019-"
BANNED = ["목동10단지", "현대건설", "에세르"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "향남역 그로브 스위첸 당첨자 발표, 1순위는 0.64 대 1"
DESC = ("향남역 그로브 스위첸 당첨자가 오늘(10월 20일) 발표됩니다. 1순위는 795가구에 511건이 접수돼 평균 0.64 대 1, "
        "특별공급은 475가구에 139건으로 0.29 대 1이었습니다. 당첨자 서류는 10월 24~28일, 정당계약은 11월 2~4일입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="1순위 0.64 대 1, 71㎡·147㎡P만 2순위 마감. 당첨 뒤 서류·계약 일정과 계약금 계산까지 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">향남역 그로브 스위첸,<br>오늘 당첨자 발표</h1>
  <p class="sub"><strong>향남역 그로브 스위첸</strong> 당첨자가 오늘(<strong>10월 20일</strong>) 발표됩니다. 1순위는 795가구에 511건이 들어와 평균 <strong>0.64 대 1</strong>이었습니다. 당첨자 서류는 <strong>24~28일</strong>, 계약은 <strong>11월 2~4일</strong>입니다. <span class="mark">전용 71㎡와 147㎡P만 2순위에서 마감됐고 나머지 주택형은 미달이었습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 발표</div><div class="kw">10월 20일</div>
      <p>오늘 <strong>당첨자 발표</strong>.</p></div>
    <div class="kcard"><div class="hot">1순위</div><div class="kw">0.64 대 1</div>
      <p>795가구에 <strong>511건</strong>.</p></div>
    <div class="kcard"><div class="hot">특별공급</div><div class="kw">0.29 대 1</div>
      <p>475가구에 <strong>139건</strong>.</p></div>
    <div class="kcard"><div class="hot">계약</div><div class="kw">11월 2~4일</div>
      <p>서류는 <strong>24~28일</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>향남역 그로브 스위첸 공급과 접수 (가구·건)</h3>
    <span class="badge">10월 12·13일</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:51.4%">475</div><div class="barv" style="--h:51.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:15%">139</div><div class="barv" style="--h:15%"></div></div>
      <div class="col dim"><div class="v" style="--h:86%">795</div><div class="barv" style="--h:86%"></div></div>
      <div class="col"><div class="v gtx" style="--h:55.3%">511</div><div class="barv" style="--h:55.3%"></div></div>
    </div>
    <div class="collbl"><span>특공 공급</span><span>특공 접수</span><span>1순위 공급</span><span>1순위 접수</span></div>
    <p class="cap">공급 가구와 접수 건수를 같은 축에 놓았습니다(한 건이 한 가구에 신청). 막대 길이는 최댓값 795를 기준으로 맞췄습니다. 10월 12·13일 청약 집계 기준이며 최종 수치는 청약홈(applyhome.co.kr)에서 확인하십시오.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 향남역 그로브 스위첸 당첨자 발표, 1순위는 0.64 대 1"),
    ("02-apply", "향남역 그로브 스위첸 공급보다 신청이 적었다"),
    ("03-ratio", "1순위 0.64 대 1, 100가구에 64건"),
    ("04-date", "당첨 발표 뒤 서류·계약 일정"),
    ("05-money", "5억5천 집이면 계약 때 2,750만원"),
    ("06-check", "향남역 그로브 스위첸 체크 3가지"),
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

ARTICLE = '''<article data-tags="향남역그로브스위첸,향남역그로브스위첸당첨자발표,향남역,화성향남,KCC건설,스위첸,청약경쟁률,당첨자발표,경기분양,청약홈">
  <h2>향남역 그로브 스위첸, 오늘 당첨자 발표</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 향남역 그로브 스위첸 당첨자 발표, 1순위는 0.64 대 1"></span>

  <p>향남역 그로브 스위첸 당첨자가 오늘(10월 20일) 발표됩니다. KCC건설이 경기 화성시 향남읍에 짓는 933가구 단지로, 지난주 12일 특별공급, 13일 1순위, 14일 2순위 청약을 받았습니다. <span class="mark">결과는 공급보다 신청이 적은 미달이었습니다.</span> 당첨 여부는 청약홈에서 확인할 수 있습니다.</p>

  <h3>향남역 그로브 스위첸 청약 결과, 공급보다 신청이 적었다</h3>
  <div class="chart" data-img="카드뉴스 2번 · 향남역 그로브 스위첸 공급보다 신청이 적었다">
    <h3>공급 가구와 접수 건수 (가구·건)</h3>
    <div class="bar"><label>특공 공급</label>
      <div class="rail"><div class="fill gray" style="width:59.7%">475</div></div></div>
    <div class="bar"><label>특공 접수</label>
      <div class="rail"><div class="fill gray" style="width:17.5%"></div><span class="railval">139</span></div></div>
    <div class="bar"><label>1순위 공급</label>
      <div class="rail"><div class="fill gray" style="width:100%">795</div></div></div>
    <div class="bar"><label>1순위 접수</label>
      <div class="rail"><div class="fill" style="width:64.3%">511</div></div></div>
    <p class="cap">공급 가구와 접수 건수를 같은 축에 놓았습니다. 막대 길이는 최댓값 795를 기준으로 맞췄습니다. 10월 12·13일 청약 집계 기준이며 최종 수치는 청약홈에서 확인하십시오.</p>
  </div>
  <p>12일 특별공급은 475가구에 139건이 접수됐습니다. 신혼부부·생애최초 등 대상자가 생각보다 적게 들어왔습니다. 13일 1순위는 795가구에 511건이 접수됐습니다. 일반공급 물량이 모집공고보다 늘어난 것은 특별공급에서 남은 물량이 일반공급으로 넘어갔기 때문으로 보입니다. <span class="mark">특별공급과 1순위 모두 신청이 공급에 못 미쳤습니다.</span></p>

  <h3>1순위 0.64 대 1, 2순위 마감은 2개 주택형</h3>
  <div class="chart" data-img="카드뉴스 3번 · 1순위 0.64 대 1, 100가구에 64건">
    <h3>향남역 그로브 스위첸 평균 경쟁률</h3>
    <h4>1순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">0.64</span>
      <span class="desc">대 1. 100가구에 64건.</span></div>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">0.29</span>
      <span class="desc">대 1. 100가구에 29건.</span></div>
    <h4>2순위 마감</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2개</span>
      <span class="desc">전용 71㎡, 147㎡P. 나머지는 미달.</span></div>
    <p class="cap">1순위·특별공급은 10월 12·13일 청약 집계, 2순위 결과는 신아일보 주간분양 보도 기준입니다. 주택형별 최종 경쟁률은 청약홈에서 확인하십시오.</p>
  </div>
  <p>1순위 평균 경쟁률은 <strong>0.64 대 1</strong>입니다. 100가구에 64건이 들어온 셈입니다. 14일 2순위까지 받은 뒤 전용 71㎡와 147㎡P는 마감됐고 나머지 주택형은 미달로 끝났습니다. 같은 주 전국 청약 단지 가운데 순위 내 마감한 곳은 없었습니다. <span class="mark">미달 주택형의 남은 물량을 어떻게 다시 공급할지는 사업주체 공고가 나와야 확정됩니다.</span></p>

  <h3>향남역 그로브 스위첸 당첨 뒤 일정, 서류 24~28일</h3>
  <div class="chart" data-img="카드뉴스 4번 · 당첨 발표 뒤 서류·계약 일정">
    <h3>당첨 발표 뒤 일정 (보도 기준)</h3>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.20</span>
      <span class="desc">오늘. 청약홈에서 확인.</span></div>
    <h4>당첨자 서류 접수</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">24~28일</span>
      <span class="desc">5일간. 부적격이면 당첨 취소.</span></div>
    <h4>정당계약</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.2~4</span>
      <span class="desc">사흘간. 계약금 5% 준비.</span></div>
    <p class="cap">파이낸셜뉴스(10월 8일) 보도 기준입니다. 서류 목록과 접수 장소는 입주자모집공고로 확인하십시오.</p>
  </div>
  <p>당첨됐다면 다음 순서는 서류입니다. 10월 24일부터 28일까지 5일간 당첨자 서류를 받습니다. 무주택 기간, 거주 요건, 특별공급 자격이 서류로 확인되지 않으면 부적격으로 당첨이 취소될 수 있습니다. 정당계약은 11월 2일부터 4일까지 사흘입니다. <span class="mark">서류 목록은 모집공고에 있으니 발표 날 바로 떼어 두는 편이 안전합니다.</span></p>

  <h3>계약금 5%, 5억5천 집이면 2,750만원</h3>
  <div class="chart" data-img="카드뉴스 5번 · 5억5천 집이면 계약 때 2,750만원">
    <h3>전용 84㎡ 5억5천만원 예시 (분양가 대비 %)</h3>
    <div class="bar"><label>계약금</label>
      <div class="rail"><div class="fill gray" style="width:8.3%"></div><span class="railval">5% · 2,750만원</span></div></div>
    <div class="bar"><label>중도금</label>
      <div class="rail"><div class="fill gray" style="width:100%">60% · 3억3,000만원</div></div></div>
    <div class="bar"><label>잔금</label>
      <div class="rail"><div class="fill" style="width:58.3%">35% · 1억9,250만원</div></div></div>
    <p class="cap">모두 같은 항목(분양가 대비 비율)이라 한 축에 놓았습니다. 막대 길이는 최댓값 60%를 기준으로 맞췄습니다. 84㎡ '5억원 중반대' 보도를 5억5천만원으로 든 예시 계산이며 주택형별 확정가는 모집공고로 확인하십시오.</p>
  </div>
  <p>전용 84㎡ 분양가는 5억원 중반대로 보도됐습니다. 5억5천만원 집이라면 계약 때 <strong>2,750만원</strong>(5%)을 냅니다. 중도금 60%는 무이자라 공사 기간 이자 부담이 없습니다. <span class="mark">대신 입주 때 잔금 35%, 약 1억9,250만원을 한 번에 내야 합니다.</span> 잔금 대출 한도는 소득과 그때의 규제에 따라 달라지므로 계약 전에 은행 상담을 받아 두십시오.</p>

  <h3>향남역 그로브 스위첸 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 향남역 그로브 스위첸 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="hng1020-06-check.png" src="../images/cards/report/hng1020-06-check.png" alt="체크포인트 카드 · 1. 오늘 청약홈에서 당첨 확인, 2. 잔금 35% 대출부터, 3. 남은 집은 공고로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>향남역 그로브 스위첸 당첨자가 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>오늘 청약홈에서 당첨 확인</strong>. 당첨됐다면 10월 24~28일 서류를 냅니다. 부적격이면 당첨이 취소될 수 있습니다.</li>
    <li><strong>잔금 35% 대출부터</strong>. 중도금이 무이자여도 입주 때 큰돈이 한 번에 나갑니다. 계약 전에 은행 상담을 받으십시오.</li>
    <li><strong>남은 집은 공고로 확인</strong>. 미달 주택형의 추가 모집 여부와 방식은 사업주체 공고가 나와야 확정됩니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>향남역 그로브 스위첸</strong> 당첨자는 오늘(10월 20일) 발표됩니다. 1순위는 795가구에 511건으로 0.64 대 1, 특별공급은 475가구에 139건으로 0.29 대 1이었고 2순위까지 마감한 주택형은 71㎡와 147㎡P 두 개였습니다. <span class="mark">당첨자 서류는 24~28일, 정당계약은 11월 2~4일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 청약 권유가 아닙니다. 경쟁률은 10월 12·13일 청약 집계, 2순위 결과는 신아일보 주간분양, 일정은 파이낸셜뉴스(2026-10-08), 분양 조건은 서울경제·파이낸셜뉴스(2026-10-08~09) 보도 기준입니다. 최종 경쟁률과 주택형별 분양가는 청약홈 입주자모집공고에서 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 파이낸셜뉴스 향남역 그로브 스위첸 청약 일정(2026-10-08) · 서울경제 향남역 그로브 스위첸 분양가(2026-10-08) · 이데일리 1순위 청약(2026-10-13) · 신아일보 주간분양 · 청약홈 청약 경쟁률 집계(2026-10-12·13)<br>
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
assert round(139 / 475, 2) == 0.29 and round(511 / 795, 2) == 0.64 and 795 - 511 == 284
for v, h in ((475, 51.4), (139, 15.0), (511, 55.3)):
    assert round(v / 795 * 86, 1) == h, (v, h)
for v, w in ((475, 59.7), (139, 17.5), (511, 64.3)):
    assert round(v / 795 * 100, 1) == w, (v, w)
assert round(5 / 60 * 100, 1) == 8.3 and round(35 / 60 * 100, 1) == 58.3
assert 55000 * 5 // 100 == 2750 and 55000 * 60 // 100 == 33000 and 55000 * 35 // 100 == 19250
KW = "향남역 그로브 스위첸"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("향남역그로브스위첸")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
