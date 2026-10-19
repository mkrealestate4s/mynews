# -*- coding: utf-8 -*-
"""2026-10-20 향남역 그로브 스위첸 당첨자 발표. 수치는 gen99.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "hng1020"
DATEK = "2026-10-20"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">10월 20일 당첨자 발표 · 화성 향남</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">향남역<br>그로브 스위첸</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    1순위 <span class="gtx">0.64 대 1</span>, 공급보다 신청이 적었다<br>
    서류 24~28일 · 계약 11월 2~4일</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">청약 결과 · 일정 · 계약금 · 체크</div>
</div>""" + foot()

cards["02-apply"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">자리보다 신청이 적었다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">공급 가구와 접수 건수 · 가구·건</div>
""" + hb("특별공급 · 공급", "475가구", 59.7, inside=True) + hb("특별공급 · 접수", "139건", 17.5) \
    + hb("1순위 · 공급", "795가구", 100, inside=True) + hb("1순위 · 접수", "511건", 64.3, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 10월 12·13일 청약 집계 기준 · 최종 수치는 청약홈 확인</div>
</div>""" + foot()

cards["03-ratio"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">1순위 평균 경쟁률</div>
  <div class="bignum gtx" style="margin-top:10px">0.64 대 1</div>
  <div class="bigcap">100가구에 64건 신청</div>
  <div class="duo">
    <div class="box"><div class="dl">특별공급</div><div class="dv">0.29 대 1</div><div class="ds">475가구에 139건</div></div>
    <div class="box"><div class="dl">2순위 마감</div><div class="dv">2개 타입</div><div class="ds">71㎡ · 147㎡P, 나머지 미달</div></div>
  </div>
</div>""" + foot()

cards["04-date"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">발표 다음은 서류, 그다음 계약</h1>
  <div style="font-size:27px;color:var(--mute)">향남역 그로브 스위첸 일정 · 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("10월 20일", "당첨자 발표", "청약홈에서 확인"),
    ("10월 24~28일", "당첨자 서류 접수", "5일간 · 부적격이면 당첨 취소"),
    ("11월 2~4일", "정당계약", "계약금 5% 준비"),
], pad=20) + """</div>
  <div class="note" style="margin-top:12px">※ 정확한 일정과 장소는 입주자모집공고로 확인</div>
</div>""" + foot()

cards["05-money"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">5억5천 집이면 계약 때 2,750만원</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">전용 84㎡ 5억5천만원으로 든 예 · 분양가 대비 %</div>
""" + hb("계약금 5%", "2,750만원", 8.3) + hb("중도금 60% · 무이자", "3억3,000만원", 100, inside=True) \
    + hb("잔금 35% · 입주 때", "1억9,250만원", 58.3, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 84㎡ 5억원 중반대 보도 기준 예시 · 주택형별 확정가는 모집공고</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">향남역 그로브 스위첸, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("오늘 청약홈에서 당첨 확인", "당첨됐다면 24~28일 서류 제출"),
    ("잔금 35% 대출부터", "중도금 무이자여도 입주 때 큰돈"),
    ("남은 집은 공고로 확인", "추가 모집 여부는 공고가 나와야 확정"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">향남역 그로브 스위첸</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">오늘<br>당첨 발표예요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    신청한 사람이 집보다 적었어요<br>
    <span style="white-space:nowrap">다음은 서류, 그다음 계약</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">결과 · 일정 · 계약금 · 5장으로</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"몇 명이나 넣었어요?"</div>
    <div class="a gtx">100집에 64명꼴이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    1순위 날 <b>795집</b>에 <b>511명</b>이 신청했어요.
    하루 먼저 받은 특별공급은 <b>100집에 29명</b>이었어요.</div>
</div>""" + foot()

insta["03-type"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"그럼 넣으면 다 붙어요?"</div>
    <div class="a gtx">평형마다 달라요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    <b>71㎡</b>와 <b>147㎡P</b>는 신청이 다 찼어요. 나머지 평형은 신청이 모자랐어요.
    내 결과는 오늘 <b>청약홈</b>에서 확인하세요.</div>
</div>""" + foot()

insta["04-date"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">붙었다면 이 순서예요</h1>
  <div style="font-size:27px;color:var(--mute)">날짜를 달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("오늘", "당첨 확인", "청약홈 · 10월 20일"),
    ("24~28일", "서류 내기", "5일 안에 · 빠지면 취소될 수 있어요"),
    ("11월 2~4일", "계약하기", "계약금 준비"),
], pad=20) + """</div>
</div>""" + foot()

insta["05-money"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">5억5천만원 집이라면 계약 날</div>
  <div class="bignum gtx" style="margin-top:10px">2,750만원</div>
  <div class="bigcap">집값의 5%만 먼저 내요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    중간에 내는 60%는 <b>이자가 없어요</b>. 대신 이사 들어갈 때
    <b>남은 35%(약 1억9천만원)</b>를 한 번에 내야 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">계약하러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("이사 갈 때 낼 돈부터", "남은 35%를 어떻게 낼지 은행에 먼저"),
    ("내 집 값은 공고에서", "5억 중반은 기사 기준이에요"),
    ("남은 집 소식은 공고로", "추가 모집은 공고가 나와야 확정"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
