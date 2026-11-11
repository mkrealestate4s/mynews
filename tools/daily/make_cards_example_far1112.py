# -*- coding: utf-8 -*-
"""2026-11-12 #123 재건축 용적률 1.2배. 수치는 gen123.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "far"
DATEK = "2026-11-12"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">민간 재건축·재개발 용적률 특례</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">재건축 용적률<br>1.2배</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    3년 한시 · <span class="gtx">강남3구·용산 제외</span><br>
    국회 통과 전 방안</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">숫자 · 조건 · 쟁점 · 일정 · 체크</div>
</div>""" + foot()

cards["02-zone"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">3종 주거는 300%에서 360%로</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">법적 상한과 1.2배 적용 후 · %</div>
""" + hb("2종 일반주거 지금", "250%", 69.4, inside=True) + hb("2종 일반주거 1.2배", "300%", 83.3, inside=True) \
    + hb("3종 일반주거 지금", "300%", 83.3, inside=True) + hb("3종 일반주거 1.2배", "360%", 100, hi=True, inside=True) + """
  <div class="note" style="margin-top:14px">※ 국토계획법 시행령 상한 × 1.2 · 같은 땅에 연면적 20% 더</div>
</div>""" + foot()

cards["03-rule"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">누가 받나, 조건 3가지</h1>
  <div style="font-size:27px;color:var(--mute)">보도된 특례 조건 (법 개정 전 방침)</div>
  <div class="tl">""" + tlrows([
    ("3년", "한시 적용", "시행 뒤 3년 동안만"),
    ("4개 구", "대상 제외", "강남·서초·송파·용산"),
    ("중도위", "먼저 판단", "중앙도시계획위원회가 적용 여부 결정"),
    ("지방위", "세부 심의", "그다음 시·도 위원회가 계획 심의"),
], pad=16) + """</div>
</div>""" + foot()

cards["04-gap"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1.2배냐 1.3배냐, 미정</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">3종 일반주거 기준 · 안별 용적률</div>
""" + hb("지금 법적 상한", "300%", 76.9, inside=True) + hb("정부·여당 1.2배", "360%", 92.3, hi=True, inside=True) \
    + hb("국민의힘 1.3배", "390%", 100, inside=True) + """
  <div class="note" style="margin-top:14px">※ 국민의힘은 공공 정비사업과 같은 1.3배 주장(보도)</div>
</div>""" + foot()

cards["05-when"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">보고는 됐지만 법은 아직</h1>
  <div style="font-size:27px;color:var(--mute)">재건축 용적률 1.2배, 지금까지 흐름</div>
  <div class="tl">""" + tlrows([
    ("9월 1일", "여당 제안", "국토위에서 민간 정비사업 1.2배 제안"),
    ("11월 6일", "연내 통과 불투명", "법 개정 전망 엇갈림(보도)"),
    ("이번 주", "국무회의 보고", "도정법 수정안 반영 검토"),
    ("미정", "국회 통과·시행", "시행령·심의 기준까지 나와야"),
], pad=16) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">용적률 1.2배, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("국회 통과 전 방안", "배수(1.2배·1.3배)와 시행일 모두 미정"),
    ("강남3구·용산 제외", "보도된 방침대로면 4개 구 단지는 대상 아님"),
    ("우리 단지는 위원회 판단", "조합·구청·정비사업 정보몽땅에서 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">재건축 용적률 1.2배</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">아파트를<br>더 높이 짓게?</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">정부가 풀어 주려는 중</span><br>
    <span style="white-space:nowrap">강남·용산은 빠져요</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">뭐가 · 얼마나 · 어디 · 언제</div>
</div>""" + foot()

insta["02-what"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"용적률이 뭐예요?"</div>
    <div class="a gtx">땅에 비해 얼마나 넓게 짓나예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    땅 100평에 용적률 300%면 층마다 합쳐
    <b>300평</b>까지 지을 수 있어요. 숫자가 커지면
    같은 땅에 <b>집을 더 많이</b> 넣을 수 있어요.</div>
</div>""" + foot()

insta["03-howmuch"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">흔한 아파트 땅(3종 주거) 기준</div>
  <div class="bignum gtx" style="margin-top:10px">300 → 360%</div>
  <div class="bigcap">같은 땅에 지을 수 있는 면적이 20% 늘어요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    늘어난 만큼 <b>일반분양</b>을 더 팔 수 있어서
    사업비 부담이 큰 낡은 단지일수록
    도움이 된다는 계산이에요.</div>
</div>""" + foot()

insta["04-where"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"우리 동네도 돼요?"</div>
    <div class="a gtx">강남·서초·송파·용산은 빠져요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    나머지 지역도 자동이 아니에요. 단지마다
    <b>정부 위원회</b>가 먼저 된다, 안 된다를 정해요.
    그리고 <b>3년 동안만</b> 열려요.</div>
</div>""" + foot()

insta["05-when"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"그럼 지금 바로 돼요?"</div>
    <div class="a gtx">아직 법이 안 바뀌었어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    이번 주 정부가 <b>계획을 보고</b>한 단계예요.
    1.2배냐 1.3배냐도 국회에서 아직 다투는 중이고,
    올해 안에 통과될지도 <b>불투명</b>해요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">재건축 집 보러 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("아직 확정 아니에요", "법이 바뀌어야 시작돼요"),
    ("강남3구·용산은 제외", "그 동네는 이 혜택 없어요"),
    ("단지마다 달라요", "조합이나 구청에 물어봐요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
