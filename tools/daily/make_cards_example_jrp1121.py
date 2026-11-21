# -*- coding: utf-8 -*-
"""2026-11-21 #133 잠실 래미안아이파크 줍줍 신청자격 (추가 발행 x1). 수치는 gen_example_133.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "jrp"
DATEK = "2026-11-21"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">송파 신천동 · 계약취소 3가구 무순위</div>
  <h1 class="serif gtx" style="font-size:66px;margin:14px 0 28px;line-height:1.2">잠실 래미안아이파크<br>줍줍 신청자격</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    <span style="white-space:nowrap">11월 23일 특공 · 24일 일반</span><br>
    <span style="white-space:nowrap">서울 거주 무주택자, 추첨</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 자격 · 가격 · 현금 · 체크</div>
</div>""" + foot()

cards["02-sched"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">접수는 하루씩, 두 번</h1>
  <div style="font-size:27px;color:var(--mute)">청약홈 · 오전 9시~오후 5시 30분</div>
  <div class="tl">""" + tlrows([
    ("11월 23일", "신혼부부 특공", "84㎡D 1가구"),
    ("11월 24일", "일반공급", "43㎡ · 59㎡A 각 1가구"),
    ("11월 27일", "당첨 발표", "서류 접수 12월 1일"),
    ("12월 4일", "계약", "계약금 30% · 잔금 30일 안"),
], pad=14) + """</div>
</div>""" + foot()

cards["03-who"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">누가 넣을 수 있나</h1>
  <div style="font-size:27px;color:var(--mute)">입주자모집공고일 기준 (보도)</div>
  <div class="tl">""" + tlrows([
    ("서울 거주", "사는 곳", "공고일 기준 서울"),
    ("무주택", "일반공급", "무주택 세대주 · 통장 없어도"),
    ("혼인 7년", "신혼 특공", "무주택 세대구성원"),
    ("추첨", "뽑는 방법", "가점·가입기간 안 봄"),
], pad=14) + """</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡, 실거래의 절반도 안 된다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">이번 공급가 vs 최근 거래 기준 · 원</div>
""" + hb("84㎡ 입주권 실거래 (7월)", "43억", 100, inside=True) + hb("84㎡D 이번 공급가", "18억5,607만", 43.2, hi=True) + hb("59㎡ 보류지 기준가 (6월)", "30억8,000만", 71.6, inside=True) + hb("59㎡A 이번 공급가", "15억7,940만", 36.7, hi=True) + """
  <div class="note" style="margin-top:12px">※ 공급가는 옵션 제외 · 84㎡ 차이 약 24억</div>
</div>""" + foot()

cards["05-cash"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">계약금만 3억~5억대</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">공급가의 30% · 12월 4일 계약</div>
""" + hb("84㎡D 특공", "5억5,682만", 100, hi=True, inside=True) + hb("59㎡A 일반", "4억7,382만", 85.1, inside=True) + hb("43㎡ 일반", "3억3,165만", 59.6, inside=True) + """
  <div class="note" style="margin-top:14px">※ 잔금 70%는 계약 후 30일 안(보도) · 옵션·취득세 별도</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">넣기 전에 볼 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("공고일 기준 서울·무주택", "세대 전체 주택 여부 · 세대주 요건"),
    ("23일 특공, 24일 일반", "유형별 하루씩 · 오후 5시 30분 마감"),
    ("계약금 30% 현금", "84㎡ 5억5,682만 · 잔금은 30일 안"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정본은 청약홈 공고문 · 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">잠실 래미안아이파크 줍줍</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">우리 집도<br>넣을 수 있을까</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">딱 3집, 추첨으로</span><br>
    <span style="white-space:nowrap">11월 23일 · 24일 신청</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">누가 · 언제 · 얼마 · 볼 것</div>
</div>""" + foot()

insta["02-who"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"아무나 넣어도 돼요?"</div>
    <div class="a gtx">서울 살고 집 없는 사람만요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    청약통장은 없어도 돼요. 점수도 안 봐요.
    <b>제비뽑기</b>예요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">신청할 수 있는 날</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:120px">하루씩</div>
  <div class="bigcap">23일 신혼부부, 24일 일반</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    청약홈에서 오전 9시부터 오후 5시 반까지.
    그날 놓치면 <b>끝</b>이에요.</div>
</div>""" + foot()

insta["04-price"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">84㎡(34평) 이번 가격</div>
  <div class="bignum gtx" style="margin-top:10px;font-size:112px">18억 6천</div>
  <div class="bigcap">7월에 같은 평형이 43억에 팔렸어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그래서 다들 <b>로또</b>라고 불러요.
    84㎡는 신혼부부만 넣을 수 있어요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"당첨되면 바로 얼마 내요?"</div>
    <div class="a gtx">가격의 30%를 12월 4일에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    작은 집도 <b style="white-space:nowrap">3억 3천</b>, 34평은 <b style="white-space:nowrap">5억 6천</b>.
    나머지도 한 달 안에 내야 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청 누르기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("우리 집 전체가 무주택?", "배우자·같이 사는 가족까지 봐요"),
    ("세대주인지", "일반공급은 세대주만 돼요"),
    ("현금이 있는지", "2년은 직접 살아야 해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
