# -*- coding: utf-8 -*-
"""2026-11-17 #128 목동4단지 유찰. 수치는 gen128.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "mkr"
DATEK = "2026-11-17"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">목동 재건축 시공사 입찰 결과</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">목동4단지<br>입찰 유찰</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    현설 4곳 중 <span class="gtx">1곳만</span> 입찰<br>
    현대건설 단독, 재입찰로</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">결과 · 다음 절차 · 공사비 · 목동 사례 · 체크</div>
</div>""" + foot()

cards["02-result"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">4곳 왔는데 1곳만 냈다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">목동4단지 현장설명회와 실제 입찰 · 곳</div>
""" + hb("현장설명회 참석 (9/30)", "4곳", 100, inside=True) + hb("입찰서 제출 (11/16)", "1곳 · 현대건설", 25, hi=True) + """
  <div class="note" style="margin-top:18px">※ 빠진 곳: 포스코이앤씨 · HDC현대산업개발 · 제일건설</div>
  <div class="note" style="margin-top:8px">※ 두 곳 이상 들어와야 경쟁입찰이 성립한다</div>
</div>""" + foot()

cards["03-next"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">유찰 다음은 재입찰</h1>
  <div style="font-size:27px;color:var(--mute)">목동4단지 시공사 선정, 남은 단계</div>
  <div class="tl">""" + tlrows([
    ("11월 16일", "1차 입찰 유찰", "현대건설 단독 응찰"),
    ("곧", "재입찰 공고", "양천구청 보고 뒤, 현설부터 다시"),
    ("또 단독이면", "수의계약 가능", "총회 의결을 거쳐야 한다"),
    ("내년 2월", "선정 총회 목표", "조합 발표 기준"),
], pad=16) + """</div>
</div>""" + foot()

cards["04-cost"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동 최고 공사비에도 단독</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">목동 단지별 3.3㎡당 예정 공사비 · 만원</div>
""" + hb("4단지", "1,010만원", 100, hi=True, inside=True) + hb("10단지", "990만원", 98.0, inside=True) \
    + hb("12·13단지", "980만원", 97.0, inside=True) + hb("8단지", "965만원", 95.5, inside=True) + """
  <div class="note" style="margin-top:14px">※ 총 예정 공사비 약 1조6,389억원 · 보도 기준</div>
</div>""" + foot()

cards["05-mokdong"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동은 단독이 흔했다</h1>
  <div style="font-size:27px;color:var(--mute)">목동 시공사 선정 결과 · 총회 찬성률</div>
  <div class="tl">""" + tlrows([
    ("6단지", "DL이앤씨 86.2%", "6월 총회"),
    ("10단지", "현대건설 95.9%", "두 차례 유찰 뒤 선정, 10월 18일"),
    ("13단지", "삼성물산 95.7%", "11월 7일 총회"),
    ("4단지", "재입찰 진행", "10단지와 같은 길"),
], pad=16) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">목동4단지, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("재입찰 공고일", "현설·마감 날짜는 조합 공지와 구청 고시로"),
    ("시공사는 아직 미정", "수의계약도 총회 의결이 있어야 정해진다"),
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
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">건설사 1곳만<br>손 들었어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">11월 16일 입찰 결과</span><br>
    <span style="white-space:nowrap">다시 입찰을 받아요</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">결과 · 다음 · 얼마 · 이웃 단지</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"유찰이 뭐예요?"</div>
    <div class="a gtx">한 곳만 와서 이번 입찰은 없던 일이 된 거예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    설명회엔 <b>4곳</b>이 왔는데 서류는 현대건설 <b>1곳</b>만 냈어요.
    두 곳 이상 와야 경쟁이 돼요.</div>
</div>""" + foot()

insta["03-next"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"그럼 이제 어떻게 돼요?"</div>
    <div class="a gtx">다시 입찰을 받아요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그때도 한 곳뿐이면 그 회사와 따로 계약할 수 있어요.
    그래도 <b>조합원 투표</b>는 꼭 거쳐요. 목표는 <b>내년 2월</b>이에요.</div>
</div>""" + foot()

insta["04-howmuch"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">평(3.3㎡)당 짓는 값</div>
  <div class="bignum gtx" style="margin-top:10px">1,010만원</div>
  <div class="bigcap">목동에서 가장 비싸게 불렀는데도 1곳</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    전체로는 약 <b>1조6천억원</b>짜리 공사예요.
    지금 1,382집이 최고 49층 <b>2,436집</b>으로
    바뀌는 계획이에요(아직 확정 전).</div>
</div>""" + foot()

insta["05-neighbor"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"옆 단지들도 그랬어요?"</div>
    <div class="a gtx">10단지도 두 번 유찰됐어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그래도 결국 현대건설로 정했고,
    100명이 투표하면 <b>96명</b>이 찬성했어요.
    4단지도 같은 길을 가고 있어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">목동 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("다시 입찰 날짜 보기", "공고가 나오면 마감일도 같이 나와요"),
    ("건설사는 아직 미정", "투표가 끝나야 정해져요"),
    ("사도 되는지 먼저 확인", "조합원 자격은 조합·구청에 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
