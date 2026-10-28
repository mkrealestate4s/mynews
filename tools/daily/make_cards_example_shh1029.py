# -*- coding: utf-8 -*-
"""2026-10-29 SH 행복주택 1차 당첨 발표 D-1. 수치는 gen108 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "shh1029"
DATEK = "2026-10-29"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">SH 2026년 1차 행복주택 · 1,884세대</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">SH 행복주택<br>내일 당첨 발표</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    10월 30일(금) 발표 예정<br>
    <span class="gtx" style="white-space:nowrap">1,497세대는 예비 자리</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">구성 · 일정 · 임대료 · 확인 · 체크</div>
</div>""" + foot()

cards["02-mix"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1,884세대 중 1,497은 예비</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:28px">모집 구성 · 세대 · 5월 공고 보도</div>
""" + hb("예비입주자", "1,497", 79.5, hi=True, inside=True) + hb("잔여 공가", "332", 17.6) + hb("신규 단지", "55", 2.9) + """
  <div class="bignum gtx" style="font-size:110px;margin-top:22px">387세대</div>
  <div class="bigcap">바로 들어갈 수 있는 집 (신규 55 + 잔여 공가 332)</div>
</div>""" + foot()

cards["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">발표 10월 30일, 계약 11월</h1>
  <div style="font-size:27px;color:var(--mute)">SH 행복주택 1차 일정</div>
  <div class="tl">""" + tlrows([
    ("6월 15~17일", "인터넷 접수", "사흘간"),
    ("7월 1~3일", "서류 제출", "서류심사 대상자만"),
    ("10월 30일", "당첨자 발표", "내일 · 예정일"),
    ("11월", "계약", "입주는 12월 이후 (보도)"),
], pad=14) + """</div>
  <div class="note" style="margin-top:12px">※ 발표 시각·계약 날짜는 SH 인터넷청약시스템 공지</div>
</div>""" + foot()

cards["04-rent"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">평균 월 임대료 24만~62만원</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">면적별 평균 · 보증금은 괄호</div>
""" + hb("59㎡ 이하 (1억6,300만)", "62만", 100, hi=True, inside=True) + hb("49㎡ 이하 (1억3,600만)", "52만", 83.9, inside=True) \
    + hb("39㎡ 이하 (1억1,400만)", "43만", 69.4, inside=True) + hb("29㎡ 이하 (6,200만)", "24만", 38.7, inside=True) + """
  <div class="note" style="margin-top:14px">※ 전체 평균 보도치 · 단지별 금액은 공고문</div>
</div>""" + foot()

cards["05-check"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">발표 날 확인할 것</h1>
  <div style="font-size:27px;color:var(--mute)">결과 화면에서 바로 볼 것</div>
  <div class="tl">""" + tlrows([
    ("당첨·예비", "어느 쪽인지", "예비면 순번을 적어 두기"),
    ("계약 날짜", "11월 · 세부는 공지", "SH 인터넷청약시스템"),
    ("보증금", "39㎡ 이상 평균 1억대", "대출은 은행 상담 먼저"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 문의 SH 콜센터 1600-3456</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">발표 뒤, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("당첨인지 예비인지", "예비면 순번이 곧 입주 가능성"),
    ("계약 날짜 확인", "11월 계약 · 세부 날짜는 SH 공지"),
    ("보증금과 대출 계획", "59㎡ 평균 보증금 1억6,300만원"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">SH 행복주택</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">6월에 넣은 그 집<br>내일 발표해요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    10월 30일(금) 발표 예정<br>
    <span style="white-space:nowrap">서울 1,884세대</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">자리 · 날짜 · 월세 · 5장으로</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"붙으면 바로 들어가요?"</div>
    <div class="a gtx">100명 중 21명만 바로 들어갈 집이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    나머지 79명은 <b>예비</b> 자리예요.
    빈집이 나면 번호 순서대로 연락이 와요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">남은 날짜</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("10월 30일", "결과 발표", "내일 · 예정일"),
    ("11월", "계약", "날짜는 SH 공지로"),
    ("12월 이후", "입주", "예비는 순서대로"),
], pad=18) + """</div>
</div>""" + foot()

insta["04-budget"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">18평쯤(59㎡) 평균 월세</div>
  <div class="bignum gtx" style="margin-top:10px">62만원</div>
  <div class="bigcap">보증금은 평균 1억6,300만원이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    가장 작은 9평쯤(29㎡)은 <b>월 24만원</b>,
    보증금 6,200만원이에요. 주변 시세의 60~80%예요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"붙으면 뭐부터 해요?"</div>
    <div class="a gtx">보증금 마련 계획부터 세워요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    계약 날 보증금 일부를 바로 내요.
    <b>대출을 쓸 거면 은행 상담</b>을 먼저 잡아 두세요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">결과 보고 할 일</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("당첨인지 예비인지", "예비면 내 번호 적어 두기"),
    ("계약 날짜 확인", "SH 청약 사이트 공지"),
    ("보증금 준비", "내 단지 금액은 공고문에"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
