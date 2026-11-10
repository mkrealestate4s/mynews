# -*- coding: utf-8 -*-
"""리포트 #122 (2026-11-11) 은마아파트 재초환 예정액 4억6,334만원. #121을 복제해 교체한다.

메인 검색어: 은마아파트 재초환

수치와 검산
  사건일과 오늘의 간격: 강남구 예정액 통지 11/2~6 주(보도 11/6, 5일 전, 리드) · 서초구 재초환 폐지 건의 11/4(7일 전).
  은마 (머니투데이·뉴스1 11/6): 조합원 1인당 평균 예정액 4억6,334만원 · 단지 전체 약 2조원대(보도) · 확정액 아님
    현재 4,424세대 · 사업시행계획 인가 7/2 · 2028년 착공 목표(보도)
  비교 1인당 (머니투데이 9/10): 한강맨션 약 6억8,000만원(조합원 694명) · 반포3주구 약 3억2,000만원 · 서울 평균 1억2,174만원
  가로 (6.8→100): 4.6334 68.1 · 3.2 47.1 · 1.2174 17.9
  부과율 (재건축이익환수법, 2024-03-27 개정 시행): 1인당 초과이익 8,000만원까지 면제
    8,000만~1억3,000만 10% · ~1억8,000만 20% · ~2억3,000만 30% · ~2억8,000만 40% · 2억8,000만 초과 50%
    대시보드 컬럼(50→86): 17.2 34.4 51.6 68.8 86
  1세대 1주택 장기보유 감면: 6년 10% · 10년 50% · 20년 이상 70% · 60세 이상 납부 유예(주택 처분 때까지)

단정하지 않은 것
  · 4억6,334만원은 예정액. 준공 뒤 실제 집값·공사비로 다시 계산한다 · 개인별 감면 해당 여부는 조합·강남구청 확인
  · 서초구 폐지 건의는 건의일 뿐 법 개정 아님 · 분담금 4.3억(84㎡→84㎡)은 5월 보도 추정, 재초환과 별개
  · 단지 총액은 기사마다 표기가 달라 '약 2조원대'로만 쓴다
"""
import pathlib
import re

ROOT = pathlib.Path("/home/user/mynews")
SRC = ROOT / "posts/2026-11-10-forena-jijeyeok.html"
DST = ROOT / "posts/2026-11-11-eunma-jaechohwan.html"
SLUG, PRE = "2026-11-11-eunma-jaechohwan", "emj"
NO, DATE = 122, "2026-11-11"
PREV_SLUG = "fjj-"
BANNED = ["포레나", "지제", "평택", "· 특집"]
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
OG = f"https://mkrealestate4s.github.io/mynews/images/cards/report/{PRE}-01-cover.png"

TITLE = "은마아파트 재초환 4.6억, 확정 아닙니다"
DESC = ("은마아파트 재초환(재건축 초과이익 환수) 예정액이 조합원 1인당 평균 4억6,334만원으로 통지됐습니다. "
        "확정액이 아니라 준공 뒤 다시 계산하는 예정액입니다. 부과율 구간, 다른 단지와 비교, 장기보유 감면을 정리했습니다.")

HEAD = f'''<title>{TITLE} | 부동산 키워드 리포트</title>
<meta name="description" content="{DESC}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="강남구가 은마 조합에 1인당 평균 4억6,334만원 예정액 통지. 한강맨션 6.8억 추정, 서울 평균 1.2억. 오래 산 1주택자는 최대 70% 감면.">
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
  <h1 class="serif gtx" style="font-size:clamp(1.9rem,6.8vw,3.8rem);line-height:1.22">은마아파트 재초환 4.6억<br>확정 아닙니다</h1>
  <p class="sub"><strong>은마아파트 재초환</strong> 예정액이 나왔습니다. 강남구청이 이번 달 첫째 주 은마 재건축조합에 <strong>조합원 1인당 평균 4억6,334만원</strong>의 재건축부담금 예정액을 통지했다고 보도됐습니다. <span class="mark">다만 이 금액은 지금 내는 돈이 아니고, 준공 뒤 실제 집값과 공사비로 다시 계산합니다.</span></p>
</header>'''

DASH = '''<section id="dashboard">
  <h2>오늘의 상위 키워드 대시보드</h2>
  <div class="grid">
    <div class="kcard"><div class="hot">HOT · 은마 재초환</div><div class="kw">4억6,334만</div>
      <p>조합원 1인당 <strong>평균 예정액</strong>.</p></div>
    <div class="kcard"><div class="hot">성격</div><div class="kw">예정액</div>
      <p><strong>준공 뒤</strong> 다시 계산해 확정.</p></div>
    <div class="kcard"><div class="hot">면제 기준</div><div class="kw">8,000만원</div>
      <p>1인당 초과이익 <strong>8,000만원까지</strong> 0원.</p></div>
    <div class="kcard"><div class="hot">장기보유 감면</div><div class="kw">최대 70%</div>
      <p>1주택 <strong>20년 이상</strong> 보유 시.</p></div>
  </div>

  <div class="colchart">
    <h3>재초환 부과율, 초과이익 구간별 (%)</h3>
    <span class="badge">2억8,000만원 넘으면 50%</span>
    <div class="cols">
      <div class="col dim"><div class="v" style="--h:17.2%">10</div><div class="barv" style="--h:17.2%"></div></div>
      <div class="col dim"><div class="v" style="--h:34.4%">20</div><div class="barv" style="--h:34.4%"></div></div>
      <div class="col dim"><div class="v" style="--h:51.6%">30</div><div class="barv" style="--h:51.6%"></div></div>
      <div class="col dim"><div class="v" style="--h:68.8%">40</div><div class="barv" style="--h:68.8%"></div></div>
      <div class="col"><div class="v gtx" style="--h:86%">50</div><div class="barv" style="--h:86%"></div></div>
    </div>
    <div class="collbl"><span>~1.3억</span><span>~1.8억</span><span>~2.3억</span><span>~2.8억</span><span>2.8억~</span></div>
    <p class="cap">조합원 1인당 평균 초과이익 구간별로 그 구간에 걸친 금액에 매기는 비율입니다. 8,000만원까지는 면제이고 첫 구간은 8,000만원 초과부터입니다. 막대 길이는 최댓값 50%를 기준으로 맞췄습니다. 2024년 3월 시행된 개정 재건축이익환수법 기준입니다.</p>
  </div>
</section>'''

CARDNAMES = [
    ("01-cover", "표지: 은마아파트 재초환 4.6억, 확정 아닙니다"),
    ("02-compare", "1인당 재초환, 은마는 서울 평균의 약 4배"),
    ("03-stage", "지금은 예정액, 확정은 준공 뒤"),
    ("04-rate", "넘는 만큼 최대 50%"),
    ("05-relief", "오래 산 1주택자는 최대 70% 감면"),
    ("06-check", "은마아파트 재초환 체크 3가지"),
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

ARTICLE = '''<article data-tags="은마아파트재초환,은마아파트,은마재건축,재초환,재건축초과이익환수,재건축부담금,대치동재건축,강남재건축,재초환감면,재건축분담금">
  <h2>은마아파트 재초환 4.6억, 확정 아닙니다</h2>
  <div class="copybar">
    <button class="cbtn" id="copyBody">📋 블로그용 본문 복사</button>
    <button class="cbtn" id="copyLink">🔗 링크 복사</button>
  </div>
  <span class="imgslot" hidden data-img="카드뉴스 1번 · 표지: 은마아파트 재초환 4.6억, 확정 아닙니다"></span>

  <p>은마아파트 재초환 예정액이 조합원 1인당 평균 4억6,334만원으로 통지됐습니다. 머니투데이·뉴스1(11월 6일)에 따르면 강남구청이 이번 달 첫째 주 은마아파트 재건축조합에 재건축부담금 예정액을 알렸습니다. 대치동 은마는 현재 4,424세대이고 7월 2일 사업시행계획 인가를 받았습니다. <span class="mark">숫자만 보면 놀랍지만, 이 금액은 고지서가 아니라 사업 중간에 미리 계산해 보는 예정액입니다.</span></p>

  <h3>은마아파트 재초환, 다른 단지와 비교하면</h3>
  <div class="chart" data-img="카드뉴스 2번 · 1인당 재초환, 은마는 서울 평균의 약 4배">
    <h3>조합원 1인당 재초환 부담금 (억원)</h3>
    <div class="bar"><label>한강맨션</label>
      <div class="rail"><div class="fill gray" style="width:100%">6.8</div></div></div>
    <div class="bar"><label>은마</label>
      <div class="rail"><div class="fill" style="width:68.1%">4.63</div></div></div>
    <div class="bar"><label>반포3주구</label>
      <div class="rail"><div class="fill gray" style="width:47.1%">3.2</div></div></div>
    <div class="bar"><label>서울 평균</label>
      <div class="rail"><div class="fill gray" style="width:17.9%"></div><span class="railval" style="left:calc(17.9% + 12px)">1.22</span></div></div>
    <p class="cap">모두 조합원 1인당 금액(억원)이라 한 축에 놓았습니다. 막대 길이는 최댓값 6.8억원을 기준으로 맞췄습니다. 은마는 강남구 예정액 통지(머니투데이·뉴스1 11월 6일), 한강맨션·반포3주구·서울 평균은 머니투데이(9월 10일) 보도 추정치로 산정 시점이 서로 다릅니다.</p>
  </div>
  <p>9월 보도 기준으로 서울 재건축 단지의 조합원 1인당 예상 부담금 평균은 1억2,174만원이었습니다. 은마의 예정액 4억6,334만원은 그 평균의 약 3.8배입니다. 용산 한강맨션은 조합원 694명에 1인당 약 6억8,000만원, 반포3주구는 약 3억2,000만원으로 추산됐습니다. <span class="mark">조합원 수가 많을수록 1인당 금액은 줄어드는 구조라, 총액만 보고 단지끼리 비교하면 틀립니다.</span></p>

  <h3>은마아파트 재초환은 예정액, 확정은 준공 뒤</h3>
  <div class="chart" data-img="카드뉴스 3번 · 지금은 예정액, 확정은 준공 뒤">
    <h3>은마 재초환이 정해지는 순서</h3>
    <h4>사업시행계획 인가</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">7월</span>
      <span class="desc">7월 2일 강남구 인가. 이 단계 뒤에 예정액을 계산한다.</span></div>
    <h4>예정액 통지</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">11월</span>
      <span class="desc">1인당 평균 4억6,334만원. 지금 내는 돈이 아니다.</span></div>
    <h4>확정 부과</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">준공 후</span>
      <span class="desc">실제 집값·공사비·사업 기간으로 다시 계산한다.</span></div>
    <p class="cap">머니투데이·뉴스1(11월 6일) 보도와 재건축이익환수법 절차 기준입니다. 조합은 2028년 착공을 목표로 한다고 보도됐습니다.</p>
  </div>
  <p>재초환은 재건축 시작 시점(조합설립인가)부터 준공 때까지 오른 집값에서 정상적인 집값 상승분과 공사비 같은 개발비용을 뺀 초과이익에 매깁니다. 지금 통지된 금액은 현재 시세와 추정 공사비로 계산한 예정액이고, 실제 고지는 준공 뒤에 다시 계산한 금액으로 나옵니다. <span class="mark">공사비가 오르거나 준공 때 집값이 덜 오르면 금액은 줄고, 반대면 늘어납니다.</span></p>

  <h3>재초환 부과율, 넘는 만큼 최대 50%</h3>
  <div class="chart" data-img="카드뉴스 4번 · 넘는 만큼 최대 50%">
    <h3>1인당 초과이익 구간별 부과율 (%)</h3>
    <div class="bar"><label>~8,000만</label>
      <div class="rail"><div class="fill gray" style="width:0%"></div><span class="railval" style="left:12px">면제</span></div></div>
    <div class="bar"><label>~1.3억</label>
      <div class="rail"><div class="fill gray" style="width:20%">10</div></div></div>
    <div class="bar"><label>~1.8억</label>
      <div class="rail"><div class="fill gray" style="width:40%">20</div></div></div>
    <div class="bar"><label>~2.3억</label>
      <div class="rail"><div class="fill gray" style="width:60%">30</div></div></div>
    <div class="bar"><label>~2.8억</label>
      <div class="rail"><div class="fill gray" style="width:80%">40</div></div></div>
    <div class="bar"><label>2.8억 초과</label>
      <div class="rail"><div class="fill" style="width:100%">50</div></div></div>
    <p class="cap">구간에 걸친 금액에만 그 비율을 매기는 누진 방식입니다. 막대 길이는 최댓값 50%를 기준으로 맞췄습니다. 2024년 3월 27일 시행된 개정 재건축이익환수법 기준입니다.</p>
  </div>
  <p>2024년 법 개정으로 면제 기준이 3,000만원에서 8,000만원으로 올랐고 구간 폭도 5,000만원으로 넓어졌습니다. 1인당 초과이익이 2억8,000만원을 넘으면 넘는 부분에는 절반(50%)이 매겨집니다. 은마처럼 예정액이 4억원대라면 초과이익 대부분이 맨 윗 구간에 걸려 있다는 뜻입니다.</p>

  <h3>오래 산 1주택자는 최대 70% 감면</h3>
  <div class="chart" data-img="카드뉴스 5번 · 오래 산 1주택자는 최대 70% 감면">
    <h3>1세대 1주택 장기보유 감면</h3>
    <h4>6년 이상 보유</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">10%</span>
      <span class="desc">감면이 시작되는 보유 기간.</span></div>
    <h4>10년 이상 보유</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">50%</span>
      <span class="desc">보유 기간이 길수록 감면 폭이 커진다.</span></div>
    <h4>20년 이상 보유</h4>
    <div class="statrow"><span class="big" style="white-space:nowrap">70%</span>
      <span class="desc">최대 감면. 60세 이상은 집을 팔 때까지 납부를 미룰 수 있다.</span></div>
    <p class="cap">2024년 3월 시행된 개정 재건축이익환수법 기준입니다. 보유 기간 계산 방법과 내 해당 여부는 조합과 강남구청에 확인하십시오.</p>
  </div>
  <p>평균 예정액이 4억원대라도 조합원마다 내는 돈은 다릅니다. 1세대 1주택자가 오래 보유했으면 6년 10%부터 20년 이상 70%까지 감면받고, 60세 이상이면 주택을 팔 때까지 납부를 미룰 수 있습니다. <span class="mark">1979년 준공된 은마에는 오래 산 1주택자가 많아, 평균 숫자보다 실제 고지액이 크게 낮은 조합원도 나올 수 있습니다.</span> 서초구는 11월 4일 국토교통부에 재초환 폐지 건의문을 냈지만 건의 단계이고 법이 바뀐 것은 아닙니다.</p>

  <h3>은마아파트 재초환 체크 3가지</h3>
  <figure class="cardimg" data-img="카드뉴스 6번 · 은마아파트 재초환 체크 3가지 (체크리스트)">
    <img class="card-art" data-file="emj-06-check.png" src="../images/cards/report/emj-06-check.png" alt="체크포인트 카드 · 1. 확정 아닌 예정액, 2. 분담금과 별개, 3. 내 감면은 조합·구청 확인" loading="lazy" width="1080" height="1080">
    <figcaption>은마아파트 재초환 기사 보고 확인할 3가지. 저장해 두고 확인하세요.</figcaption>
  </figure>
  <ol class="check">
    <li><strong>확정 아닌 예정액</strong>. 4억6,334만원은 평균 예정액입니다. 준공 뒤 실제 집값과 공사비로 다시 계산해 고지합니다.</li>
    <li><strong>분담금과 별개</strong>. 재초환은 새 집을 받으면서 내는 조합원 분담금과 다른 돈입니다. 둘을 따로 계산해야 합니다.</li>
    <li><strong>내 감면은 조합·구청 확인</strong>. 1주택 장기보유 감면(최대 70%)과 60세 이상 납부 유예 해당 여부는 개인마다 다릅니다.</li>
  </ol>

  <h3>정리</h3>
  <p><strong>은마아파트 재초환</strong> 예정액은 조합원 1인당 평균 4억6,334만원으로, 서울 평균 추정치(1억2,174만원)의 약 3.8배입니다. 다만 사업시행계획 인가 뒤 미리 계산한 예정액이고, 확정 금액은 준공 뒤 다시 정해집니다. <span class="mark">조합원이라면 평균 숫자보다 내 보유 기간과 1주택 여부로 받을 감면부터 확인하십시오.</span></p>

  <div class="note">※ 본 페이지는 정보 제공 목적이며, 투자 권유가 아닙니다. 은마 예정액은 머니투데이·뉴스1(2026-11-06), 단지별 비교는 머니투데이(2026-09-10) 보도, 부과율·감면은 재건축이익환수법(2024-03-27 시행) 기준입니다. 개인별 금액은 조합과 강남구청으로 확인하십시오.</div>
</article>'''

FOOTER = f'''<footer>
  참고 자료: 머니투데이 은마아파트 조합원 1인당 재초환 4.6억(2026-11-06) · 뉴스1 은마 재건축부담금 예정액 통지(2026-11-06) · 머니투데이 "6.8억 내라고?" 재건축 덮친 재초환(2026-09-10) · SBS Biz 서초구 재초환 부과 시동(2026-11) · 재건축초과이익 환수에 관한 법률(2024-03-27 시행)<br>
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
for v, h in zip((10, 20, 30, 40), (17.2, 34.4, 51.6, 68.8)):
    assert round(v / 50 * 86, 1) == h, (v, h)
for v, w in zip((4.6334, 3.2, 1.2174), (68.1, 47.1, 17.9)):
    assert round(v / 6.8 * 100, 1) == w, (v, w)
assert round(46334 / 12174, 1) == 3.8
KW = "은마아파트 재초환"
art0 = out[out.index("<article "):out.index("</article>")]
assert TITLE.startswith(KW)
assert sum(1 for h in re.findall(r"<h3>(.*?)</h3>", art0) if KW in h) >= 2
assert KW in re.sub(r"<[^>]+>", "", art0.split("<p>", 1)[1].split("</p>", 1)[0])[:40]
assert art0.split('data-tags="', 1)[1].startswith("은마아파트재초환")
art = art0
slots = (art.count('class="chart"') + art.count('class="colchart"')
         + art.count("<figure") + art.count('class="imgslot"'))
assert slots == 6, slots
nums = sorted(int(m) for m in re.findall(r'data-img="카드뉴스 (\d+)번', art))
assert nums == [1, 2, 3, 4, 5, 6], nums
DST.write_text(out, encoding="utf-8")
print(f"{DST.name} · img {out.count('<img')} · data-img {out.count('data-img=')} · 줄표 0")
