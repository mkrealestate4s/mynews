# -*- coding: utf-8 -*-
"""2026-10-28 아크메르 동탄 2순위. 수치는 gen107 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "akm1028"
DATEK = "2026-10-28"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">화성 동탄구 반송동 · 최고 49층 · 1,808가구</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">아크메르 동탄<br>오늘 2순위</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    특공은 726가구에 269건<br>
    평균 <span class="gtx" style="white-space:nowrap">0.37 대 1, 미달</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">특공 결과 · 일정 · 분양가 · 확인 · 체크</div>
</div>""" + foot()

cards["02-special"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">특공 726가구에 269건</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:28px">95·99 특별공급 합계 · 청약홈 기준 보도</div>
""" + hb("모집 가구", "726", 100, hi=True, inside=True) + hb("접수 건수", "269", 37.1, inside=True) + """
  <div class="bignum gtx" style="font-size:110px;margin-top:22px">0.37 대 1</div>
  <div class="bigcap">100가구에 37명꼴 · 95블록 84㎡C는 특공 마감 보도</div>
</div>""" + foot()

cards["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">2순위 오늘, 발표는 11월 3~4일</h1>
  <div style="font-size:27px;color:var(--mute)">아크메르 동탄 남은 일정 (보도 기준)</div>
  <div class="tl">""" + tlrows([
    ("10월 27일", "1순위 접수 끝", "경쟁률은 청약홈에서 타입별로"),
    ("10월 28일", "2순위 접수", "오늘 · 95·99 같은 날"),
    ("11월 3~4일", "당첨자 발표", "95는 3일, 99는 4일"),
    ("11월 16~18일", "정당계약", ""),
], pad=14) + """</div>
  <div class="note" style="margin-top:12px">※ 1순위 마감 타입은 2순위 접수 없음</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">국평 17억, 계약금만 억대</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">84㎡ 최고 분양가와 계약금 · 억원</div>
""" + hb("99 · 84㎡ 최고", "17억1,680만", 100, hi=True, inside=True) + hb("95 · 84㎡ 최고", "17억1,530만", 99.9, inside=True) \
    + hb("계약금 20%라면", "3억4,336만", 20.0) + hb("계약금 10%라면", "1억7,168만", 10.0) + """
  <div class="note" style="margin-top:14px">※ 계약금은 비율을 가정한 계산 · 실제 비율은 공고문</div>
</div>""" + foot()

cards["05-check"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">2순위 넣기 전 확인할 것</h1>
  <div style="font-size:27px;color:var(--mute)">기사로는 확인되지 않은 것</div>
  <div class="tl">""" + tlrows([
    ("1순위 마감", "내 타입 마감 여부", "청약홈 경쟁률 조회"),
    ("2순위 자격", "통장·거주 요건", "공고문 표로 확인"),
    ("계약금·전매", "10~20% 가정", "비율·제한은 공고문"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 2순위라도 당첨 기록은 남습니다</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">2순위 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 타입 1순위 마감 여부", "청약홈 경쟁률 조회에서 타입별로"),
    ("2순위 자격 공고문 확인", "통장 요건과 거주 요건"),
    ("계약금 현금 계획", "84㎡ 최고가 10%만 해도 1억7,000만원 남짓"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">아크메르 동탄</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">17억 동탄 아파트<br>특공이 남았다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    오늘(28일) 2순위 신청<br>
    <span style="white-space:nowrap">통장 1순위 아니어도 OK</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">결과 · 날짜 · 현금 · 5장으로</div>
</div>""" + foot()

insta["02-people"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"특공 얼마나 몰렸어요?"</div>
    <div class="a gtx">100집 뽑는데 37명 정도 신청했어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    726집에 <b>269명</b>. 남은 집은
    일반 신청(1·2순위)으로 넘어가요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">남은 날짜</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("10월 28일", "2순위 신청", "오늘 하루"),
    ("11월 3~4일", "당첨 발표", "두 단지가 하루 달라요"),
    ("11월 16일~", "계약", ""),
], pad=18) + """</div>
</div>""" + foot()

insta["04-price"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">30평대(84㎡) 가장 비싼 집</div>
  <div class="bignum gtx" style="margin-top:10px">17억</div>
  <div class="bigcap">정확히는 17억1,680만원으로 보도됐어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    특공이 남은 이유로 <b>비싼 값</b>이 먼저 꼽혀요.
    같은 30평대도 층과 타입에 따라 달라요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"당장 얼마 필요해요?"</div>
    <div class="a gtx">계약금이 10%라면 <span style="white-space:nowrap">1억7,000만원</span> 남짓이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    경쟁이 덜해도 <b>내야 할 돈은 같아요</b>.
    실제 비율은 모집공고에 적혀 있어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내가 고른 평형 남았나", "청약홈 경쟁률에서 먼저"),
    ("2순위도 당첨 기록 남아요", "포기할 거면 넣지 않기"),
    ("계약금 현금 세기", "당첨 뒤 바로 내야 해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
