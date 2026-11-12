# -*- coding: utf-8 -*-
"""2026-11-13 #124 목동4단지 재건축 입찰 마감. 수치는 gen124.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "mk4"
DATEK = "2026-11-13"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">목동 재건축 시공사 입찰</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">목동4단지<br>16일 입찰 마감</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    3.3㎡당 <span class="gtx">1,010만원</span> · 목동 최고<br>
    경쟁 붙을까, 단독일까</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 공사비 · 입찰 · 목동 결과 · 체크</div>
</div>""" + foot()

cards["02-when"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">16일 오후 2시 마감</h1>
  <div style="font-size:27px;color:var(--mute)">목동4단지 시공사 입찰 일정</div>
  <div class="tl">""" + tlrows([
    ("9월 21일", "입찰 공고", "입찰보증금 600억원(현금 300억)"),
    ("9월 30일", "현장설명회", "현대·포스코이앤씨·HDC현산·제일건설"),
    ("11월 16일", "입찰 마감 14시", "오후 3시 제안서 개봉"),
    ("그다음", "선정 총회", "일정은 조합 공고로 확인"),
], pad=16) + """</div>
</div>""" + foot()

cards["03-cost"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">3.3㎡당 1,010만원, 목동 최고</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">목동 단지별 3.3㎡당 예정 공사비 · 만원</div>
""" + hb("4단지", "1,010만원", 100, hi=True, inside=True) + hb("10단지", "990만원", 98.0, inside=True) \
    + hb("12·13단지", "980만원", 97.0, inside=True) + hb("8단지", "965만원", 95.5, inside=True) + """
  <div class="note" style="margin-top:14px">※ 총 예정 공사비 약 1조6,389억원 · 보도 기준</div>
</div>""" + foot()

cards["04-bid"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">현설은 4곳, 입찰은 몇 곳?</h1>
  <div style="font-size:27px;color:var(--mute)">마감 전 상황 (관측 포함, 결과 아님)</div>
  <div class="tl">""" + tlrows([
    ("4개사", "현설 참석", "현대·포스코이앤씨·HDC현산·제일"),
    ("1곳", "제안서 착수 보도", "현대건설만 착수했다는 업계 관측"),
    ("단독이면", "유찰", "재입찰, 또 단독이면 수의계약 가능"),
    ("10단지", "앞선 사례", "두 차례 유찰 뒤 현대건설 선정"),
], pad=16) + """</div>
</div>""" + foot()

cards["05-vote"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">앞선 단지들, 찬성 86~96%</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">목동 시공사 선정 찬성률 · %</div>
""" + hb("6단지 · DL이앤씨", "86.2%", 86.2, inside=True) + hb("13단지 · 삼성물산", "95.7%", 95.7, inside=True) \
    + hb("10단지 · 현대건설", "95.9%", 95.9, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 투표자 대비 찬성 · 10단지 1,557/1,624명 · 13단지 1,803/1,884명</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">목동4단지, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("16일 오후 3시 개봉 결과", "몇 곳이 입찰서를 냈는지 조합 공지로 확인"),
    ("단독 응찰은 관측", "유찰되면 재입찰 일정이 새로 잡힌다"),
    ("2,436가구는 확정 전", "지위 양도·거래 제한은 조합·구청에서 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">목동4단지 재건축</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">누가 지을지<br>월요일에 열어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">11월 16일 오후 2시 마감</span><br>
    <span style="white-space:nowrap">건설사 몇 곳이 올까</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">언제 · 얼마 · 몇 곳 · 이웃 단지</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"입찰 마감이 뭐예요?"</div>
    <div class="a gtx">건설사가 "우리가 지을게요" 서류 내는 마지막 날이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    16일 <b>오후 2시</b>에 마감하고 <b>3시</b>에 봉투를 열어요.
    여러 곳이 내면 조합원 투표로 한 곳을 골라요.</div>
</div>""" + foot()

insta["03-howmuch"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">평(3.3㎡)당 짓는 값</div>
  <div class="bignum gtx" style="margin-top:10px">1,010만원</div>
  <div class="bigcap">목동 아파트 중 처음으로 1천만원을 넘었어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    전체로는 약 <b>1조6천억원</b>짜리 공사예요.
    지금 1,382집이 최고 49층 <b>2,436집</b>으로
    바뀌는 계획이에요(아직 확정 전).</div>
</div>""" + foot()

insta["04-howmany"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"건설사가 많이 와요?"</div>
    <div class="a gtx">설명회엔 4곳 왔는데, 실제론 몰라요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    현대건설 <b>한 곳만</b> 준비 중이라는 말이 돌지만
    아직 소문이에요. 한 곳만 내면 <b>다시 입찰</b>을 받아요.</div>
</div>""" + foot()

insta["05-neighbor"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"옆 단지들은 어떻게 됐어요?"</div>
    <div class="a gtx">6·10·13단지는 이미 정했어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    6단지 DL이앤씨, 10단지 현대건설, 13단지 삼성물산.
    100명이 투표하면 <b>86~96명</b>이 찬성했어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">목동 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("16일 결과부터 보기", "몇 곳이 왔는지 뉴스로 확인해요"),
    ("2,436집은 아직 계획", "심의 때마다 숫자가 바뀌어요"),
    ("사도 되는지 먼저 확인", "조합원 자격은 조합·구청에 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
