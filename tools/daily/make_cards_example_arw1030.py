# -*- coding: utf-8 -*-
"""2026-10-30 청라 아크원 푸르지오 견본주택 개관일. 수치는 gen109 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "arw1030"
DATEK = "2026-10-30"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">청라국제업무단지 · 아파트 868가구</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">청라 아크원 푸르지오<br>오늘 견본주택</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    10월 30일(금) 개관 · 분양가상한제<br>
    <span class="gtx" style="white-space:nowrap">특공 11월 2일, 1순위 3일</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">공급 · 일정 · 분양가 · 계약금 · 체크</div>
</div>""" + foot()

cards["02-supply"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">868가구 중 일반공급은 354</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:28px">아파트 공급 구성 · 가구</div>
""" + hb("특별공급", "514", 59.2, inside=True) + hb("일반공급", "354", 40.8, hi=True, inside=True) + """
  <div class="bignum gtx" style="font-size:110px;margin-top:22px">620가구</div>
  <div class="bigcap">84㎡가 대부분 (103㎡는 248가구)</div>
</div>""" + foot()

cards["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">특공 11월 2일, 당첨 11월 10일</h1>
  <div style="font-size:27px;color:var(--mute)">청라 아크원 푸르지오 일정</div>
  <div class="tl">""" + tlrows([
    ("10월 30일", "견본주택 개관", "오늘"),
    ("11월 2일", "특별공급", "월요일"),
    ("11월 3일", "1순위", "화요일"),
    ("11월 10일", "당첨자 발표", "계약 11월 22~24일"),
], pad=14) + """</div>
  <div class="note" style="margin-top:12px">※ 2순위·세부 시간은 청약홈 입주자모집공고</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡ 8억3,780만~9억2,070만</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">주택형별 분양가 범위</div>
""" + hb("103㎡ 최고", "11억7,100만", 100, inside=True) + hb("103㎡ 최저", "10억8,880만", 93.0, inside=True) \
    + hb("84㎡ 최고", "9억2,070만", 78.6, hi=True, inside=True) + hb("84㎡ 최저", "8억3,780만", 71.5, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 하한은 자료마다 차이 · 동·호수별 금액은 공고문</div>
</div>""" + foot()

cards["05-cash"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">계약금 5%, 인천 50% 우선</h1>
  <div style="font-size:27px;color:var(--mute)">돈과 자격, 먼저 볼 것</div>
  <div class="tl">""" + tlrows([
    ("계약금 5%", "84㎡ 약 4,189만~4,604만원", "분양가 범위 × 5% 계산"),
    ("중도금 60%", "대출 조건은 공고문", "보도 기준 비율"),
    ("지역 50%", "인천 거주자 우선", "서울·경기도 청약 가능"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 전매제한·실거주 의무 기간은 공고문 확인</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">청약 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("특공 자격과 통장", "특공 11월 2일 · 1순위 3일"),
    ("동·호수별 분양가표", "84㎡도 8천만원 넘게 차이"),
    ("전매제한·실거주 의무", "분양가상한제 단지 · 공고문 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">청라 아크원 푸르지오</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">청라 새 아파트<br>오늘 모델하우스</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    10월 30일(금) 문 열어요<br>
    <span style="white-space:nowrap">아파트 868가구</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">자리 · 날짜 · 가격 · 5장으로</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"통장 점수로 겨루는 집은 몇 채?"</div>
    <div class="a gtx">100채 중 41채예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    나머지 59채는 <b>신혼부부·첫 집·다자녀</b> 같은
    특별공급 몫이에요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">남은 날짜</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("10월 30일", "모델하우스", "오늘부터 주말까지"),
    ("11월 2~3일", "청약 신청", "2일 특별 · 3일 일반"),
    ("11월 10일", "결과 발표", "계약은 22~24일"),
], pad=18) + """</div>
</div>""" + foot()

insta["04-budget"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">34평쯤(84㎡) 가격</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">8억~9억대</div>
  <div class="bigcap">층과 방향 따라 8천만원 넘게 달라요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    42평쯤(103㎡)은 <b>10억~11억대</b>예요.
    정확한 값은 모집공고에서 확인하세요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"처음에 얼마 있어야 해요?"</div>
    <div class="a gtx">34평이면 4천만원대예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    계약금이 집값의 <b>5%</b>예요.
    절반은 인천에 사는 사람에게 먼저 돌아가요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">모델하우스 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 청약 자격", "청약홈에서 통장 확인"),
    ("원하는 동 가격표", "현장에서 먼저 받기"),
    ("되팔기·실거주 조건", "모집공고에서 기간 확인"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
