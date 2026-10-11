# -*- coding: utf-8 -*-
"""2026-10-11 이번 주 청약 일정. 수치는 gen92.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "wk1011"
DATEK = "2026-10-11"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">10월 12일 ~ 16일</div>
  <h1 class="serif gtx" style="font-size:78px;margin:14px 0 28px;line-height:1.2">이번 주 청약 일정</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    화요일에 몰렸다 · SH 매입임대 + 1순위 2곳<br>
    수요일 청담르엘 <span class="gtx">서류심사 발표</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">요일별로 놓치지 않게 · 5장으로</div>
</div>""" + foot()

cards["02-week"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">이번 주 청약 일정 요일별</h1>
  <div style="font-size:27px;color:var(--mute)">접수 · 발표 · 마감</div>
  <div class="tl">""" + tlrows([
    ("12일 월", "향남 특별공급", "향남역 그로브 스위첸"),
    ("13일 화", "SH 매입임대 접수 시작", "향남·양평 1순위 · 세종 신희타 · 계양 전시관"),
    ("14일 수", "청담르엘 서류심사 발표", "향남 2순위"),
    ("15일 목", "SH 매입임대 마감 17시", "인천석남 행복주택 마감"),
], pad=16) + """</div>
</div>""" + foot()

cards["03-sh"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">SH 신혼·신생아 매입임대Ⅰ</div>
  <div class="bignum gtx" style="margin-top:10px">서울 347호</div>
  <div class="bigcap">13일 10시 ~ 15일 17시 · 1순위 신생아 가구</div>
  <div class="duo">
    <div class="box"><div class="dl">임대료</div><div class="dv">30~50%</div></div>
    <div class="box"><div class="dl">Ⅰ·Ⅱ 중복</div><div class="dv">결격</div></div>
  </div>
  <div class="note" style="margin-top:18px">※ 자격은 공고일(9월 30일) 기준 · 소득·자산 표는 공고문</div>
</div>""" + foot()

cards["04-cheongdam"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">수요일, 청담르엘 서류심사 발표</h1>
  <div style="font-size:27px;color:var(--mute)">SH 제51차 장기전세 신청자</div>
  <div class="tl">""" + tlrows([
    ("10월 14일", "서류심사 대상 발표", "SH 인터넷청약시스템"),
    ("10월 19~21일", "서류 우편 제출", "기한 넘기면 탈락할 수 있다"),
    ("2027년 3월 5일", "당첨자 발표", ""),
], pad=18) + """</div>
  <div class="note" style="margin-top:14px">※ 제출 서류는 공고문·발표 안내에서 확인</div>
</div>""" + foot()

cards["05-public"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">LH 쪽 일정도 있다</h1>
  <div style="font-size:27px;color:var(--mute)">공공임대 · 신혼희망타운</div>
  <div class="tl">""" + tlrows([
    ("13~15일", "세종 4-2 M3 신희타 행복주택", "55㎡ 예비입주자 129명"),
    ("15일", "인천석남 어울림센터 행복주택", "최초모집 마감"),
    ("13일~", "인천계양 A17 신희타 전시관", "부천 오정동 · 일반 접수 26~27일"),
], pad=18) + """</div>
  <div class="note" style="margin-top:14px">※ LH청약플러스 목록·정리 자료 기준 · 공고문 확인</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">이번 주, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("SH 매입임대Ⅰ·Ⅱ는 하나만", "둘 다 넣으면 모두 결격"),
    ("청담르엘 신청자는 14일 확인", "대상이면 19~21일 우편 제출"),
    ("마감 시각은 공고문으로", "SH 매입임대 15일 오후 5시"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">10월 12일 ~ 15일</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">이번 주 청약,<br>화요일을 비워 두세요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    신혼 임대주택부터 새 아파트까지<br>
    <span style="white-space:nowrap">하루에 몰렸어요</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">요일별로 · 5장으로</div>
</div>""" + foot()

insta["02-week"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">요일별로 보면</h1>
  <div style="font-size:27px;color:var(--mute)">이번 주 청약 달력</div>
  <div class="tl">""" + tlrows([
    ("월", "화성 향남 새 아파트", "특별공급"),
    ("화", "서울 신혼 임대주택 접수", "새 아파트 1순위 2곳도"),
    ("수", "청담르엘 1차 결과", "서류 낼 사람 발표"),
    ("목", "신혼 임대주택 마감", "오후 5시까지"),
], pad=16) + """</div>
</div>""" + foot()

insta["03-sh"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"신혼부부 임대주택 이번에 나와요?"</div>
    <div class="a gtx">서울 347집, 화요일부터요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    아기 낳은 지 2년 안이거나 임신 중이면 <b>1순위</b>예요.
    집세는 주변 시세의 <b>30~50%</b>예요.</div>
</div>""" + foot()

insta["04-trap"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">이것만은 조심</div>
  <div class="bignum gtx" style="margin-top:10px">Ⅰ 또는 Ⅱ</div>
  <div class="bigcap">둘 다 넣으면 모두 탈락이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    같은 날 나온 매입임대 Ⅰ과 Ⅱ 중 <b>하나만</b> 고르세요.</div>
</div>""" + foot()

insta["05-cheongdam"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"청담르엘 넣었는데요?"</div>
    <div class="a gtx">수요일에 결과 확인하세요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    서류 낼 사람으로 뽑혔으면 <b>19~21일</b>에 우편으로 보내야 해요.
    최종 발표는 내년 3월 5일이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">이번 주 기억할 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("화요일 아침 10시", "신혼 임대주택 접수 시작"),
    ("Ⅰ, Ⅱ 중 하나만", "둘 다 넣으면 탈락"),
    ("목요일 오후 5시 마감", "미루지 마세요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요 · 내일 한 번 더 알려 드릴게요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
