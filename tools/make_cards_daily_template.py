# -*- coding: utf-8 -*-
"""2026-08-26 '모두 줄었는데 20대만 늘었다' 카드뉴스 · 6장 × 3테마."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "isipdae"
DATEK = "2026-08-26"

COLCSS = """
.flow{display:flex;flex-direction:column;align-items:stretch}
.fbox{background:var(--panel);border:1px solid var(--line);border-radius:18px;
  padding:19px 32px;display:flex;align-items:center;gap:24px}
.fbox .n{font-weight:900;font-size:38px;flex:none}
.fbox .t{font-size:31px;font-weight:700}
.fbox .s{font-size:24px;color:var(--mute);font-weight:400}
.farrow{text-align:center;font-size:30px;line-height:1;color:var(--accent);
  font-weight:900;padding:1px 0}
.note{font-size:23px;color:var(--mute)}
.duo{display:flex;gap:22px;margin-top:26px}
.duo .box{flex:1;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:30px 32px}
.duo .dl{font-size:25px;color:var(--mute);margin-bottom:10px}
.duo .dv{font-weight:900;font-size:54px;line-height:1.1;white-space:nowrap}
.duo .ds{font-size:23px;color:var(--mute);margin-top:14px;line-height:1.5;word-break:keep-all}
.bignum{font-weight:900;font-size:150px;line-height:1.02}
.bigcap{font-size:30px;color:var(--body);margin-top:16px;word-break:keep-all}
/* zero-baseline columns */
.zwrap{background:var(--panel);border:1px solid var(--line);border-radius:22px;padding:34px 34px}
.zcols{position:relative;height:300px;display:flex;gap:26px}
.zcols::before{content:"";position:absolute;left:0;right:0;top:33%;height:2px;background:var(--line)}
.zcol{flex:1;position:relative;height:100%}
.zcol .zbar{position:absolute;left:50%;transform:translateX(-50%);width:100%;max-width:110px}
.zcol .zbar.up{bottom:67%;height:var(--h);border-radius:10px 10px 0 0}
.zcol .zbar.dn{top:33%;height:var(--h);border-radius:0 0 10px 10px}
.zcol .zbar.hi{background:var(--grad)}
.zcol .zbar.lo{background:var(--fillgray)}
.zcol .zv{position:absolute;left:-16px;right:-16px;text-align:center;font-size:28px;font-weight:900}
.zcol .zv.up{bottom:calc(67% + var(--h) + 8px)}
.zcol .zv.dn{top:calc(33% + var(--h) + 8px)}
.zlbl{display:flex;gap:26px;margin-top:14px}
.zlbl span{flex:1;text-align:center;color:var(--mute);font-size:22px;line-height:1.35}
"""

def top(pnum):
    return ('<div class="top"><div class="eyebrow">{{EYEBROW}}</div>'
            f'<div class="pnum">{pnum} / {TOTAL}</div></div>')

def foot():
    return ('<div class="footwrap"><div class="trace"></div><div class="foot">'
            '<span>{{BRAND}}</span>'
            f'<span>데이터 기준일 {DATEK}</span></div></div>')

def hbar(label, value, pct, gray=False, h=46, fs=27, mb=20):
    return (f'<div class="hbar" style="margin-bottom:{mb}px">'
            f'<div class="lb" style="margin-bottom:8px;font-size:{fs}px"><span>{label}</span>'
            f'<span class="v {"" if gray else "gtx"}" style="font-size:{fs + 2}px">{value}</span></div>'
            f'<div class="railx" style="height:{h}px"><div class="fillx{" gray" if gray else ""}" style="width:{pct}%"></div></div></div>')

def zcol(val, pct, up=False):
    d = "up" if up else "dn"
    tone = "hi" if up else "lo"
    g = " gtx" if up else ""
    return (f'<div class="zcol"><div class="zv {d}{g}" style="--h:{pct}%">{val}</div>'
            f'<div class="zbar {d} {tone}" style="--h:{pct}%"></div></div>')

cards = {}

cards["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:35px;color:var(--mute);font-weight:500">2분기 신규 주택담보대출</div>
  <h1 class="serif gtx" style="font-size:92px;margin:14px 0 28px;line-height:1.18">모두 줄었는데<br>20대만 늘었다</h1>
  <div style="font-size:38px;color:var(--ink);font-weight:700;line-height:1.55">
    한 건당 <span class="gtx" style="font-size:46px">2,110만원</span> 줄었는데<br>
    20대만 <span class="gtx" style="font-size:46px">392만원</span> 늘었다</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">한국은행 2026년 2분기 · 5장으로</div>
</div>""" + foot()

cards["02-flow"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin:6px 0 24px">왜 20대만 비켜갔나</h1>
  <div class="flow">
    <div class="fbox"><span class="n gtx">1</span>
      <div><div class="t">문턱이 높아졌다</div>
      <div class="s">DSR·총량 관리 강화로 빌릴 수 있는 금액이 깎였다</div></div></div>
    <div class="farrow">↓</div>
    <div class="fbox"><span class="n gtx">2</span>
      <div><div class="t">20대는 예외 통로가 있다</div>
      <div class="s">무주택·생애최초 비중이 높다 (LTV 최대 80%)</div></div></div>
    <div class="farrow">↓</div>
    <div class="fbox"><span class="n gtx">3</span>
      <div><div class="t">통과한 사람만 남았다</div>
      <div class="s">소득이 되는 소수만 실행 → 평균 금액이 올라간다</div></div></div>
  </div>
  <div class="note" style="margin-top:24px;word-break:keep-all">※ 규제를 피한 게 아니라, 규제를 통과할 수 있는 사람만 남은 구조입니다</div>
</div>""" + foot()

cards["03-drop"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:6px">대출은 진짜 줄었다</h1>
  <div style="font-size:26px;color:var(--mute);margin-bottom:14px">새로 받은 주담대 한 건의 크기</div>
  <div class="duo">
    <div class="box">
      <div class="dl">2분기 평균</div>
      <div class="dv gtx">2억 829만원</div>
      <div class="ds">주담대 <strong>1건당</strong> 평균 금액</div>
    </div>
    <div class="box">
      <div class="dl">전 분기 대비</div>
      <div class="dv">−2,110만원</div>
      <div class="ds"><strong>2013년 통계 시작 이후</strong> 최대 감소</div>
    </div>
  </div>
  <div class="note" style="margin-top:28px;word-break:keep-all">※ 3억을 빌릴 계획이었다면 석 달 만에 2,100만원이 사라진 셈 (한국은행 2026년 2분기)</div>
</div>""" + foot()

cards["04-age"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:6px">20대만 늘었다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">연령별 신규 주담대 증감 (전 분기 대비 · 만원)</div>
  <div class="zwrap">
    <div class="zcols">""" \
    + zcol("+392", 5.5, up=True) + zcol("−169", 2.4) + zcol("−1,281", 18.1) \
    + zcol("−2,632", 37.2) + zcol("−3,537", 50) + """
    </div>
    <div class="zlbl"><span>20대</span><span>60대<br>이상</span><span>50대</span><span>30대</span><span>40대</span></div>
  </div>
  <div style="font-size:28px;color:var(--body);margin-top:20px;word-break:keep-all">
    규제는 <strong>30·40대</strong>에 걸렸다. 집을 사는 주력 연령대다.</div>
</div>""" + foot()

cards["05-share"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:6px">빌린 20대는 100명 중 6명</h1>
  <div style="font-size:26px;color:var(--mute);margin-bottom:26px">신규 주담대 연령별 비중 (2분기)</div>
""" + hbar("30대", "43.7%", 100, gray=True) \
    + hbar("40대", "24.5%", 56, gray=True) \
    + hbar("50대", "15.9%", 36, gray=True) \
    + hbar("60대 이상", "9.9%", 23, gray=True) \
    + hbar("20대", "6.0%", 14, mb=0) + """
  <div class="note" style="margin-top:26px;word-break:keep-all">※ '20대 평균 2억'은 20대 전체가 아니라, <strong>빌릴 수 있었던 6%</strong>의 평균입니다</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:26px">중개 현장, 이 3가지만</h1>
  <div style="display:flex;flex-direction:column;gap:18px">""" + "".join(
    f'<div class="panel" style="display:flex;gap:28px;align-items:flex-start;padding:26px 34px">'
    f'<div class="serif gtx" style="font-size:46px;font-weight:900;line-height:1.1">0{i}</div>'
    f'<div><div style="font-size:32px;font-weight:700;margin-bottom:6px">{t}</div>'
    f'<div style="font-size:25px;color:var(--mute);word-break:keep-all">{d}</div></div></div>'
    for i, (t, d) in enumerate([
        ("젊은 손님은 생애최초부터", "무주택·생애최초면 LTV 최대 80%, 예산 구간이 바뀐다"),
        ("30·40대는 한도 재확인", "한 분기에 3,537만원 · 2,632만원 줄었다. 옛 예산은 안 나온다"),
        ("줄어든 건 한 건의 크기", "가계신용은 사상 첫 2,000조, 시장이 죽은 게 아니다"),
    ], start=1)) + """
  </div>
  <div class="note" style="margin-top:22px">※ 시장 정보 제공 목적이며 특정 거래·투자를 권유하지 않습니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS,
            eyebrow="2026 · 8월 부동산 키워드 리포트")
