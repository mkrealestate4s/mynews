# -*- coding: utf-8 -*-
"""2026-11-19 #130 디에이치 반포124 분양가 vs 원베일리. 수치는 gen130.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "dbw"
DATEK = "2026-11-19"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">반포주공1단지 1·2·4주구 · 모집공고 11월 27일 예정</div>
  <h1 class="serif gtx" style="font-size:70px;margin:14px 0 28px;line-height:1.2">디에이치 반포124<br>vs 원베일리</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    84㎡ 분양가 추정 <span class="gtx" style="white-space:nowrap">30억대</span><br>
    옆 단지 84㎡ 실거래 <span style="white-space:nowrap">70억대</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">비교 · 일정 · 평형 · 자금 · 체크</div>
</div>""" + foot()

cards["02-vs"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡, 옆 단지 절반 아래</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">전용 84㎡ 가격 비교 · 억원</div>
""" + hb("원베일리 실거래 (2025.6)", "72억", 100, inside=True) + hb("원베일리 실거래 (2025.3)", "70억", 97.2, inside=True) + hb("반포124 · 3.3㎡당 1억 가정", "34억", 47.2, hi=True, inside=True) + hb("반포124 · 3.3㎡당 9,000만 가정", "30.6억", 42.5, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 반포124 분양가는 업계 추정으로 계산한 값 · 확정 전</div>
</div>""" + foot()

cards["03-when"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">공고까지 8일 남았다</h1>
  <div style="font-size:27px;color:var(--mute)">디에이치 반포124 청약 일정 (계획)</div>
  <div class="tl">""" + tlrows([
    ("11월 27일", "입주자 모집공고", "확정 분양가가 여기서 나온다"),
    ("12월 7일", "특별공급 접수", "보도된 계획 일정"),
    ("12월 8일", "일반 1순위 접수", "서울 거주 우선 여부는 공고로"),
    ("12월 16일", "특별공급 당첨 발표", "이후 일정은 공고 확인"),
], pad=14) + """</div>
</div>""" + foot()

cards["04-type"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">넷 중 세 집은 84㎡</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">일반분양 1,832가구 평형 구성 · 가구</div>
""" + hb("84㎡", "1,358", 100, hi=True, inside=True) + hb("59㎡", "281", 20.7) + hb("99㎡", "82", 6.0) + hb("114㎡ · 130㎡ (각)", "44", 3.2) + hb("80㎡", "23", 1.7) + """
  <div class="note" style="margin-top:10px">※ 보도 기준 · 다른 매체는 1,801가구 · 최종은 공고로</div>
</div>""" + foot()

cards["05-cash"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">대출은 2억, 나머지는 내 돈</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">84㎡ · 3.3㎡당 9,000만 가정</div>
  <div class="tl">""" + tlrows([
    ("30.6억", "추정 분양가", "84㎡ × 3.3㎡당 9,000만원 가정"),
    ("2억", "잔금 주담대 한도", "분양가 25억 넘는 경우 (보도)"),
    ("28.6억", "자기 돈", "계약금·중도금 방식은 공고로"),
], pad=16) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">반포124 청약 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("11월 27일 공고문", "확정 분양가·거주 요건은 여기서"),
    ("자금 계획 먼저", "25억 넘으면 잔금 대출 2억"),
    ("시세차익은 관측", "옆 단지 값은 1년 전 거래"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">반포 새 아파트 청약</div>
  <h1 class="serif gtx" style="font-size:70px;margin:16px 0 28px;line-height:1.22">옆 단지보다<br>얼마나 쌀까</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">디에이치 반포124</span><br>
    <span style="white-space:nowrap">공고 11월 27일 예정</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">가격 · 날짜 · 크기 · 필요한 돈</div>
</div>""" + foot()

insta["02-price"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마예요?"</div>
    <div class="a gtx">아직 몰라요. 30억 안팎이라는 말이 돌아요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    방 3개 크기(84㎡) 기준 추정이에요.
    진짜 가격은 <b>11월 27일 공고</b>에 나와요.</div>
</div>""" + foot()

insta["03-next"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">바로 옆 원베일리 같은 크기</div>
  <div class="bignum gtx" style="margin-top:10px">70억대</div>
  <div class="bigcap">작년에 실제로 팔린 값이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그래서 '로또'라는 말이 나와요.
    다만 <b>1년 전 거래</b>라 지금 값은 달라요.</div>
</div>""" + foot()

insta["04-size"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"어떤 크기가 많아요?"</div>
    <div class="a gtx">100집 중 74집이 방 3개(84㎡)예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    일반에 나오는 집은 <b>1,832집</b> 안팎이에요.
    작은 집(59㎡)은 15집 정도예요.</div>
</div>""" + foot()

insta["05-cash"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">30억짜리라면 은행에서 빌릴 수 있는 돈</div>
  <div class="bignum gtx" style="margin-top:10px">2억</div>
  <div class="bigcap">나머지 28억은 내 돈이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    25억 넘는 집은 잔금 대출이 <b>2억까지</b>라고 해요.
    내 한도는 은행에 꼭 물어봐요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">청약 넣기 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("공고문 날짜", "11월 27일, 진짜 가격이 나와요"),
    ("내 돈 계산", "대출 2억 빼고 얼마 있는지"),
    ("집 없는지 확인", "자격은 공고문에서 확인해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
