# -*- coding: utf-8 -*-
"""2026-10-19 목동10단지 재건축 현대건설 선정. 수치는 gen98.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "mkd1019"
DATEK = "2026-10-19"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">10월 18일 토지등소유자 전체회의</div>
  <h1 class="serif gtx" style="font-size:78px;margin:14px 0 28px;line-height:1.2">목동10단지 재건축<br>현대건설 확정</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    단독 입찰에 <span class="gtx">95.9% 찬성</span><br>
    최고 40층 4,248가구 · 디에이치 목동 에세르</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">표결 · 규모 · 공사비 · 다음 일정</div>
</div>""" + foot()

cards["02-vote"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">투표한 100명 중 96명이 찬성</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">시공자 선정 안건 · 명</div>
""" + hb("사업시행자 지정 동의자", "1,960명", 100, inside=True) + hb("투표 (현장·온라인·서면)", "1,624명", 82.9, inside=True) \
    + hb("현대건설 찬성", "1,557명 · 95.9%", 79.4, hi=True, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">1차 현설</div><div class="dv">6개사</div><div class="ds">입찰은 현대건설만</div></div>
    <div class="box"><div class="dl">유찰</div><div class="dv">2회</div><div class="ds">우선협상 뒤 확정</div></div>
  </div>
</div>""" + foot()

cards["03-scale"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">2,160가구 · 최고 15층에서</div>
  <div class="bignum gtx" style="margin-top:10px">4,248가구</div>
  <div class="bigcap">최고 40층 · 지금의 약 1.97배</div>
  <div class="duo">
    <div class="box"><div class="dl">예정공사비</div><div class="dv">2조6,135억</div><div class="ds">가구당 단순 계산 약 6억1,500만원</div></div>
    <div class="box"><div class="dl">늘어나는 집</div><div class="dv">+2,088</div><div class="ds">신정동 311 일대</div></div>
  </div>
  <div class="note" style="margin-top:18px">※ 통합심의 전 계획 · 가구수·층수는 바뀔 수 있음 · 가구당 금액은 분담금 아님</div>
</div>""" + foot()

cards["04-cost"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공사비는 거의 같은 선</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">목동 3.3㎡당 예정공사비 · 만원</div>
""" + hb("4단지 (입찰 중)", "1,010", 100, inside=True) + hb("10단지 현대건설", "990", 98, hi=True, inside=True) \
    + hb("12단지 GS건설", "980", 97, inside=True) + hb("13단지 삼성물산", "980", 97, inside=True) \
    + hb("8단지 대우건설", "965", 95.5, inside=True) + """
  <div class="note" style="margin-top:14px">※ 차이는 조건에서: 공사비 인상분 12개월 현대 부담 · 이주비 LTV 100% 제안</div>
</div>""" + foot()

cards["05-next"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동 다음 선정은 11월</h1>
  <div style="font-size:27px;color:var(--mute)">시공사 선정 일정 · 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("6월 · 10월", "6단지 DL이앤씨 · 10단지 현대건설", "선정 완료"),
    ("10월 말", "13단지 삼성물산 홍보관", "제안명 래미안 모브13"),
    ("11월", "12단지 GS · 13단지 삼성 총회", "4단지 입찰 마감 16일 · 7단지 입찰공고"),
    ("12월 중순", "8단지 대우건설 총회", "목표 일정"),
], pad=16) + """</div>
  <div class="note" style="margin-top:12px">※ 11~12월은 보도된 목표 · 각 단지 공고로 확인</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">목동10단지, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("확정된 것은 시공사", "4,248가구·40층은 통합심의 전 계획"),
    ("이주비 LTV 100%는 제안", "본계약 조건과 대출 규제로 판단"),
    ("거래 전 지위 양도 확인", "양천구청 · 정비사업 정보몽땅"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">목동10단지 재건축</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">누가 짓나,<br>어제 정해졌어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    현대건설 · 투표한 100명 중 96명 찬성<br>
    <span style="white-space:nowrap">새 이름은 디에이치 목동 에세르</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">목동 다른 단지 일정까지 · 5장으로</div>
</div>""" + foot()

insta["02-vote"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"경쟁은 있었어요?"</div>
    <div class="a gtx">아니요, 한 곳만 들어왔어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    건설사 6곳이 설명회에 왔지만 입찰은 <b>현대건설 한 곳</b>뿐이었어요.
    그래도 투표한 <b>100명 중 96명</b>이 찬성했어요.</div>
</div>""" + foot()

insta["03-bigger"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">지금 2,160집 · 15층에서</div>
  <div class="bignum gtx" style="margin-top:10px">4,248집</div>
  <div class="bigcap">최고 40층 · 집이 두 배 가까이 늘어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    아직 <b>계획</b>이에요. 서울시 심의를 거치면서 숫자가 바뀔 수 있어요.</div>
</div>""" + foot()

insta["04-offer"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"현대건설은 뭘 약속했어요?"</div>
    <div class="a gtx">1년 동안 오르는 공사비는 현대가 낸대요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    이사 갈 때 빌려주는 돈(이주비)도 <b>집 감정값의 100%까지</b> 주겠다고 했어요.
    다만 <b>제안</b>이라 실제 계약과 대출 규정을 봐야 해요.</div>
</div>""" + foot()

insta["05-next"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동 다른 단지는요?</h1>
  <div style="font-size:27px;color:var(--mute)">누가 지을지 정하는 날</div>
  <div class="tl">""" + tlrows([
    ("끝", "6단지 DL이앤씨 · 10단지 현대", "올해 6월 · 어제"),
    ("11월", "12단지 GS · 13단지 삼성", "투표 목표"),
    ("11월", "4단지 · 7단지", "건설사 신청 받는 중 · 곧 공고"),
    ("12월", "8단지 대우건설", "투표 목표"),
], pad=16) + """</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">목동 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("정해진 건 건설사뿐", "층수·집 수는 아직 바뀔 수 있어요"),
    ("이주비 100%는 약속 단계", "실제 금액은 계약 때 확인"),
    ("사고팔 땐 구청에 먼저", "새 집 받을 권리가 넘어오는지"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요 · 11월 결과도 알려 드릴게요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
