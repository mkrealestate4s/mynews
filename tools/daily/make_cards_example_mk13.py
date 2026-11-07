# -*- coding: utf-8 -*-
"""2026-11-08 #119 목동13단지 재건축 삼성물산 확정. 수치는 gen119.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "mk13"
DATEK = "2026-11-08"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">양천구 목동 · 시공사 확정</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">목동13단지 재건축<br>삼성물산 확정</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    참석자 <span class="gtx">95.7%</span> 찬성 · 11월 7일 전체회의<br>
    도급액 2조3,763억 · 최고 49층 3,852세대</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">투표 · 흐름 · 공사비 · 목동 현황 · 체크</div>
</div>""" + foot()

cards["02-vote"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1,884명 중 1,803명이 삼성물산</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">11월 7일 제2차 토지등소유자 전체회의 · 명</div>
""" + hb("사업 동의 토지등소유자", "2,127", 100, inside=True) + hb("참석 (부재자 투표 포함)", "1,884", 88.6, inside=True) \
    + hb("삼성물산 선택", "1,803", 84.8, hi=True, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">참석자 기준</div><div class="dv gtx">95.7%</div><div class="ds">1,803 ÷ 1,884</div></div>
    <div class="box"><div class="dl">동의자 전체 기준</div><div class="dv">84.8%</div><div class="ds">1,803 ÷ 2,127</div></div>
  </div>
</div>""" + foot()

cards["03-sched"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">두 번 단독 응찰, 어제 확정</h1>
  <div style="font-size:27px;color:var(--mute)">목동13단지 시공사 선정 흐름</div>
  <div class="tl">""" + tlrows([
    ("1차 입찰", "유찰", "삼성물산 한 곳만 응찰"),
    ("재입찰", "다시 단독 응찰", "경쟁사 없음"),
    ("9.29", "우선협상대상자 선정", "삼성물산"),
    ("11.7", "전체회의 확정", "1,803명 찬성 · 어제"),
], pad=16) + """</div>
  <div class="note" style="margin-top:14px">※ 단지명 '래미안 모브13'은 제안 단계 · 보도 기준</div>
</div>""" + foot()

cards["04-cost"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">3.3㎡당 980만원, 같은 선</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">목동 재건축 3.3㎡당 예정공사비 · 만원 · 부가세 제외</div>
""" + hb("4단지", "1,010", 100, inside=True) + hb("10단지", "990", 98, inside=True) \
    + hb("13단지", "980", 97, hi=True, inside=True) + hb("9단지", "980", 97, inside=True) \
    + hb("12단지", "980", 97, inside=True) + hb("8단지", "965", 95.5, inside=True) + """
  <div class="note" style="margin-top:12px">※ 13단지 도급액 약 2조3,763억원 · 보도 기준</div>
</div>""" + foot()

cards["05-map"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동, 정해진 곳과 남은 곳</h1>
  <div style="font-size:27px;color:var(--mute)">목동 재건축 시공사 현황 · 11월 8일</div>
  <div class="tl">""" + tlrows([
    ("확정 3곳", "6 · 10 · 13단지", "DL이앤씨 · 현대건설 · 삼성물산"),
    ("우선협상 2곳", "8 · 12단지", "대우건설 · GS건설"),
    ("11.16", "4단지 입찰 마감", "다음 결과"),
    ("이달", "7단지 입찰공고 예정", "9단지는 2027.1.11 마감"),
], pad=15) + """</div>
  <div class="note" style="margin-top:14px">※ 정해진 5곳 모두 단독 응찰 · 보도 기준</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">목동13단지 재건축, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("3,852세대 · 49층은 계획", "심의·인가 단계에서 바뀔 수 있다 · 분담금 미정"),
    ("래미안 모브13은 제안 이름", "최종 단지명은 이후 절차에서 정한다"),
    ("조합원 지위는 따로 확인", "대신자산신탁 · 양천구청 · 정비사업 정보몽땅"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">목동13단지 재건축</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">삼성물산이<br>짓기로 했어요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">100명 중 96명이 찬성</span><br>
    <span style="white-space:nowrap">49층 아파트 3,852집 계획</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">투표 · 과정 · 공사비 · 목동 · 5장으로</div>
</div>""" + foot()

insta["02-vote"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">투표하러 온 100명 중</div>
  <div class="bignum gtx" style="margin-top:10px">96명</div>
  <div class="bigcap">삼성물산에 찬성했어요 · 11월 7일</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    1,884명이 왔고 <b>1,803명</b>이 찬성했어요.
    다만 후보가 <b>삼성물산 한 곳</b>뿐인
    찬반 투표였어요.</div>
</div>""" + foot()

insta["03-how"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"경쟁해서 이긴 거예요?"</div>
    <div class="a gtx">두 번 다 혼자 들어왔어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    첫 입찰은 한 곳뿐이라 무산됐고, 다시 열어도
    <b>삼성물산만</b> 왔어요. 9월 말 협상 상대가 됐고
    어제 주민 투표로 <b>최종 확정</b>됐어요.</div>
</div>""" + foot()

insta["04-cost"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"공사비는 얼마예요?"</div>
    <div class="a gtx">평당 980만원, 목동 평균이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    전체로는 <span style="white-space:nowrap"><b>2조3,763억원</b></span>이에요.
    목동 다른 단지도 평당 965만~1,010만원이라
    거의 같은 수준이에요.</div>
</div>""" + foot()

insta["05-mokdong"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">목동 다른 단지는요?</h1>
  <div style="font-size:27px;color:var(--mute)">14개 단지 중 5곳 윤곽</div>
  <div class="tl">""" + tlrows([
    ("확정", "6 · 10 · 13단지", "DL · 현대 · 삼성물산"),
    ("협상 중", "8 · 12단지", "대우 · GS"),
    ("11월 16일", "4단지 마감", "다음 결과가 나와요"),
], pad=16) + """</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("3,852집 · 49층은 아직 계획", "심사를 거치며 바뀔 수 있어요"),
    ("내가 낼 돈(분담금)은 미정", "공사비가 정해졌다고 끝이 아니에요"),
    ("사기 전에 구청에 확인", "재건축 집은 사고팔 때 제한이 있을 수 있어요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
