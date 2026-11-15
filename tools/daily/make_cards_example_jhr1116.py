# -*- coding: utf-8 -*-
"""2026-11-16 #127 중화역 라온프라이빗 센트로. 수치는 gen127.py 와 같다."""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "jhr"
DATEK = "2026-11-16"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">중랑구 중화동 · 7호선 중화역 · 176가구</div>
  <h1 class="serif gtx" style="font-size:66px;margin:14px 0 28px;line-height:1.2">중화역<br>라온프라이빗 센트로</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    내일(17일) <span class="gtx">1순위 해당지역</span><br>
    59㎡ 9억원대, 84㎡ 12억원대</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">공급 · 일정 · 분양가 · 개요 · 체크</div>
</div>""" + foot()

cards["02-mix"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">176가구 중 일반분양 113</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:26px">중화역 라온프라이빗 센트로 공급 구성 · 가구</div>
""" + hb("전체", "176", 100, inside=True) + hb("일반분양 (청약)", "113", 64.2, hi=True, inside=True) \
    + hb("특별공급", "60", 34.1, inside=True) + hb("일반공급 (1·2순위)", "53", 30.1, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">가장 많은 타입</div><div class="dv gtx">84㎡ 35</div></div>
    <div class="box"><div class="dl">면적</div><div class="dv">45~126㎡</div></div>
  </div>
  <div class="note" style="margin-top:14px">※ 특공·일반 배분과 타입별 가구는 분양정보 사이트 기준 · 공고문 확인</div>
</div>""" + foot()

cards["03-sched"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">1순위 17일, 발표 25일</h1>
  <div style="font-size:27px;color:var(--mute)">중화역 라온프라이빗 센트로 청약 일정</div>
  <div class="tl">""" + tlrows([
    ("11.16 (월)", "특별공급", "오늘 청약홈 접수"),
    ("11.17 (화)", "1순위 해당지역", "서울 2년 이상 거주"),
    ("11.18 (수)", "1순위 기타지역", "서울 2년 미만·인천·경기 · 2순위 19일"),
    ("11.25 (수)", "당첨자 발표", "계약 12월 7~9일"),
], pad=16) + """</div>
  <div class="note" style="margin-top:14px">※ 분양캘린더 보도(11월 13~14일) 기준 · 청약홈 공고문으로 확인</div>
</div>""" + foot()

cards["04-price"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">59㎡ 9억대, 84㎡ 12억대</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">타입별 분양가 · 만원</div>
""" + hb("126㎡", "202,100", 100, inside=True) + hb("84㎡", "127,700", 63.2, hi=True, inside=True) \
    + hb("59㎡", "95,600", 47.3, inside=True) + hb("45㎡", "65,800", 32.6, inside=True) + """
  <div class="duo">
    <div class="box"><div class="dl">3.3㎡당</div><div class="dv gtx">3,750만</div></div>
    <div class="box"><div class="dl">59㎡ 평균</div><div class="dv">9억3,530만</div></div>
  </div>
  <div class="note" style="margin-top:14px">※ 분양정보 사이트·스트레이트뉴스 기준 · 확정 금액은 공고문</div>
</div>""" + foot()

cards["05-site"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">7호선 중화역까지 걸어서</div>
  <div class="bignum gtx" style="margin-top:10px">3분</div>
  <div class="bigcap">지하 3층~지상 26층 3개 동 · 시공 라온건설</div>
  <div class="duo">
    <div class="box"><div class="dl">입주 예정</div><div class="dv" style="font-size:44px">2029년 2월</div></div>
  </div>
  <div class="duo" style="margin-top:18px">
    <div class="box"><div class="dl">오피스텔 74실</div><div class="dv" style="font-size:44px">25~26일 따로</div></div>
  </div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:48px;margin-bottom:24px">넣기 전에 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 접수일 17일? 18일?", "서울 2년 이상이면 17일 · 미만·인천·경기는 18일"),
    ("분양가는 공고문 금액으로", "자료마다 조금씩 다르다 · 청약홈 공고가 정본"),
    ("오피스텔 74실은 다른 상품", "이름이 같아도 별개 · 25~26일 따로 접수"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">중화역 라온프라이빗 센트로</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">내일<br>1순위예요</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    <span style="white-space:nowrap">중랑구 역 앞 새 아파트</span><br>
    <span style="white-space:nowrap">59㎡ 9억원대</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">몇 집 · 언제 · 얼마 · 5장으로</div>
</div>""" + foot()

insta["02-howmany"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"몇 집이나 나와요?"</div>
    <div class="a gtx">청약으로 113집이에요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    그중 60집은 오늘 특별공급이라
    내일부터 일반으로 나오는 건 <b>53집</b>쯤이에요.
    84㎡가 35집으로 제일 많아요.</div>
</div>""" + foot()

insta["03-when"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">서울 2년 이상 산 사람</div>
  <div class="bignum gtx" style="margin-top:10px">11월 17일</div>
  <div class="bigcap">2년이 안 됐거나 경기·인천이면 18일이에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    발표는 <b>11월 25일</b>,
    계약은 <b>12월 7~9일</b>이에요.</div>
</div>""" + foot()

insta["04-money"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"얼마예요?"</div>
    <div class="a gtx">59㎡ <span style="white-space:nowrap">9억원대</span>예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    84㎡는 <span style="white-space:nowrap"><b>12억원대</b></span>,
    제일 작은 45㎡는 <span style="white-space:nowrap"><b>6억원대</b></span>예요.
    층마다 달라서 공고에서 내 층 값을 봐요.</div>
</div>""" + foot()

insta["05-officetel"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"오피스텔도 같은 거예요?"</div>
    <div class="a gtx">아니요, 따로예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    이름이 같은 <b>오피스텔 74실</b>은
    25~26일에 따로 받아요.
    아파트 청약과 다른 상품이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">넣기 전에 볼 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 접수일", "서울 2년 이상이면 17일이에요"),
    ("공고 속 내 층 값", "자료마다 조금씩 달라요"),
    ("내 통장 1순위인지", "가입 기간·예치금을 확인해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
