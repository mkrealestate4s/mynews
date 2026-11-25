# -*- coding: utf-8 -*-
"""2026-11-26 #139 잠실 래미안아이파크 줍줍 경쟁률 (목 비교형). 수치는 gen_example_139.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "jrr"
DATEK = "2026-11-26"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">송파 신천동 · 계약취소 3가구 무순위</div>
  <h1 class="serif gtx" style="font-size:66px;margin:14px 0 28px;line-height:1.2">잠실 래미안아이파크<br>줍줍 경쟁률</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    <span style="white-space:nowrap">3가구에 6만3,950명</span><br>
    <span style="white-space:nowrap">당첨 발표 11월 27일</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">신청자 · 가격 비교 · 2024년 · 일정 · 체크</div>
</div>""" + foot()

cards["02-people"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">59㎡ 한 집에 3만3,125명</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">유형별 신청자 · 각 1가구 · 청약홈 집계 보도</div>
""" + hb("59㎡A 일반 (11/24)", "3만3,125명", 100, hi=True, inside=True) + hb("43㎡ 일반 (11/24)", "2만322명", 61.3, inside=True) + hb("84㎡D 신혼 특공 (11/23)", "1만503명", 31.7, inside=True) + """
  <div class="note" style="margin-top:14px">※ 일반 2가구 5만3,447명, 평균 2만6,723.5대 1</div>
</div>""" + foot()

cards["03-price"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡, 실거래의 절반도 안 된다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">이번 공급가 vs 최근 거래 기준 · 원</div>
""" + hb("84㎡ 입주권 실거래 (7월)", "43억", 100, inside=True) + hb("84㎡D 이번 공급가", "18억5,607만", 43.2, hi=True) + hb("59㎡ 보류지 기준가 (6월)", "30억8,000만", 71.6, inside=True) + hb("59㎡A 이번 공급가", "15억7,940만", 36.7, hi=True) + """
  <div class="note" style="margin-top:12px">※ 공급가는 옵션 제외 · 84㎡ 차이 약 24억</div>
</div>""" + foot()

cards["04-vs2024"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">2년 전 59㎡는 591대 1이었다</h1>
  <div style="font-size:27px;color:var(--mute)">같은 단지 경쟁률 · 2024년 10월 vs 이번</div>
  <div class="tl">""" + tlrows([
    ("268.7대 1", "2024 일반 1순위", "307가구에 8만2,487명"),
    ("591.2대 1", "2024 59㎡A", "24가구에 1만4,190명"),
    ("3만3,125대 1", "이번 59㎡A", "1가구 · 약 56배"),
    ("1만503대 1", "이번 84㎡D 특공", "1가구 · 신혼부부"),
], pad=14) + """</div>
</div>""" + foot()

cards["05-next"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">내일 발표, 계약은 12월 4일</h1>
  <div style="font-size:27px;color:var(--mute)">당첨되면 이어지는 일정 (보도)</div>
  <div class="tl">""" + tlrows([
    ("11월 27일", "당첨자 발표", "청약홈에서 확인"),
    ("12월 1일", "서류 접수", "자격 검증"),
    ("12월 4일", "계약", "계약금 30% · 84㎡ 5억5,682만"),
    ("30일 안", "잔금", "84㎡ 12억9,925만 · 옵션 별도"),
], pad=14) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">발표 전에 볼 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("27일 청약홈 당첨 조회", "서류는 12월 1일 하루"),
    ("계약금 30% 현금", "84㎡ 5억5,682만 · 잔금 30일 안"),
    ("실거주 2년 · 재당첨 10년", "포기해도 당첨 이력이 남을 수 있다"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정본은 청약홈 공고문 · 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">잠실 래미안아이파크 줍줍</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">3집에<br>6만4천 명</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">제비뽑기 결과는</span><br>
    <span style="white-space:nowrap">11월 27일 발표</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 명 · 얼마 · 왜 · 다음</div>
</div>""" + foot()

insta["02-odds"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"59㎡ 넣었는데, 될까요?"</div>
    <div class="a gtx">3만3천 명 중 1명이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    10만 명이 넣으면 <b>3명</b> 정도 되는 확률.
    43㎡는 2만 명, 신혼부부 34평은 1만 명이 넣었어요.</div>
</div>""" + foot()

insta["03-price"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">84㎡(34평) 이번 가격</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:112px">18억 6천</div>
  <div class="bigcap">7월에 같은 평형이 43억에 팔렸어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    59㎡도 <b style="white-space:nowrap">15억 8천</b>이에요.
    그래서 다들 <b>로또</b>라고 불러요.</div>
</div>""" + foot()

insta["04-why"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"왜 이렇게 싸요?"</div>
    <div class="a gtx">2년 전 분양 가격 그대로라서요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그사이 잠실 집값이 많이 올랐어요.
    2년 전 59㎡는 <b style="white-space:nowrap">591대 1</b>, 이번엔 <b style="white-space:nowrap">3만대 1</b>.</div>
</div>""" + foot()

insta["05-next"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">당첨되면 바로</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">12월 4일</div>
  <div class="bigcap">가격의 30%를 내고 계약해요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    34평은 <b style="white-space:nowrap">5억 6천</b>.
    나머지도 <b>한 달 안</b>에 내야 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">발표 날 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("27일 청약홈 조회", "문자만 기다리지 말고 직접 봐요"),
    ("현금이 준비됐는지", "계약금은 한 번에 내요"),
    ("2년은 직접 살 수 있는지", "세 놓고 잔금 치르기는 어려워요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
