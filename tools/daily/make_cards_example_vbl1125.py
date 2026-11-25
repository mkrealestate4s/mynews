# -*- coding: utf-8 -*-
"""2026-11-25 #138 특집 위반건축물 양성화. 수치는 gen_example_138.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "vbl"
DATEK = "2026-11-25"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">특집 · 특정건축물 정리 특별조치법</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">위반건축물 양성화,<br>12월 17일 시작</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    <span style="white-space:nowrap">2028년 6월 16일까지 18개월</span><br>
    <span style="white-space:nowrap">2023년 말 이전 소규모 주거용</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">규모 · 일정 · 대상 · 절차 · 체크</div>
</div>""" + foot()

cards["02-scale"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">약 4만동이 대상</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">전국 위반건축물 · 국토부 2025년 10월 발표</div>
""" + hb("전체 위반건축물", "14.8만동", 100, inside=True) + hb("주거용", "8.3만동", 56.1, inside=True) + hb("단독·다가구·다세대", "4.6만동", 31.1, inside=True) + hb("양성화 예상 범위", "약 4만동", 27.0, hi=True) + """
  <div class="note" style="margin-top:18px">※ 양성화 예상 범위는 국토부 추정</div>
</div>""" + foot()

cards["03-when"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">언제부터 언제까지</h1>
  <div style="font-size:27px;color:var(--mute)">위반건축물 양성화 일정</div>
  <div class="tl">""" + tlrows([
    ("6월 16일", "법 공포", "특정건축물 정리 특별조치법"),
    ("11월 9일", "시행령 입법예고 마감", "9월 30일부터 의견 접수"),
    ("12월 17일", "시행 · 신고 시작", "오늘부터 22일 뒤"),
    ("2028.6.16", "신고 마감", "18개월 한시"),
], pad=14) + """</div>
</div>""" + foot()

cards["04-who"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">우리 집이 대상인지</h1>
  <div style="font-size:27px;color:var(--mute)">보도·해설 기준 · 시행령 확인</div>
  <div class="tl">""" + tlrows([
    ("2023년 말", "이전에 사실상 완공", "2024년 이후 위반은 제외"),
    ("165㎡", "단독주택 연면적", "당정 협의 보도"),
    ("660㎡", "다가구주택 연면적", "당정 협의 보도"),
    ("85㎡", "다세대 세대당 전용", "해설 자료 기준"),
], pad=14) + """</div>
  <div class="note" style="margin-top:10px">※ 개발제한구역·정비구역·투기성 위반은 빠짐</div>
</div>""" + foot()

cards["05-how"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:24px">신고에서 사용승인까지</h1>
  <div class="flow" style="gap:16px">
    <div class="fbox"><span class="n gtx">1</span><div><div class="t">건축사 도면</div><div class="s">설계도서 · 현장조사서</div></div></div>
    <div class="fbox"><span class="n gtx">2</span><div><div class="t">구청에 신고</div><div class="s">시·군·구 건축 부서</div></div></div>
    <div class="fbox"><span class="n gtx">3</span><div><div class="t">심의</div><div class="s">안전·주차 기준 검토</div></div></div>
    <div class="fbox"><span class="n gtx">4</span><div><div class="t">과태료 내고 사용승인</div><div class="s">금액은 시행령·구청 확인</div></div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">양성화 전에, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("건축물대장부터", "정부24에서 위반 표시·내용 확인"),
    ("근생빌라는 구청 확인", "포함 여부·조건이 자료마다 다름"),
    ("건축사 일정 미리", "마감은 2028년 6월 16일"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 법률·건축 자문이 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">위반건축물 양성화</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">불법 딱지 붙은 집,<br>떼는 길 열려요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">12월 17일부터 1년 반</span><br>
    <span style="white-space:nowrap">10년 만에 다시 열려요</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">왜 · 언제 · 우리 집 · 어떻게 · 볼 것</div>
</div>""" + foot()

insta["02-why"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"딱지 붙으면 뭐가 문제예요?"</div>
    <div class="a gtx">해마다 돈 내고, 전세도 어려워요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    고칠 때까지 돈을 계속 내야 하고, 전세대출이 막혀 세입자 구하기도 힘들어요.
    모르고 산 사람도 똑같아요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"언제까지 해야 돼요?"</div>
    <div class="a gtx">2028년 6월 16일까지요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    <b>12월 17일</b>부터 신청을 받아요.
    도면 준비에 시간이 걸려서 미리 알아보는 게 좋아요.</div>
</div>""" + foot()

insta["04-mine"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"우리 집도 돼요?"</div>
    <div class="a gtx">2023년 말 전에 지은 작은 집이면요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    단독·다가구·빌라처럼 사람이 사는 작은 건물이 대상이에요.
    그린벨트·재개발 구역 안이면 안 돼요.</div>
</div>""" + foot()

insta["05-how"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">어떻게 신청해요?</h1>
  <div class="flow" style="gap:16px">
    <div class="fbox"><span class="n gtx">1</span><div><div class="t">건축사에게 도면 받기</div></div></div>
    <div class="fbox"><span class="n gtx">2</span><div><div class="t">구청에 신고하기</div></div></div>
    <div class="fbox"><span class="n gtx">3</span><div><div class="t">구청이 살펴보기</div></div></div>
    <div class="fbox"><span class="n gtx">4</span><div><div class="t">과태료 내면 정식 건물로</div></div></div>
  </div>
  <div class="note" style="margin-top:20px">금액은 아직 확정 전이라 구청에 물어보세요</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("건축물대장 떼 보기", "정부24에서 무료, 위반 표시 확인"),
    ("딱지 있으면 물어보기", "양성화 신청할지, 비용은 누가"),
    ("계약서에 적어 두기", "말로만 약속하지 않기"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
