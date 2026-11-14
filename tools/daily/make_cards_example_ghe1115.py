# -*- coding: utf-8 -*-
"""2026-11-15 #126 경희궁 에피트. 수치는 gen126.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "ghe"
DATEK = "2026-11-15"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">종로 교남동 · 돈의문2구역 · 228가구</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">경희궁<br>에피트</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    84㎡ 최고 <span class="gtx">25억7,484만</span><br>
    분양가상한제 아닙니다</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">공급 · 일정 · 분양가 · 개요 · 체크</div>
</div>""" + foot()

cards["02-mix"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">228가구 중 일반분양 135</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">경희궁 에피트 공급 구성 · 가구</div>
""" + hb("전체", "228", 100, inside=True) + hb("일반분양 (청약)", "135", 59.2, hi=True, inside=True) \
    + hb("그 외", "93", 40.8, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">면적</div><div class="dv gtx">39·59·84㎡</div></div>
    <div class="box"><div class="dl">규모</div><div class="dv">2개 동</div></div>
  </div>
  <div class="note" style="margin-top:14px">※ '그 외'는 전체에서 일반분양을 뺀 값 · 타입별 가구 수는 공고문</div>
</div>""" + foot()

cards["03-sched"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">특공 25일, 1순위 26일</h1>
  <div style="font-size:27px;color:var(--mute)">경희궁 에피트 청약 일정 · 안내 기준</div>
  <div class="tl">""" + tlrows([
    ("11.25 (수)", "특별공급", "청약홈 접수"),
    ("11.26 (목)", "1순위 해당지역", "기타지역은 27일"),
    ("12.4 (금)", "당첨자 발표", "청약홈에서 확인"),
    ("12.16~18", "계약", "입주 2030년 8월 예정"),
], pad=16) + """</div>
  <div class="note" style="margin-top:14px">※ 청약 정보 사이트 안내 · 한 차례 연기 이력, 공고문으로 확인</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">84㎡ 평균 24억7,751만</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">전용 84㎡ 분양가 · 만원</div>
""" + hb("84A 최고", "257,484", 100, hi=True, inside=True) + hb("84B 최고", "251,744", 97.8, inside=True) \
    + hb("84㎡ 평균", "247,751", 96.2, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">3.3㎡당</div><div class="dv gtx">7,450만</div></div>
    <div class="box"><div class="dl">59㎡ 최고</div><div class="dv">18억9,843만</div></div>
  </div>
  <div class="note" style="margin-top:14px">※ 보도·청약 정보 사이트 기준 · 확정 금액은 공고문</div>
</div>""" + foot()

cards["05-site"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">4대문 안 · 지하 6층~지상 21층</div>
  <div class="bignum gtx" style="margin-top:10px">2030.8</div>
  <div class="bigcap">입주 예정. 당첨부터 4년 가까이 기다린다</div>
  <div class="duo">
    <div class="box"><div class="dl">시공</div><div class="dv" style="font-size:44px">HL디앤아이한라</div></div>
  </div>
  <div class="duo" style="margin-top:18px">
    <div class="box"><div class="dl">견본주택</div><div class="dv" style="font-size:44px">은평구 증산동</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">경희궁 에피트, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("분상제 미적용, 시세 비교부터", "당첨이 곧 시세 차익이 아니다 · 옆 단지 실거래와 비교"),
    ("일정은 공고문으로", "한 차례 미뤄졌다 · 특공 25일·1순위 26일 안내"),
    ("투기과열지구 1순위 조건", "통장 기간·예치금·세대주 · 순위(가입)확인서로"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">경희궁 에피트 · 종로</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">로또 청약<br>아니에요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">4대문 안 새 아파트</span><br>
    <span style="white-space:nowrap">84㎡ 25억대</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 집 · 언제 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-howmany"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"몇 집이나 나와요?"</div>
    <div class="a gtx">청약으로 135집이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    전체 228집 중 <b>100집 기준 59집</b>꼴이
    청약으로 나와요. 면적은 39·59·84㎡
    세 가지라 한 타입당 집이 많지 않아요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">특별공급 (안내 기준)</div>
  <div class="bignum gtx" style="margin-top:10px">11월 25일</div>
  <div class="bigcap">일반 1순위는 다음 날 26일이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    발표는 <b>12월 4일</b>로 안내돼 있어요.
    한 번 미뤄진 적이 있어서
    청약홈 공고로 날짜를 꼭 다시 봐요.</div>
</div>""" + foot()

insta["04-money"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"84㎡ 얼마예요?"</div>
    <div class="a gtx">평균 <span style="white-space:nowrap">24억7,751만원</span>이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    제일 비싼 집은 <span style="white-space:nowrap"><b>25억7,484만원</b></span>이에요.
    제일 작은 39㎡도 <span style="white-space:nowrap"><b>11억원대</b></span>예요(보도 기준).</div>
</div>""" + foot()

insta["05-lotto"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"당첨되면 무조건 이득 아니에요?"</div>
    <div class="a gtx">그렇지 않을 수 있어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    분양가를 묶는 <b>상한제가 없는 단지</b>예요.
    주변 시세만큼 받을 수 있어서
    옆 아파트 실제로 팔린 값과 비교해 봐야 해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">넣기 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("옆 단지 실제 값", "경희궁자이 등과 비교해 봐요"),
    ("청약홈 공고 날짜", "25일·26일 안내, 다시 확인해요"),
    ("내 통장 1순위인지", "가입 기간·예치금을 확인해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
