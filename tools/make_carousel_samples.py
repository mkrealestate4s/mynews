# -*- coding: utf-8 -*-
"""캐러셀 4:5 (1080x1350) 디자인 후보 5안 — 같은 카드 내용으로 비교."""
import pathlib
BASE = pathlib.Path(__file__).parent
OUT = BASE / "samples"; OUT.mkdir(exist_ok=True)

D = {
"1-ink": dict(
  name="먹지 다크", bg="#1A1714", panel="#231F1A", ink="#F3ECE1", mute="#A0917E",
  accent="#E0913C", accent2="#C4553A", line="#3B3329", rail="#131110", fillgray="#3E362C",
  head="'Gothic A1',sans-serif", hw="900", hls="-0.02em",
  body="'Gowun Dodum',sans-serif", num="'Gothic A1',sans-serif",
  rad="8px", ebls=".14em", ebtr="none", solid=True, grid=False,
),
"2-mono": dict(
  name="터미널 데이터", bg="#0B0B0C", panel="#131316", ink="#EDEDEF", mute="#8A8A93",
  accent="#FFB020", accent2="#FFB020", line="#26262C", rail="#0F0F11", fillgray="#2A2A31",
  head="'IBM Plex Sans KR',sans-serif", hw="700", hls="-0.01em",
  body="'IBM Plex Sans KR',sans-serif", num="'IBM Plex Mono',monospace",
  rad="0", ebls=".26em", ebtr="uppercase", solid=True, grid=True,
),
"3-coral": dict(
  name="미드나잇 코랄", bg="#12132A", panel="#1E1F3D", ink="#F2F3FF", mute="#9A9CC4",
  accent="#FF6B5A", accent2="#FFA36B", line="#2E3060", rail="#171834", fillgray="#343665",
  head="'Gothic A1',sans-serif", hw="900", hls="-0.025em",
  body="'Noto Sans KR',sans-serif", num="'Gothic A1',sans-serif",
  rad="22px", ebls=".12em", ebtr="none", solid=False, grid=False,
),
"4-paper": dict(
  name="신문 명조 (라이트)", bg="#FBFAF7", panel="#FFFFFF", ink="#16130F", mute="#7A6F62",
  accent="#A32B22", accent2="#A32B22", line="#DED7CB", rail="#EFEAE1", fillgray="#CFC6B7",
  head="'Gowun Batang',serif", hw="700", hls="0",
  body="'IBM Plex Sans KR',sans-serif", num="'IBM Plex Sans KR',sans-serif",
  rad="0", ebls=".18em", ebtr="none", solid=True, grid=False,
),
"5-poster": dict(
  name="볼드 모노크롬", bg="#101010", panel="#191919", ink="#FFFFFF", mute="#8E8E8E",
  accent="#FF3B30", accent2="#FF3B30", line="#2B2B2B", rail="#141414", fillgray="#3A3A3A",
  head="'Gothic A1',sans-serif", hw="900", hls="-0.035em",
  body="'Noto Sans KR',sans-serif", num="'Gothic A1',sans-serif",
  rad="0", ebls=".2em", ebtr="uppercase", solid=True, grid=False,
),
}

TPL = """<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">
<link href="gf-local.css" rel="stylesheet"><link href="gf2-local.css" rel="stylesheet">
<style>
:root{{--bg:{bg};--panel:{panel};--ink:{ink};--mute:{mute};--accent:{accent};
  --accent2:{accent2};--line:{line};--rail:{rail};--fillgray:{fillgray};--rad:{rad};
  --fill:{fill}}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:var(--bg);color:var(--ink);font-family:{body};
  display:flex;flex-direction:column;padding:78px 88px 150px;line-height:1.6;position:relative}}
.top{{display:flex;justify-content:space-between;align-items:baseline;flex:none;
  padding-bottom:20px;border-bottom:{topline}}}
.eb{{color:var(--accent);font-weight:700;letter-spacing:{ebls};font-size:23px;
  text-transform:{ebtr};font-family:{num}}}
.pn{{color:var(--mute);font-size:23px;letter-spacing:.1em;font-family:{num}}}
.mid{{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center}}
h1{{font-family:{head};font-weight:{hw};letter-spacing:{hls};font-size:{h1};line-height:1.1;
  color:{h1c}}}
.sub{{font-size:26px;color:var(--mute);margin-top:12px}}
.wrap{{background:var(--panel);border:1px solid var(--line);border-radius:var(--rad);
  padding:34px 32px;margin-top:34px;{gridbg}}}
.zcols{{position:relative;height:300px;display:flex;gap:24px}}
.zcols::before{{content:"";position:absolute;left:0;right:0;top:33%;height:2px;background:var(--line)}}
.zcol{{flex:1;position:relative;height:100%}}
.zbar{{position:absolute;left:50%;transform:translateX(-50%);width:100%;max-width:104px}}
.zbar.up{{bottom:67%;height:var(--h);border-radius:var(--rad) var(--rad) 0 0;background:var(--fill)}}
.zbar.dn{{top:33%;height:var(--h);border-radius:0 0 var(--rad) var(--rad);background:var(--fillgray)}}
.zv{{position:absolute;left:-16px;right:-16px;text-align:center;font-size:28px;font-weight:700;
  font-family:{num}}}
.zv.up{{bottom:calc(67% + var(--h) + 8px);color:var(--accent)}}
.zv.dn{{top:calc(33% + var(--h) + 8px)}}
.zlbl{{display:flex;gap:24px;margin-top:14px}}
.zlbl span{{flex:1;text-align:center;color:var(--mute);font-size:22px;line-height:1.35}}
.close{{font-size:28px;margin-top:26px;word-break:keep-all}}
.close b{{color:var(--ink);font-weight:700}}
.foot{{position:absolute;left:88px;right:88px;bottom:56px}}
.foot .ln{{height:1px;background:var(--line);margin-bottom:18px}}
.foot .rw{{display:flex;justify-content:space-between;color:var(--mute);font-size:21px}}
.tag{{position:absolute;top:78px;left:50%;transform:translateX(-50%);
  font-size:20px;color:var(--mute);letter-spacing:.1em}}
</style></head><body>
<div class="top"><div class="eb">2026 · 8월 부동산 키워드 리포트</div><div class="pn">04 / 06</div></div>
<div class="mid">
  <h1>20대만 늘었다</h1>
  <div class="sub">연령별 신규 주담대 증감 (전 분기 대비 · 만원)</div>
  <div class="wrap">
    <div class="zcols">
      <div class="zcol"><div class="zv up" style="--h:5.5%">+392</div><div class="zbar up" style="--h:5.5%"></div></div>
      <div class="zcol"><div class="zv dn" style="--h:2.4%">−169</div><div class="zbar dn" style="--h:2.4%"></div></div>
      <div class="zcol"><div class="zv dn" style="--h:18.1%">−1,281</div><div class="zbar dn" style="--h:18.1%"></div></div>
      <div class="zcol"><div class="zv dn" style="--h:37.2%">−2,632</div><div class="zbar dn" style="--h:37.2%"></div></div>
      <div class="zcol"><div class="zv dn" style="--h:50%">−3,537</div><div class="zbar dn" style="--h:50%"></div></div>
    </div>
    <div class="zlbl"><span>20대</span><span>60대<br>이상</span><span>50대</span><span>30대</span><span>40대</span></div>
  </div>
  <div class="close">규제는 <b>30·40대</b>에 걸렸다 — 집을 사는 주력 연령대다.</div>
</div>
<div class="foot"><div class="ln"></div><div class="rw">
  <span>부동산 인사이트 — 데일리 키워드 리포트</span><span>2026-08-26</span></div></div>
</body></html>"""

for key, d in D.items():
    fill = d["accent"] if d["solid"] else f'linear-gradient(92deg,{d["accent"]},{d["accent2"]})'
    gridbg = ("background-image:repeating-linear-gradient(to right,transparent 0 63px,"
              f'{d["line"]} 63px 64px);' if d["grid"] else "")
    topline = f'2px solid {d["ink"]}' if key in ("4-paper", "5-poster") else f'1px solid {d["line"]}'
    h1 = "88px" if key == "5-poster" else ("74px" if key == "4-paper" else "78px")
    html = TPL.format(fill=fill, gridbg=gridbg, topline=topline, h1=h1,
                      h1c="var(--ink)" if key != "3-coral" else "var(--ink)", **d)
    (BASE / f"sample-{key}.html").write_text(html, encoding="utf-8")
    print("wrote", key, "·", d["name"])
