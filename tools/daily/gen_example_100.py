# -*- coding: utf-8 -*-
"""리포트 #100 (2026-10-21) 고덕강일3단지 토지임대부 본청약. #99를 복제해 교체한다.

메인 검색어: 고덕강일3단지 본청약

수치와 검산
  사건일과 오늘의 간격: 입주자모집공고 10/16 → 5일. 첫 접수(사전청약 당첨자) 10/26 → D-5.
  공급 (뉴스핌·이투데이 10/16): 총 1,305 = 사전청약 당첨자 592 + 특별공급 566 + 일반공급 147
    주택형: 49㎡ 590 · 59㎡ 715 (합 1,305)
  건물 분양가: 49㎡ 2억8천~3억2천 · 59㎡ 3억4천~3억9천 (뉴스핌)
  월 토지임대료: 49㎡ 42만6,000원 · 59㎡ 51만1,500원 (아주경제). 최대 60% 보증금 전환(SH와 합의)
    연 환산: 42.6만×12 = 511.2만 · 51.15만×12 = 613.8만
  일정 (파이낸셜신문 등): 사전청약 당첨자 10/26~27 · 특공 11/2~3 · 일반 1순위 서울 2년 이상 11/4
    · 서울 2년 미만·경기·인천 11/5 · 2순위 11/6 · 발표 11/26
  전매제한 10년 · 40년 거주 후 재계약 최장 80년 (이투데이)
  자격: 공고일 기준 수도권 무주택 가구구성원 + 청약통장. 서울 2년 이상 50% 우선 (뉴스핌)
  공급 가로 (592 → 100%): 566 → 95.6 · 147 → 24.8
  분양가 가로 (3.9억 → 100%): 2.8 → 71.8 · 3.2 → 82.1 · 3.4 → 87.2
  대시보드 세로 (3.9 → 86%): 2.8 → 61.7 · 3.2 → 70.6 · 3.4 → 75.0

단정하지 않은 것
  · 소득·자산 기준은 검색 요약에 없다 → 모집공고문 확인 안내
  · 토지임대료 인상·보증금 전환 비율은 계약 때 안내 → 확정 아님
  · 분양가는 동·층별 범위(보도 기준)
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-20-hyangnam-result.html"
DST = ROOT / "posts/2026-10-21-godeok3.html"
SLUG, PRE = "2026-10-21-godeok3", "gdk1021"
NO, DATE = 100, "2026-10-21"
PREV_SLUG = "hng1020-"
BANNED = ["향남", "스위첸", "KCC"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "고덕강일3단지 본청약, 1,305가구 중 일반공급은 147가구"
DESC = ("고덕강일3단지 본청약이 시작됐습니다. SH 토지임대부 분양주택 1,305가구 가운데 사전청약 당첨자 몫이 592가구, "
        "특별공급 566가구, 일반공급은 147가구입니다. 건물 분양가는 49㎡ 2억8천만원부터, 월 토지임대료는 42만6천원입니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="사전청약 10월 26일, 특별공급 11월 2일, 일반 1순위 11월 4일. 분양가와 매달 내는 토지임대료까지 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">고덕강일3단지 본청약,<br>일반공급은 147가구</h1>
  <p class="sub"><strong>고덕강일3단지 본청약</strong>이 시작됐습니다. SH 토지임대부 분양주택 <strong>1,305가구</strong> 가운데 사전청약 당첨자 몫을 빼면 새로 뽑는 집은 713가구, 그중 일반공급은 <strong>147가구</strong>입니다. 사전청약 당첨자 접수는 <strong>10월 26일</strong>, 일반 1순위는 <strong>11월 4일</strong>입니다. <span class="mark">건물만 분양받고 땅값은 매달 토지임대료로 냅니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 본청약</div><div class="kw">1,305가구</div>
      <p>49㎡ 590 · <strong>59㎡ 715</strong>.</p></div>
    <div class="kcard"><div class="hot">일반공급</div><div class="kw">147가구</div>
      <p>특별공급은 <strong>566가구</strong>.</p></div>
    <div class="kcard"><div class="hot">건물 분양가</div><div class="kw">2억8천~</div>
      <p>49㎡ 기준, 59㎡는 <strong>3억4천~</strong>.</p></div>
    <div class="kcard"><div class="hot">일반 1순위</div><div class="kw">11월 4일</div>
      <p>서울 2년 이상 거주자.</p></div>
  </div>

  <div class="colchart">
    <h3>고덕강일3단지 건물 분양가 범위 (억원)</h3>
    <span class="badge">10월 16일 공고</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:61.7%">2.8</div><div class="barv" style="--h:61.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:70.6%">3.2</div><div class="barv" style="--h:70.6%"></div></div>
      <div class="col"><div class="v gtx" style="--h:75%">3.4</div><div class="barv" style="--h:75%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">3.9</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>49㎡ 하단</span><span>49㎡ 상단</span><span>59㎡ 하단</span><span>59㎡ 상단</span></div>
    <p class="cap">건물 분양가의 하단·상단입니다(땅값 제외). 막대 길이는 최댓값 3.9억원을 기준으로 맞췄습니다. 뉴스핌(10월 16일) 보도 기준이며 동·층별 확정가는 SH 입주자모집공고에서 확인하십시오.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 고덕강일3단지 본청약, 1,305가구 중 일반공급은 147가구"),
    ("02-supply", "고덕강일3단지 새로 뽑는 집은 713가구"),
    ("03-date", "접수 일정, 10월 26일부터 11월 6일까지"),
    ("04-price", "건물값 2억8천만원부터, 땅은 빌린다"),
    ("05-rent", "땅값은 매달, 49㎡ 월 42만6천원"),
    ("06-check", "고덕강일3단지 본청약 체크 3가지"),
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

ARTICLE = '''<article data-tags="고덕강일3단지본청약,고덕강일3단지,토지임대부,토지임대부분양주택,SH청약,강동구,고덕강일,공공분양,무주택청약,청약일정">
  <h2>고덕강일3단지 본청약, 일반공급은 147가구</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 고덕강일3단지 본청약, 1,305가구 중 일반공급은 147가구"></span>

  <p>고덕강일3단지 본청약이 시작됐습니다. 서울주택도시공사(SH)가 지난 16일 강동구 고덕강일3단지 토지임대부 분양주택 1,305가구의 입주자모집공고를 냈습니다. 토지임대부는 땅은 공공이 갖고 건물만 분양하는 방식입니다. <span class="mark">그래서 분양가가 3억원 안팎으로 낮은 대신, 땅값을 매달 토지임대료로 냅니다.</span> 첫 접수는 10월 26일 사전청약 당첨자부터입니다.</p>

  <h3>고덕강일3단지 본청약 물량, 새로 뽑는 집은 713가구</h3>
  <div class="chart" data-img="카드뉴스 2번 · 고덕강일3단지 새로 뽑는 집은 713가구">
    <h3>공급 구성 (가구)</h3>
    <div class="bar"><label>사전청약 당첨자</label>
      <div class="rail"><div class="fill gray" style="width:100%">592</div></div></div>
    <div class="bar"><label>특별공급</label>
      <div class="rail"><div class="fill gray" style="width:95.6%">566</div></div></div>
    <div class="bar"><label>일반공급</label>
      <div class="rail"><div class="fill" style="width:24.8%"></div><span class="railval">147</span></div></div>
    <p class="cap">합계 1,305가구(전용 49㎡ 590가구, 59㎡ 715가구). 막대 길이는 최댓값 592를 기준으로 맞췄습니다. 뉴스핌·이투데이(10월 16일) 보도 기준입니다.</p>
  </div>
  <p>1,305가구 가운데 592가구는 사전청약 당첨자에게 먼저 배정됩니다. 본청약으로 새로 뽑는 집은 713가구이고, 이 중 566가구가 신혼부부·생애최초 같은 특별공급, <strong>일반공급은 147가구</strong>입니다. 경쟁이 붙으면 서울에 2년 이상 계속 산 사람에게 절반을 먼저 줍니다. <span class="mark">일반공급만 노린다면 문이 좁으니 특별공급 자격부터 따져 보는 편이 낫습니다.</span></p>

  <h3>고덕강일3단지 접수 일정, 10월 26일부터</h3>
  <div class="chart" data-img="카드뉴스 3번 · 접수 일정, 10월 26일부터 11월 6일까지">
    <h3>본청약 접수 일정 (보도 기준)</h3>
    <h4>사전청약 당첨자</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10.26~27</span>
      <span class="desc">다음 주 월·화.</span></div>
    <h4>특별공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.2~3</span>
      <span class="desc">신혼부부·생애최초 등.</span></div>
    <h4>일반공급</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.4~6</span>
      <span class="desc">4일 서울 2년 이상, 5일 그 밖 수도권, 6일 2순위.</span></div>
    <h4>당첨자 발표</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.26</span>
      <span class="desc">목요일.</span></div>
    <p class="cap">뉴스핌·파이낸셜신문(10월 16일) 보도 기준입니다. 접수 시간과 방법은 SH 인터넷청약시스템 공고문으로 확인하십시오.</p>
  </div>
  <p>사전청약 당첨자는 10월 26~27일 본청약을 신청해야 자기 몫을 지킵니다. 특별공급은 11월 2~3일, 일반공급은 11월 4~6일입니다. 일반공급은 거주지에 따라 날짜가 갈립니다. 서울에 2년 이상 산 1순위는 4일, 서울 2년 미만과 경기·인천 거주자는 5일, 2순위는 6일입니다. <span class="mark">당첨자 발표는 11월 26일입니다.</span></p>

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
  <p>건물값과 별도로 매달 토지임대료가 나갑니다. 49㎡는 월 42만6천원, 59㎡는 월 51만1,500원입니다. 1년이면 각각 약 511만원, 614만원입니다. 임대료의 최대 60%는 SH와 합의해 보증금으로 돌릴 수 있습니다. <span class="mark">보증금으로 돌리면 월 부담은 줄지만 목돈이 더 들어가니, 대출 이자와 비교해 정하십시오.</span></p>

  <h3>고덕강일3단지 본청약 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 고덕강일3단지 본청약 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="gdk1021-06-check.png" src="../images/cards/report/gdk1021-06-check.png" alt="체크포인트 카드 · 1. 소득·자산 기준은 공고문으로, 2. 서울 2년 거주면 11월 4일, 3. 분양가에 토지임대료 더해 계산" loading="lazy" width="1080" height="1080">
    <figcaption>고덕강일3단지 본청약 전에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>소득·자산 기준은 공고문으로</strong>. 공고일(10월 16일) 기준 수도권 무주택 가구구성원이면서 청약통장이 있어야 합니다. 소득·자산 기준은 공급 유형마다 다르니 SH 모집공고문에서 확인하십시오.</li>
    <li><strong>서울 2년 거주면 11월 4일</strong>. 일반공급은 거주지별로 접수일이 다릅니다. 날짜를 놓치면 다음 순서로 밀립니다.</li>
    <li><strong>분양가에 토지임대료 더해 계산</strong>. 건물값 대출 이자에 월 42만~51만원이 더해집니다. 전매 10년 제한도 함께 따져 보십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>고덕강일3단지 본청약</strong>은 SH 토지임대부 1,305가구 가운데 사전청약 당첨자 592가구를 뺀 713가구를 새로 뽑습니다. 특별공급 566가구, 일반공급 147가구입니다. 건물 분양가는 49㎡ 2억8천만원부터, 월 토지임대료는 42만6천원부터입니다. <span class="mark">사전청약 당첨자 10월 26~27일, 특별공급 11월 2~3일, 일반 1순위 11월 4일, 발표 11월 26일입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 청약 권유가 아닙니다. 공급 규모·분양가·일정은 뉴스핌·이투데이·파이낸셜신문(2026-10-16), 토지임대료는 아주경제(2026-10-16) 보도 기준입니다. 소득·자산 기준과 동·층별 분양가는 SH 인터넷청약시스템(i-sh.co.kr) 입주자모집공고에서 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 뉴스핌 고덕강일3단지 토지임대부 본청약(2026-10-16) · 이투데이 고덕강일3단지 본청약 시작(2026-10-16) · 아주경제 분양가·토지임대료(2026-10-16) · 파이낸셜신문 1,305세대 공급(2026-10-16) · SH 서울주택도시공사 입주자모집공고<br>
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
for v, w in ((566, 95.6), (147, 24.8)):
    assert round(v / 592 * 100, 1) == w, (v, w)
for v, w in ((2.8, 71.8), (3.2, 82.1), (3.4, 87.2)):
    assert round(v / 3.9 * 100, 1) == w, (v, w)
for v, h in ((2.8, 61.7), (3.2, 70.6), (3.4, 75.0)):
    assert round(v / 3.9 * 86, 1) == h, (v, h)
assert 426000 * 12 == 5112000 and 511500 * 12 == 6138000
KW = "고덕강일3단지 본청약"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("고덕강일3단지본청약")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
