# -*- coding: utf-8 -*-
"""2026-11-28 #141 송파 아파트값 −0.50% vs 성북 +0.33%. 수치는 gen141.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "spsb"
DATEK = "2026-11-28"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">부동산원 11월 넷째 주 · 11월 26일 발표</div>
  <h1 class="serif gtx" style="font-size:68px;margin:14px 0 28px;line-height:1.2">송파는 내리고,<br>성북은 올랐다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    송파 <span class="gtx" style="white-space:nowrap">−0.50%</span> · 서울 최대 하락<br>
    성북 <span class="gtx" style="white-space:nowrap">+0.33%</span> · 서울 1위</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">날짜 · 송파 · 성북 · 전세 · 체크</div>
</div>""" + foot()

cards["02-dates"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">12월에 볼 날짜 3개</h1>
  <div style="font-size:27px;color:var(--mute)">송파·성북 아파트값 달력</div>
  <div class="tl">""" + tlrows([
    ("12월 3일", "부동산원 다음 주간 발표", "매주 목요일 · 11월 30일 기준"),
    ("12월 4일", "잠실 래미안아이파크 줍줍 계약", "3가구에 6만3,950명 신청"),
    ("12월 31일", "토지거래허가구역 기한", "연장 여부는 아직 발표 전"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 12월 3일은 관행 기준 예정일</div>
</div>""" + foot()

cards["03-songpa"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">송파, 3주째 더 떨어졌다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">송파구 아파트값 주간 하락률 (%)</div>
""" + hb("11월 9일 기준", "−0.35", 70, inside=True) + hb("11월 16일 기준", "−0.42", 84, inside=True) + hb("11월 23일 기준", "−0.50", 100, hi=True, inside=True) + """
  <div class="bigcap" style="margin-top:20px">20억 아파트면 <b class="gtx" style="font-size:44px;white-space:nowrap">한 주 1,000만원</b></div>
  <div class="note" style="margin-top:14px">※ 20억 × 0.50% · 주간 지수는 표본 기준이라 개별 단지와 다를 수 있다</div>
</div>""" + foot()

cards["04-seongbuk"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">같은 주, 성북구 아파트값</div>
  <div class="bignum gtx" style="margin-top:10px">+0.33%</div>
  <div class="bigcap">서울 25개 구 중 1위 · 정릉·돈암동 위주</div>
  <div class="duo">
    <div class="box"><div class="dl">11월 둘째 주</div><div class="dv">+0.39%</div><div class="ds">이때도 서울 1위</div></div>
    <div class="box"><div class="dl">10억 아파트면</div><div class="dv gtx">+330만</div><div class="ds">한 주에 오른 몫</div></div>
  </div>
</div>""" + foot()

cards["05-jeonse"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">전세는 강북이 더 올랐다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">11월 넷째 주 아파트 전셋값 변동률 (%)</div>
""" + hb("노원", "+0.40", 100, hi=True, inside=True) + hb("성북", "+0.27", 67.5, hi=True, inside=True) + hb("서울 평균", "+0.14", 35, inside=True) + """
  <div class="bigcap" style="margin-top:20px">5억 전세면 <b class="gtx" style="font-size:44px;white-space:nowrap">한 주 200만원</b></div>
  <div class="note" style="margin-top:14px">※ 5억 × 0.40% · 한국부동산원 11월 23일 기준</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:24px">집 보러 가기 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("주간 지수와 실거래는 다르다", "관심 단지는 실거래가 공개시스템으로"),
    ("대출 한도 구간", "15억 이하 6억 · 25억 초과 2억"),
    ("12월 날짜", "3일 주간 발표 · 31일 토허 기한"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">이번 주 서울 아파트값</div>
  <h1 class="serif gtx" style="font-size:66px;margin:16px 0 28px;line-height:1.22">송파는 내리고<br>성북은 올랐다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">송파 서울에서 가장 많이 ↓</span><br>
    <span style="white-space:nowrap">성북 서울에서 가장 많이 ↑</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">얼마나 · 왜 · 전세 · 볼 것</div>
</div>""" + foot()

insta["02-songpa"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"송파 얼마나 내렸어요?"</div>
    <div class="a gtx">20억 집이면 한 주에 1,000만원쯤이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    3주째 <b>내리는 폭이 커졌어요.</b>
    잠실·문정동 큰 단지들이 앞장섰어요.</div>
</div>""" + foot()

insta["03-seongbuk"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">같은 주 성북, 10억 집이면</div>
  <div class="bignum gtx" style="margin-top:10px">+330만</div>
  <div class="bigcap">한 주에 이만큼 올랐어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    서울 25개 구 중 <b>가장 많이</b> 올랐어요.
    정릉·돈암동이 앞장섰어요.</div>
</div>""" + foot()

insta["04-why"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"왜 이렇게 갈려요?"</div>
    <div class="a gtx">빌릴 수 있는 돈이 달라서예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    15억 아래 집은 <b>6억까지</b>, 25억 넘는 집은
    <b>2억까지</b>만 빌릴 수 있어요.</div>
</div>""" + foot()

insta["05-jeonse"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">노원에서 5억 전세라면</div>
  <div class="bignum gtx" style="margin-top:10px">+200만</div>
  <div class="bigcap">한 주에 오른 몫이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    집값은 멈칫해도 <b>전세는 계속 올라요.</b>
    성북 전세도 같이 올랐어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("그 단지 실제 값", "실제로 팔린 값을 따로 봐요"),
    ("내가 빌릴 수 있는 돈", "집값 구간마다 달라요"),
    ("12월 3일", "다음 주 숫자가 나와요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
