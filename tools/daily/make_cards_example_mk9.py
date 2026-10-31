# -*- coding: utf-8 -*-
"""2026-11-01 #112 목동9단지 재건축 현설 D-1. 수치는 gen112.py 와 같다.
4번 카드 가로 (5,123 -> 100): 82.9 · 77.3 · 75.2 · 54.9 · 47.6
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "mk9"
DATEK = "2026-11-01"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">양천구 목동 · 시공사 입찰</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">목동9단지 재건축<br>내일 현장설명회</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    예정 공사비 <span class="gtx">2조6,067억</span> · 3.3㎡당 980만원<br>
    입찰 마감 2027년 1월 11일</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 공사비 · 규모 · 입찰 조건 · 체크</div>
</div>""" + foot()

cards["02-sched"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">내일 현설, 1월 11일 입찰 마감</h1>
  <div style="font-size:27px;color:var(--mute)">목동9단지 시공사 선정 일정</div>
  <div class="tl">""" + tlrows([
    ("10.23", "입찰공고", "사업시행자 한국자산신탁"),
    ("10.31", "참가신청 마감", "어제"),
    ("11.2", "현장설명회", "내일 · 참석해야 입찰 자격"),
    ("2027.1.11", "입찰 마감", "입찰제안서 제출"),
    ("2027 1분기", "시공사 선정 목표", "유찰되면 밀린다"),
], pad=13) + """</div>
</div>""" + foot()

cards["03-cost"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">3.3㎡당 980만원, 거의 같은 선</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">목동 재건축 3.3㎡당 예정공사비 · 만원</div>
""" + hb("4단지", "1,010", 100, inside=True) + hb("10단지", "990", 98, inside=True) \
    + hb("9단지", "980", 97, hi=True, inside=True) + hb("12단지", "980", 97, inside=True) \
    + hb("13단지", "980", 97, inside=True) + hb("8단지", "965", 95.5, inside=True) + """
  <div class="note" style="margin-top:12px">※ 차이가 작아 승부는 제안 조건에서 · 보도 기준</div>
</div>""" + foot()

cards["04-size"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">3,961세대, 목동에서 세 번째</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">재건축 후 계획 가구수 · 확정 전</div>
""" + hb("14단지", "5,123", 100, inside=True) + hb("10단지", "4,248", 82.9) + hb("9단지 · 최고 49층", "3,961", 77.3, hi=True) \
    + hb("13단지", "3,852", 75.2) + hb("12단지", "2,810", 54.9) + hb("4단지", "2,436", 47.6) + """
  <div class="note" style="margin-top:12px">※ 계획이 알려진 단지 기준 · 심의 단계마다 바뀔 수 있다</div>
</div>""" + foot()

cards["05-rule"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">목동9단지 입찰보증금</div>
  <div class="bignum gtx" style="margin-top:10px">800억</div>
  <div class="bigcap">현금 500억 + 이행보증증권 300억 · 컨소시엄 불가</div>
  <div class="duo">
    <div class="box"><div class="dl">앞서 정해진 목동</div><div class="dv">5곳</div><div class="ds">6·10단지 확정 · 8·12·13단지 우선협상</div></div>
    <div class="box"><div class="dl">그중 경쟁입찰</div><div class="dv">0곳</div><div class="ds">5곳 모두 단독 응찰</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">목동9단지 재건축, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("현설 참석은 입찰이 아니다", "경쟁 여부는 1월 11일 입찰서에서 갈린다"),
    ("3,961세대 · 49층은 계획", "심의·인가 단계에서 바뀔 수 있다 · 분담금 미정"),
    ("조합원 지위는 따로 확인", "사업시행자 · 양천구청 · 정비사업 정보몽땅"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">목동9단지 재건축</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">누가 지을까,<br>내일 첫 설명회</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    공사비만 <span style="white-space:nowrap">2조6천억원</span><br>
    <span style="white-space:nowrap">49층 아파트 3,961집 계획</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">언제 · 얼마 · 누가 · 5장으로</div>
</div>""" + foot()

insta["02-when"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">건설사는 언제 정해져요?</h1>
  <div style="font-size:27px;color:var(--mute)">내년 봄이 목표예요</div>
  <div class="tl">""" + tlrows([
    ("11월 2일", "건설사 설명회", "여기 와야 도전할 수 있어요"),
    ("1월 11일", "건설사 제안서 마감", "2027년"),
    ("1~3월", "건설사 결정", "목표, 늦어질 수 있어요"),
], pad=16) + """</div>
</div>""" + foot()

insta["03-cost"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"공사비가 비싼 편이에요?"</div>
    <div class="a gtx">목동 다른 단지랑 비슷해요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    평당 <b>980만원</b>이에요. 목동 다른 단지도
    965만~1,010만원 사이예요. 그래서 건설사들은
    값보다 <b>이주비·단지 이름</b> 같은 조건으로 겨뤄요.</div>
</div>""" + foot()

insta["04-size"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">다 지으면 몇 집이에요?</div>
  <div class="bignum gtx" style="margin-top:10px">3,961집</div>
  <div class="bigcap">최고 49층 · 아직 계획이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    목동에서 <b>세 번째로 커요</b>. 14단지 5,123집,
    10단지 4,248집 다음이에요. 심사를 거치면서
    숫자가 바뀔 수 있어요.</div>
</div>""" + foot()

insta["05-compete"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"건설사끼리 경쟁해요?"</div>
    <div class="a gtx">목동에선 아직 한 번도 없었어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    먼저 정해진 <b>5곳</b>은 모두 건설사가 한 곳만 들어왔어요.
    9단지는 삼성물산·GS건설이 관심 있다는 얘기가 있지만
    <b>아직 소문</b>이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("설명회에 온 건설사 수에 속지 않기", "실제 경쟁은 1월 제안서에서 갈려요"),
    ("3,961집은 아직 계획", "부담할 돈(분담금)도 안 정해졌어요"),
    ("사기 전에 구청에 확인", "재건축 집은 사고팔 때 제한이 있을 수 있어요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
