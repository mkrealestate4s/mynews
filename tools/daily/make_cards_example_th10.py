# -*- coding: utf-8 -*-
"""2026-11-14 #125 서울 토지거래허가 신청 10월. 수치는 gen125.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "th10"
DATEK = "2026-11-14"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">서울 아파트 10월 집계</div>
  <h1 class="serif gtx" style="font-size:68px;margin:14px 0 28px;line-height:1.2">토지거래허가 신청<br>두 달째 늘었다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    10월 <span class="gtx">3,947건</span> · 전월보다 8.2%↑<br>
    그런데 강남은 신청가 내렸다</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 건수 · 가격 · 비중 · 체크</div>
</div>""" + foot()

cards["02-when"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">지정 1년, 12월 31일 끝</h1>
  <div style="font-size:27px;color:var(--mute)">서울 아파트 토지거래허가 일정</div>
  <div class="tl">""" + tlrows([
    ("2025.10.20", "서울 전역 지정", "25개구 아파트가 허가 대상"),
    ("10월 말까지", "누적 신청 63,447건", "지정 뒤 약 1년 동안"),
    ("11월 13일", "10월 집계 발표", "3,947건, 두 달 연속 증가"),
    ("12월 31일", "지정 기간 끝", "연장 여부는 아직 발표 전"),
], pad=16) + """</div>
</div>""" + foot()

cards["03-count"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">신청 증가, 강남3구·용산 1위</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">10월 신청 건수 증가율 · 전월 대비 %</div>
""" + hb("강남3구·용산", "20.6%", 100, hi=True, inside=True) + hb("한강벨트 7개구", "9.7%", 47.1) \
    + hb("서남권 4개구", "9.5%", 46.1) + hb("서울 전체", "8.2%", 39.8) + """
  <div class="note" style="margin-top:14px">※ 한강벨트 784→860건 · 서남권 708→775건 · 서울시 발표</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">가격은 강남만 내렸다</h1>
  <div style="font-size:27px;color:var(--mute)">10월 신청가격 변동 · 전월 대비</div>
  <div class="tl">""" + tlrows([
    ("−0.92%", "강남3구·용산", "9월 −0.41%에서 하락폭 확대"),
    ("+1.04%", "한강벨트 7개구", "오름폭 확대"),
    ("+0.89%", "서남권 4개구", "오름세 둔화"),
    ("+0.52%", "강북권", "오름세 둔화"),
], pad=16) + """</div>
  <div class="note" style="margin-top:10px">※ 신청서에 적힌 가격 · 실거래가와 다름</div>
</div>""" + foot()

cards["05-share"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">강남3구·용산 비중, 석 달째↑</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">서울 전체 신청 중 강남3구·용산 비중 · %</div>
""" + hb("8월", "11.9%", 73.5, inside=True) + hb("9월", "14.5%", 89.5, inside=True) \
    + hb("10월", "16.2%", 100, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 가격이 내린 곳에서 신청이 늘었다 · 서울시 발표</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">토지거래허가, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("12월 31일 연장 발표", "연장·조정 여부는 국토부·서울시 발표로 확인"),
    ("신청가격은 실거래가가 아니다", "시세는 실거래가 공개시스템에서 확인"),
    ("실거주 조건은 구청 확인", "입주 기한·예외는 사람·주택마다 다르다"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">서울 토지거래허가 신청</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">사겠다는 사람<br>다시 늘었어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">10월 3,947건, 두 달째 증가</span><br>
    <span style="white-space:nowrap">강남은 값을 낮춰 적었어요</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">뭔데 · 얼마나 · 어디 · 언제까지</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"토지거래허가 신청이 뭐예요?"</div>
    <div class="a gtx">서울에서 아파트 사려면 구청 허락부터 받아요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    작년 10월 20일부터 서울 <b>25개구 전부</b>가 그래요.
    그래서 신청 건수를 보면 <b>사려는 사람이 얼마나 되는지</b> 보여요.</div>
</div>""" + foot()

insta["03-howmany"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">10월 서울 아파트 신청</div>
  <div class="bignum gtx" style="margin-top:10px">3,947건</div>
  <div class="bigcap">9월보다 100건 중 8건꼴로 늘었어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    8월 2,939건이 바닥이었어요.
    그래도 가장 많던 4월(8,886건)의 <b>절반이 안 돼요</b>.</div>
</div>""" + foot()

insta["04-where"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"어디가 제일 늘었어요?"</div>
    <div class="a gtx">강남3구·용산이요. 그런데 값은 내렸어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    신청은 <b>20.6%</b> 늘었는데, 적어 낸 값은 <b>0.92%</b> 낮아졌어요.
    한강변 7개구는 <b>1.04%</b> 올랐고요.</div>
</div>""" + foot()

insta["05-until"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">지금 규칙이 끝나는 날</div>
  <div class="bignum gtx" style="margin-top:10px">12월 31일</div>
  <div class="bigcap">늘릴지 말지는 아직 안 정해졌어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    정부는 10월에 <b>"시장 보며 검토"</b>라고만 했어요.
    발표가 나오면 바로 정리해 드릴게요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">서울 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("연말 발표 챙기기", "12월 31일 뒤 규칙이 바뀔 수 있어요"),
    ("적어 낸 값 ≠ 팔린 값", "실제로 팔린 값은 실거래가로 봐요"),
    ("들어가 살아야 하는지", "조건은 구청 담당자에게 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
