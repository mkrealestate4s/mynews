# -*- coding: utf-8 -*-
"""2026-11-05 #116 서울 아파트 매물 8만건. 수치는 gen_example_116.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "sl1105"
DATEK = "2026-11-05"

COLCSS = """
.flow{display:flex;flex-direction:column;align-items:stretch}
.fbox{background:var(--panel);border:1px solid var(--line);border-radius:18px;
  padding:22px 32px;display:flex;align-items:center;gap:24px}
.fbox .n{font-weight:900;font-size:36px;flex:none}
.fbox .t{font-size:31px;font-weight:700}
.fbox .s{font-size:24px;color:var(--mute);font-weight:400;word-break:keep-all}
.note{font-size:23px;color:var(--mute);word-break:keep-all}
.duo{display:flex;gap:22px;margin-top:26px}
.duo .box{flex:1;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:30px 32px}
.duo .dl{font-size:26px;color:var(--mute);margin-bottom:10px}
.duo .dv{font-weight:900;font-size:56px;line-height:1.1;white-space:nowrap}
.duo .ds{font-size:23px;color:var(--mute);margin-top:14px;line-height:1.5;word-break:keep-all}
.bignum{font-weight:900;font-size:140px;line-height:1.02;white-space:nowrap}
.bigcap{font-size:30px;color:var(--body);margin-top:16px;word-break:keep-all}
.hb{margin-bottom:11px}
.hb .hl{font-size:25px;font-weight:700;margin-bottom:4px;color:var(--body)}
.hb .ht{background:var(--rail);border:1px solid var(--line);border-radius:8px;
  height:46px;position:relative;overflow:hidden}
.hb .hf{position:absolute;left:0;top:0;bottom:0;width:var(--w);background:var(--fillgray)}
.hb .hf.hi{background:var(--grad)}
.hb .hv{position:absolute;top:50%;transform:translateY(-50%);left:calc(var(--w) + 16px);
  font-size:27px;font-weight:900;white-space:nowrap}
.hb .hv.ins{left:20px;color:var(--onfill)}
.tl{display:flex;flex-direction:column;gap:0;margin-top:22px}
.tl .r{display:flex;align-items:flex-start;gap:22px;padding:18px 0;
  border-bottom:1px solid var(--line)}
.tl .r:last-child{border-bottom:0}
.tl .r .y{font-size:29px;font-weight:900;color:var(--accent);flex:none;width:200px}
.tl .r .d{font-size:30px;font-weight:700}
.tl .r .s{font-size:24px;color:var(--mute);font-weight:400;margin-top:4px;word-break:keep-all}
.qbox{background:var(--panel);border:1px solid var(--line);border-radius:18px;
  padding:30px 34px;margin-top:24px}
.qbox .q{font-size:34px;font-weight:700;color:var(--mute);margin-bottom:12px}
.hb .hf:not(.hi) + .hv.ins{color:var(--ink)}
.qbox .a{font-size:44px;font-weight:900;line-height:1.35;word-break:keep-all}
"""


def top(pnum):
    return ('<div class="top"><div class="eyebrow">{{EYEBROW}}</div>'
            f'<div class="pnum">{pnum} / {TOTAL}</div></div>')


def foot():
    return ('<div class="footwrap"><div class="trace"></div><div class="foot">'
            '<span>{{BRAND}}</span>'
            f'<span>데이터 기준일 {DATEK}</span></div></div>')


def hb(label, value, pct, hi=False, inside=False):
    return (f'<div class="hb"><div class="hl">{label}</div>'
            f'<div class="ht"><div class="hf{" hi" if hi else ""}" style="--w:{pct}%"></div>'
            f'<div class="hv{" ins" if inside else ""}{" gtx" if hi and not inside else ""}"'
            f' style="--w:{pct}%">{value}</div></div></div>')


def tlrows(rows, pad=15):
    return "".join(
        f'<div class="r" style="padding:{pad}px 0"><span class="y">{y}</span>'
        f'<div><div class="d">{d}</div><div class="s">{s}</div></div></div>' for y, d, s in rows)


def checks(items, fs=25):
    return "".join(
        f'<div class="fbox" style="align-items:flex-start;padding:24px 32px">'
        f'<span class="n gtx" style="font-size:34px;line-height:1.4">{i:02d}</span>'
        f'<div><div class="t" style="margin-bottom:6px">{t}</div>'
        f'<div style="font-size:{fs}px;color:var(--mute);word-break:keep-all">{d}</div></div></div>'
        for i, (t, d) in enumerate(items, start=1))






cards = {}

cards["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:33px;color:var(--mute);font-weight:500">아실 집계 · 11월 4일 기준</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">서울 아파트 매물<br>8만건 넘었다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    석 달 새 <span class="gtx">2만21건</span> 늘어 8만430건<br>
    8월 3일 세제 개편안 발표 뒤 33.1%</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">추이 · 강남3구 · 증가율 · 거래 · 체크</div>
</div>""" + foot()

cards["02-trend"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">석 달 새 2만건 늘었다</h1>
  <div style="font-size:27px;color:var(--mute)">서울 아파트 매물 · 건 · 아실</div>
  <div class="tl">""" + tlrows([
    ("8월 3일", "6만409건", "세제 개편안 발표 날"),
    ("9월 말", "7만2,099건", "두 달 남짓 +1만1,690건"),
    ("11월 4일", "8만430건", "한 달여 +8,331건 · 올해 최다"),
], pad=18) + """</div>
  <div class="note" style="margin-top:14px">※ 중개 플랫폼 등록 매물 수 · 실제 거래 건수와 다르다</div>
</div>""" + foot()

cards["03-gangnam"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">강남3구, 서초가 가장 많이</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">8월 3일 → 11월 4일 늘어난 매물 · 건</div>
""" + hb("서초구 · 7,630 → 1만502", "+2,872", 100, hi=True, inside=True) \
    + hb("강남구 · 9,453 → 1만2,126", "+2,673", 93.1, inside=True) \
    + hb("송파구 · 5,099 → 7,174", "+2,075", 72.2, inside=True) + """
  <div class="note" style="margin-top:14px">※ 세 구 합계 +7,620건 · 서울 증가분의 38%</div>
</div>""" + foot()

cards["04-rate"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">늘어난 비율로 보면 1등은</div>
  <div class="bignum gtx" style="margin-top:10px">성북 61.1%</div>
  <div class="bigcap">25개 구 중 매물 증가율 최고 · 8월 3일 대비</div>
  <div class="duo">
    <div class="box"><div class="dl">강남3구</div><div class="dv">34.4%</div><div class="ds">2만2,182 → 2만9,802건</div></div>
    <div class="box"><div class="dl">나머지 22개 구</div><div class="dv">32.4%</div><div class="ds">강남만의 일이 아니다</div></div>
  </div>
</div>""" + foot()

cards["05-deal"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">매물은 늘고 거래는 최저</h1>
  <div style="font-size:27px;color:var(--mute)">파는 집과 팔린 집 · 단위가 달라 따로 적음</div>
  <div class="tl">""" + tlrows([
    ("11월 4일", "매물 8만430건", "팔려고 내놓은 집 · 올해 최다"),
    ("9월 한 달", "거래 3,431건", "실제로 팔린 집 · 9개월 만의 최저"),
], pad=22) + """</div>
  <div class="note" style="margin-top:14px">※ 거래는 서울부동산정보광장 · 강남3구는 값 낮춘 매물, 성북·서대문·노원은 상승 거래(서울신문)</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">서울 아파트 매물, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("매물 수는 거래가 아니다", "같은 집이 여러 번 잡힐 수 있다"),
    ("호가와 실거래가는 다르다", "국토부 실거래가 공개시스템에서 확인"),
    ("세금은 내 경우로 확인", "주택 수·지역·보유 기간마다 다르다"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">서울 아파트 매물</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">파는 집이<br>8만 채 넘었어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">석 달 전보다 2만 채 더</span><br>
    <span style="white-space:nowrap">우리 구는 얼마나?</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">어디가 · 얼마나 · 5장으로</div>
</div>""" + foot()

insta["02-more"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"파는 집이 얼마나 늘었어요?"</div>
    <div class="a gtx">100채가 133채가 됐어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    8월 3일 <b>6만409채</b>에서 11월 4일 <b>8만430채</b>로
    석 달 만에 2만 채 넘게 늘었어요. 올해 들어 가장 많아요.</div>
</div>""" + foot()

insta["03-gangnam"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">강남3구는 얼마나?</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">석 달 새 늘어난 파는 집 · 채</div>
""" + hb("서초구", "+2,872", 100, hi=True, inside=True) \
    + hb("강남구", "+2,673", 93.1, inside=True) \
    + hb("송파구", "+2,075", 72.2, inside=True) + """
  <div class="note" style="margin-top:14px">세 구에서만 7,620채가 늘었어요</div>
</div>""" + foot()

insta["04-seongbuk"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">늘어난 비율로는 여기가 1등</div>
  <div class="bignum gtx" style="margin-top:10px">성북구</div>
  <div class="bigcap">100채였다면 161채가 됐어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    강남3구 말고 나머지 22개 구도 <b>100채 → 132채</b>.
    서울 어디서나 파는 집이 늘었어요.</div>
</div>""" + foot()

insta["05-deal"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"그럼 많이 팔렸어요?"</div>
    <div class="a gtx">오히려 덜 팔렸어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    9월 한 달 실제로 팔린 집은 <b>3,431채</b>.
    9개월 만에 가장 적어요. 파는 쪽과 사는 쪽이
    <b>값을 두고 버티는</b> 중이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("올라온 값은 팔린 값이 아니에요", "실제로 팔린 값을 따로 찾아보세요"),
    ("같은 집이 여러 번 보일 수 있어요", "여러 부동산에 함께 올라가요"),
    ("세금은 내 경우로 물어보세요", "집 수·지역마다 달라요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
