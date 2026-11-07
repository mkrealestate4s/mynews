# -*- coding: utf-8 -*-
"""리포트 #119 (2026-11-08) 목동13단지 재건축 시공사 삼성물산 확정. #118을 복제해 교체한다.

메인 검색어: 목동13단지 재건축

수치와 검산
  사건일과 오늘의 간격: 제2차 토지등소유자 전체회의 11/7(어제, 리드) · 우협 선정 9/29(배경).
  목동13단지 (머니투데이방송 11/7 · 하우징타임즈 · 위클리한국주택경제 · 데일리한국 보도):
    사업시행자 대신자산신탁 · 11/7 동양미래대 대강당 · 동의 토지등소유자 2,127명 중 1,884명 참석(부재자 포함)
    1,803명(95.7%) 삼성물산 선택 · 도급액 약 2조3,763억원 · 3.3㎡당 980만원(부가세 제외)
    지하4~지상49층 3,852세대 계획 · 1차 입찰 단독 응찰 유찰 → 재입찰 단독 → 9/29 우협
    삼성물산 올해 정비 누적 12조8,449억원, 목표 13조까지 1,551억원 · 단지명 '래미안 모브13' 제안(MTN 10/8)
  목동 현황 (뉴스웨이 11/5 · 서울경제TV 10/28): 6단지 DL이앤씨 · 10단지 현대건설(2조6,136억) 확정,
    8 대우 · 12 GS 우협, 4단지 11/16 입찰 마감, 7단지 이달 공고 예정, 14단지 5,123가구.
  투표 가로 (2,127 → 100): 1,884 → 88.6 · 1,803 → 84.8
  계획 가구수 대시보드(#112 동일): 14 5,123 · 10 4,248 · 9 3,961 · 13 3,852 · 12 2,810 · 4 2,436
  3.3㎡당 공사비(#112 동일): 4 1,010 · 10 990 · 9 980 · 12 980 · 13 980 · 8 965

단정하지 않은 것
  · 3,852세대·49층은 계획(확정 전) · 래미안 모브13은 제안 단지명 · 분담금 미정
  · 조합원 지위 양도 제한은 단계마다 다름 → 사업시행자·정비사업 정보몽땅 확인
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-07-gwanggyo-equity.html"
DST = ROOT / "posts/2026-11-08-mokdong13.html"
SLUG, PRE = "2026-11-08-mokdong13", "mk13"
NO, DATE = 119, "2026-11-08"
PREV_SLUG = "gk1107-"
BANNED = ["광교", "지분적립형", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "목동13단지 재건축, 삼성물산 95.7%로 확정"
DESC = ("목동13단지 재건축 시공사가 11월 7일 전체회의에서 삼성물산으로 확정됐습니다. 참석자 1,884명 중 1,803명이 찬성했습니다. "
        "도급액 약 2조3,763억원, 3.3㎡당 980만원, 최고 49층 3,852세대 계획입니다. 목동 시공사 현황과 다음 일정을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="두 번 모두 단독 응찰, 그리고 95.7% 찬성. 공사비 2조3,763억원, 3,852세대 계획. 목동 14개 단지 중 시공사가 정해진 곳과 남은 곳을 정리했습니다.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">목동13단지 재건축<br>삼성물산 95.7%로 확정</h1>
  <p class="sub"><strong>목동13단지 재건축</strong> 시공사가 <strong>어제(11월 7일)</strong> 토지등소유자 전체회의에서 <strong>삼성물산</strong>으로 확정됐습니다. 참석자 1,884명 중 1,803명(95.7%)이 찬성했습니다. 도급액은 약 <strong>2조3,763억원</strong>, 최고 49층 3,852세대 계획입니다. <span class="mark">목동에서 시공사가 확정된 세 번째 단지이고, 이번에도 경쟁 없이 단독 응찰이었습니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 목동13단지</div><div class="kw">11월 7일</div>
      <p>시공사 <strong>삼성물산</strong> 확정.</p></div>
    <div class="kcard"><div class="hot">찬성률</div><div class="kw">95.7%</div>
      <p>참석 1,884명 중 <strong>1,803명</strong>.</p></div>
    <div class="kcard"><div class="hot">도급액</div><div class="kw">2조3,763억</div>
      <p>3.3㎡당 <strong>980만원</strong>.</p></div>
    <div class="kcard"><div class="hot">계획 규모</div><div class="kw">3,852세대</div>
      <p>최고 <strong>49층</strong>, 확정 전.</p></div>
  </div>

  <div class="colchart">
    <h3>목동 재건축 단지별 계획 가구수 (가구 · 아래 숫자는 단지)</h3>
    <span class="badge">13단지는 네 번째</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:86%">5,123</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:71.3%">4,248</div><div class="barv" style="--h:71.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:66.5%">3,961</div><div class="barv" style="--h:66.5%"></div></div>
      <div class="col"><div class="v gtx" style="--h:64.7%">3,852</div><div class="barv" style="--h:64.7%"></div></div>
      <div class="col dim"><div class="v" style="--h:47.2%">2,810</div><div class="barv" style="--h:47.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:40.9%">2,436</div><div class="barv" style="--h:40.9%"></div></div>
    </div>
    <div class="collbl"><span>14</span><span>10</span><span>9</span><span>13</span><span>12</span><span>4</span></div>
    <p class="cap">모두 재건축 후 계획 가구수라 한 축에 놓았습니다. 막대 길이는 최댓값 5,123가구를 기준으로 맞췄습니다. 심의 단계에서 바뀔 수 있는 계획 수치이며, 뉴시스(10월 20일)·머니투데이방송(10월 6~23일) 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 목동13단지 재건축, 삼성물산 95.7%로 확정"),
    ("02-vote", "참석 1,884명 중 1,803명이 삼성물산"),
    ("03-sched", "두 번 단독 응찰, 어제 확정까지"),
    ("04-cost", "3.3㎡당 980만원, 목동 다른 단지와 같은 선"),
    ("05-map", "목동 시공사, 정해진 곳과 남은 곳"),
    ("06-check", "목동13단지 재건축 체크 3가지"),
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

ARTICLE = '''<article data-tags="목동13단지재건축,목동13단지,목동재건축,목동신시가지,래미안모브13,삼성물산,양천구재건축,시공사선정,목동4단지,재건축">
  <h2>목동13단지 재건축, 삼성물산 95.7%로 확정</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 목동13단지 재건축, 삼성물산 95.7%로 확정"></span>

  <p>목동13단지 재건축 시공사가 삼성물산으로 확정됐습니다. 사업시행자 대신자산신탁은 어제(11월 7일) 동양미래대학교 대강당에서 제2차 토지등소유자 전체회의를 열고 삼성물산을 시공사로 선정했습니다. <span class="mark">도급액은 약 2조3,763억원, 3.3㎡당 공사비는 980만원(부가세 제외)입니다.</span></p>

  <h3>목동13단지 재건축 전체회의 투표 결과</h3>
  <div class="chart" data-img="카드뉴스 2번 · 참석 1,884명 중 1,803명이 삼성물산">
    <h3>목동13단지 제2차 전체회의 투표 (명)</h3>
    <div class="bar"><label>사업 동의</label>
      <div class="rail"><div class="fill gray" style="width:100%">2,127</div></div></div>
    <div class="bar"><label>참석</label>
      <div class="rail"><div class="fill gray" style="width:88.6%">1,884</div></div></div>
    <div class="bar"><label>삼성물산</label>
      <div class="rail"><div class="fill" style="width:84.8%">1,803</div></div></div>
    <p class="cap">모두 사람 수(명)라 한 축에 놓았습니다. 막대 길이는 사업에 동의한 토지등소유자 2,127명을 기준으로 맞췄습니다. 참석에는 부재자 투표가 포함됩니다. 머니투데이방송(11월 7일) 보도 기준입니다.</p>
  </div>
  <p>사업에 동의한 토지등소유자 2,127명 가운데 1,884명이 참석했고(부재자 투표 포함), 그중 1,803명이 삼성물산을 골랐습니다. 참석자 기준 95.7%입니다. <span class="mark">단독 후보에 대한 찬반이었지만, 동의자 전체로 봐도 열에 여덟 이상이 찬성한 셈입니다.</span></p>

  <h3>두 번 단독 응찰, 어제 확정까지</h3>
  <div class="chart" data-img="카드뉴스 3번 · 두 번 단독 응찰, 어제 확정까지">
    <h3>목동13단지 시공사 선정 흐름</h3>
    <h4>1차 입찰</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">유찰</span>
      <span class="desc">삼성물산 한 곳만 응찰해 경쟁이 성립하지 않았다.</span></div>
    <h4>재입찰 · 우선협상</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">9.29</span>
      <span class="desc">다시 단독 응찰. 삼성물산을 우선협상대상자로 정했다.</span></div>
    <h4>전체회의 확정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.7</span>
      <span class="desc">어제. 1,803명 찬성으로 시공사 확정.</span></div>
    <p class="cap">하우징타임즈·위클리한국주택경제·머니투데이방송(11월 7일) 보도 기준입니다.</p>
  </div>
  <p>목동13단지는 1차 입찰에서 삼성물산만 응찰해 유찰됐고, 재입찰에서도 단독 응찰해 9월 29일 우선협상대상자가 됐습니다. 어제 전체회의는 그 결과를 확정하는 자리였습니다. 삼성물산은 단지명으로 '래미안 모브13'을 제안한 것으로 보도됐습니다. <span class="mark">다만 이건 제안 이름이고, 최종 단지명은 이후 절차에서 정해집니다.</span> 이번 수주로 삼성물산의 올해 도시정비 누적 수주액은 12조8,449억원이 됐습니다.</p>

  <h3>목동13단지 재건축 공사비, 3.3㎡당 980만원</h3>
  <div class="chart" data-img="카드뉴스 4번 · 3.3㎡당 980만원, 목동 다른 단지와 같은 선">
    <h3>목동 재건축 3.3㎡당 예정공사비 (만원)</h3>
    <div class="bar"><label>4단지</label>
      <div class="rail"><div class="fill gray" style="width:100%">1,010</div></div></div>
    <div class="bar"><label>10단지</label>
      <div class="rail"><div class="fill gray" style="width:98%">990</div></div></div>
    <div class="bar"><label>13단지</label>
      <div class="rail"><div class="fill" style="width:97%">980</div></div></div>
    <div class="bar"><label>9단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>12단지</label>
      <div class="rail"><div class="fill gray" style="width:97%">980</div></div></div>
    <div class="bar"><label>8단지</label>
      <div class="rail"><div class="fill gray" style="width:95.5%">965</div></div></div>
    <p class="cap">모두 3.3㎡당 예정공사비(만원, 부가세 제외)라 한 축에 놓았습니다. 막대 길이는 최댓값 1,010만원을 기준으로 맞췄습니다. 13단지는 머니투데이방송(11월 7일), 나머지는 머니투데이방송(10월 6·8·23일)·머니투데이(10월 5일) 보도 기준입니다.</p>
  </div>
  <p>3.3㎡당 980만원은 목동 다른 단지(965만~1,010만원)와 거의 같은 선입니다. 지하 4층~지상 49층, 3,852세대 계획으로 목동에서 14단지(5,123가구)·10단지(4,248가구)·9단지(3,961가구) 다음 규모입니다. <span class="mark">세대수와 층수는 심의 단계마다 바뀔 수 있는 계획 수치라 확정 전입니다.</span></p>

  <h3>목동 시공사, 정해진 곳과 남은 곳</h3>
  <div class="chart" data-img="카드뉴스 5번 · 목동 시공사, 정해진 곳과 남은 곳">
    <h3>목동 재건축 시공사 현황</h3>
    <h4>확정</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3곳</span>
      <span class="desc">6단지 DL이앤씨, 10단지 현대건설, 13단지 삼성물산.</span></div>
    <h4>우선협상</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2곳</span>
      <span class="desc">8단지 대우건설, 12단지 GS건설. 최종 선정 절차 중.</span></div>
    <h4>다음 입찰 마감</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.16</span>
      <span class="desc">4단지. 7단지는 이달 입찰공고 예정.</span></div>
    <p class="cap">뉴스웨이(11월 5일)·서울경제TV(10월 28일)·머니투데이방송(11월 7일) 보도 기준입니다. 지금까지 정해진 5곳은 모두 단독 응찰이었습니다.</p>
  </div>
  <p>목동 14개 단지 가운데 시공사가 확정된 곳은 13단지까지 3곳입니다. 8단지(대우건설)와 12단지(GS건설)는 우선협상대상자로 최종 선정 절차를 밟고 있습니다. 다음은 11월 16일 입찰을 마감하는 4단지이고, 7단지는 이달 입찰공고가 예정돼 있습니다. 9단지는 2027년 1월 11일 입찰 마감입니다. <span class="mark">지금까지 5곳이 모두 단독 응찰이어서, 남은 단지에서 첫 경쟁입찰이 나올지가 관전 포인트입니다.</span></p>

  <h3>목동13단지 재건축 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 목동13단지 재건축 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="mk13-06-check.png" src="../images/cards/report/mk13-06-check.png" alt="체크포인트 카드 · 1. 3,852세대는 계획 수치, 2. 단지명은 제안 단계, 3. 조합원 지위는 따로 확인" loading="lazy" width="1080" height="1080">
    <figcaption>목동13단지 재건축 상담에 바로 쓰는 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>3,852세대·49층은 계획 수치</strong>. 심의와 사업시행계획인가 단계에서 바뀔 수 있습니다. 분담금도 아직 정해지지 않았습니다.</li>
    <li><strong>래미안 모브13은 제안 이름</strong>. 시공사가 제안한 단지명이며 최종 이름은 이후 절차에서 정해집니다.</li>
    <li><strong>조합원 지위는 따로 확인</strong>. 거래 제한은 사업 단계마다 다릅니다. 사고팔기 전에 사업시행자(대신자산신탁)·양천구청·정비사업 정보몽땅(cleanup.seoul.go.kr)에서 확인하십시오.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>목동13단지 재건축</strong> 시공사가 11월 7일 삼성물산으로 확정됐습니다. 참석자 1,884명 중 1,803명(95.7%)이 찬성했고, 도급액은 약 2조3,763억원(3.3㎡당 980만원), 최고 49층 3,852세대 계획입니다. <span class="mark">목동에서 확정 3곳, 우선협상 2곳이 모두 단독 응찰이었습니다. 11월 16일 4단지 입찰 마감이 다음 관전 포인트입니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 목동13단지 선정 결과는 머니투데이방송(2026-11-07)·하우징타임즈·위클리한국주택경제·데일리한국, 목동 시공사 현황은 뉴스웨이(2026-11-05)·서울경제TV(2026-10-28)·뉴시스(2026-10-20), 단지별 계획·공사비는 머니투데이방송(2026-10-06·08·23)·머니투데이(2026-10-05) 보도 기준입니다. 계획 세대수·층수는 확정 전이며 사업시행자 공고로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 머니투데이방송 삼성물산 목동13단지 수주(2026-11-07) · 하우징타임즈 목동13단지 래미안 깃발 · 위클리한국주택경제 목동13단지 전체회의 · 데일리한국 2.3조 목동13단지 · 뉴스웨이 목동 수주전(2026-11-05) · 서울경제TV 목동 5곳 단독응찰(2026-10-28) · 뉴시스 30조 목동 시공사 확정(2026-10-20)<br>
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
H = (5123, 4248, 3961, 3852, 2810, 2436)
for v, h in zip(H[1:], (71.3, 66.5, 64.7, 47.2, 40.9)):
    assert round(v / 5123 * 86, 1) == h, (v, h)
for v, w in zip((990, 980, 965), (98.0, 97.0, 95.5)):
    assert round(v / 1010 * 100, 1) == w, (v, w)
assert round(1884 / 2127 * 100, 1) == 88.6 and round(1803 / 2127 * 100, 1) == 84.8
assert round(1803 / 1884 * 100, 1) == 95.7 and 130000 - 128449 == 1551
KW = "목동13단지 재건축"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("목동13단지재건축")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
