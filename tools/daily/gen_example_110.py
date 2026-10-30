# -*- coding: utf-8 -*-
"""리포트 #110 (2026-10-31) 고덕강일3단지 특별공급 월요일 접수(D-2). #109를 복제해 교체한다.

메인 검색어: 고덕강일3단지 특별공급

수치와 검산
  사건일과 오늘의 간격: 특별공급 접수 11/2(월) → D-2. 일반 1순위 11/4 → D-4.
    이투데이 11월 첫째 주 분양캘린더(10/30)에도 4일 고덕강일3단지 접수로 올라 있다.
  #100(10/21) 수치를 그대로 쓴다 (공고 10/16 보도: 뉴스핌·이투데이·아주경제·파이낸셜신문·경향신문)
  공급: 총 1,305 = 사전청약 당첨자 592 + 특별공급 566 + 일반공급 147
  건물 분양가: 49㎡ 2억8천~3억2천 · 59㎡ 3억4천~3억9천
  월 토지임대료: 49㎡ 42만6,000원 · 59㎡ 51만1,500원. 최대 60% 보증금 전환
  일정: 사전청약 당첨자 10/26~27(지남) · 특공 11/2~3 · 일반 1순위 서울 2년 이상 11/4
    · 서울 2년 미만·경기·인천 11/5 · 2순위 11/6 · 발표 11/26
  공급 가로 (592 → 100%): 566 → 95.6 · 147 → 24.8
  새로 뽑는 713 중 특공 비중: 566/713 = 79.4% → 100명 중 79명
  분양가 가로 (3.9억 → 100%): 2.8 → 71.8 · 3.2 → 82.1 · 3.4 → 87.2
  대시보드 세로 (566 → 86%): 147 → 22.3

단정하지 않은 것
  · 특별공급 유형별(신혼·생애최초·다자녀 등) 배정 수는 검색 요약에 없다 → 공고문 확인
  · 소득·자산 기준, 사전청약 당첨자 본청약 신청 결과(미신청 물량 이월 여부)는 확인 못 함
  · 분양가는 동·층별 범위(보도 기준)
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-30-cheongna-arkone.html"
DST = ROOT / "posts/2026-10-31-godeok3-special.html"
SLUG, PRE = "2026-10-31-godeok3-special", "gdk1031"
NO, DATE = 110, "2026-10-31"
PREV_SLUG = "arw1030-"
BANNED = ["청라", "아크원", "푸르지오"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "고덕강일3단지 특별공급 월요일 접수, 566가구"
DESC = ("고덕강일3단지 특별공급 접수가 11월 2일 월요일에 시작됩니다. SH 토지임대부 분양주택에서 새로 뽑는 713가구 가운데 "
        "566가구가 특별공급, 일반공급은 147가구입니다. 건물 분양가는 49㎡ 2억8천만원부터, 월 토지임대료는 42만6천원입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="특별공급 11월 2~3일, 일반 1순위 11월 4일, 발표 11월 26일. 접수 전에 볼 분양가와 매달 내는 토지임대료를 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">고덕강일3단지 특별공급,<br>월요일 접수</h1>
  <p class="sub"><strong>고덕강일3단지 특별공급</strong> 접수가 <strong>11월 2일 월요일</strong>에 시작됩니다. SH 토지임대부 분양주택에서 새로 뽑는 713가구 가운데 <strong>566가구</strong>가 특별공급입니다. 일반 1순위는 <strong>11월 4일</strong>, 당첨자 발표는 11월 26일입니다. <span class="mark">주말 동안 공고문으로 내 유형과 소득·자산 기준을 먼저 맞춰 보십시오.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 특별공급</div><div class="kw">566가구</div>
      <p>새로 뽑는 713가구의 <strong>79%</strong>.</p></div>
    <div class="kcard"><div class="hot">특공 접수</div><div class="kw">11월 2일</div>
      <p>월·화 이틀, <strong>3일</strong>까지.</p></div>
    <div class="kcard"><div class="hot">건물 분양가</div><div class="kw">2억8천~</div>
      <p>49㎡ 기준, 59㎡는 <strong>3억4천~</strong>.</p></div>
    <div class="kcard"><div class="hot">일반 1순위</div><div class="kw">11월 4일</div>
      <p>서울 2년 이상 거주자.</p></div>
  </div>

  <div class="colchart">
    <h3>고덕강일3단지 본청약에서 새로 뽑는 집 (가구)</h3>
    <span class="badge">11월 2일 특공 접수</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">566</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:22.3%">147</div><div class="barv" style="--h:22.3%"></div></div>
    </div>
    <div class="collbl"><span>특별공급</span><span>일반공급</span></div>
    <p class="cap">사전청약 당첨자 몫 592가구를 뺀 713가구입니다. 막대 길이는 최댓값 566을 기준으로 맞췄습니다. 뉴스핌·이투데이(10월 16일) 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 고덕강일3단지 특별공급 월요일 접수, 566가구"),
    ("02-supply", "새로 뽑는 713가구 중 566가구가 특별공급"),
    ("03-date", "특공 11월 2일, 일반 11월 4일"),
    ("04-price", "건물값 2억8천만원부터, 땅은 빌린다"),
    ("05-rent", "땅값은 매달, 49㎡ 월 42만6천원"),
    ("06-check", "고덕강일3단지 특별공급 접수 전 체크 3가지"),
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

ARTICLE = '''<article data-tags="고덕강일3단지특별공급,고덕강일3단지,고덕강일3단지본청약,토지임대부,토지임대부분양주택,SH청약,강동구,특별공급,공공분양,11월청약">
  <h2>고덕강일3단지 특별공급, 월요일 접수</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 고덕강일3단지 특별공급 월요일 접수, 566가구"></span>

  <p>고덕강일3단지 특별공급 접수가 11월 2일 월요일에 시작됩니다. 서울주택도시공사(SH)가 강동구 고덕강일3단지 토지임대부 분양주택 1,305가구를 본청약으로 공급하는데, 사전청약 당첨자 접수(10월 26~27일)는 끝났고 이제 새로 뽑는 순서입니다. 토지임대부는 땅은 공공이 갖고 건물만 분양하는 방식입니다. <span class="mark">분양가가 3억원 안팎으로 낮은 대신 땅값을 매달 토지임대료로 냅니다.</span></p>

  <h3>고덕강일3단지 특별공급 566가구, 새로 뽑는 집의 79%</h3>
  <div class="chart" data-img="카드뉴스 2번 · 새로 뽑는 713가구 중 566가구가 특별공급">
    <h3>공급 구성 (가구)</h3>
    <div class="bar"><label>사전청약 당첨자</label>
      <div class="rail"><div class="fill gray" style="width:100%">592</div></div></div>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill" style="width:95.6%">566</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill gray" style="width:24.8%"></div><span class="railval">147</span></div></div>
    <p class="cap">합계 1,305가구(전용 49㎡ 590가구, 59㎡ 715가구). 막대 길이는 최댓값 592를 기준으로 맞췄습니다. 뉴스핌·이투데이(10월 16일) 보도 기준입니다.</p>
  </div>
  <p>1,305가구 가운데 592가구는 사전청약 당첨자 몫입니다. 본청약으로 새로 뽑는 집은 713가구이고, 이 중 <strong>566가구가 특별공급</strong>, 일반공급은 147가구입니다. 새로 뽑는 집 100채 가운데 79채가 특별공급인 셈입니다. <span class="mark">신혼부부·생애최초 같은 특별공급 자격이 있다면 일반공급보다 이쪽 문이 훨씬 넓습니다.</span> 유형별 배정 수는 SH 모집공고문에서 확인하십시오.</p>

  <h3>고덕강일3단지 특별공급 일정, 11월 2~3일</h3>
  <div class="chart" data-img="카드뉴스 3번 · 특공 11월 2일, 일반 11월 4일">
    <h3>남은 접수 일정 (보도 기준)</h3>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.2~3</span>
      <span class="desc">월·화 이틀.</span></div>
    <h4>일반 1순위 (서울 2년 이상)</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.4</span>
      <span class="desc">수요일.</span></div>
    <h4>일반 1순위 (그 밖 수도권)·2순위</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.5~6</span>
      <span class="desc">5일 1순위, 6일 2순위.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.26</span>
      <span class="desc">목요일.</span></div>
    <p class="cap">뉴스핌·파이낸셜신문(10월 16일)과 이투데이 분양캘린더(10월 30일) 기준입니다. 접수 시간과 방법은 SH 인터넷청약시스템 공고문으로 확인하십시오.</p>
  </div>
  <p>특별공급은 11월 2~3일 이틀입니다. 일반공급은 거주지에 따라 날짜가 갈립니다. 서울에 2년 이상 산 1순위는 4일, 서울 2년 미만과 경기·인천 거주자는 5일, 2순위는 6일입니다. 경쟁이 붙으면 서울 2년 이상 거주자에게 물량 절반을 먼저 줍니다. <span class="mark">당첨자 발표는 11월 26일입니다.</span></p>

  <h3>건물값 2억8천만원부터, 땅은 빌린다</h3>
  <div class="chart" data-img="카드뉴스 4번 · 건물값 2억8천만원부터, 땅은 빌린다">
    <h3>건물 분양가 범위 (억원)</h3>
    <div class="bar"><label>49㎡ 하단</label>
      <div class="rail"><div class="fill gray" style="width:71.8%">2.8억</div></div></div>
    <div class="bar"><label>49㎡ 상단</label>
      <div class="rail"><div class="fill gray" style="width:82.1%">3.2억</div></div></div>
    <div class="bar"><label>59㎡ 하단</label>
      <div class="rail"><div class="fill" style="width:87.2%">3.4억</div></div></div>
    <div class="bar"><label>59㎡ 상단</label>
      <div class="rail"><div class="fill" style="width:100%">3.9억</div></div></div>
    <p class="cap">땅값을 뺀 건물 분양가입니다. 막대 길이는 최댓값 3.9억원을 기준으로 맞췄습니다. 뉴스핌(10월 16일) 보도 기준이며 동·층별 확정가는 모집공고에서 확인하십시오.</p>
  </div>
  <p>건물 분양가는 전용 49㎡가 2억8천만~3억2천만원, 59㎡가 3억4천만~3억9천만원입니다. 강동구 새 아파트로는 낮은 값이지만 땅이 포함되지 않은 가격입니다. 전매는 10년 동안 막혀 있고, 그 뒤로는 개인 간 거래가 허용됩니다. <span class="mark">땅은 40년 동안 빌려 쓰고, 재계약하면 최장 80년까지 살 수 있습니다.</span></p>

  <h3>토지임대료, 49㎡ 월 42만6천원</h3>
  <div class="chart" data-img="카드뉴스 5번 · 땅값은 매달, 49㎡ 월 42만6천원">
    <h3>월 토지임대료 (보도 기준)</h3>
    <h4>전용 49㎡</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">42.6만</span>
      <span class="desc">원. 1년이면 약 511만원.</span></div>
    <h4>전용 59㎡</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">51.2만</span>
      <span class="desc">원(51만1,500원). 1년이면 약 614만원.</span></div>
    <h4>보증금 전환</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">60%</span>
      <span class="desc">임대료의 최대 60%까지, SH와 합의해 보증금으로.</span></div>
    <p class="cap">아주경제·뉴스핌(10월 16일) 보도 기준입니다. 1년치는 월액에 12를 곱한 단순 계산입니다. 전환 비율과 임대료 조정 방식은 계약 때 안내됩니다.</p>
  </div>
  <p>건물값과 별도로 매달 토지임대료가 나갑니다. 49㎡는 월 42만6천원, 59㎡는 월 51만1,500원입니다. 1년이면 각각 약 511만원, 614만원입니다. 임대료의 최대 60%는 SH와 합의해 보증금으로 돌릴 수 있습니다. <span class="mark">특별공급에 넣기 전에 건물값 대출 이자와 토지임대료를 더한 한 달 부담을 계산해 두십시오.</span></p>

  <h3>고덕강일3단지 특별공급 접수 전 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 고덕강일3단지 특별공급 접수 전 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="gdk1031-06-check.png" src="../images/cards/report/gdk1031-06-check.png" alt="체크포인트 카드 · 1. 내 특공 유형과 배정 수는 공고문으로, 2. 소득·자산 기준은 유형마다 다르다, 3. 분양가에 토지임대료 더해 계산" loading="lazy" width="1080" height="1080">
    <figcaption>고덕강일3단지 특별공급 접수 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>내 특공 유형과 배정 수는 공고문으로</strong>. 신혼부부·생애최초·다자녀 등 유형별 물량은 SH 모집공고문에 나옵니다. 특별공급은 평생 한 번이니 유형을 고를 때 신중하십시오.</li>
    <li><strong>소득·자산 기준은 유형마다 다르다</strong>. 공고일(10월 16일) 기준 수도권 무주택 가구구성원이면서 청약통장이 있어야 합니다. 세부 기준은 공고문으로 확인하십시오.</li>
    <li><strong>분양가에 토지임대료 더해 계산</strong>. 건물값 대출 이자에 월 42만~51만원이 더해집니다. 전매 10년 제한도 함께 따져 보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>고덕강일3단지 특별공급</strong>은 11월 2~3일 접수합니다. SH 토지임대부 1,305가구 가운데 새로 뽑는 713가구의 79%인 566가구가 특별공급이고, 일반공급은 147가구입니다. 건물 분양가는 49㎡ 2억8천만원부터, 월 토지임대료는 42만6천원부터입니다. <span class="mark">특별공급 11월 2~3일, 일반 1순위 11월 4일, 발표 11월 26일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 청약 권유가 아닙니다. 공급 규모·분양가·일정은 뉴스핌·이투데이·파이낸셜신문(2026-10-16)과 이투데이 분양캘린더(2026-10-30), 토지임대료는 아주경제(2026-10-16) 보도 기준입니다. 특별공급 유형별 물량, 소득·자산 기준과 동·층별 분양가는 SH 인터넷청약시스템(i-sh.co.kr) 입주자모집공고에서 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 뉴스핌 고덕강일3단지 토지임대부 본청약(2026-10-16) · 이투데이 고덕강일3단지 본청약 시작(2026-10-16) · 이투데이 11월 첫째 주 분양캘린더(2026-10-30) · 아주경제 분양가·토지임대료(2026-10-16) · 파이낸셜신문 1,305세대 공급(2026-10-16) · SH 서울주택도시공사 입주자모집공고<br>
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
assert 592 + 566 + 147 == 1305 and 590 + 715 == 1305 and 566 + 147 == 713
assert round(566 / 713 * 100, 1) == 79.4
for v, w in ((566, 95.6), (147, 24.8)):
    assert round(v / 592 * 100, 1) == w, (v, w)
for v, w in ((2.8, 71.8), (3.2, 82.1), (3.4, 87.2)):
    assert round(v / 3.9 * 100, 1) == w, (v, w)
assert round(147 / 566 * 86, 1) == 22.3
assert 426000 * 12 == 5112000 and 511500 * 12 == 6138000
KW = "고덕강일3단지 특별공급"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("고덕강일3단지특별공급")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
