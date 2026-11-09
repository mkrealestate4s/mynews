# -*- coding: utf-8 -*-
"""2026-11-10 #121 한화포레나 지제역. 수치는 gen121.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "fjj"
DATEK = "2026-11-10"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">평택 세교동 · 1,098가구</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">한화포레나<br>지제역</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    오늘 <span class="gtx">1순위</span> · 내일 2순위<br>
    84㎡ 6억대부터 · 18일 발표</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">공급 · 일정 · 분양가 · 계약금 · 체크</div>
</div>""" + foot()

cards["02-mix"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1,098가구 중 일반 570가구</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">한화포레나 지제역 공급 구성 · 가구</div>
""" + hb("전체", "1,098", 100, inside=True) + hb("일반공급 (오늘 1순위)", "570", 51.9, hi=True, inside=True) \
    + hb("특별공급 (어제 접수)", "528", 48.1, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">특공 최다</div><div class="dv gtx">신혼 141</div></div>
    <div class="box"><div class="dl">그다음</div><div class="dv">다자녀 106</div></div>
  </div>
</div>""" + foot()

cards["03-sched"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">오늘 1순위, 18일 발표</h1>
  <div style="font-size:27px;color:var(--mute)">한화포레나 지제역 일정</div>
  <div class="tl">""" + tlrows([
    ("11.10 (화)", "1순위 청약", "오늘 · 청약홈 접수"),
    ("11.11 (수)", "2순위 청약", "1순위에서 남으면"),
    ("11.18 (수)", "당첨자 발표", "청약홈에서 확인"),
    ("11.29~12.1", "정당계약", "입주 2029년 말 예정"),
], pad=16) + """</div>
  <div class="note" style="margin-top:14px">※ 같은 순위 경쟁 시 평택 6개월 이상 거주자 우선 · 보도 기준</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡ 6억2,695만원부터</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">타입별 최저층 분양가 · 만원</div>
""" + hb("84B", "62,695", 94.8, hi=True, inside=True) + hb("84C", "64,850", 98, inside=True) \
    + hb("84A (주력)", "64,875", 98.1, inside=True) + hb("84D", "66,150", 100, inside=True) + """
  <div class="note" style="margin-top:14px">※ 최고층 7억95만~7억2,450만원 · 84A는 층따라 6,000만원 차이</div>
</div>""" + foot()

cards["05-pay"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">84A 1층 계약금 (분양가의 10%)</div>
  <div class="bignum gtx" style="margin-top:10px">약 6,490만</div>
  <div class="bigcap">계약 때 1,000만원, 30일 안에 약 5,490만원</div>
  <div class="duo">
    <div class="box"><div class="dl">계약금</div><div class="dv gtx">10%</div></div>
    <div class="box"><div class="dl">중도금 이자후불</div><div class="dv">60%</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">포레나 지제역, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("평택 6개월 거주자 우선", "같은 순위 안에서 경쟁하면 평택 거주자가 먼저"),
    ("오늘 1순위 · 내일 2순위", "통장 12개월 + 예치금 · 기준은 청약홈에서"),
    ("계약금 10%는 30일 안에", "84㎡면 6천만원대 · 전매·재당첨 제한은 공고문"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">한화포레나 지제역 · 평택</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">오늘이<br>1순위 날이에요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">1,098집 대단지</span><br>
    <span style="white-space:nowrap">84㎡ 6억대부터</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">누가 · 언제 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-who"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"집 있어도 넣을 수 있어요?"</div>
    <div class="a gtx">1순위로 넣을 수 있어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    청약통장 <b>12개월</b>에 예치금을 채웠다면
    세대원도, 집이 있어도 1순위래요(보도 기준).
    다만 <b>평택에 6개월 넘게 산 사람</b>이 먼저예요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">당첨자 발표</div>
  <div class="bignum gtx" style="margin-top:10px">11월 18일</div>
  <div class="bigcap">다음 주 수요일이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    오늘(10일) 1순위, 내일(11일) 2순위예요.
    당첨되면 <b>11월 29일~12월 1일</b>에 계약하고
    2029년 말에 들어가요.</div>
</div>""" + foot()

insta["04-money"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"84㎡ 얼마예요?"</div>
    <div class="a gtx"><span style="white-space:nowrap">6억2,695만원부터</span>예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    제일 비싼 집은 <span style="white-space:nowrap"><b>7억2,450만원</b></span>이에요.
    같은 84㎡라도 1층과 꼭대기 층이
    <b>6,000만원</b>쯤 차이 나요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"당장 얼마 있어야 해요?"</div>
    <div class="a gtx"><span style="white-space:nowrap">6천만원대</span>가 필요해요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    계약금이 집값의 <b>10%</b>예요. 계약 날 1,000만원,
    한 달 안에 나머지를 내요. 중도금 60%는
    이자를 나중에 내는 방식이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">넣기 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("평택에 산 기간", "6개월이 넘으면 먼저 뽑혀요"),
    ("내 통장 예치금", "청약홈에서 1순위인지 확인해요"),
    ("계약금 6천만원대", "당첨 발표 뒤 열흘 남짓이면 계약이에요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
