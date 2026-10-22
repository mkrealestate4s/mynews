# -*- coding: utf-8 -*-
"""2026-10-23 계양 신혼희망타운 본청약. 수치는 gen_example_102.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "gya1023"
DATEK = "2026-10-23"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">인천계양 A17블록 · LH 본청약</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">계양 신혼희망타운<br>월요일부터 접수</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    <span class="gtx">10월 26~27일</span> 이틀 · 일반공급 176가구<br>
    전용 55㎡ 평균 5억400만원</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 물량 · 분양가 · 조건 · 체크</div>
</div>""" + foot()

cards["02-date"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">접수는 10월 26~27일 이틀</h1>
  <div style="font-size:27px;color:var(--mute)">계양 신혼희망타운 남은 일정 · LH 공고 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("10월 26~27일", "일반 접수", "예비신혼부부·신혼부부·한부모가족"),
    ("11월 5일", "당첨자 발표", "접수 마감 9일 뒤"),
    ("2027년 2월", "계약", ""),
    ("2029년 11월", "입주", "예정"),
], pad=14) + """</div>
  <div class="note" style="margin-top:10px">※ 사전청약 당첨자 신청은 10월 19~20일에 끝났습니다</div>
</div>""" + foot()

cards["03-supply"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">309가구 중 일반공급 176가구</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">공공분양 물량 나눔 · 가구</div>
""" + hb("공공분양 전체", "309가구", 100, inside=True) + hb("이번 일반공급", "176가구", 57.0, hi=True, inside=True) \
    + hb("사전청약 당첨 몫", "133가구", 43.0, inside=True) + """
  <div class="note" style="margin-top:14px">※ 단지 전체 463가구 · 행복주택 154가구는 따로 모집</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">전용 55㎡ 평균 5억400만원</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">분양가 · 만원</div>
""" + hb("가장 높은 값", "5억844만", 100, inside=True) + hb("평균", "5억400만", 99.1, hi=True, inside=True) \
    + hb("가장 낮은 값", "4억7,673만", 93.8, inside=True) + """
  <div class="note" style="margin-top:14px">※ 평균은 보도, 최고·최저는 청약 정보 사이트 정리 · 타입별 금액은 공고문</div>
</div>""" + foot()

cards["05-rules"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">전매 3년, 실거주 의무는 없다</h1>
  <div style="font-size:27px;color:var(--mute)">당첨 후 붙는 조건 · 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("전매제한", "3년", "이 기간에는 팔 수 없음"),
    ("실거주 의무", "없음", "공고문으로 다시 확인"),
    ("전용 모기지", "연 1.3% 고정", "의무 적용 · 팔 때 차익 일부를 나눔"),
], pad=18) + """</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">접수 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("접수는 10월 26~27일 이틀", "LH 청약플러스 · 접수 시간은 공고문"),
    ("소득·자산 기준은 공고문 표로", "가구원 수별 금액 · 예비부부는 두 사람 합산"),
    ("전용 모기지 정산 조건 읽기", "연 1.3% 고정 · 팔 때 차익을 나눔"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">계양 신혼희망타운</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">신혼부부 집,<br>월요일부터 신청</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    인천 계양 새 아파트 176집<br>
    <span style="white-space:nowrap">10월 26~27일 이틀만</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">누가 · 언제 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-who"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"누가 넣을 수 있어요?"</div>
    <div class="a gtx">신혼부부, 결혼 앞둔 커플, 한부모가족이요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    집이 없어야 하고 <b>소득·재산 기준</b>도 있어요.
    가족 수마다 금액이 달라서 <b>공고문 표</b>로 확인해야 정확해요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">날짜는 이렇게</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("10월 26~27일", "신청", "LH 청약플러스"),
    ("11월 5일", "당첨 발표", ""),
    ("2027년 2월", "계약", ""),
    ("2029년 11월", "입주", "예정"),
], pad=14) + """</div>
</div>""" + foot()

insta["04-count"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">이번에 새로 뽑는 집</div>
  <div class="bignum gtx" style="margin-top:10px">176집</div>
  <div class="bigcap">309집 가운데 133집은 미리 뽑힌 사람 몫이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    크기는 <b>전용 55㎡</b> 하나예요. 방 셋 정도 되는
    20평대 초반 집이라고 보면 돼요.</div>
</div>""" + foot()

insta["05-budget"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마예요?"</div>
    <div class="a gtx">평균 <span style="white-space:nowrap">5억400만원</span>이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    층과 타입에 따라 <b>4억7,673만~5억844만원</b>.
    전용 대출(연 1.3%)이 붙는데, 팔 때 <b>오른 값 일부를 나눠요.</b></div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("이틀만 열려요", "10월 26일 월요일, 27일 화요일"),
    ("두 사람 소득 합쳐 보기", "결혼 앞둔 커플도 합쳐서 봐요"),
    ("입주까지 4년 계획", "지금 집 만기와 맞춰 보기"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
