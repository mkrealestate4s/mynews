# -*- coding: utf-8 -*-
"""리포트 #111 특집 (2026-10-31 오후) 수도권 신규택지 6곳 발표. #110을 복제해 교체한다.

메인 검색어: 신규택지 발표

수치와 검산
  사건일과 오늘의 간격: 국토부 제2차 주택공급 정례브리핑 10/29 → 2일. 토허 해제 효력 11/3 → D-3.
  6곳 7만6,700호 (더구루·금융소비자뉴스·서울경제 10/29):
    김포 아라 37,000 · 구리 건원 14,600 · 하남 미사 K컬처 12,000 · 하남 감일2 6,500
    · 고양 대곡지식융합 4,000 · 의정부 다락원 2,600  (합 76,700)
  기존 3곳 2만7,200호 (#89): 남양주도심 21,700 · 경기광주역세권2 4,500 · 서울 강서 염창 1,000
    → 수도권 신규 공공택지 합 103,900
  8월 예고 물량 7만3,000호(#89) → 실제 7만6,700호 (+3,700)
  착공까지 68개월(3기 신도시 평균) → 37개월 목표, 2030년 내 착공, 입주 이르면 2033년 (이투데이·이데일리 일문일답)
  모두 서울 경계 약 5㎞ 이내, 훼손된 그린벨트 중심. 서울 안 택지는 이번에 없음(용산 미군기지 반환부지는 협의 중)
  토지거래허가: 8·13 때 지정한 서울·인접 그린벨트 토지 토허구역 11/3 해제(송파 일부 유지, 뉴스핌·아주경제)
    · 아파트 토허제는 해제 아님 · 하남 감일·감북·미사동 11/3~2029/11/2 재지정(인천일보·데일리한국)
  6곳 가로 (37,000 → 100%): 14,600 → 39.5 · 12,000 → 32.4 · 6,500 → 17.6 · 4,000 → 10.8 · 2,600 → 7.0
  대시보드 세로 (37,000 → 86%): 33.9 · 27.9 · 15.1 · 9.3 · 6.0
  기간 가로 (68 → 100%): 37 → 54.4
  김포 아라 비중: 37,000/76,700 = 48.2% → 100채 중 48채

단정하지 않은 것
  · 지구별 위치·면적, 분양 시기·분양가는 미정 → 쓰지 않는다
  · 37개월 단축은 공공주택특별법 개정 전제(#89) → '목표'로 쓴다
  · 해제 지역이 다음 택지 검토에서 빠지는지는 정부 답 없음
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-10-31-godeok3-special.html"
DST = ROOT / "posts/2026-10-31-newland6.html"
SLUG, PRE = "2026-10-31-newland6", "nl1031"
NO, DATE = 111, "2026-10-31"
PREV_SLUG = "gdk1031-"
BANNED = ["고덕강일", "특별공급 월요일"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "신규택지 6곳 발표, 우리 동네 있을까"
DESC = ("국토부가 10월 29일 수도권 신규택지 6곳, 7만6,700가구를 발표했습니다. 김포 아라 3만7,000가구가 가장 크고 "
        "구리 건원, 하남 미사 K컬처, 하남 감일2, 고양 대곡, 의정부 다락원이 뒤를 잇습니다. 서울 안 택지는 없고, "
        "서울 그린벨트 토지거래허가구역은 11월 3일 풀립니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="김포·구리·하남·고양·의정부 6곳 7만6,700가구. 2030년 착공 목표, 입주는 이르면 2033년. 11월 3일 풀리는 토지거래허가구역까지 정리했습니다.">
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
  <div class="eyebrow">2026 · 10월 부동산 키워드 리포트 #{NO} · 특집</div>
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">신규택지 6곳 발표,<br>우리 동네 있을까</h1>
  <p class="sub"><strong>신규택지 발표</strong>가 나왔습니다. 국토교통부가 10월 29일 서울 경계에서 5㎞ 안쪽 수도권 6곳에 <strong>7만6,700가구</strong>를 짓겠다고 밝혔습니다. 가장 큰 곳은 <strong>김포 아라(3만7,000가구)</strong>입니다. 서울 안 택지는 이번에도 빠졌고, 서울 그린벨트 토지거래허가구역은 <strong>11월 3일</strong> 풀립니다. <span class="mark">착공 목표는 2030년, 입주는 이르면 2033년입니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 신규택지</div><div class="kw">7만6,700</div>
      <p>가구, 수도권 <strong>6곳</strong>.</p></div>
    <div class="kcard"><div class="hot">최대 지구</div><div class="kw">김포 아라</div>
      <p><strong>3만7,000가구</strong>, 전체의 48%.</p></div>
    <div class="kcard"><div class="hot">착공 목표</div><div class="kw">2030년</div>
      <p>입주는 이르면 <strong>2033년</strong>.</p></div>
    <div class="kcard"><div class="hot">토허 해제</div><div class="kw">11월 3일</div>
      <p>서울 그린벨트 토지. <strong>아파트는 그대로</strong>.</p></div>
  </div>

  <div class="colchart">
    <h3>신규택지 6곳 물량 (가구)</h3>
    <span class="badge">10월 29일 발표</span>
    <div class="cols">
      <div class="col"><div class="v gtx" style="--h:86%">3.7만</div><div class="barv" style="--h:86%"></div></div>
      <div class="col dim"><div class="v" style="--h:33.9%">1.46만</div><div class="barv" style="--h:33.9%"></div></div>
      <div class="col dim"><div class="v" style="--h:27.9%">1.2만</div><div class="barv" style="--h:27.9%"></div></div>
      <div class="col dim"><div class="v" style="--h:15.1%">6,500</div><div class="barv" style="--h:15.1%"></div></div>
      <div class="col dim"><div class="v" style="--h:9.3%">4,000</div><div class="barv" style="--h:9.3%"></div></div>
      <div class="col dim"><div class="v" style="--h:6%">2,600</div><div class="barv" style="--h:6%"></div></div>
    </div>
    <div class="collbl"><span>김포 아라</span><span>구리 건원</span><span>하남 미사</span><span>하남 감일2</span><span>고양 대곡</span><span>의정부 다락원</span></div>
    <p class="cap">막대 길이는 최댓값 3만7,000가구를 기준으로 맞췄습니다. 하남 미사는 'K컬처', 고양 대곡은 '지식융합' 지구입니다. 국토교통부 10월 29일 발표, 더구루·금융소비자뉴스 보도 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 신규택지 6곳 발표, 우리 동네 있을까"),
    ("02-six", "6곳 중 김포 아라가 절반 가까이, 3만7,000가구"),
    ("03-total", "앞서 3곳까지 더하면 10만3,900가구"),
    ("04-time", "착공까지 68개월을 37개월로"),
    ("05-toheo", "11월 3일 풀리는 것, 그대로인 것"),
    ("06-check", "신규택지 발표 뒤 체크 3가지"),
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

ARTICLE = '''<article data-tags="신규택지발표,신규택지,김포아라,구리건원,하남미사,하남감일2,고양대곡,의정부다락원,공공택지,토지거래허가구역해제">
  <h2>신규택지 6곳 발표, 우리 동네 있을까</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 신규택지 6곳 발표, 우리 동네 있을까"></span>

  <p>신규택지 발표가 드디어 나왔습니다. 국토교통부는 10월 29일 제2차 주택공급 정례브리핑에서 수도권 신규 공공택지 후보지 6곳, 7만6,700가구를 발표했습니다. 8·13 대책에서 "연내 7만3,000가구"로 예고했던 물량입니다. 6곳 모두 서울 경계에서 약 5㎞ 안쪽이고, 이미 훼손돼 보전 가치가 낮은 개발제한구역(그린벨트)이 중심입니다. <span class="mark">다만 서울 안 택지는 이번에도 없습니다.</span></p>

  <h3>신규택지 발표 6곳, 김포 아라가 절반 가까이</h3>
  <div class="chart" data-img="카드뉴스 2번 · 6곳 중 김포 아라가 절반 가까이, 3만7,000가구">
    <h3>지구별 공급 물량 (가구)</h3>
    <div class="bar"><label>김포 아라</label>
      <div class="rail"><div class="fill" style="width:100%">37,000</div></div></div>
    <div class="bar"><label>구리 건원</label>
      <div class="rail"><div class="fill gray" style="width:39.5%">14,600</div></div></div>
    <div class="bar"><label>하남 미사 K컬처</label>
      <div class="rail"><div class="fill gray" style="width:32.4%">12,000</div></div></div>
    <div class="bar"><label>하남 감일2</label>
      <div class="rail"><div class="fill gray" style="width:17.6%"></div><span class="railval">6,500</span></div></div>
    <div class="bar"><label>고양 대곡지식융합</label>
      <div class="rail"><div class="fill gray" style="width:10.8%"></div><span class="railval">4,000</span></div></div>
    <div class="bar"><label>의정부 다락원</label>
      <div class="rail"><div class="fill gray" style="width:7%"></div><span class="railval">2,600</span></div></div>
    <p class="cap">합계 7만6,700가구. 막대 길이는 최댓값 3만7,000을 기준으로 맞췄습니다. 국토교통부 10월 29일 발표, 더구루·금융소비자뉴스·서울경제 보도 기준입니다.</p>
  </div>
  <p>가장 큰 곳은 김포 아라로 3만7,000가구, 이번 물량의 48%입니다. 구리 건원 1만4,600가구, 하남 미사 K컬처 1만2,000가구가 뒤를 잇습니다. 하남은 감일2(6,500가구)까지 두 곳이라 합치면 1만8,500가구입니다. 고양 대곡지식융합 4,000가구, 의정부 다락원 2,600가구는 규모가 작습니다. <span class="mark">서울 동쪽(구리·하남)과 서쪽(김포·고양), 북쪽(의정부)에 고르게 흩어진 구성입니다.</span></p>

  <h3>앞서 3곳까지 더하면 10만3,900가구</h3>
  <div class="chart" data-img="카드뉴스 3번 · 앞서 3곳까지 더하면 10만3,900가구">
    <h3>8·13 대책 수도권 신규 공공택지 (가구)</h3>
    <h4>8월 먼저 지정한 3곳</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">2만7,200</span>
      <span class="desc">남양주도심 2만1,700 · 경기광주역세권2 4,500 · 서울 강서 염창 1,000.</span></div>
    <h4>10월 29일 발표 6곳</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">7만6,700</span>
      <span class="desc">8월 예고(7만3,000)보다 3,700가구 많다.</span></div>
    <h4>합계</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10만3,900</span>
      <span class="desc">목표였던 '10만호+α'를 채웠다.</span></div>
    <p class="cap">8월 지정 3곳은 8·13 대책 보도(본지 #89 정리), 6곳은 10월 29일 발표 기준입니다.</p>
  </div>
  <p>8·13 대책의 신규택지 목표는 10만호+α였습니다. 8월에 남양주도심·경기광주역세권2·서울 강서 염창 3곳 2만7,200가구를 먼저 지정했고, 이번 6곳을 더하면 10만3,900가구입니다. 발표는 "9월 말~10월 초"에서 "연내"로 한 번 밀렸다가 10월 말에 나왔습니다. <span class="mark">서울 안 물량은 여전히 강서 염창 1,000가구뿐이고, 용산 미군기지 반환부지는 서울시와 협의를 이어가고 있습니다.</span></p>

  <h3>신규택지 착공, 68개월을 37개월로</h3>
  <div class="chart" data-img="카드뉴스 4번 · 착공까지 68개월을 37개월로">
    <h3>발표에서 착공까지 걸리는 기간 (개월)</h3>
    <div class="bar"><label>3기 신도시 평균</label>
      <div class="rail"><div class="fill gray" style="width:100%">68개월</div></div></div>
    <div class="bar"><label>이번 목표</label>
      <div class="rail"><div class="fill" style="width:54.4%">37개월</div></div></div>
    <p class="cap">막대 길이는 68개월을 기준으로 맞췄습니다. 37개월은 정부 목표이며 공공주택특별법 개정이 전제입니다. 이투데이·이데일리 일문일답(10월 29일) 기준입니다.</p>
  </div>
  <p>정부는 발표에서 착공까지 3기 신도시 평균 68개월 걸리던 기간을 37개월로 줄여 2030년 안에 착공하겠다고 했습니다. 입주는 이르면 2033년입니다. <span class="mark">지금 청약통장을 준비하는 사람에게는 7년 뒤 이야기입니다.</span> 지구 경계와 면적, 분양 시기·분양가는 아직 정해지지 않았습니다.</p>

  <h3>토지거래허가구역, 11월 3일 풀리는 것과 그대로인 것</h3>
  <div class="chart" data-img="카드뉴스 5번 · 11월 3일 풀리는 것, 그대로인 것">
    <h3>토지거래허가구역 조정 (보도 기준)</h3>
    <h4>풀린다</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11.3</span>
      <span class="desc">8·13 때 묶은 서울·인접 그린벨트 토지. 신규택지와 그 주변은 빼고.</span></div>
    <h4>그대로</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">아파트</span>
      <span class="desc">서울 아파트 토지거래허가는 해제가 아니다.</span></div>
    <h4>다시 묶인다</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">3년</span>
      <span class="desc">하남 감일·감북·미사동, 2029년 11월 2일까지. 송파 일부도 유지.</span></div>
    <p class="cap">뉴스핌·아주경제(10월 29일), 인천일보·데일리한국(하남 재지정) 보도 기준입니다. 필지별 해당 여부는 토지이음(eum.go.kr)에서 확인하십시오.</p>
  </div>
  <p>정부는 8·13 대책 때 서울과 서울 인접 그린벨트에 걸어 둔 토지거래허가구역을 11월 3일 해제합니다. 신규택지 사업지구와 주변 영향권은 빼고, 서울에서는 하남 감일2 지구와 맞닿은 송파구 일부 그린벨트가 남습니다. 하남시는 감일·감북·미사동 일대를 11월 3일부터 3년간 다시 묶었습니다. <span class="mark">헷갈리기 쉬운 점은 서울 아파트 토지거래허가와 별개라는 것입니다. 아파트 쪽은 그대로입니다.</span></p>

  <h3>신규택지 발표 뒤 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 신규택지 발표 뒤 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="nl1031-06-check.png" src="../images/cards/report/nl1031-06-check.png" alt="체크포인트 카드 · 1. 후보지 땅은 여전히 허가 대상, 2. 입주는 이르면 2033년, 3. 아파트 토허제와 헷갈리지 않기" loading="lazy" width="1080" height="1080">
    <figcaption>신규택지 발표 뒤에 볼 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>후보지 땅은 여전히 허가 대상</strong>. 그린벨트 토허구역이 풀려도 신규택지 지구와 주변은 빠집니다. 하남 감일·감북·미사동은 3년 재지정입니다. 토지 거래 전에 토지이음에서 필지별로 확인하십시오.</li>
    <li><strong>입주는 이르면 2033년</strong>. 2030년 착공은 목표입니다. 법 개정이 늦어지면 일정도 밀립니다. 당장의 내 집 마련 계획은 지금 나오는 공고로 세우십시오.</li>
    <li><strong>아파트 토허제와 헷갈리지 않기</strong>. 11월 3일 해제는 그린벨트 토지 이야기입니다. 서울 아파트 거래의 실거주 의무는 그대로입니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>신규택지 발표</strong> 결과 수도권 6곳 7만6,700가구가 새로 나왔습니다. 김포 아라 3만7,000, 구리 건원 1만4,600, 하남 미사 K컬처 1만2,000, 하남 감일2 6,500, 고양 대곡지식융합 4,000, 의정부 다락원 2,600가구입니다. 앞서 지정한 3곳까지 더하면 10만3,900가구입니다. <span class="mark">착공 목표 2030년, 입주 이르면 2033년이고, 서울 그린벨트 토지거래허가구역은 11월 3일 풀립니다.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 지구별 물량은 국토교통부 10월 29일 발표(더구루·금융소비자뉴스·서울경제 보도), 일정은 이투데이·이데일리 일문일답, 토지거래허가구역 조정은 뉴스핌·아주경제·인천일보·데일리한국(2026-10-29) 보도 기준입니다. 지구 경계·면적과 분양 일정은 아직 정해지지 않았습니다.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 국토교통부 제2차 주택공급 정례브리핑(2026-10-29) · 더구루 서울 5km 이내 신규택지 7.67만호(2026-10-29) · 서울경제 서울 5㎞내 7.7만가구(2026-10-29) · 이투데이·이데일리 신규택지 일문일답(2026-10-29) · 뉴스핌·아주경제 그린벨트 토지거래허가구역 해제(2026-10-29) · 인천일보 하남 토지거래허가구역 재지정<br>
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
V = (37000, 14600, 12000, 6500, 4000, 2600)
assert sum(V) == 76700 and 21700 + 4500 + 1000 == 27200 and 76700 + 27200 == 103900
assert 76700 - 73000 == 3700 and 12000 + 6500 == 18500 and round(37000 / 76700 * 100) == 48
for v, w in zip(V[1:], (39.5, 32.4, 17.6, 10.8, 7.0)):
    assert round(v / 37000 * 100, 1) == w, (v, w)
for v, h in zip(V[1:], (33.9, 27.9, 15.1, 9.3, 6.0)):
    assert round(v / 37000 * 86, 1) == h, (v, h)
assert round(37 / 68 * 100, 1) == 54.4
KW = "신규택지 발표"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith("신규택지")
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("신규택지발표")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
