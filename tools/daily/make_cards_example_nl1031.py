# -*- coding: utf-8 -*-
"""2026-10-31 특집 신규택지 6곳 발표. 수치는 gen_example_111.py 와 같다.
"""
import pathlib
import make_cards as base

BASE = pathlib.Path(__file__).parent
TOTAL = "06"
SLUG = "nl1031"
DATEK = "2026-10-31"

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
  <div style="font-size:33px;color:var(--mute);font-weight:500">국토부 10월 29일 · 수도권 공공택지</div>
  <h1 class="serif gtx" style="font-size:76px;margin:14px 0 28px;line-height:1.2">신규택지 6곳 발표,<br>우리 동네 있을까</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.55">
    김포 · 구리 · 하남 · 고양 · 의정부 <span class="gtx">7만6,700가구</span><br>
    착공 2030년 목표 · 토허 해제 11월 3일</div>
  <div style="font-size:28px;color:var(--mute);margin-top:26px">지구 · 누적 · 일정 · 토지거래허가 · 체크</div>
</div>""" + foot()

cards["02-six"] = top("02") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">김포 아라 3만7천, 절반 가까이</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:22px">신규택지 6곳 물량 · 가구</div>
""" + hb("김포 아라", "37,000", 100, hi=True, inside=True) + hb("구리 건원", "14,600", 39.5) \
    + hb("하남 미사 K컬처", "12,000", 32.4) + hb("하남 감일2", "6,500", 17.6) \
    + hb("고양 대곡지식융합", "4,000", 10.8) + hb("의정부 다락원", "2,600", 7.0) + """
  <div class="note" style="margin-top:12px">※ 모두 서울 경계 약 5㎞ 안 · 서울 안 택지는 없음 · 10/29 발표</div>
</div>""" + foot()

cards["03-total"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">8·13 대책 수도권 신규 공공택지 합계</div>
  <div class="bignum gtx" style="margin-top:10px">10만3,900</div>
  <div class="bigcap">가구 · 목표 '10만호+α'를 채웠다</div>
  <div class="duo">
    <div class="box"><div class="dl">8월 먼저 3곳</div><div class="dv">2만7,200</div><div class="ds">남양주도심 · 경기광주역세권2 · 강서 염창</div></div>
    <div class="box"><div class="dl">10월 29일 6곳</div><div class="dv">7만6,700</div><div class="ds">8월 예고 7만3,000보다 3,700 많다</div></div>
  </div>
</div>""" + foot()

cards["04-time"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">착공까지 68개월을 37개월로</h1>
  <div style="font-size:27px;color:var(--mute);margin-bottom:24px">발표에서 착공까지 · 개월</div>
""" + hb("3기 신도시 평균", "68개월", 100, inside=True) + hb("이번 목표", "37개월", 54.4, hi=True, inside=True) + """
  <div class="tl" style="margin-top:18px">""" + tlrows([
    ("2026.10", "후보지 발표", "지구 경계 · 면적은 아직"),
    ("2030년 안", "착공 목표", "공공주택특별법 개정이 전제"),
    ("2033년~", "입주", "가장 빠른 경우"),
], pad=12) + """</div>
</div>""" + foot()

cards["05-toheo"] = top("05") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">11월 3일, 풀리는 것과 그대로인 것</h1>
  <div style="font-size:27px;color:var(--mute)">토지거래허가구역 조정 · 보도 기준</div>
  <div class="tl">""" + tlrows([
    ("풀린다", "서울·인접 그린벨트 토지", "8·13 때 묶은 곳 · 신규택지와 주변은 제외"),
    ("그대로", "서울 아파트 토허제", "이번 해제와 별개"),
    ("다시 묶임", "하남 감일·감북·미사동", "2029년 11월 2일까지 3년 · 송파 일부도 유지"),
], pad=16) + """</div>
</div>""" + foot()

cards["06-check"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:50px;margin-bottom:24px">신규택지 발표 뒤, 이 3가지</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("후보지 땅은 여전히 허가 대상", "지구·주변은 해제 제외 · 필지별로 토지이음 확인"),
    ("입주는 이르면 2033년", "2030년 착공은 목표 · 법 개정이 늦으면 밀린다"),
    ("아파트 토허제와 헷갈리지 않기", "11월 3일 해제는 그린벨트 토지 이야기"),
]) + """
  </div>
  <div class="note" style="margin-top:22px">※ 정보 제공 목적이며 투자 권유가 아닙니다.</div>
</div>""" + foot()

base.render(SLUG, cards, extra_css=COLCSS, themes=["report", "white", "editorial"],
            eyebrow="2026 · 10월 부동산 키워드 리포트")

insta = {}

insta["01-cover"] = top("01") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:36px;color:var(--mute);font-weight:500">신규택지 6곳 발표</div>
  <h1 class="serif gtx" style="font-size:72px;margin:16px 0 28px;line-height:1.22">서울 옆에<br>새 동네 6곳</h1>
  <div style="font-size:35px;color:var(--ink);font-weight:700;line-height:1.5">
    김포 · 구리 · 하남 · 고양 · 의정부<br>
    <span style="white-space:nowrap">우리 동네도 있을까?</span></div>
  <div style="font-size:29px;color:var(--mute);margin-top:28px">어디 · 몇 집 · 언제 · 5장으로</div>
</div>""" + foot()

insta["02-where"] = top("02") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"어디에 제일 많이 지어요?"</div>
    <div class="a gtx">김포예요. 100집 중 48집.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    6곳 합쳐 <b>7만6,700집</b>이에요. 김포 아라 3만7천,
    구리 건원 1만4,600, 하남 두 곳 1만8,500,
    고양 대곡 4천, 의정부 다락원 2,600집이에요.</div>
</div>""" + foot()

insta["03-seoul"] = top("03") + """
<div class="mid" style="justify-content:center">
  <div class="qbox">
    <div class="q">"서울 안에는 없어요?"</div>
    <div class="a gtx">이번엔 없어요.</div>
  </div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    6곳 모두 서울 경계에서 <b>5㎞ 안쪽</b> 경기도예요.
    서울은 앞서 정한 강서 염창 <b>1,000집</b>뿐이고,
    용산 미군기지 땅은 아직 이야기 중이에요.</div>
</div>""" + foot()

insta["04-when"] = top("04") + """
<div class="mid">
  <h1 class="serif" style="font-size:46px;margin-bottom:4px">언제 들어가 살 수 있어요?</h1>
  <div style="font-size:27px;color:var(--mute)">정부가 잡은 목표예요</div>
  <div class="tl">""" + tlrows([
    ("2026년 10월", "어디에 지을지 발표", "경계 · 분양가는 아직"),
    ("2030년 안", "공사 시작", "목표, 늦어질 수 있어요"),
    ("2033년부터", "입주", "가장 빠를 때"),
], pad=16) + """</div>
</div>""" + foot()

insta["05-land"] = top("05") + """
<div class="mid" style="justify-content:center">
  <div style="font-size:31px;color:var(--mute)">서울 그린벨트 땅 거래 허가, 풀리는 날</div>
  <div class="bignum gtx" style="margin-top:10px">11월 3일</div>
  <div class="bigcap">그런데 아파트 얘기는 아니에요</div>
  <div style="font-size:31px;color:var(--body);margin-top:26px;line-height:1.62;word-break:keep-all">
    풀리는 건 <b>그린벨트 땅</b>이에요. 서울 아파트 살 때
    허가받는 규칙은 그대로예요. 하남 감일·미사 쪽 땅은
    오히려 <b>3년 더</b> 묶였어요.</div>
</div>""" + foot()

insta["06-tip"] = top("06") + """
<div class="mid">
  <h1 class="serif" style="font-size:44px;margin-bottom:24px">기억해 둘 것</h1>
  <div class="flow" style="gap:18px">
""" + checks([
    ("당장 살 집은 지금 공고로", "새 동네 입주는 빨라도 7년 뒤"),
    ("후보지 근처 땅은 조심", "여전히 허가가 필요해요"),
    ("청약통장은 계속 넣기", "공공분양은 통장 기간이 중요해요"),
], fs=26) + """
  </div>
  <div class="note" style="margin-top:22px">저장해 두고 보세요</div>
</div>""" + foot()

base.render(SLUG, insta, extra_css=COLCSS, themes=["insta"])
