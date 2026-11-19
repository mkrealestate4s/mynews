# -*- coding: utf-8 -*-
"""2026-11-20 #131 하안주공5단지 재건축 시공사 한화. 수치는 gen131.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "hah"
DATEK = "2026-11-20"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">광명 하안주공 재건축 · 11월 18일 시공사 선정총회</div>
  <h1 class="serif gtx" style="font-size:70px;margin:14px 0 28px;line-height:1.2">하안주공5단지,<br>시공사는 한화</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    공사비 <span class="gtx" style="white-space:nowrap">1조698억</span><br>
    하안주공 <span style="white-space:nowrap">12개 단지 중 처음</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">규모 · 비교 · 수주 · 남은 단계 · 체크</div>
</div>""" + foot()

cards["02-size"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">숫자 셋으로 보면</h1>
  <div style="font-size:27px;color:var(--mute)">하안주공5단지 재건축 계획 (보도 기준)</div>
  <div class="tl">""" + tlrows([
    ("1조698억", "공사비", "본계약에서 바뀔 수 있다"),
    ("2,886가구", "계획 가구", "일부 보도 2,885 · 인가에서 바뀐다"),
    ("45층", "최고 층수", "지하 5층~지상 45층 계획"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 사업시행자 한국자산신탁 · 신탁 방식</div>
</div>""" + foot()

cards["03-cost"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">올해 대어 셋 중 하나</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">올해 시공사를 정한 재건축 공사비 · 억원</div>
""" + hb("압구정3구역 · 현대건설", "5조5,610", 100, inside=True) + hb("목동10단지 · 현대건설", "2조6,136", 47.0, inside=True) + hb("하안주공5단지 · 한화", "1조698", 19.2, hi=True) + """
  <div class="note" style="margin-top:14px">※ 보도·공시 금액 · 본계약에서 바뀔 수 있음</div>
</div>""" + foot()

cards["04-share"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">한화 건설부문 올해 정비사업 수주 2조5,264억 중</div>
  <div class="bignum gtx" style="margin-top:10px">42%</div>
  <div class="bigcap">하안주공5단지 한 곳에서 나왔다</div>
  <div style="margin-top:30px">""" + hb("올해 누적", "2조5,264억", 100, inside=True) + hb("하안주공5단지", "1조698억", 42.3, hi=True, inside=True) + """</div>
  <div class="note" style="margin-top:10px">※ 회사 발표 기준 · 지난해의 3배 이상</div>
</div>""" + foot()

cards["05-next"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">착공은 아직이다</h1>
  <div style="font-size:27px;color:var(--mute)">하안주공 재건축 남은 단계 (2025년 보도 계획)</div>
  <div class="tl">""" + tlrows([
    ("2027년", "사업시행인가", "설계·가구수가 여기서 굳는다"),
    ("2028년", "관리처분인가", "분담금이 숫자로 나온다"),
    ("2030년", "착공", "하안주공 전체 계획 · 5단지 확정 아님"),
], pad=18) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">하안주공 소유자, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("본계약 공사비", "3.3㎡당 단가·물가 반영 조건"),
    ("계획 가구수는 확정 전", "2,886가구·45층은 인가에서 바뀐다"),
    ("다음 단계 일정", "사업시행자 공지·광명시 고시로"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">광명 하안주공 재건축</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">5단지, 지을<br>회사가 정해졌다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">한화 건설부문</span><br>
    <span style="white-space:nowrap">11월 18일 선정</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">크기 · 돈 · 남은 일 · 볼 것</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마나 크게 지어요?"</div>
    <div class="a gtx">45층, 2,886집 계획이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    아직 <b>계획</b>이에요.
    허가 받는 과정에서 숫자가 바뀔 수 있어요.</div>
</div>""" + foot()

insta["03-money"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">짓는 데 드는 돈 (공사비)</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">1조698억</div>
  <div class="bigcap">하안주공 12곳 중 처음 정해졌어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    올해 입찰에 <b>아무도 안 들어온 적</b>이 여러 번 있었어요.
    이번에 겨우 정해진 거예요.</div>
</div>""" + foot()

insta["04-first"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"분양가도 나왔어요?"</div>
    <div class="a gtx">아니요. 공사비는 분양가가 아니에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    집주인이 낼 돈(분담금)은
    <b>몇 년 뒤</b> 계획이 굳어야 나와요.</div>
</div>""" + foot()

insta["05-when"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">공사 시작은 언제?</div>
  <div class="bignum gtx" style="margin-top:10px">2030년</div>
  <div class="bigcap">하안주공 전체 계획 기준이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    작년에 나온 계획이라 <b>밀릴 수 있어요.</b>
    5단지만의 확정 날짜는 아니에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">하안동 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("몇 단지인지", "5단지만 회사가 정해졌어요"),
    ("숫자는 계획", "집 수·층수는 바뀔 수 있어요"),
    ("사고팔 조건", "광명시·사업시행자에 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
