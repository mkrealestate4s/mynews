# -*- coding: utf-8 -*-
"""2026-10-24 디에이치 반포124 일반분양. 수치는 gen_example_103.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "dhb1024"
DATEK = "2026-10-24"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">반포주공1단지 1·2·4주구 · 5,007가구</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">디에이치 반포124<br>분양가는 아직 추정</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    일반분양 <span class="gtx">1,832가구</span> · 84㎡ 1,358가구<br>
    모집공고 11월 27일 예정</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">일정 · 평형 · 예상 분양가 · 미확정 · 체크</div>
</div>""" + foot()

cards["02-date"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공고 11월 27일, 특공 12월 7일</h1>
  <div style="font-size:27px;color:var(--mute)">디에이치 반포124 예정 일정 · 10월 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("11월 27일", "입주자 모집공고", "분양가·물량·자격 확정"),
    ("12월 7일", "특별공급 접수", "계획"),
    ("12월 8일", "1순위 접수", "계획"),
    ("12월 16일", "특별공급 당첨 발표", "입주는 2027년 말 목표"),
], pad=14) + """</div>
  <div class="note" style="margin-top:10px">※ 공고 전 계획 일정 · 청약홈 공고문으로 다시 확인</div>
</div>""" + foot()

cards["03-size"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">일반분양 넷 중 셋은 84㎡</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">평형별 일반분양 · 가구 (합계 1,832)</div>
""" + hb("84㎡", "1,358가구", 100, hi=True, inside=True) + hb("59㎡", "281가구", 20.7) \
    + hb("99㎡", "82가구", 6.0) + hb("114㎡ · 130㎡", "각 44가구", 3.2) + hb("80㎡", "23가구", 1.7) + """
  <div class="note" style="margin-top:14px">※ 10월 보도 기준 계획 물량 · 1,801가구로 보도한 매체도 있음</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡ 30억은 가정치입니다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">3.3㎡당 분양가를 가정한 계산 · 억원</div>
""" + hb("84㎡ · 3.3㎡당 1억", "34억", 100, inside=True) + hb("84㎡ · 3.3㎡당 9,000만", "30억6,000만", 90.0, hi=True, inside=True) \
    + hb("59㎡ · 3.3㎡당 1억", "25억", 73.5, inside=True) + hb("59㎡ · 3.3㎡당 9,000만", "22억5,000만", 66.2, inside=True) + """
  <div class="note" style="margin-top:14px">※ 업계 거론 범위 3.3㎡당 8,000만~1억원 · 확정 분양가 아님</div>
</div>""" + foot()

cards["05-unsure"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">아직 확정 아닌 것 3가지</h1>
  <div style="font-size:27px;color:var(--mute)">모두 모집공고 전 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("분양가", "업계 추정", "3.3㎡당 8,000만~1억원 거론"),
    ("일반분양 물량", "31가구 차이", "매체마다 1,832 · 1,801"),
    ("청약 날짜", "계획 단계", "공고 11월 27일 예정"),
], pad=18) + """</div>
  <div class="note" style="margin-top:12px">※ 대출 가능 금액은 공고문 · 은행 상담으로 확인</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">청약 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("공고 11월 27일, 확정 분양가 확인", "지금 30억원은 가정치 · 평형별 금액은 공고문 표"),
    ("청약홈에서 내 순위 미리 확인", "순위·거주 요건은 공고일 기준"),
    ("계약금·중도금 현금 계획", "대출 한도는 공고문 · 은행 상담으로"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">디에이치 반포124</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">"30억 로또"<br>아직 확정 아니에요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    반포 새 아파트 1,832집 분양<br>
    <span style="white-space:nowrap">공고는 11월 27일 예정</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">언제 · 몇 집 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"어디 얘기예요?"</div>
    <div class="a gtx">반포주공1단지를 다시 지은 5,007집 단지예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    10월에 이름이 <b>디에이치 반포124</b>로 바뀌었어요.
    강남에서 <b>39년 만에 가장 큰 분양</b>이라는 보도가 나왔어요.</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">날짜는 이렇게 (예정)</h1>
  <div style="font-size:27px;color:var(--mute)">달력에 적어 두세요</div>
  <div class="tl">""" + tlrows([
    ("11월 27일", "모집공고", "값과 자격이 이날 나와요"),
    ("12월 7일", "특별공급 신청", ""),
    ("12월 8일", "1순위 신청", ""),
    ("12월 16일", "특별공급 발표", ""),
], pad=14) + """</div>
</div>""" + foot()

insta["04-size"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">일반 사람에게 돌아가는 집</div>
  <div class="bignum gtx" style="margin-top:10px">1,832집</div>
  <div class="bigcap">100집 중 74집이 84㎡(30평대)예요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    20평대(59㎡)는 <b>281집</b>, 40평대 이상 큰 집은
    다 합쳐 <b>170집</b>뿐이에요.</div>
</div>""" + foot()

insta["05-budget"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마예요?"</div>
    <div class="a gtx">아직 몰라요. 30평대 <span style="white-space:nowrap">30억원 안팎</span>이라는 추정만 있어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    가정을 조금만 바꿔도 <b>30억6,000만~34억원</b>까지 움직여요.
    대출로 채울 몫이 작아서 <b>현금 계획</b>이 먼저예요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">신청 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("11월 27일 공고 기다리기", "진짜 값은 이날 나와요"),
    ("내 청약 순위 미리 보기", "청약홈에서 바로 확인돼요"),
    ("현금이 얼마 있나 세기", "계약금·중도금부터 계산"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
