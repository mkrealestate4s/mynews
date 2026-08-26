# -*- coding: utf-8 -*-
"""릴스 스크립트 + 9:16 카드로 자막이 구워진 mp4를 만든다.

  이미지(1080x1920) + 자막 + 나레이션 음성  →  1080x1920 / 30fps / H.264 mp4

자막은 ffmpeg drawtext 대신 **크롬으로 카드 위에 얹어 스크린샷**한다.
정적 ffmpeg 빌드에는 drawtext(libfreetype)가 없고, 어차피 카드와 같은
폰트·색을 쓰는 편이 타이포가 깔끔하다.

음성은 두 경로 중 하나:
  --audio <mp3>   이미 만들어 둔 나레이션 파일을 붙인다 (클로바더빙 등)
  --tts edge      edge-tts(무료·키 불필요)로 씬별 음성을 만들어 붙인다
                  → pip install edge-tts  (로컬 PC에서 권장)
둘 다 없으면 무음 트랙을 넣는다 (자막·타이밍 확인용).

사용법:
  python3 tools/make_reels_video.py <slug> [--tts edge] [--audio out.mp3]
      [--voice ko-KR-SunHiNeural] [--out publish/reels/<slug>.mp4]
"""
import argparse, json, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/opt/pw-browsers/chromium"
W, H, FPS = 1080, 1920, 30

ap = argparse.ArgumentParser()
ap.add_argument("slug")                       # 예: isipdae
ap.add_argument("--script")                   # 기본: publish/reels/*-<slug>-script.txt
ap.add_argument("--cards")                    # 기본: images/cards/reels
ap.add_argument("--fonts")                    # gf-local.css / gf2-local.css 가 있는 폴더
ap.add_argument("--audio")                    # 붙일 mp3/m4a
ap.add_argument("--tts", choices=["edge"])    # edge-tts로 직접 생성
ap.add_argument("--voice", default="ko-KR-SunHiNeural")
ap.add_argument("--cap", choices=["line", "nar", "sub", "none"], default="line",
                help="자막 원문: line=[자막문장](기본, 숫자 표기) / nar=[나레이션](한글 숫자) "
                     "/ sub=[자막] 키워드 / none=없음")
ap.add_argument("--out")
a = ap.parse_args()

script = pathlib.Path(a.script) if a.script else next(
    (ROOT / "publish/reels").glob(f"*-{a.slug}-script.txt"))
cards = pathlib.Path(a.cards) if a.cards else ROOT / "images/cards/reels"
out = pathlib.Path(a.out) if a.out else ROOT / f"publish/reels/{script.stem.replace('-script','')}.mp4"

# ── 1) 씬 파싱 ──────────────────────────────────────────────────
SC = script.read_text(encoding="utf-8")
scenes = []
for m in re.finditer(r'씬\s*\d+\s*·\s*(\S+?)\s*·\s*(\d+):(\d{2})\s*~\s*(\d+):(\d{2})'
                     r'\n\n\[나레이션\]\n(.+?)\n\n\[자막\]\n(.+?)\n\n'
                     r'(?:\[자막문장\]\n(.+?)\n\n)?\n', SC, re.S):
    img, m1, s1, m2, s2, nar, cap, line = m.groups()
    scenes.append(dict(img=img,
                       start=int(m1) * 60 + int(s1), end=int(m2) * 60 + int(s2),
                       nar=nar.strip(), cap=cap.strip(),
                       line=(line or "").strip()))
assert scenes, "씬을 파싱하지 못했습니다 — 스크립트 형식을 확인하세요"
for sc in scenes:
    assert (cards / sc["img"]).exists(), f"카드 없음: {cards / sc['img']}"
print(f"씬 {len(scenes)}개 · 총 {scenes[-1]['end']}초")

tmp = pathlib.Path(tempfile.mkdtemp(prefix="reelsvid-"))

# ── 2) 자막을 카드 위에 구워 프레임 만들기 ──────────────────────
# 자막 띠: 카드 본문이 끝나는 y≈1130 아래를 스크림으로 덮고 그 위에 얹는다.
# 카드의 마감 문장·푸터와 겹치지 않게 완전히 가린다.
# 하단 420px는 인스타 UI 영역이라 침범하지 않는다.
CAP_TOP, CAP_H = 1130, 370
FRAME_TPL = """<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="{gf}" rel="stylesheet"><link href="{gf2}" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#0B0B0C}}
.bg{{position:absolute;inset:0;width:{W}px;height:{H}px;display:block}}
.band{{position:absolute;left:0;right:0;top:{ct}px;height:{ch}px;
  background:linear-gradient(to bottom,rgba(11,11,12,0) 0,rgba(11,11,12,.96) 46px,
    rgba(11,11,12,.96) calc(100% - 46px),rgba(11,11,12,0) 100%)}}
.cap{{position:absolute;left:88px;right:88px;top:{ct}px;height:{ch}px;
  display:flex;flex-direction:column;justify-content:center;
  font-family:'IBM Plex Sans KR',sans-serif;font-weight:700;
  font-size:{cf}px;line-height:1.42;color:#fff;letter-spacing:-0.01em;
  word-break:keep-all}}
.cap .bar{{width:64px;height:6px;background:#FFB020;margin-bottom:20px;flex:none}}
</style></head><body>
<img class="bg" src="{img}">
<div class="band"></div>
<div class="cap"><span class="bar"></span><span>{cap}</span></div>
</body></html>"""

def font_css(name):
    """gf-local.css / gf2-local.css 를 찾는다 (없으면 시스템 폰트로 폴백)."""
    bases = []
    if a.fonts:
        bases.append(pathlib.Path(a.fonts))
    bases += [ROOT / "tools", cards, pathlib.Path.cwd()]
    for base in bases:
        p = base / name
        if p.exists():
            return p.resolve().as_uri()
    return ""


if not font_css("gf2-local.css"):
    print("주의: gf2-local.css를 못 찾았습니다 — 자막 폰트가 대체 서체로 나옵니다.\n"
          "      --fonts <폰트 폴더> 로 지정하거나 tools/fetch_fonts.py 를 먼저 실행하세요.")

def cap_text(sc):
    """자막 문구.

    기본은 [자막문장] — 나레이션과 같은 문장이지만 숫자를 아라비아 숫자로 쓴 것.
    나레이션은 TTS 오독을 막으려 숫자를 한글로 적으므로("삼천오백만") 자막에 그대로
    쓰면 읽기 어렵다. [자막] 키워드 블록은 카드 내용과 겹치는 경우가 많다.
    """
    if a.cap == "none":
        return ""
    if a.cap == "sub":
        return sc["cap"].replace("\n", "<br>")
    if a.cap == "nar":
        return sc["nar"]
    return sc.get("line") or sc["nar"]


def cap_size(txt):
    """줄 수를 보고 폰트를 줄여 띠 안에 들어오게 한다 (한 줄 ≈ 20자 @44px)."""
    n = len(re.sub(r"<[^>]+>", "", txt))
    return 46 if n <= 34 else (42 if n <= 48 else 38)


frames = []
for i, sc in enumerate(scenes):
    cap = cap_text(sc)
    html = FRAME_TPL.format(
        W=W, H=H, ct=CAP_TOP, ch=CAP_H, cf=cap_size(cap),
        gf=font_css("gf-local.css"), gf2=font_css("gf2-local.css"),
        img=(cards / sc["img"]).resolve().as_uri(),
        cap=cap)
    hp = tmp / f"frame{i:02d}.html"
    hp.write_text(html, encoding="utf-8")
    png = tmp / f"frame{i:02d}.png"
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", f"--window-size={W},{H}",
                    "--virtual-time-budget=20000", f"--screenshot={png}", str(hp)],
                   check=True, capture_output=True)
    frames.append(png)
    print(f"  프레임 {i + 1}/{len(scenes)} — {sc['img']}")

from PIL import Image
for p in frames:
    im = Image.open(p)
    if im.size != (W, H):
        im.crop((0, 0, W, H)).save(p)

# ── 3) 나레이션 음성 ────────────────────────────────────────────
audio = pathlib.Path(a.audio) if a.audio else None
if a.tts == "edge":
    try:
        import edge_tts, asyncio
    except ImportError:
        sys.exit("edge-tts가 없습니다 — pip install edge-tts")

    async def synth():
        parts = []
        for i, sc in enumerate(scenes):
            f = tmp / f"nar{i:02d}.mp3"
            await edge_tts.Communicate(sc["nar"], a.voice).save(str(f))
            parts.append(f)
        return parts

    parts = asyncio.run(synth())
    lst = tmp / "audio.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
    audio = tmp / "narration.mp3"
    subprocess.run([FF := __import__("imageio_ffmpeg").get_ffmpeg_exe(),
                    "-y", "-hide_banner", "-loglevel", "error",
                    "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", str(audio)], check=True)
    print(f"  edge-tts 음성 {len(parts)}개 합성 완료 ({a.voice})")

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

# 씬 길이: 음성이 있으면 실제 길이에 맞추는 편이 좋지만, 스크립트 초수가
# 이미 글자 수로 산출된 값이므로 그대로 쓴다(sync_reels_script.py가 계산).
durs = [sc["end"] - sc["start"] for sc in scenes]

concat = tmp / "video.txt"
lines = []
for p, d in zip(frames, durs):
    lines.append(f"file '{p}'\nduration {d}\n")
lines.append(f"file '{frames[-1]}'\n")   # concat demuxer는 마지막 항목을 한 번 더 요구한다
concat.write_text("".join(lines), encoding="utf-8")

cmd = [FF, "-y", "-hide_banner", "-loglevel", "error",
       "-f", "concat", "-safe", "0", "-i", str(concat)]
if audio:
    cmd += ["-i", str(audio)]
else:
    cmd += ["-f", "lavfi", "-t", str(sum(durs)),
            "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"]
cmd += ["-map", "0:v:0", "-map", "1:a:0",
        "-vf", f"fps={FPS},format=yuv420p",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart"]
if audio:
    cmd += ["-shortest"]
cmd += [str(out)]

out.parent.mkdir(parents=True, exist_ok=True)
subprocess.run(cmd, check=True)
size = out.stat().st_size / 1e6
print(f"완료: {out}  ({size:.1f} MB · {sum(durs)}초 · {W}x{H} · {FPS}fps"
      f" · 음성 {'있음' if audio else '무음'})")
shutil.rmtree(tmp, ignore_errors=True)
