# -*- coding: utf-8 -*-
"""2026-11-21 #134 동탄 신고가 · 한강벨트 거래 감소. 수치는 gen_example_134.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "dth"
DATEK = "2026-11-22"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">화성 동탄 · 11월 18일까지 신고분</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">동탄 신고가,<br>2건 중 1건</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    매매 211건 중 <span class="gtx" style="white-space:nowrap">94건</span> 최고가<br>
    <span style="white-space:nowrap">한강벨트 10월 거래는 −73%</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">거래량 · 신고가 · 사례 · 대출 · 체크</div>
</div>""" + foot()

cards["02-drop"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">한강벨트가 가장 많이 줄었다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">10월 아파트 거래 감소율 · 작년 같은 달 대비</div>
""" + hb("한강벨트 7개구 · 2,865 → 770건", "−73.1%", 100, hi=True, inside=True) + hb("서울 전체", "−54.0%", 73.9, inside=True) + hb("반도체벨트 3곳 · 2,458 → 1,323건", "−46.2%", 63.2, inside=True) + """
  <div class="note" style="margin-top:14px">※ 한강벨트: 광진·성동·마포·동작·양천·영등포·강동 · 반도체벨트: 영통·기흥·동탄</div>
</div>""" + foot()

cards["03-high"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">동탄 11월 아파트 매매 중 신고가</div>
  <div class="bignum gtx" style="margin-top:10px">44.5%</div>
  <div class="bigcap">211건 가운데 94건이 종전 최고가를 넘었다</div>
  <div class="note" style="margin-top:26px">※ 11월 18일까지 신고된 거래 · 신고 기한(30일)이 남아 숫자가 바뀔 수 있음</div>
</div>""" + foot()

cards["04-case"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">한 번에 8,800만원 올랐다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">동탄역 반도유보라 아이비파크8.0 · 전용 73.6㎡</div>
""" + hb("11월 거래", "15억5,800만", 100, hi=True, inside=True) + hb("직전 신고가", "14억7,000만", 94.4, inside=True) + """
  <div class="duo"><div class="box"><div class="dl">8,800만원을 빌리면</div><div class="dv gtx">월 29만원</div>
    <div class="ds">연 4% 가정, 이자만 연 약 352만원</div></div></div>
</div>""" + foot()

cards["05-loan"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">15억 아래는 대출 6억</h1>
  <div style="font-size:27px;color:var(--mute)">집값 구간별 주택담보대출 한도 (10·15 대책)</div>
  <div class="tl">""" + tlrows([
    ("15억 이하", "최대 6억", "동탄 대부분 단지가 여기"),
    ("15억~25억", "최대 4억", "한강벨트 84㎡ 상당수"),
    ("25억 초과", "최대 2억", "강남3구 대표 단지"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 14억 집은 현금 8억, 20억 집은 현금 16억이 필요</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">동탄 신고가, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("거래 취소 여부", "실거래가 공개시스템에서 취소 표시 확인"),
    ("15억 선과 대출 한도", "15억을 넘으면 대출 6억 → 4억"),
    ("같은 단지 층·동 비교", "신고가 한 건이 단지 시세는 아니다"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">동탄 신고가</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">팔린 집 절반이<br>역대 최고값</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">서울 한강 쪽은 거래가 뚝</span><br>
    <span style="white-space:nowrap">11월 동탄 실거래</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 명 · 얼마 · 왜 · 볼 것</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">동탄에서 집 산 100명 중</div>
  <div class="bignum gtx" style="margin-top:10px">45명</div>
  <div class="bigcap">역대 가장 비싼 값에 샀어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    11월 18일까지 신고된 211건 중 <b>94건</b>이
    그 단지 그 평수 최고값이었어요.</div>
</div>""" + foot()

insta["03-seoul"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"서울은 어때요?"</div>
    <div class="a gtx">한강 쪽 7개구는 거래가 4분의 1로 줄었어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    작년 10월 <b>100건</b> 팔리던 게
    올해 10월엔 <b>27건</b>만 팔렸어요.</div>
</div>""" + foot()

insta["04-price"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">동탄역 반도유보라 아이비파크8.0 · 전용 22평</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:112px">+8,800만</div>
  <div class="bigcap">직전 최고값 14억7천 → 이번 <span style="white-space:nowrap">15억5,800만</span></div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그만큼 빌리면 이자만
    <b>한 달 29만원</b> 더 내요(연 4% 가정).</div>
</div>""" + foot()

insta["05-why"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"왜 동탄만 올라요?"</div>
    <div class="a gtx">15억 아래 집은 대출이 6억까지 나와요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    15억이 넘으면 4억, 25억이 넘으면 2억.
    20억 집은 <b>내 돈 16억</b>이 있어야 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">동탄 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("취소된 거래인지", "최고값 거래도 나중에 취소돼요"),
    ("15억 넘는지", "넘으면 대출이 확 줄어요"),
    ("층·동 맞춰 보기", "한 건이 그 단지 값은 아니에요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
