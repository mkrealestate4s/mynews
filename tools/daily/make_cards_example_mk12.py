# -*- coding: utf-8 -*-
"""2026-11-24 #136 목동12단지 재건축 GS건설. 수치는 gen_example_136.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "mk12"
DATEK = "2026-11-24"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">11월 22일 총회 · 시공사 선정</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">목동12단지 재건축,<br>GS건설 확정</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    공사비 <span class="gtx" style="white-space:nowrap">1조7,887억</span><br>
    <span style="white-space:nowrap">1,860가구 → 2,810가구</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">규모 · 과정 · 공사비 · 목동 현황 · 체크</div>
</div>""" + foot()

cards["02-size"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1,860가구가 2,810가구로</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">최고 15층 → 43층 · 계획 기준</div>
""" + hb("재건축 계획", "2,810가구", 100, hi=True, inside=True) + hb("지금", "1,860가구", 66.2, inside=True) + """
  <div class="duo"><div class="box"><div class="dl">늘어나는 가구</div><div class="dv gtx">+950</div></div>
    <div class="box"><div class="dl">지금 대비</div><div class="dv">1.51배</div></div></div>
  <div class="note" style="margin-top:14px">※ 심의 단계마다 바뀔 수 있는 계획 숫자</div>
</div>""" + foot()

cards["03-path"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">두 번 단독, 그래서 수의계약</h1>
  <div style="font-size:27px;color:var(--mute)">목동12단지 시공사 선정 흐름</div>
  <div class="tl">""" + tlrows([
    ("8월", "1차 입찰 유찰", "GS건설 혼자 응찰"),
    ("9월", "2차 입찰도 단독", "2차 현설 뒤 같은 결과"),
    ("11월 22일", "총회에서 선정", "조합원 투표로 확정"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 10단지 현대, 13단지 삼성도 같은 경로</div>
</div>""" + foot()

cards["04-cost"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공사비, 목동에서 중간</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">3.3㎡당 예정 공사비</div>
""" + hb("4단지", "1,010만", 100, inside=True) + hb("12단지", "980만", 97.0, hi=True, inside=True) + hb("13단지 · 9단지", "980만", 97.0, inside=True) + hb("8단지", "965만", 95.5, inside=True) + """
  <div class="note" style="margin-top:14px">※ 각 단지 입찰공고·총회 보도 기준</div>
</div>""" + foot()

cards["05-map"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동 시공사, 지금 어디까지</h1>
  <div style="font-size:27px;color:var(--mute)">2026년 11월 24일 기준</div>
  <div class="tl">""" + tlrows([
    ("10단지", "현대건설", "10월 18일 선정 · 찬성 95.9%"),
    ("13단지", "삼성물산", "11월 7일 선정 · 찬성 95.7%"),
    ("12단지", "GS건설", "11월 22일 선정"),
    ("4단지", "재입찰 예정", "11월 16일 현대 단독 유찰"),
    ("9단지", "입찰 진행 중", "2027년 1월 11일 마감"),
], pad=12) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">목동12단지, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("계획 가구는 확정 전", "2,810가구·43층은 심의에서 바뀔 수 있음"),
    ("제안 단지명", "'리플리제 자이'는 GS건설 제안"),
    ("조합원 지위 양도", "단계마다 달라 조합·구청 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">목동12단지 재건축</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">목동12단지,<br>자이로 짓는다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">GS건설이 시공사로</span><br>
    <span style="white-space:nowrap">1,860집이 2,810집으로</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 집 · 왜 혼자 · 얼마 · 목동 · 볼 것</div>
</div>""" + foot()

insta["02-homes"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마나 커져요?"</div>
    <div class="a gtx">950집이 늘어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지금 15층짜리 <b>1,860집</b>이 계획대로면
    43층 <b>2,810집</b>이 돼요. 아직 바뀔 수 있는 숫자예요.</div>
</div>""" + foot()

insta["03-alone"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"왜 한 곳만 왔어요?"</div>
    <div class="a gtx">두 번 다 GS만 들어왔어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    두 번 혼자면 투표로 바로 정할 수 있어요.
    목동 10·13단지도 이렇게 정했어요.</div>
</div>""" + foot()

insta["04-cost"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">짓는 데 드는 돈, 한 집에</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:112px">약 6억</div>
  <div class="bigcap">전체 <span style="white-space:nowrap">1조7,887억</span> ÷ <span style="white-space:nowrap">2,810집</span></div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    평형이 달라 대략이에요.
    13단지도 한 집에 <b>6억</b>쯤이에요.</div>
</div>""" + foot()

insta["05-mokdong"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:4px">목동, 어디가 정해졌나</h1>
  <div class="tl">""" + tlrows([
    ("10단지", "현대건설", "10월에 정했어요"),
    ("13단지", "삼성물산", "11월 초에 정했어요"),
    ("12단지", "GS건설", "이번 주말에 정했어요"),
    ("4·9단지", "아직이에요", "다시 받거나 1월 마감"),
], pad=17) + """</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">목동 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("층수·집 수", "아직 계획이라 바뀔 수 있어요"),
    ("아파트 이름", "'리플리제 자이'는 제안이에요"),
    ("사도 조합원이 되는지", "조합·구청에 꼭 물어보세요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
