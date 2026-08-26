# -*- coding: utf-8 -*-
"""임장로그 릴스 영상 만들기 — 로컬 PC 단독 실행판.

사이트에서 카드 이미지와 나레이션 스크립트를 직접 받아오므로
저장소를 클론할 필요가 없다. 크롬도 쓰지 않는다(자막은 PIL로 그린다).

  이미지(1080x1920) + 자막 + 나레이션 음성  →  1080x1920 / 30fps / H.264 mp4

── 처음 한 번만 (프로젝트 폴더에서) ──────────────────────────────
    .venv\\Scripts\\python.exe -m pip install edge-tts imageio-ffmpeg pillow

── 매일 ───────────────────────────────────────────────────────────
    .venv\\Scripts\\python.exe make_reels_local.py
        (인자 없으면 사이트의 오늘 리포트를 자동으로 집는다)

    .venv\\Scripts\\python.exe make_reels_local.py --slug 2026-08-26-isipdae
    .venv\\Scripts\\python.exe make_reels_local.py --voice ko-KR-InJoonNeural
    .venv\\Scripts\\python.exe make_reels_local.py --no-tts      (무음 · 자막 확인용)

목소리: ko-KR-SunHiNeural(여, 기본) / ko-KR-InJoonNeural(남)
        ko-KR-HyunsuMultilingualNeural (자연스러움 · 지역에 따라 미제공)
"""
import argparse, io, json, pathlib, re, subprocess, sys, tempfile, urllib.request

SITE = "https://mkrealestate4s.github.io/mynews"
W, H, FPS = 1080, 1920, 30
CAP_TOP, CAP_H = 1130, 370          # 자막 띠 (하단 420px 인스타 UI 영역은 침범 안 함)
MARGIN = 88

ap = argparse.ArgumentParser()
ap.add_argument("--slug", help="예: 2026-08-26-isipdae (생략하면 사이트에서 자동 판별)")
ap.add_argument("--base", default=SITE, help="사이트 주소 또는 로컬 저장소 폴더")
ap.add_argument("--voice", default="ko-KR-SunHiNeural")
ap.add_argument("--no-tts", action="store_true", help="음성 없이 무음으로 만든다")
ap.add_argument("--cap", choices=["line", "nar", "sub", "none"], default="line")
ap.add_argument("--font", help="자막 폰트 ttf 경로 (기본: 맑은 고딕 Bold)")
ap.add_argument("--out", help="출력 mp4 경로")
a = ap.parse_args()

LOCAL = not a.base.startswith("http")
BASE = pathlib.Path(a.base) if LOCAL else a.base.rstrip("/")


def fetch(rel, binary=False):
    if LOCAL:
        p = BASE / rel
        return p.read_bytes() if binary else p.read_text(encoding="utf-8")
    url = f"{BASE}/{rel}"
    req = urllib.request.Request(url, headers={"User-Agent": "reels-local/1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


# ── 1) 오늘 리포트 알아내기 ─────────────────────────────────────
slug = a.slug
if not slug:
    slug = json.loads(fetch("publish/manifest.json"))["post"]["slug"]
    print(f"오늘 리포트: {slug}")

# ── 2) 스크립트 받아서 씬 파싱 ──────────────────────────────────
SC = fetch(f"publish/reels/{slug}-script.txt")
scenes = []
for m in re.finditer(r'씬\s*\d+\s*·\s*(\S+?)\s*·\s*(\d+):(\d{2})\s*~\s*(\d+):(\d{2})'
                     r'\n\n\[나레이션\]\n(.+?)\n\n\[자막\]\n(.+?)\n\n'
                     r'(?:\[자막문장\]\n(.+?)\n\n)?\n', SC, re.S):
    img, m1, s1, m2, s2, nar, cap, line = m.groups()
    scenes.append(dict(img=img, dur=(int(m2) * 60 + int(s2)) - (int(m1) * 60 + int(s1)),
                       nar=nar.strip(), cap=cap.strip(), line=(line or "").strip()))
if not scenes:
    sys.exit("씬을 파싱하지 못했습니다 — 스크립트 형식을 확인하세요")
print(f"씬 {len(scenes)}개 · 총 {sum(s['dur'] for s in scenes)}초")

tmp = pathlib.Path(tempfile.mkdtemp(prefix="reels-"))

# ── 3) 자막을 이미지에 그리기 (PIL — 브라우저 불필요) ───────────
from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [a.font] if a.font else []
FONT_CANDIDATES += [
    r"C:\Windows\Fonts\malgunbd.ttf",      # 맑은 고딕 Bold (한국어 윈도우 기본)
    r"C:\Windows\Fonts\malgun.ttf",
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
FONT_PATH = next((f for f in FONT_CANDIDATES if f and pathlib.Path(f).exists()), None)
if not FONT_PATH:
    sys.exit("자막용 한글 폰트를 찾지 못했습니다 — --font 로 ttf 경로를 지정하세요")
print(f"자막 폰트: {FONT_PATH}")


# 폰트에 없어서 두부(□)로 나오기 쉬운 기호를 안전한 문자로 바꾼다.
# 맑은 고딕에는 대부분 있지만, 폰트를 바꿔 쓰는 경우를 대비한다.
SAFE = {"\u2212": "-", "\u2011": "-", "\u2013": "-", "\u2012": "-",
        "\u00a0": " ", "\u2009": " ", "\u200b": ""}


def safe(t):
    for k, v in SAFE.items():
        t = t.replace(k, v)
    return t


def cap_text(sc):
    if a.cap == "none":
        return ""
    if a.cap == "sub":
        return sc["cap"].replace("\n", " ")
    if a.cap == "nar":
        return sc["nar"]
    return sc["line"] or sc["nar"]


def wrap(draw, text, font, maxw):
    """어절 단위 줄바꿈 (한국어는 단어 중간에서 끊지 않는다)."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


frames = []
for i, sc in enumerate(scenes):
    im = Image.open(io.BytesIO(fetch(f"images/cards/reels/{sc['img']}", binary=True))).convert("RGB")
    if im.size != (W, H):
        im = im.resize((W, H))
    text = safe(cap_text(sc))
    if text:
        # 스크림 띠: 카드 마감 문장·푸터를 덮어 자막이 겹치지 않게 한다
        band = Image.new("RGB", (W, CAP_H), (11, 11, 12))
        mask = Image.new("L", (W, CAP_H), 0)
        md = ImageDraw.Draw(mask)
        TOP_FADE, BOT_FADE, OPA = 54, 10, 252
        md.rectangle([0, TOP_FADE, W, CAP_H - BOT_FADE], fill=OPA)
        for y in range(TOP_FADE):                          # 위쪽만 부드럽게 이어붙인다
            md.line([(0, y), (W, y)], fill=int(OPA * y / TOP_FADE))
        for y in range(BOT_FADE):                          # 아래는 짧게 — 푸터를 확실히 덮는다
            md.line([(0, CAP_H - 1 - y), (W, CAP_H - 1 - y)],
                    fill=int(OPA * y / BOT_FADE))
        im.paste(band, (0, CAP_TOP), mask)

        d = ImageDraw.Draw(im)
        maxw = W - MARGIN * 2
        size = 46 if len(text) <= 34 else (42 if len(text) <= 48 else 38)
        font = ImageFont.truetype(FONT_PATH, size)
        lines = wrap(d, text, font, maxw)
        lh = int(size * 1.42)
        block = 6 + 20 + len(lines) * lh                   # 앰버 바 + 여백 + 본문
        y = CAP_TOP + (CAP_H - block) // 2
        d.rectangle([MARGIN, y, MARGIN + 64, y + 6], fill=(255, 176, 32))   # 앰버 바
        y += 6 + 20
        for ln in lines:
            d.text((MARGIN, y), ln, font=font, fill=(255, 255, 255))
            y += lh
    p = tmp / f"f{i:02d}.png"
    im.save(p)
    frames.append(p)
    print(f"  프레임 {i + 1}/{len(scenes)} — {sc['img']}")

# ── 4) 나레이션 음성 (edge-tts · 무료 · 키 불필요) ──────────────
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

audio = None
if not a.no_tts:
    try:
        import asyncio, edge_tts
    except ImportError:
        sys.exit("edge-tts가 없습니다 —  python -m pip install edge-tts")

    async def synth():
        out = []
        for i, sc in enumerate(scenes):
            f = tmp / f"n{i:02d}.mp3"
            await edge_tts.Communicate(sc["nar"], a.voice).save(str(f))
            out.append(f)
            print(f"  음성 {i + 1}/{len(scenes)}")
        return out

    parts = asyncio.run(synth())
    lst = tmp / "a.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
    audio = tmp / "narration.mp3"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error",
                    "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", str(audio)], check=True)
    print(f"음성 합성 완료 ({a.voice})")

# ── 5) mp4 합성 ─────────────────────────────────────────────────
durs = [sc["dur"] for sc in scenes]
concat = tmp / "v.txt"
concat.write_text("".join(f"file '{p.as_posix()}'\nduration {d}\n"
                         for p, d in zip(frames, durs))
                  + f"file '{frames[-1].as_posix()}'\n", encoding="utf-8")

out = pathlib.Path(a.out) if a.out else pathlib.Path(f"{slug}-reels.mp4")
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
subprocess.run(cmd, check=True)

print(f"\n완료 → {out.resolve()}")
print(f"  {out.stat().st_size / 1e6:.1f} MB · {sum(durs)}초 · {W}x{H} · "
      f"{'음성 있음' if audio else '무음'}")
print("  인스타 앱에서 릴스로 올리면 됩니다.")
