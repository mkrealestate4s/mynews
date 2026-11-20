# -*- coding: utf-8 -*-
"""2026-11-21 #132 성수2지구 시공사 총회 · 성수 4개 지구. 수치는 gen_example_132.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "ssu"
DATEK = "2026-11-21"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">성동구 성수전략정비구역 · 11월 21일 총회</div>
  <h1 class="serif gtx" style="font-size:70px;margin:14px 0 28px;line-height:1.2">성수2지구,<br>오늘 시공사 총회</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    DL이앤씨 <span class="gtx" style="white-space:nowrap">아크로 성수</span> 제안<br>
    <span style="white-space:nowrap">성수 네 지구 중 마지막</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">달력 · 오늘 총회 · 규모 · 공사비 · 체크</div>
</div>""" + foot()

cards["02-cal"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">올해 성수 시공사 달력</h1>
  <div style="font-size:27px;color:var(--mute)">성수전략정비구역 1~4지구 (보도 기준)</div>
  <div class="tl">""" + tlrows([
    ("4월", "1지구 · GS건설", "시공사 선정"),
    ("7월 5일", "4지구 · 롯데건설", "대우건설과 표 대결"),
    ("9월 19일", "3지구 · 삼성물산", "단독 응찰 뒤 수의계약"),
    ("11월 21일", "2지구 · DL이앤씨", "오늘 총회에서 선정 여부 결정"),
], pad=14) + """</div>
</div>""" + foot()

cards["03-today"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">성수2지구, 숫자 셋</h1>
  <div style="font-size:27px;color:var(--mute)">DL이앤씨 '아크로 성수' 제안 (보도 기준)</div>
  <div class="tl">""" + tlrows([
    ("2조137억", "사업비", "본계약에서 바뀔 수 있다"),
    ("2,381가구", "제안 가구", "일부 보도 2,350 · 인가에서 바뀐다"),
    ("65층", "최고 층수", "지하 6층~지상 65층, 11개 동"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 1·2차 입찰 모두 DL이앤씨 단독 응찰</div>
</div>""" + foot()

cards["04-size"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">네 지구 중 가장 크다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">성수 2·3·4지구 계획 가구</div>
""" + hb("2지구 · DL이앤씨", "2,381가구", 100, hi=True, inside=True) + hb("3지구 · 삼성물산", "2,213가구", 92.9, inside=True) + hb("4지구 · 롯데건설", "1,439가구", 60.4, inside=True) + """
  <div class="note" style="margin-top:14px">※ 제안·보도 기준 · 인가 단계에서 바뀔 수 있음</div>
</div>""" + foot()

cards["05-cost"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공사비도 2지구가 맨 위</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">성수 2·3·4지구 공사비 · 억원</div>
""" + hb("2지구 · DL이앤씨", "2조137", 100, hi=True, inside=True) + hb("3지구 · 삼성물산", "1조8,275", 90.8, inside=True) + hb("4지구 · 롯데건설", "1조3,099", 65.0, inside=True) + """
  <div class="note" style="margin-top:14px">※ 보도 금액 · 기사마다 기준이 다르고 본계약에서 바뀜</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">성수 재개발, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("성수2지구 총회 결과", "오늘 표결 · 부결되면 입찰 다시"),
    ("계획 숫자는 확정 전", "가구수·층수·공사비는 바뀐다"),
    ("거래 조건은 구청에", "토지거래허가·조합원 지위는 단계마다 다르다"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">성수2지구 재개발</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">오늘, 지을 회사를<br>정하는 날</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">후보는 DL이앤씨 한 곳</span><br>
    <span style="white-space:nowrap">11월 21일 총회</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">성수 4곳 · 크기 · 돈 · 볼 것</div>
</div>""" + foot()

insta["02-four"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"성수 다른 곳은요?"</div>
    <div class="a gtx">세 곳은 이미 정해졌어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    1지구 <b>GS</b>, 3지구 <b>삼성</b>, 4지구 <b>롯데</b>.
    오늘 2지구가 정해지면 넷 다 채워져요.</div>
</div>""" + foot()

insta["03-size"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">성수2지구에 짓는 집 (계획)</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">2,381집</div>
  <div class="bigcap">최고 65층, 성수 네 곳 중 가장 커요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    아직 <b>계획</b>이에요.
    허가 받는 과정에서 숫자가 바뀔 수 있어요.</div>
</div>""" + foot()

insta["04-money"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"2조원이면 분양가가 얼마예요?"</div>
    <div class="a gtx">아직 몰라요. 공사비는 분양가가 아니에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    집주인이 낼 돈(분담금)은
    <b>몇 년 뒤</b> 계획이 굳어야 나와요.</div>
</div>""" + foot()

insta["05-alone"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">입찰에 들어온 회사</div>
  <div class="bignum gtx" style="margin-top:10px">1곳</div>
  <div class="bigcap">두 번 다 DL이앤씨 혼자였어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그래서 경쟁 없이 바로 계약하는 길로 왔어요.
    오늘 <b>찬성이 모자라면</b> 처음부터 다시 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">성수동 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("몇 지구인지", "지구마다 속도가 달라요"),
    ("숫자는 계획", "집 수·층수는 바뀔 수 있어요"),
    ("사고팔 조건", "성동구청·조합에 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
