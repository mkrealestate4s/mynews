# -*- coding: utf-8 -*-
"""리포트 #101 (2026-10-22) SH 재개발임대 서류심사 대상자 발표 D-1. #100을 복제해 교체한다.

메인 검색어: SH 재개발임대 서류심사

수치와 검산
  사건일과 오늘의 간격: 서류심사 대상자 발표 10/23(금) → D-1 (ops/calendar.md 10/23 줄)
  재공고(9/9) 보도(#79): 서울 162개 단지 3,821가구 · 주로 39㎡ 이하 · 1순위 소득 50% · 2순위 70%
    · 총자산 3억4,500만 · 자동차 4,542만 · 당첨 2027-03-30 · 입주 2027년 4월
  첫 공고(7/30) SH 공고 페이지: 155개 단지 3,421가구 → 연기(8/10) → 재공고(9/9)
  날 수: 접수 시작 9/29 → 서류발표 10/23 = 24 · 10/23 → 3/30 = 158 · 9/29 → 3/30 = 182
  가로 (182 → 100%): 158 → 86.8 · 24 → 13.2 ; (3,821 → 100%): 3,421 → 89.5
  대시보드 세로 (182 → 86%): 3 → 1.4 · 9 → 4.3 · 24 → 11.3

단정하지 않은 것
  · 서류 제출 기간·방법·서류 목록: 검색으로 확인 못 함 → 발표 안내·공고문 확인
  · 발표 시각: 확인 못 함
  · 3,421(첫 공고)과 3,821(재공고 보도) 차이의 이유는 확인 못 함 → 숫자만 병기
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-21-godeok3.html"
SLUG, PRE = "2026-10-22-shrdv-doc", "shd1022"
DST = ROOT / f"posts/{SLUG}.html"
NO, DATE = 101, "2026-10-22"
PREV_SLUG = "gdk1021-"
BANNED = ["고덕", "토지임대부"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "SH 재개발임대 서류심사 대상자, 내일 발표합니다"
DESC = ("SH 재개발임대 서류심사 대상자가 10월 23일 발표됩니다. 서울 162개 단지 3,821가구 모집이며, "
        "서류심사 대상은 당첨이 아닙니다. 당첨자 발표는 2027년 3월 30일, 입주는 2027년 4월 예정입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="10월 23일 서류심사 대상자 발표. 당첨까지 158일이 더 남았습니다. 서류로 다시 보는 소득·자산 기준을 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">SH 재개발임대 서류심사,<br>내일 발표</h1>
  <p class="sub"><strong>SH 재개발임대 서류심사</strong> 대상자가 내일, <strong>10월 23일</strong> 발표됩니다. 서울 162개 단지 <strong>3,821가구</strong>를 뽑는 모집입니다. 대상자로 뽑혀도 당첨은 아닙니다. <span class="mark">당첨자 발표는 2027년 3월 30일, 158일 뒤입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · D-1</div><div class="kw">10월 23일</div>
      <p>서류심사 대상자 <strong>발표</strong>.</p></div>
    <div class="kcard"><div class="hot">모집 물량</div><div class="kw">3,821가구</div>
      <p>서울 <strong>162개 단지</strong>.</p></div>
    <div class="kcard"><div class="hot">당첨까지</div><div class="kw">158일</div>
      <p>2027년 <strong>3월 30일</strong> 발표.</p></div>
    <div class="kcard"><div class="hot">입주</div><div class="kw">2027년 4월</div>
      <p>예정, 주로 39㎡ 이하.</p></div>
  </div>

  <div class="colchart">
    <h3>SH 재개발임대 접수 시작(9월 29일)부터 걸린 날 (일)</h3>
    <span class="badge">9월 9일 재공고</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:1.4%">3</div><div class="barv" style="--h:1.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:4.3%">9</div><div class="barv" style="--h:4.3%"></div></div>
      <div class="col"><div class="v gtx" style="--h:11.3%">24</div><div class="barv" style="--h:11.3%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">182</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>선순위 마감</span><span>후순위</span><span>서류심사 발표</span><span>당첨 발표</span></div>
    <p class="cap">9월 29일에서 각 일정까지의 날 수입니다. 막대 길이는 최댓값 182일을 기준으로 맞췄습니다. 일정은 SH 재공고(9월 9일)를 다룬 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: SH 재개발임대 서류심사 대상자, 내일 발표합니다"),
    ("02-date", "내일 발표, 그다음은 3월 30일"),
    ("03-wait", "서류심사에서 당첨까지 158일"),
    ("04-check", "서류로 다시 보는 기준 3가지"),
    ("05-supply", "재공고로 162개 단지 3,821가구"),
    ("06-tips", "SH 재개발임대 서류심사 체크 3가지"),
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

ARTICLE = '''<article data-tags="SH재개발임대서류심사,SH재개발임대,재개발임대주택,SH임대주택,서류심사대상자,서울임대주택,공공임대,무주택,1인가구,SH청약">
  <h2>SH 재개발임대 서류심사 대상자, 내일 발표</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: SH 재개발임대 서류심사 대상자, 내일 발표합니다"></span>

  <p>SH 재개발임대 서류심사 대상자가 내일(10월 23일) 발표됩니다. 서울주택도시공사(SH)가 9월 29일부터 접수한 2026년 재개발임대주택 모집의 다음 단계입니다. 서울 162개 단지에서 3,821가구를 뽑습니다. <span class="mark">서류심사 대상자는 당첨자가 아니라 서류를 내고 자격을 다시 확인받을 사람입니다.</span></p>

  <h3>SH 재개발임대 서류심사 발표, 그다음은 3월 30일</h3>
  <div class="chart" data-img="카드뉴스 2번 · 내일 발표, 그다음은 3월 30일">
    <h3>남은 일정 (재공고 보도 기준)</h3>
    <h4>서류심사 대상자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.23</span>
      <span class="desc">금요일. 대상이 되면 안내에 따라 서류를 냅니다.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3.30</span>
      <span class="desc">2027년.</span></div>
    <h4>입주</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4월</span>
      <span class="desc">2027년 예정.</span></div>
    <p class="cap">SH 재개발임대주택 입주자 모집 재공고(9월 9일)를 다룬 보도 기준입니다. 발표 시각, 서류 제출 기간과 방법은 SH 인터넷청약시스템 공고문과 발표 안내로 확인하십시오.</p>
  </div>
  <p>발표는 SH 인터넷청약시스템(i-sh.co.kr)에서 확인합니다. 대상자로 나오면 정해진 기간 안에 서류를 내야 합니다. <span class="mark">서류 제출 기간과 목록은 이 글에서 확인하지 못했습니다.</span> 발표 화면의 안내와 공고문을 그대로 따르십시오. 기간을 넘기면 대상에서 빠질 수 있습니다.</p>

  <h3>SH 재개발임대 서류심사에서 당첨까지 158일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 서류심사에서 당첨까지 158일">
    <h3>일정 사이 날 수 (일)</h3>
    <div class="bar"><label>접수 시작 → 당첨</label>
      <div class="rail"><div class="fill gray" style="width:100%">182</div></div></div>
    <div class="bar"><label>서류발표 → 당첨</label>
      <div class="rail"><div class="fill" style="width:86.8%">158</div></div></div>
    <div class="bar"><label>접수 시작 → 서류발표</label>
      <div class="rail"><div class="fill gray" style="width:13.2%"></div><span class="railval">24</span></div></div>
    <p class="cap">접수 시작 9월 29일, 서류심사 발표 10월 23일, 당첨 발표 2027년 3월 30일 사이의 날 수입니다. 막대 길이는 최댓값 182일을 기준으로 맞췄습니다.</p>
  </div>
  <p>접수부터 서류심사 발표까지는 24일이었지만, 서류심사 발표에서 당첨까지는 158일, 약 5개월이 더 걸립니다. 입주는 2027년 4월 예정입니다. <span class="mark">지금 사는 집 계약이 내년 봄 전에 끝난다면 재개발임대만 기다리지 말고 중간 거처를 함께 계획하십시오.</span></p>

  <h3>서류로 다시 보는 기준 3가지</h3>
  <div class="chart" data-img="카드뉴스 4번 · 서류로 다시 보는 기준 3가지">
    <h3>일반공급 신청 자격 (재공고 보도 기준)</h3>
    <h4>소득</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">50%</span>
      <span class="desc">도시근로자 월평균소득 이하가 1순위. 2순위는 70% 이하.</span></div>
    <h4>세대 총자산</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3억4,500만</span>
      <span class="desc">원 이하.</span></div>
    <h4>자동차</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">4,542만</span>
      <span class="desc">원 이하.</span></div>
    <p class="cap">공고일(9월 9일) 현재 서울 거주 무주택세대구성원이 대상입니다. 가구원 수별 소득 금액과 산정 방법은 공고문 표로 확인하십시오.</p>
  </div>
  <p>신청할 때 스스로 적은 소득·자산을 서류심사 단계에서 확인합니다. 기준은 소득 50% 이하가 1순위, 70% 이하가 2순위이고, 세대 총자산 3억4,500만원, 자동차 4,542만원 이하입니다. <span class="mark">퍼센트가 아니라 가구원 수별 금액으로 다시 맞춰 보십시오.</span> 세대원의 소득·자산도 함께 들어갑니다.</p>

  <h3>SH 재개발임대 물량, 재공고로 3,821가구</h3>
  <div class="chart" data-img="카드뉴스 5번 · 재공고로 162개 단지 3,821가구">
    <h3>모집 물량 (가구)</h3>
    <div class="bar"><label>첫 공고 7월 30일</label>
      <div class="rail"><div class="fill gray" style="width:89.5%">3,421</div></div></div>
    <div class="bar"><label>재공고 9월 9일</label>
      <div class="rail"><div class="fill" style="width:100%">3,821</div></div></div>
    <p class="cap">첫 공고는 SH 공고 페이지(155개 단지), 재공고는 9월 9일 보도(162개 단지) 기준입니다. 막대 길이는 최댓값 3,821을 기준으로 맞췄습니다. 예비입주자 모집이 함께 포함된 숫자입니다.</p>
  </div>
  <p>이번 모집은 7월 30일 첫 공고를 8월 10일 연기했다가 9월 9일 다시 낸 재공고입니다. 첫 공고는 155개 단지 3,421가구였고, 재공고 보도는 162개 단지 3,821가구입니다. 재공고에서 연령 가점이 빠지고 사회취약계층 가점은 되살아났습니다. <span class="mark">주로 전용 39㎡ 이하 소형이라 1~2인 가구에 맞는 집입니다.</span></p>

  <h3>SH 재개발임대 서류심사 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · SH 재개발임대 서류심사 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="shd1022-06-tips.png" src="../images/cards/report/shd1022-06-tips.png" alt="체크포인트 카드 · 1. 10월 23일 발표 확인, 2. 서류는 기간 안에, 3. 당첨까지 158일 거처 계획" loading="lazy" width="1080" height="1080">
    <figcaption>SH 재개발임대 서류심사 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>10월 23일 발표 확인</strong>. SH 인터넷청약시스템에서 본인 결과를 봅니다. 발표 시각은 공고문으로 확인하십시오.</li>
    <li><strong>서류는 기간 안에</strong>. 제출 기간·방법·서류 목록은 발표 안내를 따릅니다. 세대원 서류도 함께 챙기십시오.</li>
    <li><strong>당첨까지 158일 거처 계획</strong>. 당첨 발표는 2027년 3월 30일, 입주는 4월입니다. 지금 집 만기를 함께 보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>SH 재개발임대 서류심사</strong> 대상자는 내일(10월 23일) 발표됩니다. 서울 162개 단지 3,821가구 모집이며, 대상자로 뽑혀도 당첨은 아닙니다. 서류를 기간 안에 내고 소득·자산을 다시 확인받아야 합니다. <span class="mark">당첨자 발표는 2027년 3월 30일, 입주는 2027년 4월 예정입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 특정 청약을 권유하지 않습니다. 모집 물량·자격·일정은 SH 2026년 재개발임대주택 입주자 모집 재공고(9월 9일)를 다룬 보도(헤럴드경제·서울경제·디벨로퍼뉴스·아시아투데이·한국경제)와 SH 공고 페이지 기준입니다. 발표 시각, 서류 제출 기간·방법·목록은 확인하지 못해 적지 않았습니다. SH 인터넷청약시스템(i-sh.co.kr) 공고문과 발표 안내로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 헤럴드경제·서울경제·디벨로퍼뉴스 SH 재개발임대주택 재공고(2026-09-09) · 아시아투데이·한국경제 재개발임대 3,821가구 모집(2026-09) · SH 서울주택도시공사 재개발임대주택 입주자 모집공고(2026-07-30)<br>
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
import datetime as _d
assert (_d.date(2027, 3, 30) - _d.date(2026, 10, 23)).days == 158
assert (_d.date(2027, 3, 30) - _d.date(2026, 9, 29)).days == 182
assert (_d.date(2026, 10, 23) - _d.date(2026, 9, 29)).days == 24
for v, w in ((158, 86.8), (24, 13.2)):
    assert round(v / 182 * 100, 1) == w
assert round(3421 / 3821 * 100, 1) == 89.5
for v, h in ((3, 1.4), (9, 4.3), (24, 11.3)):
    assert round(v / 182 * 86, 1) == h
KW = "SH 재개발임대 서류심사"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("SH재개발임대서류심사")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
