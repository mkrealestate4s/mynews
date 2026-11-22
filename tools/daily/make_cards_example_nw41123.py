# -*- coding: utf-8 -*-
"""2026-11-23 #135 11월 넷째 주 청약 일정 서울 4곳. 수치는 gen_example_135.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "nw4"
DATEK = "2026-11-23"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">11월 23~27일 · 이번 주 청약</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">11월 넷째 주 청약,<br>서울 4곳</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    전국 <span class="gtx" style="white-space:nowrap">6,295가구</span>, 전주의 3.7배<br>
    <span style="white-space:nowrap">84㎡ 18억부터 25억까지</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">달력 · 줍줍 · 분양가 · 물량 · 체크</div>
</div>""" + foot()

cards["02-cal"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">이번 주 서울 청약 달력</h1>
  <div style="font-size:27px;color:var(--mute)">2026년 11월 23~27일</div>
  <div class="tl">""" + tlrows([
    ("23일 월", "래미안아이파크 줍줍 특공", "문래 특별공급도 같은 날"),
    ("24일 화", "문래 1순위 · 래미안 일반", "해링턴 플레이스 문래 해당지역"),
    ("25일 수", "경희궁 에피트 특공", "문래 1순위 기타지역"),
    ("26일 목", "경희궁 에피트 1순위", "문래 2순위"),
    ("27일 금", "반포124 공고 예정", "계획 · 청약홈 확인"),
], pad=13) + """</div>
</div>""" + foot()

cards["03-zup"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">래미안아이파크 줍줍 3가구</h1>
  <div style="font-size:27px;color:var(--mute)">잠실 계약취소 재공급 · 공급가</div>
  <div class="tl">""" + tlrows([
    ("84㎡D", "18억5,607만", "23일 신혼 특공 · 1가구"),
    ("59㎡A", "15억7,940만", "24일 일반 · 1가구"),
    ("43㎡", "11억548만", "24일 일반 · 1가구"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 서울 거주 무주택 · 계약금 30% · 발표 27일</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡ 분양가, 7억 넘게 차이</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">이번 주 서울 84㎡ · 최고가 기준</div>
""" + hb("경희궁 에피트 · 26일 1순위", "25억7,484만", 100, hi=True, inside=True) + hb("래미안아이파크 줍줍 · 23일", "18억5,607만", 72.1, inside=True) + hb("해링턴 플레이스 문래 · 24일", "18억2,700만", 71.0, inside=True) + """
  <div class="note" style="margin-top:14px">※ 각 단지 입주자모집공고 보도 기준 · 래미안은 계약취소분 공급가</div>
</div>""" + foot()

cards["05-week"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">11월 넷째 주 전국 청약 물량</div>
  <div class="bignum gtx" style="margin-top:10px">6,295</div>
  <div class="bigcap">전주 1,681가구의 3.7배, 15곳에서 접수</div>
  <div class="duo"><div class="box"><div class="dl">수도권 8곳</div><div class="dv">2,904</div></div>
    <div class="box"><div class="dl">지방 7곳</div><div class="dv">3,391</div></div></div>
  <div class="note" style="margin-top:22px">※ 리얼투데이 집계 · 오피스텔 포함</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">이번 주 청약, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("날짜별 자격", "줍줍은 통장 없이, 1순위는 통장 조건"),
    ("계약금 마련 시점", "래미안 12월 4일 · 문래 12월 14일~"),
    ("반포124 공고일", "27일은 계획 · 청약홈에서 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">11월 넷째 주 청약</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">이번 주 서울<br>새 아파트 4곳</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">잠실 · 문래 · 경희궁 · 반포</span><br>
    <span style="white-space:nowrap">무슨 요일에 넣나</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">요일 · 통장 · 얼마 · 볼 것</div>
</div>""" + foot()

insta["02-days"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:4px">요일별로 보면</h1>
  <div class="tl">""" + tlrows([
    ("월", "잠실 래미안아이파크", "신혼부부 1집 · 통장 없이"),
    ("화", "문래 해링턴 · 잠실", "문래 1순위 · 잠실 2집"),
    ("목", "경희궁 에피트", "1순위 (수요일은 특공)"),
    ("금", "반포124 공고 예정", "아직 계획이에요"),
], pad=17) + """</div>
</div>""" + foot()

insta["03-zup"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"통장 없어도 돼요?"</div>
    <div class="a gtx">잠실 3집은 통장 없이 넣어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    대신 <b>서울 사는 무주택</b>이어야 하고,
    34평은 계약할 때 <b>5억5천만원</b>이 먼저 필요해요.</div>
</div>""" + foot()

insta["04-price"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">같은 34평인데</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:112px">7억 차이</div>
  <div class="bigcap">문래 <span style="white-space:nowrap">18억2,700만</span> · 경희궁 <span style="white-space:nowrap">25억7,484만</span></div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    둘 다 가장 비싼 층 기준이에요.
    잠실 34평은 <b>18억5,607만</b>.</div>
</div>""" + foot()

insta["05-many"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"이번 주 왜 이렇게 많아요?"</div>
    <div class="a gtx">지난주보다 거의 4배 나왔어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    전국 15곳 <b>6,295집</b>.
    연말 전에 분양을 끝내려는 곳이 몰렸어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">청약 넣기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("통장이 필요한지", "줍줍은 없이, 1순위는 있어야 해요"),
    ("계약금 날짜", "당첨되면 2~3주 안에 내요"),
    ("공고가 떴는지", "청약홈에서 직접 확인해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
