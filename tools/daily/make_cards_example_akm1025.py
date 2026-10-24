# -*- coding: utf-8 -*-
"""2026-10-25 아크메르 동탄 청약. 수치는 gen104 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "akm1025"
DATEK = "2026-10-25"

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
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">아크메르 동탄 청약<br>내일 특별공급</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    특공 10월 26일 · 1순위 27일<br>
    84㎡ 최고 <span class="gtx" style="white-space:nowrap">17억1,680만원</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 이번 주 물량 · 분양가 · 확인 · 체크</div>
</div>""" + foot()

cards["02-date"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">특공 26일, 1순위 27일</h1>
  <div style="font-size:27px;color:var(--mute)">아크메르 동탄 95·99 청약 일정 (보도 기준)</div>
  <div class="tl">""" + tlrows([
    ("10월 26일", "특별공급", "95·99 같은 날"),
    ("10월 27~28일", "1순위 · 2순위", ""),
    ("11월 3~4일", "당첨자 발표", "95는 3일, 99는 4일 · 하루 차"),
    ("11월 16~18일", "정당계약", ""),
], pad=14) + """</div>
  <div class="note" style="margin-top:12px">※ 접수 시간은 청약홈 공고문으로 확인</div>
</div>""" + foot()

cards["03-week"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">이번 주 청약 단지 중 가장 크다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">10월 26일~11월 1일 청약 · 가구(오피스텔은 실)</div>
""" + hb("아크메르 동탄 (화성)", "1,808", 100, hi=True, inside=True) + hb("트리븐센텀 1·2단지 (부산)", "1,644", 90.9, inside=True) \
    + hb("신분평 에피트 더웨이시티 (청주)", "992", 54.9, inside=True) + hb("GD메트로타워 (서울 · 오피스텔)", "770", 42.6, inside=True) \
    + hb("매교역 펠루시드 (수원 · 오피스텔)", "154", 8.5) + """
  <div class="note" style="margin-top:14px">※ 리얼투데이 집계 보도 · 전국 8곳 5,555가구</div>
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
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공고문에서 확인할 것 3가지</h1>
  <div style="font-size:27px;color:var(--mute)">기사로는 확인되지 않은 것</div>
  <div class="tl">""" + tlrows([
    ("중복 청약", "95·99 발표일 하루 차", "함께 넣는 조건은 공고문으로"),
    ("계약금 비율", "10~20% 가정", "위 계산은 가정치"),
    ("전매·재당첨", "규제 적용 여부", "공고문에서 직접 확인"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 대출 가능 금액은 은행 상담으로 확인</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">청약 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("특공 26일 · 1순위 27일 날짜 확인", "2순위 28일 · 청약홈 접수 시간 미리 보기"),
    ("95·99 중복 청약 조건 확인", "발표일이 하루 다름 · 공고문 조항 읽기"),
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
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">동탄 30평대<br>17억 시대</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    49층 새 아파트 1,808집<br>
    <span style="white-space:nowrap">내일(26일)부터 신청</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">언제 · 얼마 · 현금 · 5장으로</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"어디 얘기예요?"</div>
    <div class="a gtx">화성 동탄 반송동에 짓는 49층짜리 1,808집이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    <b>95</b>와 <b>99</b>, 두 단지로 나눠 받아요.
    이번 주 전국에서 신청받는 곳 중 <b>가장 커요</b>.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">날짜는 이렇게</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("10월 26일", "특별공급 신청", "신혼·생애최초 등"),
    ("10월 27일", "1순위 신청", ""),
    ("11월 3~4일", "당첨 발표", "두 단지가 하루 달라요"),
    ("11월 16일~", "계약", ""),
], pad=14) + """</div>
</div>""" + foot()

insta["04-price"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">30평대(84㎡) 가장 비싼 집</div>
  <div class="bignum gtx" style="margin-top:10px">17억</div>
  <div class="bigcap">정확히는 17억1,680만원으로 보도됐어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    "동탄 새 기록"이라는 말이 나왔어요.
    같은 30평대도 <b>층과 타입</b>에 따라 값이 달라요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"당장 얼마 필요해요?"</div>
    <div class="a gtx">계약금이 10%라면 <span style="white-space:nowrap">1억7,000만원</span> 남짓이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    20%라면 <b>3억4,000만원</b> 남짓이에요.
    실제 비율은 <b>모집공고</b>에 적혀 있어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내일 특공, 모레 1순위", "날짜부터 달력에"),
    ("두 단지 같이 넣어도 되나", "공고문에서 먼저 확인"),
    ("계약금 현금 세기", "당첨 뒤 바로 내야 해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
