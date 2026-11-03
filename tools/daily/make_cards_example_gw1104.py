# -*- coding: utf-8 -*-
"""2026-11-04 #115 가락우성1차 재건축 2차 현설 대우 단독. 수치는 gen_example_115.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "gw1104"
DATEK = "2026-11-04"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">송파구 가락동 · 시공사 입찰</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">가락우성1차 재건축<br>두 번 다 대우건설 혼자</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    11월 3일 2차 현설도 <span class="gtx">단독</span><br>
    예정 공사비 5,019억 · 계획 967가구</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 공사비 · 쌍문한양1차 · 수의계약 · 체크</div>
</div>""" + foot()

cards["02-sched"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">가락우성1차, 어디까지 왔나</h1>
  <div style="font-size:27px;color:var(--mute)">시공사 선정 진행 · 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("1차 입찰", "유찰", "대우건설 단독 참여"),
    ("11.3", "2차 현장설명회", "어제 · 이번에도 대우건설만"),
    ("조건", "하이엔드 브랜드", "대우는 '써밋' 제안 예정(보도)"),
    ("2027.2월 말", "시공사 선정 총회", "이르면 · 확정 일정 아님"),
], pad=15) + """</div>
</div>""" + foot()

cards["03-cost"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">3.3㎡당 985만원, 목동과 같은 선</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">3.3㎡당 예정공사비 · 만원</div>
""" + hb("목동4단지", "1,010", 100, inside=True) + hb("목동10단지", "990", 98, inside=True) \
    + hb("가락우성1차", "985", 97.5, hi=True, inside=True) + hb("목동9단지", "980", 97, inside=True) \
    + hb("목동8단지", "965", 95.5, inside=True) + """
  <div class="note" style="margin-top:12px">※ 공사비가 낮아서 안 온 것은 아니다 · 보도 기준</div>
</div>""" + foot()

cards["04-ssang"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">쌍문한양1차도 DL이앤씨 혼자</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">재건축 후 계획 세대수 · 확정 전</div>
""" + hb("쌍문한양1차 · 도봉 · 최고 38층", "1,166", 100, hi=True, inside=True) + hb("가락우성1차 · 송파", "967", 82.9, inside=True) + """
  <div class="tl" style="margin-top:20px">""" + tlrows([
    ("10.30", "1차 현설", "DL이앤씨만 참석"),
    ("11.3", "2차 입찰공고", "입찰보증금 200억"),
    ("11.11", "2차 현설", "다음 주 수요일"),
], pad=12) + """</div>
</div>""" + foot()

cards["05-rule"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">경쟁입찰이 두 번 유찰되면</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">수의계약</div>
  <div class="bigcap">총회 의결을 거쳐 그 회사와 계약할 수 있다</div>
  <div class="duo">
    <div class="box"><div class="dl">가락우성1차</div><div class="dv">2번째</div><div class="ds">1차 유찰 · 2차 현설도 대우 단독</div></div>
    <div class="box"><div class="dl">목동 정해진 5곳</div><div class="dv">0곳</div><div class="ds">경쟁입찰 없이 모두 단독 응찰</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">가락우성1차 재건축, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("유력은 결과가 아니다", "시공사는 총회 의결로 정해진다"),
    ("967가구는 계획 수치", "심의·인가 단계에서 바뀔 수 있다"),
    ("조합원 지위는 따로 확인", "조합 · 송파구청 · 정비사업 정보몽땅"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">가락우성1차 재건축</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">건설사가<br>한 곳만 왔어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">두 번 불렀는데 두 번 다</span><br>
    <span style="white-space:nowrap">대우건설 혼자</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">왜 · 그다음은 · 5장으로</div>
</div>""" + foot()

insta["02-when"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">지금 어디까지 왔어요?</h1>
  <div style="font-size:27px;color:var(--mute)">건설사 고르는 단계예요</div>
  <div class="tl">""" + tlrows([
    ("1차", "건설사 모집", "한 곳만 와서 무효"),
    ("11월 3일", "다시 설명회", "또 대우건설 한 곳"),
    ("내년 2월 말", "건설사 결정 투표", "빠르면, 아직 예정이에요"),
], pad=16) + """</div>
</div>""" + foot()

insta["03-cost"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"공사비가 싸서 안 온 거예요?"</div>
    <div class="a gtx">그렇진 않아요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    평당 <b>985만원</b>이에요. 목동 재건축도
    965만~1,010만원이라 비슷해요. 건설사들이
    <b>이길 곳만 골라</b> 들어가는 분위기예요.</div>
</div>""" + foot()

insta["04-ssang"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">강북도 같은 날 같은 일</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:110px">쌍문한양1차</div>
  <div class="bigcap">도봉구 · 1,166집 계획</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    설명회에 <b>DL이앤씨 한 곳</b>만 왔어요.
    그래서 11월 3일 다시 모집을 냈고
    <b>11월 11일</b>에 설명회를 또 열어요.</div>
</div>""" + foot()

insta["05-next"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"계속 한 곳만 오면요?"</div>
    <div class="a gtx">그 회사와 바로 계약할 수 있어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    두 번 넘게 경쟁이 안 되면 <b>투표를 거쳐</b>
    그 회사와 계약할 수 있어요. 대신 비교할 상대가 없으니
    <b>계약 조건</b>을 더 꼼꼼히 봐야 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("‘유력’은 결정이 아니에요", "건설사는 조합 투표로 정해져요"),
    ("967집은 아직 계획", "심사를 거치며 바뀔 수 있어요"),
    ("사기 전에 구청에 확인", "송파는 살 때 허가가 필요한 곳이에요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
