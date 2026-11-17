# -*- coding: utf-8 -*-
"""2026-11-18 #129 리모델링 동의율 70%. 수치는 gen129.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "rmd"
DATEK = "2026-11-18"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">주택법 시행령 개정 · 11월 17일 국무회의</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">리모델링 동의율<br>75% → 70%</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    내년 <span class="gtx">1월 1일</span> 허가 신청부터<br>
    동별 50% 요건은 그대로</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">얼마나 · 언제 · 몇 명 · 같이 바뀐 것 · 체크</div>
</div>""" + foot()

cards["02-rate"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1,000가구면 50명 덜 받는다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">1,000가구 단지가 받아야 하는 동의 · 명</div>
""" + hb("지금 (75%)", "750명", 100, inside=True) + hb("내년 1월부터 (70%)", "700명", 93.3, hi=True, inside=True) + """
  <div class="note" style="margin-top:18px">※ 구분소유자 수와 의결권 두 기준에 각각 적용</div>
  <div class="note" style="margin-top:8px">※ 단지 전체 리모델링의 동별 50% 이상 요건은 유지</div>
</div>""" + foot()

cards["03-when"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">허가 신청일이 기준이다</h1>
  <div style="font-size:27px;color:var(--mute)">주택법 시행령 개정, 언제부터</div>
  <div class="tl">""" + tlrows([
    ("11월 17일", "국무회의 의결", "주택법 시행령 일부개정령안"),
    ("공포 즉시", "군인 거주의무 · 지주택 혼인", "공포일은 관보로 확인"),
    ("2027.1.1", "동의율 70% · 검토기관 추가", "이날 이후 허가 신청분부터"),
], pad=18) + """</div>
</div>""" + foot()

cards["04-size"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">우리 단지는 몇 명 덜?</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">단지 규모별 줄어드는 동의 수 · 명 (5%p)</div>
""" + hb("500가구", "25명", 25) + hb("1,000가구", "50명", 50, hi=True) + hb("2,000가구", "100명", 100, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 가구 수 × 5%p 단순 계산 · 실제는 구분소유자 수 기준</div>
</div>""" + foot()

cards["05-more"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">같이 바뀐 3가지</h1>
  <div style="font-size:27px;color:var(--mute)">이번 주택법 시행령 개정에 함께 담긴 것</div>
  <div class="tl">""" + tlrows([
    ("수직증축", "검토기관 2곳 → 3곳", "한국부동산원 추가"),
    ("군인", "분상제 거주의무 예외", "10년 이상 장기복무, 지역 제한 없이"),
    ("지주택", "조합원끼리 결혼해도", "부부 모두 조합원 자격 유지"),
], pad=18) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">리모델링 단지, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("허가 신청 시점", "2027년 1월 1일 이후 신청분부터 70%"),
    ("동별 50%는 그대로", "한 동이라도 반이 안 되면 단지 전체는 어렵다"),
    ("조합 공지로 확인", "우리 단지 동의율 현황은 조합·구청에서"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">아파트 리모델링</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">찬성 문턱이<br>낮아져요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">100명 중 75명 → 70명</span><br>
    <span style="white-space:nowrap">내년 1월부터</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">얼마나 · 언제 · 우리 단지 · 같이 바뀐 것</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"뭐가 바뀐 거예요?"</div>
    <div class="a gtx">찬성이 100명 중 70명이면 돼요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지금은 <b>75명</b>이 찬성해야 리모델링 허가를 신청할 수 있어요.
    내년부터는 <b>70명</b>이에요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"언제부터예요?"</div>
    <div class="a gtx">2027년 1월 1일 신청부터요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그 전에 신청하면 예전 기준(75명)이에요.
    11월 17일 국무회의를 통과했어요.</div>
</div>""" + foot()

insta["04-ours"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">1,000집 단지라면</div>
  <div class="bignum gtx" style="margin-top:10px">50명</div>
  <div class="bigcap">찬성을 이만큼 덜 받아도 돼요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    750명에서 <b>700명</b>으로 줄어요.
    다만 동마다 <b>절반 이상</b> 찬성은
    그대로 있어야 해요.</div>
</div>""" + foot()

insta["05-also"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"다른 것도 바뀌었어요?"</div>
    <div class="a gtx">조합원끼리 결혼해도 둘 다 자격이 남아요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지역주택조합 이야기예요.
    오래 복무한 <b>군인</b>은 발령으로 이사해도
    거주한 걸로 쳐 줘요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">리모델링 단지 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("찬성률 먼저 묻기", "지금 몇 % 모였는지 조합에 물어봐요"),
    ("동마다 반 넘었나", "한 동이라도 모자라면 어려워요"),
    ("신청 날짜 보기", "내년 1월 이후 신청이어야 70%예요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
