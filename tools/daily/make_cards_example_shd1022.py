# -*- coding: utf-8 -*-
"""2026-10-22 SH 재개발임대 서류심사. 수치는 gen101.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "shd1022"
DATEK = "2026-10-22"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">SH 재개발임대주택 · 서울 162개 단지</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">재개발임대<br>서류심사 발표</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    내일 <span class="gtx">10월 23일</span> · 3,821가구 모집<br>
    대상자는 당첨이 아닙니다</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 남은 날 · 자격 · 물량 · 체크</div>
</div>""" + foot()

cards["02-date"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">내일 발표, 그다음은 3월 30일</h1>
  <div style="font-size:27px;color:var(--mute)">SH 재개발임대 남은 일정 · 재공고 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("10월 23일", "서류심사 대상자 발표", "SH 인터넷청약시스템에서 확인"),
    ("발표 후", "서류 제출", "기간·목록은 발표 안내대로"),
    ("2027년 3월 30일", "당첨자 발표", "서류심사 결과 반영"),
    ("2027년 4월", "입주", "예정"),
], pad=14) + """</div>
</div>""" + foot()

cards["03-wait"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">서류심사에서 당첨까지 158일</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">일정 사이 날 수 · 일</div>
""" + hb("접수 시작(9/29) → 당첨(3/30)", "182일", 100, inside=True) + hb("서류발표(10/23) → 당첨", "158일", 86.8, hi=True, inside=True) \
    + hb("접수 시작 → 서류발표", "24일", 13.2) + """
  <div class="note" style="margin-top:14px">※ 약 5개월 · 지금 집 만기가 봄 전이면 중간 거처 계획</div>
</div>""" + foot()

cards["04-check"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">서류로 다시 보는 기준 3가지</h1>
  <div style="font-size:27px;color:var(--mute)">일반공급 신청 자격 · 재공고 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("소득", "1순위 50% 이하", "2순위 70% 이하 · 도시근로자 월평균소득"),
    ("총자산", "3억4,500만원 이하", "세대 합산"),
    ("자동차", "4,542만원 이하", "보유 차량 가액"),
], pad=18) + """</div>
  <div class="note" style="margin-top:10px">※ 공고일(9/9) 서울 거주 무주택세대구성원 · 가구원 수별 금액은 공고문</div>
</div>""" + foot()

cards["05-supply"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">재공고로 3,821가구</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">SH 재개발임대 모집 물량 · 가구</div>
""" + hb("첫 공고 7월 30일 · 155개 단지", "3,421가구", 89.5, inside=True) + hb("재공고 9월 9일 · 162개 단지", "3,821가구", 100, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 주로 39㎡ 이하 · 재공고에서 연령 가점 삭제 · 예비입주자 포함</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">서류심사, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("10월 23일 발표 확인", "SH 인터넷청약시스템 · 발표 시각은 공고문"),
    ("서류는 기간 안에", "제출 기간·목록은 발표 안내 · 세대원 서류도"),
    ("당첨까지 158일 거처 계획", "당첨 2027년 3월 30일 · 입주 4월"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">SH 재개발임대 서류심사</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">내일 발표,<br>아직 당첨은 아니에요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    서울 작은 임대집 3,821집<br>
    <span style="white-space:nowrap">10월 23일 결과 확인</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">언제 · 얼마나 · 무엇을 · 5장으로</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"서류심사 대상이면 된 거예요?"</div>
    <div class="a gtx">아직이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    서류를 내고 <b>소득·재산</b>을 다시 확인받는 단계예요.
    정해진 기간에 서류를 못 내면 빠질 수 있어요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">앞으로 날짜는?</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("10월 23일", "서류 낼 사람 발표", "SH 홈페이지"),
    ("발표 후", "서류 내기", "안내된 기간 안에"),
    ("내년 3월 30일", "당첨 발표", ""),
    ("내년 4월", "입주", "예정"),
], pad=14) + """</div>
</div>""" + foot()

insta["04-wait"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">서류 발표에서 당첨까지</div>
  <div class="bignum gtx" style="margin-top:10px">158일</div>
  <div class="bigcap">약 5개월을 더 기다려요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지금 집 계약이 <b>내년 봄 전에</b> 끝나면
    그사이 살 곳도 같이 생각해 두세요.</div>
</div>""" + foot()

insta["05-budget"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"재산 기준이 얼마예요?"</div>
    <div class="a gtx">집 전체 3억4,500만원까지요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    자동차는 <b>4,542만원</b>까지예요. 소득은 가족 수마다
    금액이 달라서 <b>공고문 표</b>로 확인해야 정확해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">내일 확인할 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("결과 화면 끝까지 읽기", "서류 내는 기간·방법이 나와요"),
    ("가족 서류도 챙기기", "같이 사는 가족 소득·재산도 봐요"),
    ("지금 집 만기 확인", "입주는 내년 4월 예정"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
