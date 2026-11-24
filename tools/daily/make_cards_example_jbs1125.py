# -*- coding: utf-8 -*-
"""2026-11-25 #137 종부세 비거주 1주택 공제. 수치는 gen_example_137.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "jbs"
DATEK = "2026-11-25"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">11월 23일 부총리 · 이번 주 조세소위</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">종부세 비거주 1주택,<br>14억은 아직</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    <span style="white-space:nowrap">실거주 14억 · 비거주 12억</span><br>
    <span style="white-space:nowrap">정부는 차등 유지</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">공제 · 일정 · 예시 · 같이 바뀌는 것 · 체크</div>
</div>""" + foot()

cards["02-deduct"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공제, 지금 나온 숫자 셋</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">1주택 종부세 기본공제 · 공시가격 기준</div>
""" + hb("실거주 (정부안)", "14억", 100, hi=True, inside=True) + hb("비거주 (정부안 · 지금과 같음)", "12억", 85.7, inside=True) + hb("비거주 (8월 원안 · 철회)", "9억", 64.3, inside=True) + """
  <div class="note" style="margin-top:18px">※ 여당은 거주 상관없이 14억 통일 요구</div>
</div>""" + foot()

cards["03-when"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">언제 정해지나</h1>
  <div style="font-size:27px;color:var(--mute)">종부세 개편 일정</div>
  <div class="tl">""" + tlrows([
    ("8월 3일", "세제개편안 발표", "실거주 14억 · 비거주 9억"),
    ("9월 1일", "정부 수정", "비거주 12억 유지로 되돌림"),
    ("11월 23일", "부총리 차등 유지", "예외 사유는 시행령에서"),
    ("이번 주", "국회 조세소위", "세법개정안 심의 시작"),
], pad=14) + """</div>
</div>""" + foot()

cards["04-example"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공시가 16억이면</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">과세표준 예시 · 비율 70% 가정</div>
""" + hb("공제 12억 (비거주)", "2억8천만", 100, inside=True) + hb("공제 14억 (실거주)", "1억4천만", 50, hi=True) + """
  <div class="duo"><div class="box"><div class="dl">공제 2억 차이</div><div class="dv gtx">2배</div></div>
    <div class="box"><div class="dl">철회된 9억 안</div><div class="dv">4억9천만</div></div></div>
  <div class="note" style="margin-top:14px">※ (공시가 − 공제) × 70%. 세액은 사람마다 달라 뺐음</div>
</div>""" + foot()

cards["05-also"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공제 말고 같이 바뀌는 것</h1>
  <div style="font-size:27px;color:var(--mute)">정부안 · 국회에서 바뀔 수 있음</div>
  <div class="tl">""" + tlrows([
    ("70%", "공정시장가액비율", "1주택, 지금 60%에서 인상"),
    ("150%", "세부담 상한 유지", "200% 인상안은 9월 철회"),
    ("600만", "세액공제 한도", "2027년 800만 → 2028년 600만"),
    ("2028년", "보유 공제 폐지", "산 기간 기준으로 바꿈"),
], pad=14) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">비거주 1주택, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("공제액은 국회 결론 뒤", "정부 12억 차등 vs 여당 14억 통일"),
    ("예외 사유는 시행령", "부득이한 비거주 인정 범위 미정"),
    ("올해 고지서는 현행법", "공제 12억 · 납부 12월 1~15일"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 세무 자문이 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">종부세 비거주 1주택</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">집 비워 두면,<br>공제가 달라요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">살면 14억, 안 살면 12억</span><br>
    <span style="white-space:nowrap">아직 국회에서 정하는 중</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">얼마 · 언제 · 내 집이면 · 올해 · 볼 것</div>
</div>""" + foot()

insta["02-who"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"저도 비거주예요?"</div>
    <div class="a gtx">집 한 채를 두고 딴 데 살면요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지방 발령, 아이 학교, 부모님 돌봄으로 집을 비운 경우가 다 들어가요.
    정부는 피치 못할 사정은 따로 봐주겠다고 했어요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"언제 정해져요?"</div>
    <div class="a gtx">이번 주 국회에서 시작해요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    정부는 <b>살면 14억, 안 살면 12억</b>.
    여당은 <b>다 14억</b>으로 맞추자고 해요. 보통 연말에 결론이 나요.</div>
</div>""" + foot()

insta["04-mine"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">공시가 16억 집이라면, 세금 매기는 금액</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:112px">2배</div>
  <div class="bigcap">안 살면 <span style="white-space:nowrap">2억8천만</span> · 살면 <span style="white-space:nowrap">1억4천만</span></div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    빼 주는 금액이 2억 차이라 그래요.
    실제 세금은 나이·보유 기간마다 달라요.</div>
</div>""" + foot()

insta["05-thisyear"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"올해 고지서도 바뀌어요?"</div>
    <div class="a gtx">아니요, 올해는 그대로예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    올해는 지금 법대로 <b>12억</b>을 빼고 매겨요.
    내는 기간은 <b>12월 1일부터 15일</b>까지예요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 비워 두기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("14억은 아직 결정 전", "연말 국회 결과를 보세요"),
    ("내 사정이 예외인지", "나중에 나올 기준을 확인해요"),
    ("올해 고지서", "집값·한 채 여부가 맞는지 봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
