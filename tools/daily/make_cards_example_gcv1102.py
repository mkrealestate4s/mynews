# -*- coding: utf-8 -*-
"""2026-11-02 계양 카이브 유보라 특공 접수일. 수치는 gen113 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "gcv1102"
DATEK = "2026-11-02"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">계양신도시 첫 민간분양 · 1,110가구</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">계양 카이브 유보라<br>오늘 특별공급</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    11월 2일(월) 특공 · 분양가상한제<br>
    <span class="gtx" style="white-space:nowrap">1순위 내일 11월 3일</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">공급 · 일정 · 분양가 · 자격 · 체크</div>
</div>""" + foot()

cards["02-supply"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1,110가구 중 일반공급은 472</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:28px">공급 구성 · 가구</div>
""" + hb("특별공급", "638", 57.5, inside=True) + hb("일반공급", "472", 42.5, hi=True, inside=True) + """
  <div class="bignum gtx" style="font-size:110px;margin-top:22px">2개 블록</div>
  <div class="bigcap">AC3 614가구 · AC4 496가구</div>
</div>""" + foot()

cards["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">특공 11월 2일, 1순위 3일</h1>
  <div style="font-size:27px;color:var(--mute)">계양 카이브 유보라 일정</div>
  <div class="tl">""" + tlrows([
    ("11월 2일", "특별공급", "오늘"),
    ("11월 3일", "1순위", "4일 2순위"),
    ("11월 10~11일", "당첨자 발표", "AC3 10일 · AC4 11일"),
    ("11월 23~25일", "계약", "입주 2029년 8월 예정"),
], pad=14) + """</div>
  <div class="note" style="margin-top:12px">※ 세부 시간은 청약홈 입주자모집공고</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡ 7억3,100만~8억1,850만</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">분양가 범위 · 3.3㎡당 2,400만원 선</div>
""" + hb("정리 자료 최고", "9억1,200만", 100, inside=True) \
    + hb("84㎡ 최고", "8억1,850만", 89.7, hi=True, inside=True) + hb("84㎡ 최저", "7억3,100만", 80.2, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 자료마다 범위 차이 · 동·호수별 금액은 공고문</div>
</div>""" + foot()

cards["05-rule"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">수도권 누구나 1순위, 계약금 5%</h1>
  <div style="font-size:27px;color:var(--mute)">자격과 돈, 먼저 볼 것</div>
  <div class="tl">""" + tlrows([
    ("1순위", "수도권 거주 만 19세 이상", "비규제지역 · 통장 요건 충족 시"),
    ("계약금 5%", "84㎡ 약 3,660만~4,090만원", "분양가 범위 × 5% 계산"),
    ("중복 청약", "두 블록 발표일이 달라 가능", "보도 기준 · 유형별 공고문 확인"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 전매제한·실거주 의무 기간은 공고문 확인</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">청약 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("AC3·AC4 중복 청약", "내 유형도 되는지 공고문 확인"),
    ("동·호수별 분양가표", "84㎡도 8천만원 넘게 차이"),
    ("전매제한·실거주 의무", "분양가상한제 단지 · 공고문 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">계양 카이브 유보라</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">계양신도시 새 아파트<br>오늘 청약 시작</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    11월 2일(월) 특별공급부터<br>
    <span style="white-space:nowrap">1,110가구</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 채 · 날짜 · 가격 · 5장으로</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"통장 점수로 겨루는 집은 몇 채?"</div>
    <div class="a gtx">100채 중 43채예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    나머지 57채는 <b>신혼부부·첫 집·다자녀</b> 같은
    특별공급 몫이에요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">남은 날짜</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("11월 2~4일", "청약 신청", "2일 특별 · 3일 1순위 · 4일 2순위"),
    ("11월 10~11일", "결과 발표", "두 단지가 하루씩 달라요"),
    ("11월 23~25일", "계약", "입주는 2029년 8월 예정"),
], pad=18) + """</div>
</div>""" + foot()

insta["04-budget"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">34평쯤(84㎡) 가격</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">7억~8억대</div>
  <div class="bigcap">층과 방향 따라 8천만원 넘게 달라요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    조금 더 넓은 집(92·93㎡)은 <b>9억 초반</b>까지예요.
    정확한 값은 모집공고에서 확인하세요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"서울 살아도 넣을 수 있어요?"</div>
    <div class="a gtx">수도권이면 1순위 가능해요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    계약금은 집값의 <b>5%</b>, 34평이면
    <b style="white-space:nowrap">4천만원 안팎</b>이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">청약 넣기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 청약 자격", "청약홈에서 통장 확인"),
    ("두 단지 같이 넣기", "되는지 모집공고로 확인"),
    ("되팔기·실거주 조건", "모집공고에서 기간 확인"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
