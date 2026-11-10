# -*- coding: utf-8 -*-
"""2026-11-11 #122 은마아파트 재초환. 수치는 gen122.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "emj"
DATEK = "2026-11-11"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">대치동 은마 · 재건축부담금 예정액</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">은마아파트<br>재초환 4.6억</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    조합원 1인당 <span class="gtx">평균 예정액</span><br>
    확정은 준공 뒤 다시 계산</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">비교 · 순서 · 부과율 · 감면 · 체크</div>
</div>""" + foot()

cards["02-compare"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">은마, 서울 평균의 약 4배</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">조합원 1인당 재초환 · 억원</div>
""" + hb("한강맨션 (9월 추정)", "6.8", 100, inside=True) + hb("은마 (11월 예정액)", "4.63", 68.1, hi=True, inside=True) \
    + hb("반포3주구 (9월 추정)", "3.2", 47.1, inside=True) + hb("서울 평균 (9월 추정)", "1.22", 17.9) + """
  <div class="note" style="margin-top:14px">※ 은마 46,334만원 ÷ 서울 평균 12,174만원 = 약 3.8배 · 산정 시점 다름</div>
</div>""" + foot()

cards["03-stage"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">지금은 예정액, 확정은 준공 뒤</h1>
  <div style="font-size:27px;color:var(--mute)">은마 재초환이 정해지는 순서</div>
  <div class="tl">""" + tlrows([
    ("2026. 7", "사업시행계획 인가", "7월 2일 강남구 인가"),
    ("2026. 11", "예정액 통지", "1인당 평균 4억6,334만원 · 지금 내는 돈 아님"),
    ("2028 목표", "착공", "조합 목표(보도) · 공사비 따라 금액 변동"),
    ("준공 후", "확정 부과", "실제 집값·공사비로 다시 계산"),
], pad=16) + """</div>
</div>""" + foot()

cards["04-rate"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">넘는 만큼 최대 50%</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">1인당 초과이익 구간별 부과율</div>
""" + hb("8,000만원까지", "면제", 0) + hb("~1억3,000만원", "10%", 20, inside=True) + hb("~1억8,000만원", "20%", 40, inside=True) \
    + hb("~2억3,000만원", "30%", 60, inside=True) + hb("~2억8,000만원", "40%", 80, inside=True) + hb("2억8,000만원 초과", "50%", 100, hi=True, inside=True) + """
  <div class="note" style="margin-top:10px">※ 구간에 걸친 금액에만 매기는 누진 방식 · 2024년 3월 개정법 기준</div>
</div>""" + foot()

cards["05-relief"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">1세대 1주택 20년 이상 보유하면</div>
  <div class="bignum gtx" style="margin-top:10px">70% 감면</div>
  <div class="bigcap">60세 이상은 집을 팔 때까지 납부 유예</div>
  <div class="duo">
    <div class="box"><div class="dl">6년 이상</div><div class="dv">10%</div></div>
    <div class="box"><div class="dl">10년 이상</div><div class="dv gtx">50%</div></div>
  </div>
  <div class="note" style="margin-top:18px">※ 내 해당 여부는 조합·강남구청 확인</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">은마 재초환, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("확정 아닌 예정액", "준공 뒤 실제 집값·공사비로 다시 계산"),
    ("분담금과 별개", "새 집 받으며 내는 분담금과 따로 계산"),
    ("내 감면은 조합·구청 확인", "1주택 장기보유 최대 70% · 60세 이상 유예"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">은마아파트 재초환 · 대치동</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">4억6천만원,<br>지금 내는 돈?</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">아니에요, 아직 예정액</span><br>
    <span style="white-space:nowrap">다 지은 뒤 다시 계산해요</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">무슨 돈 · 얼마 · 깎는 법 · 5장으로</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"재초환이 뭐예요?"</div>
    <div class="a gtx">많이 오른 만큼 내는 돈이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    재건축으로 집값이 오른 것 중에서
    보통 오르는 몫과 공사비를 빼고 <b>남는 이익</b>의 일부를
    나라가 걷어요. 한 사람당 <b>8,000만원</b>까지는 안 내요.</div>
</div>""" + foot()

insta["03-howmuch"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">은마 조합원 한 사람 평균</div>
  <div class="bignum gtx" style="margin-top:10px">4억6,334만</div>
  <div class="bigcap">서울 재건축 평균(1억2천만원)의 약 4배예요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    용산 한강맨션은 <b>6억8천만원</b>쯤으로
    추정됐어요(9월 보도). 강남구가 이번 달
    은마 조합에 알려 준 숫자예요.</div>
</div>""" + foot()

insta["04-notyet"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"그럼 이 돈 그대로 내요?"</div>
    <div class="a gtx">아직 몰라요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지금 숫자는 <b>지금 시세</b>로 미리 계산한 거예요.
    아파트를 <b>다 지은 뒤</b> 그때 집값과
    실제 공사비로 다시 계산해서 고지서가 나와요.</div>
</div>""" + foot()

insta["05-cut"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"오래 산 사람도 똑같이 내요?"</div>
    <div class="a gtx">최대 <span style="white-space:nowrap">70%</span> 깎아 줘요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    집이 한 채뿐이고 <b>20년 넘게</b> 가졌으면 70%,
    10년이면 50%를 깎아 줘요. 60세가 넘었으면
    집을 팔 때까지 <b>미뤄서</b> 낼 수 있어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">은마 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("4.6억은 평균 예정액", "다 지은 뒤 다시 계산해요"),
    ("분담금은 따로예요", "새 집 받을 때 내는 돈과 별개예요"),
    ("감면은 사람마다 달라요", "조합이나 강남구청에 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
