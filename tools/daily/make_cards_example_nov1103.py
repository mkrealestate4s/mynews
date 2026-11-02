# -*- coding: utf-8 -*-
"""2026-11-03 11월 청약 일정, 견본주택 5곳. 수치는 gen114 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "nov1103"
DATEK = "2026-11-03"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">11월 첫째 주 · 전국 4,216가구</div>
  <h1 class="serif gtx" style="font-size:72px;margin:14px 0 28px;line-height:1.2">11월 청약 일정<br>견본주택 5곳 연다</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    평택 · 천안 · 시흥 2곳 · 구미<br>
    <span class="gtx" style="white-space:nowrap">개관 11월 6일 · 1순위 10일</span></div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">규모 · 일정 · 이번 주 접수 · 비율 · 체크</div>
</div>""" + foot()

cards["02-size"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">가장 큰 곳은 천안 1,290가구</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:28px">단지 전체 가구수</div>
""" + hb("더샵 천안라크원", "1,290", 100, hi=True, inside=True) + hb("한화포레나 지제역", "1,098", 85.1) \
    + hb("시흥 거모 아테라", "720", 55.8) + hb("엘리프 시흥 더프라임", "338", 26.2) + """
  <div class="note" style="margin-top:14px">※ 형곡 센트럴 아테라는 일반분양 135가구만 보도</div>
</div>""" + foot()

cards["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">6일 개관, 9일 특공, 10일 1순위</h1>
  <div style="font-size:27px;color:var(--mute)">견본주택 5곳 공통 일정 (대부분)</div>
  <div class="tl">""" + tlrows([
    ("11월 6일", "견본주택 개관", "금요일"),
    ("11월 9일", "특별공급", "월요일"),
    ("11월 10~11일", "1순위 · 2순위", "화·수요일"),
    ("11월 17~18일", "당첨자 발표", "단지별 하루씩 다름"),
], pad=14) + """</div>
  <div class="note" style="margin-top:12px">※ 단지별 일정은 청약홈 입주자모집공고</div>
</div>""" + foot()

cards["04-thisweek"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">이번 주 접수: 오늘 계양, 4일 고덕강일</h1>
  <div style="font-size:27px;color:var(--mute)">견본주택보다 먼저 받는 곳</div>
  <div class="tl">""" + tlrows([
    ("11월 3일", "계양 카이브 유보라 1순위", "4일 2순위 · 인천 계양신도시"),
    ("11월 4일", "고덕강일3단지 일반 1순위", "토지임대부 · 발표 11월 26일"),
], pad=22) + """</div>
  <div class="note" style="margin-top:12px">※ 리포트 #113 · #110 보도 기준</div>
</div>""" + foot()

cards["05-share"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">일반분양 몫, 단지마다 다르다</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:28px">전체 중 청약으로 나오는 비율</div>
""" + hb("엘리프 시흥 · 일반", "89.9%", 89.9, hi=True, inside=True) + hb("천안라크원 · 일반", "80.0%", 80, hi=True, inside=True) \
    + hb("거모 아테라 · 신혼희망타운", "66.7%", 66.7) + """
  <div class="note" style="margin-top:14px">※ 304/338 · 1,032/1,290 · 480/720 계산</div>
</div>""" + foot()

cards["06-tips"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">청약 전, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("단지별 접수일", "하루씩 다른 곳 있음 · 청약홈 공고"),
    ("발표일 겹침", "같은 날 발표면 중복 청약 불가가 많음"),
    ("분양가와 전매 조건", "보도에 분양가 없음 · 공고문 확인"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 청약 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 11월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">11월 청약 일정</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">이번 주 금요일<br>모델하우스 5곳</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    평택 · 천안 · 시흥 · 구미<br>
    <span style="white-space:nowrap">새 아파트 4,216가구</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">어디 · 언제 · 몇 채 · 5장으로</div>
</div>""" + foot()

insta["02-where"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">어디에 생기나요</h1>
  <div style="font-size:27px;color:var(--mute)">단지 크기 순서</div>
  <div class="tl">""" + tlrows([
    ("천안", "더샵 천안라크원", "1,290가구 · 34평~"),
    ("평택", "한화포레나 지제역", "1,098가구 · 34평 등"),
    ("시흥", "거모 아테라 · 엘리프", "720가구 · 338가구"),
    ("구미", "형곡 센트럴 아테라", "24평쯤 135가구"),
], pad=14) + """</div>
</div>""" + foot()

insta["03-date"] = top("03") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">날짜만 기억하세요</h1>
  <div style="font-size:27px;color:var(--mute)">대부분 단지 기준</div>
  <div class="tl">""" + tlrows([
    ("11월 6일", "모델하우스 문 열어요", "주말에 구경 가기 좋아요"),
    ("11월 9~11일", "청약 신청", "9일 특별 · 10일 1순위 · 11일 2순위"),
    ("11월 17~18일", "결과 발표", "단지마다 하루씩 달라요"),
], pad=18) + """</div>
</div>""" + foot()

insta["04-share"] = top("04") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"천안 단지, 청약으로 몇 채 나와요?"</div>
    <div class="a gtx">10채 중 8채예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    1,290가구 중 <b style="white-space:nowrap">1,032가구</b>가 일반분양이에요.
    시흥 엘리프는 10채 중 9채예요.</div>
</div>""" + foot()

insta["05-newlywed"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"신혼부부만 넣는 곳도 있어요?"</div>
    <div class="a gtx">시흥 거모 아테라예요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    720가구 중 <b style="white-space:nowrap">480가구</b>가 신혼희망타운이에요.
    100채 중 67채 꼴이에요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">모델하우스 가기 전에</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("내 청약 자격", "청약홈에서 통장 확인"),
    ("발표 날짜 겹침", "같은 날이면 한 곳만 넣기"),
    ("가격표", "모집공고에서 층별 가격 확인"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
