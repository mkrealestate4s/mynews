# -*- coding: utf-8 -*-
"""2026-11-07 #118 광교 지분적립형. 수치는 gen_example_118.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "gk1107"
DATEK = "2026-11-07"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">GH 광교 A17블록 · 전국 첫 공급</div>
  <h1 class="serif gtx" style="font-size:70px;margin:14px 0 28px;line-height:1.2">광교 지분적립형<br>월요일 특공</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    분양가 <span class="gtx">25%</span>로 입주, 나머지는 20년<br>
    59㎡ 240가구 · 11월 9일 접수 시작</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">구조 · 일정 · 가격 · 물량 · 체크</div>
</div>""" + foot()

cards["02-how"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">25% 먼저, 나머지는 20년</h1>
  <div style="font-size:27px;color:var(--mute)">지분적립형 분양주택을 사는 순서</div>
  <div class="tl">""" + tlrows([
    ("입주할 때", "지분 25% 취득", "계약 때 10% · 입주 때 15%"),
    ("살면서", "나머지 75% 단계 취득", "20년에 걸쳐 · 최초 공급가 + 기간이자"),
    ("그동안", "GH 지분에 임대료", "임대보증금 또는 월 임대료"),
], pad=18) + """</div>
  <div class="note" style="margin-top:14px">※ 분당신문·이투데이·아시아경제 보도 · 취득 주기·임대료는 공고문 확인</div>
</div>""" + foot()

cards["03-when"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">9일 특공부터</h1>
  <div style="font-size:27px;color:var(--mute)">광교 지분적립형 청약 일정 · 청약홈</div>
  <div class="tl">""" + tlrows([
    ("11월 9일 (월)", "특별공급", "청년·신생아·신혼부부 등"),
    ("11월 10~11일", "일반공급", "10일 1순위 · 11일 2순위"),
    ("11월 18일", "당첨자 발표", "계약 2027년 1월 25~27일"),
    ("2029년 10월", "입주 예정", "거주의무 5년 · 전매제한 10년"),
], pad=14) + """</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">첫 지분은 1억7,150만원</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">최고 공급가 기준 · 만원</div>
""" + hb("84㎡ 일반분양 최고", "94,930", 100, inside=True) \
    + hb("59㎡ 지분적립형 최고", "68,590", 72.3, hi=True, inside=True) \
    + hb("59㎡ 첫 지분 25%", "17,150", 18.1, hi=True) + """
  <div class="note" style="margin-top:14px">※ 59㎡ 하한은 보도마다 6억3,450만·6억6,790만원 · 25%는 최고가로 계산</div>
</div>""" + foot()

cards["05-supply"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">지분적립형 240가구 중</div>
  <div class="bignum gtx" style="margin-top:10px">특공 168</div>
  <div class="bigcap">70%가 특별공급, 일반공급은 72가구</div>
  <div class="duo">
    <div class="box"><div class="dl">청년 특공 (신설)</div><div class="dv">36가구</div><div class="ds">만 19~39세 미혼 · 본인 무주택</div></div>
    <div class="box"><div class="dl">신생아 특공</div><div class="dv">48가구</div><div class="ds">나머지는 공고문 배분 확인</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">넣기 전 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("임대료까지 계산했나", "GH 지분 임대료 + 앞으로 살 지분 값"),
    ("5년 거주 · 10년 전매제한", "오래 살 집으로 보고 넣는다"),
    ("소득·자산 기준은 공고문으로", "공급 유형마다 다르다 · 청약홈 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">광교 지분적립형</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">집값 4분의 1로<br>광교 새 아파트</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">월요일(11/9)부터 청약 시작</span><br>
    <span style="white-space:nowrap">나머지는 어떻게 내는 걸까?</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">5장으로 정리했어요</div>
</div>""" + foot()

insta["02-how"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"4분의 1만 내면 끝이에요?"</div>
    <div class="a gtx">아니요, 20년에 나눠 사요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    처음엔 집값의 <b>25%</b>만 내고 들어가 살아요.
    나머지 <b>75%</b>는 20년 동안 조금씩 사고,
    그동안 공공 몫에는 <b>임대료</b>를 내요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">언제 넣어요?</h1>
  <div style="font-size:27px;color:var(--mute)">청약홈에서 접수해요</div>
  <div class="tl">""" + tlrows([
    ("11월 9일", "특별공급", "청년·신생아·신혼부부"),
    ("11월 10일", "1순위", "11일은 2순위"),
    ("11월 18일", "당첨 발표", "계약은 내년 1월 말"),
], pad=18) + """</div>
</div>""" + foot()

insta["04-budget"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">처음에 필요한 돈 (59㎡ 가장 비싼 집)</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">1억7천만원</div>
  <div class="bigcap">6억8,590만원짜리 집의 4분의 1</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    같은 단지 84㎡ 일반 분양은 <b style="white-space:nowrap">최고 9억4,930만원</b>이에요.
    임대보증금은 따로 있어요.</div>
</div>""" + foot()

insta["05-who"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"누가 유리해요?"</div>
    <div class="a gtx">10채 중 7채가 특공이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    240채 중 <b>168채</b>가 특별공급이에요.
    미혼 청년(19~39세) 몫 <b>36채</b>가 새로 생겼고,
    아기 낳은 집 몫이 <b>48채</b>예요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">넣기 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("매달 나갈 임대료를 계산해요", "공고문 납부 표에 나와요"),
    ("5년은 꼭 살아야 해요", "10년 동안 팔 수도 없어요"),
    ("소득·재산 기준을 확인해요", "청약홈 공고문에서 봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
