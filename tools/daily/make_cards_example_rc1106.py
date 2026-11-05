# -*- coding: utf-8 -*-
"""2026-11-06 #117 재건축 통합지원센터. 수치는 gen_example_117.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "rc1106"
DATEK = "2026-11-06"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">국토부 1차관 · 11월 5일</div>
  <h1 class="serif gtx" style="font-size:70px;margin:14px 0 28px;line-height:1.2">재건축 통합지원센터<br>이달 말 출범</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    인허가와 돈 문제를 <span class="gtx">한 창구</span>에서<br>
    서울 재건축·재개발 매년 3만호 착공 목표</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">무엇 · 속도 · 시점 · 사례 · 체크</div>
</div>""" + foot()

cards["02-what"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">두 창구를 하나로</h1>
  <div style="font-size:27px;color:var(--mute)">재건축 통합지원센터가 합치는 것</div>
  <div class="tl">""" + tlrows([
    ("국토교통부", "인허가 지원", "심의·인가 지연 · 지자체 해석 차이 조정"),
    ("금융위원회", "금융지원센터", "사업비·이주비 대출과 보증"),
    ("전담 관리", "1명이 20곳", "감독원 직원 1명이 수도권 사업장 약 20개"),
], pad=18) + """</div>
  <div class="note" style="margin-top:14px">※ 머니투데이방송 11/5 · 뉴스핌 10/16 보도 · 정식 명칭 확정 전</div>
</div>""" + foot()

cards["03-speed"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">구청은 이미 빨라졌다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">조합설립인가 처리 기간 · 일</div>
""" + hb("법정 처리기한", "30일", 100, inside=True) \
    + hb("송파한양1차 (송파구)", "3일", 10, hi=True) + """
  <div class="note" style="margin-top:14px">※ 한국경제 10/13 보도 · 접수 사흘 만에 인가</div>
</div>""" + foot()

cards["04-when"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">출범 시점이 당겨졌다</div>
  <div class="bignum gtx" style="margin-top:10px">이달 말</div>
  <div class="bigcap">11월 5일 김이탁 1차관 도시정비포럼 축사</div>
  <div class="duo">
    <div class="box"><div class="dl">10월 16일 브리핑</div><div class="dv">연내</div><div class="ds">통합 지원센터로 일원화</div></div>
    <div class="box"><div class="dl">아직 안 나온 것</div><div class="dv">날짜</div><div class="ds">정확한 출범일 · 대상 사업장</div></div>
  </div>
</div>""" + foot()

cards["05-gaepo"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">개포주공6·7단지 사례</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">관리처분계획 인가 · 가구</div>
""" + hb("지금", "1,960", 72.6, inside=True) \
    + hb("재건축 후 · 최고 35층", "2,698", 100, hi=True, inside=True) + """
  <div class="qbox"><div class="q">늘어나는 집</div><div class="a gtx">+738가구 (37.7%)</div></div>
  <div class="note" style="margin-top:14px">※ 한국경제 10/13 보도 · 계획 가구 수는 단계마다 바뀔 수 있다</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">통합지원센터, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("출범일은 공식 발표로", "'이달 말'은 발언, 보도자료 날짜를 따른다"),
    ("우리 단지가 대상인지", "조합·구청 · 정비사업 정보몽땅 확인"),
    ("계획 가구 수는 확정 전", "심의·인가 단계마다 바뀐다"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">재건축 통합지원센터</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">멈춘 재건축,<br>정부가 붙잡는다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">이달 말 새 창구가 열려요</span><br>
    <span style="white-space:nowrap">우리 단지에 뭐가 달라질까?</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">5장으로 정리했어요</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"그게 뭐 하는 곳이에요?"</div>
    <div class="a gtx">허가랑 돈 문제를 한 곳에서.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    지금까지는 허가는 <b>국토부</b>, 대출은 <b>금융위</b>를 따로 찾아야 했어요.
    이제 담당자 한 명이 <b>단지 20곳</b>쯤을 맡아 챙겨요.</div>
</div>""" + foot()

insta["03-fast"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">구청은 벌써 빨라졌어요</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">조합 만드는 허가에 걸린 날</div>
""" + hb("원래 기한", "30일", 100, inside=True) \
    + hb("송파한양1차", "3일", 10, hi=True) + """
  <div class="note" style="margin-top:14px">송파구는 사흘 만에 허가를 내줬어요</div>
</div>""" + foot()

insta["04-goal"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">정부가 내건 목표</div>
  <div class="bignum gtx" style="margin-top:10px">매년 3만호</div>
  <div class="bigcap">서울 재건축·재개발 공사 시작</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    서울은 새 땅이 거의 없어요. 낡은 단지를 다시 지을 때
    <b>늘어나는 집</b>이 사실상 새 집이에요.</div>
</div>""" + foot()

insta["05-gaepo"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마나 늘어나요?"</div>
    <div class="a gtx">100채가 138채로.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    개포주공6·7단지는 지금 <b>1,960채</b>.
    다시 지으면 최고 35층 <b>2,698채</b>가 돼요.
    숫자는 심의 때마다 바뀔 수 있어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">우리 단지 확인 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("문 여는 날은 아직 미정이에요", "정부 공식 발표를 기다려요"),
    ("우리 단지가 대상인지 물어보세요", "조합이나 구청이 가장 정확해요"),
    ("기사 속 가구 수는 바뀔 수 있어요", "심의 단계마다 달라져요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
