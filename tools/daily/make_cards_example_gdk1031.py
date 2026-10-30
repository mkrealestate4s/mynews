# -*- coding: utf-8 -*-
"""2026-10-31 고덕강일3단지 특별공급 월요일 접수(D-2). 수치는 gen_example_110.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "gdk1031"
DATEK = "2026-10-31"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">SH 토지임대부 · 강동구 고덕강일</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">고덕강일3단지<br>특별공급 월요일</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    새로 뽑는 713가구 중 <span class="gtx">566가구</span><br>
    특공 11월 2~3일 · 일반 1순위 11월 4일</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">물량 · 일정 · 분양가 · 토지임대료 · 체크</div>
</div>""" + foot()

cards["02-supply"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">713가구 중 566가구가 특공</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">고덕강일3단지 1,305가구 공급 구성 · 가구</div>
""" + hb("사전청약 당첨자 몫", "592가구", 100, inside=True) + hb("특별공급", "566가구", 95.6, hi=True, inside=True) \
    + hb("일반공급", "147가구", 24.8) + """
  <div class="note" style="margin-top:14px">※ 새로 뽑는 100채 중 79채가 특별공급 · 유형별 배정은 공고문 · 10/16 보도 기준</div>
</div>""" + foot()

cards["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">특공 11월 2일, 일반 11월 4일</h1>
  <div style="font-size:27px;color:var(--mute)">고덕강일3단지 남은 접수 일정 · 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("10월 26~27일", "사전청약 당첨자", "접수 끝남"),
    ("11월 2~3일", "특별공급", "월·화 이틀 · 신혼부부 · 생애최초 등"),
    ("11월 4~6일", "일반공급", "4일 서울 2년 이상 · 5일 그 밖 수도권 · 6일 2순위"),
    ("11월 26일", "당첨자 발표", "SH 인터넷청약시스템"),
], pad=14) + """</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">건물값 2억8천부터, 땅은 빌린다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">건물 분양가 범위 · 땅값 제외 · 억원</div>
""" + hb("49㎡ 하단", "2.8억", 71.8, inside=True) + hb("49㎡ 상단", "3.2억", 82.1, inside=True) \
    + hb("59㎡ 하단", "3.4억", 87.2, hi=True, inside=True) + hb("59㎡ 상단", "3.9억", 100, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 전매 10년 제한 · 40년 거주 후 재계약 최장 80년 · 동·층별 확정가는 공고문</div>
</div>""" + foot()

cards["05-rent"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">49㎡ 매달 내는 토지임대료</div>
  <div class="bignum gtx" style="margin-top:10px">42만6천원</div>
  <div class="bigcap">1년이면 약 511만원</div>
  <div class="duo">
    <div class="box"><div class="dl">59㎡</div><div class="dv">51만1,500원</div><div class="ds">1년이면 약 614만원</div></div>
    <div class="box"><div class="dl">보증금 전환</div><div class="dv">최대 60%</div><div class="ds">SH와 합의해 정함</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">특공 넣기 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 특공 유형과 배정 수", "신혼·생애최초·다자녀 등 물량은 SH 공고문"),
    ("소득·자산 기준은 유형마다 다르다", "수도권 무주택 + 청약통장 · 공고일 10/16 기준"),
    ("분양가에 토지임대료 더해 계산", "대출 이자 + 월 42만~51만원 · 전매 10년"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">고덕강일3단지 특별공급</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">서울 새 아파트<br>3억 안팎</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    대신 땅은 빌려 써요<br>
    <span style="white-space:nowrap">11월 2일 월요일 접수</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 집 · 언제 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"특별공급은 몇 집이에요?"</div>
    <div class="a gtx">새로 뽑는 100집 중 79집이요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    전체 <b>1,305집</b> 중 592집은 미리 당첨된 사람 몫이에요.
    남은 713집 가운데 신혼부부 등 특별공급이 <b>566집</b>,
    누구나 넣는 일반공급은 <b>147집</b>이에요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">내 접수 날은 언제?</h1>
  <div style="font-size:27px;color:var(--mute)">날짜를 달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("11월 2~3일", "신혼부부 등", "특별공급 · 월·화 이틀"),
    ("11월 5일", "서울 2년 안 된 사람", "경기·인천 포함"),
    ("11월 4일", "서울 2년 넘게 산 사람", "일반공급 첫날"),
    ("11월 26일", "발표", "SH 홈페이지"),
], pad=14) + """</div>
</div>""" + foot()

insta["04-budget"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"집값이 얼마예요?"</div>
    <div class="a gtx">작은 집 2억8천부터요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    방 2개쯤 되는 <b>49㎡</b>가 2억8천~3억2천,
    조금 큰 <b>59㎡</b>가 3억4천~3억9천이에요.
    땅값이 빠진 <b>건물 값</b>이에요.</div>
</div>""" + foot()

insta["05-money"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">땅 빌리는 값, 작은 집 기준 매달</div>
  <div class="bignum gtx" style="margin-top:10px">42만6천원</div>
  <div class="bigcap">1년이면 약 511만원이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    59㎡는 매달 <b>51만원</b>쯤이에요. 목돈이 있으면
    일부를 <b>보증금</b>으로 돌려 매달 내는 돈을 줄일 수 있어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청하기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내가 어느 특공인지부터", "신혼·생애최초 등 SH 공고문 확인"),
    ("매달 나갈 돈 더해 보기", "대출 이자 + 땅 빌리는 값"),
    ("10년은 못 팔아요", "오래 살 집인지 먼저 생각"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
