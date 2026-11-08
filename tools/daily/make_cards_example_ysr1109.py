# -*- coding: utf-8 -*-
"""2026-11-09 #120 해링턴플레이스 용산 리버뷰. 수치는 gen120.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "ysr"
DATEK = "2026-11-09"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">용산구 용문동 · 청년안심주택</div>
  <h1 class="serif gtx" style="font-size:70px;margin:14px 0 28px;line-height:1.2">해링턴플레이스<br>용산 리버뷰</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    분양 아닌 <span class="gtx">월세 임대</span> · 635세대<br>
    11월 12일 1순위 · 월 41만원부터</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">구성 · 일정 · 비용 · 이번 주 청약 · 체크</div>
</div>""" + foot()

cards["02-mix"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">988세대 중 635세대가 임대</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">해링턴플레이스 용산 리버뷰 공급 구성 · 세대</div>
""" + hb("단지 전체", "988", 100, inside=True) + hb("청년안심주택 (이번 모집)", "635", 64.3, hi=True, inside=True) \
    + hb("일반공급", "507", 51.3, inside=True) + hb("특별공급", "128", 13) + """
  <div class="duo">
    <div class="box"><div class="dl">청년</div><div class="dv gtx">25 · 35형</div></div>
    <div class="box"><div class="dl">신혼부부</div><div class="dv">56 · 61형</div></div>
  </div>
</div>""" + foot()

cards["03-sched"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">이번 주 목요일 1순위</h1>
  <div style="font-size:27px;color:var(--mute)">해링턴플레이스 용산 리버뷰 일정</div>
  <div class="tl">""" + tlrows([
    ("10월", "준공 예정", "지어진 집에 들어가는 모집"),
    ("11.12 (목)", "1순위 청약", "분양 캘린더 보도 기준"),
    ("특공", "접수일 확인 필요", "보도에 없음"),
    ("신청 전", "모집공고문 확인", "시간 · 방법 · 서류"),
], pad=16) + """</div>
  <div class="note" style="margin-top:14px">※ 최종 일정은 모집공고 기준 · 보도 기준</div>
</div>""" + foot()

cards["04-cost"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">보증금 6,200만, 월 41만부터</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:18px">보증금 비율 30~50% 선택 · 만원</div>
  <div style="font-size:26px;font-weight:700;margin-bottom:6px">보증금</div>
""" + hb("최저", "6,200", 26.1, hi=True) + hb("최고", "23,800", 100, inside=True) + """
  <div style="font-size:26px;font-weight:700;margin:14px 0 6px">월 임대료</div>
""" + hb("최저", "41", 33.9, hi=True) + hb("최고", "121", 100, inside=True) + """
  <div class="note" style="margin-top:12px">※ 월 41만원 = 연 492만원 · 월 121만원 = 연 1,452만원</div>
</div>""" + foot()

cards["05-week"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">이번 주 전국 청약 12곳</h1>
  <div style="font-size:27px;color:var(--mute)">11월 둘째 주(9~15일) 분양 일정</div>
  <div class="tl">""" + tlrows([
    ("5,215가구", "12곳 청약 접수", "경기 79% · 경기 남부 중심"),
    ("11.12", "용산 리버뷰 1순위", "서울 청년안심주택"),
    ("11.13", "부천대장 하우스토리 디센트", "견본주택 개관 · 548가구"),
    ("8곳 · 11곳", "당첨 발표 · 정당계약", "이번 주 함께 진행"),
], pad=15) + """</div>
  <div class="note" style="margin-top:14px">※ 리얼투데이 집계 · 보도 기준</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">용산 리버뷰, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("분양이 아닌 임대", "당첨 = 임대차 계약 · 기간·갱신은 공고문"),
    ("청년 25·35형 · 신혼 56·61형", "내 유형의 보증금·월세부터 확인"),
    ("자격 · 날짜는 공고문", "소득·자산 기준과 특공 접수일은 보도에 없음"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">해링턴플레이스 용산 리버뷰</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">사는 집이 아니라<br>세 드는 집이에요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">청년 · 신혼부부 635집</span><br>
    <span style="white-space:nowrap">이번 주 목요일 접수</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">누가 · 언제 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-who"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"누가 넣을 수 있어요?"</div>
    <div class="a gtx">청년과 신혼부부예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    작은 집(25·35형)은 <b>청년</b>, 조금 큰 집(56·61형)은
    <b>신혼부부</b> 몫이에요. 소득·재산 기준은
    모집공고에서 꼭 확인하세요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">1순위 접수일</div>
  <div class="bignum gtx" style="margin-top:10px">11월 12일</div>
  <div class="bigcap">이번 주 목요일이에요 (보도 기준)</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    10월에 다 지은 집이라 <b>당첨되면 바로</b>
    들어가는 모집이에요. 특별공급 날짜는
    공고문으로 확인하세요.</div>
</div>""" + foot()

insta["04-money"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"한 달에 얼마예요?"</div>
    <div class="a gtx">월 41만~121만원이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    보증금은 <span style="white-space:nowrap"><b>6,200만~2억3,800만원</b></span>.
    보증금을 많이 내면 월세가 줄어요.
    월 41만원이면 1년에 <b>492만원</b>이에요.</div>
</div>""" + foot()

insta["05-mine"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"나중에 내 집이 되나요?"</div>
    <div class="a gtx">아니요, 임대예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    이름은 분양 아파트 같지만 <b>공공지원 민간임대</b>예요.
    전체 988집 중 <b>635집</b>이 이번 임대 모집이에요.
    몇 년 살 수 있는지는 공고문에 나와요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내가 청년인지 신혼인지", "넣을 수 있는 집 크기가 달라요"),
    ("보증금을 얼마나 낼지", "30~50% 중 고르면 월세가 바뀌어요"),
    ("모집공고문 한 번 읽기", "소득·재산 기준, 접수 시간이 다 있어요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
