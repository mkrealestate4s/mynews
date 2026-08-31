# -*- coding: utf-8 -*-
"""파비콘·홈화면 아이콘 생성기.

    python3 tools/make_favicon.py

만드는 것 (저장소 루트 기준):
    favicon.svg / favicon.ico              블로그 '부동산 인사이트' (탭 아이콘)
    images/icons/blog-*.png                16·32·48·180·192·512 + maskable
    images/icons/insta-icon.svg
    images/icons/insta-*.png               인스타 '임장로그' (insta.html 홈화면용)
    site.webmanifest / insta.webmanifest

마크는 **지붕 + 오르는 막대 3개**다. 집(부동산)과 데이터(리포트)를 한 칸에 넣은 모양이고,
16px 로 줄여도 지붕 각도와 막대 3단이 살아남는다(다른 후보들은 이 크기에서 뭉갰다).

채널이 둘이므로 아이콘도 둘이다 (CLAUDE.md '채널 두 개' 참조).
같은 실루엣에 팔레트만 바꿔 한 집안으로 보이게 하고, 색이 완전히 달라 탭이나 홈화면에서
두 개를 헷갈리지 않게 한다.
    블로그  네이비 바탕(#0D1829) + 민트 지붕 + 민트→남보라 막대
    인스타  테라코타 바탕(#C2542B) + 아이보리 마크

브라우저를 쓰지 않고 PIL 로 직접 그린다 (4배 수퍼샘플 후 LANCZOS 축소).
아트보드는 32 단위 좌표계이며 SVG 와 좌표가 같으므로 둘이 어긋나지 않는다.
"""
import pathlib
import struct
import zlib

from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
ICONS = ROOT / "images" / "icons"

SS = 4          # 수퍼샘플 배수
ART = 32.0      # 아트보드 한 변 (SVG viewBox 와 동일)

NAVY = "#0D1829"
MINT = "#5EE6D0"
INDIGO = "#7C8CF8"
TERRA = "#C2542B"
IVORY = "#FBF7F0"

# 마크 좌표 (32 단위). SVG 와 공유한다.
ROOF = [(6, 13.6), (16, 6), (26, 13.6)]
ROOF_W = 2.6
BARS = [  # x, y, w, h
    (8.8, 20.8, 4.4, 5.2),
    (13.8, 18.2, 4.4, 7.8),
    (18.8, 15.6, 4.4, 10.4),
]
BAR_R = 1.2
BG_R = 7.0

BLOG = {
    "bg": NAVY,
    "roof": MINT,
    "bars": ["#7E93B4", "#C6D3E4", "grad"],
    "grad": (MINT, INDIGO),
    "roof_w": ROOF_W,
}
INSTA = {
    "bg": TERRA,
    "roof": IVORY,
    # 아이보리 한 색을 투명도 3단으로 쓴다. 색을 하나만 써야 16px 에서 깔끔하다.
    "bars": [IVORY + "80", IVORY + "BF", IVORY],
    "grad": None,
    "roof_w": 2.8,
}


def _rgba(c):
    c = c.lstrip("#")
    if len(c) == 6:
        c += "FF"
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4, 6))


def _diag_gradient(n, c0, c1):
    """왼쪽 아래 → 오른쪽 위 45도 그라디언트."""
    a, b = _rgba(c0), _rgba(c1)
    img = Image.new("RGBA", (n, n))
    px = img.load()
    for y in range(n):
        for x in range(n):
            t = (x + (n - 1 - y)) / (2 * (n - 1))
            px[x, y] = tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(4))
    return img


def draw_icon(size, pal, radius=BG_R, fill=0.0, mark_scale=1.0):
    """아이콘 한 장을 그린다.

    radius      바탕 모서리 둥글기(32 단위). 0 이면 각진 사각형 (iOS·마스커블용).
    fill        바탕을 그라디언트로 채울 비율은 쓰지 않는다. 예약 인자.
    mark_scale  마크를 아트보드 대비 몇 배로 그릴지. 마스커블은 0.62 (안전영역).
    """
    n = size * SS
    k = n / ART                      # 32 단위 → 픽셀
    img = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    if radius > 0:
        d.rounded_rectangle((0, 0, n - 1, n - 1), radius=radius * k, fill=_rgba(pal["bg"]))
    else:
        d.rectangle((0, 0, n - 1, n - 1), fill=_rgba(pal["bg"]))

    # 마크는 별도 레이어에 그려 합성한다 (반투명 막대가 바탕과 섞이도록).
    layer = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)

    off = (ART - ART * mark_scale) / 2

    def P(x, y):
        return ((off + x * mark_scale) * k, (off + y * mark_scale) * k)

    w = pal["roof_w"] * mark_scale * k
    pts = [P(*p) for p in ROOF]
    ld.line(pts, fill=_rgba(pal["roof"]), width=round(w), joint="curve")
    for cx, cy in (pts[0], pts[2]):      # 둥근 끝단 (PIL 은 라인 캡이 각지다)
        r = w / 2
        ld.ellipse((cx - r, cy - r, cx + r, cy + r), fill=_rgba(pal["roof"]))

    for (bx, by, bw, bh), col in zip(BARS, pal["bars"]):
        x0, y0 = P(bx, by)
        x1, y1 = P(bx + bw, by + bh)
        box = (x0, y0, x1, y1)
        rr = BAR_R * mark_scale * k
        if col == "grad":
            mask = Image.new("L", (n, n), 0)
            ImageDraw.Draw(mask).rounded_rectangle(box, radius=rr, fill=255)
            layer.paste(_diag_gradient(n, *pal["grad"]), (0, 0), mask)
        else:
            ld.rounded_rectangle(box, radius=rr, fill=_rgba(col))

    img = Image.alpha_composite(img, layer)
    return img.resize((size, size), Image.LANCZOS)


def svg(pal, radius=BG_R):
    """같은 마크의 벡터판. 크기 제한이 없는 최신 브라우저가 이걸 쓴다."""
    grad = ""
    bars = []
    for (bx, by, bw, bh), col in zip(BARS, pal["bars"]):
        if col == "grad":
            grad = ('<linearGradient id="g" x1="0" y1="1" x2="1" y2="0">'
                    f'<stop offset="0" stop-color="{pal["grad"][0]}"/>'
                    f'<stop offset="1" stop-color="{pal["grad"][1]}"/></linearGradient>')
            f = 'fill="url(#g)"'
        elif len(col) == 9:
            f = f'fill="{col[:7]}" opacity="{int(col[7:], 16) / 255:.2f}"'
        else:
            f = f'fill="{col}"'
        bars.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" '
                    f'rx="{BAR_R}" {f}/>')
    roof = " ".join(f"{'ML'[i > 0]}{x} {y}" for i, (x, y) in enumerate(ROOF))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
            f'<defs>{grad}</defs>'
            f'<rect width="32" height="32" rx="{radius}" fill="{pal["bg"]}"/>'
            f'<path d="{roof}" fill="none" stroke="{pal["roof"]}" '
            f'stroke-width="{pal["roof_w"]}" stroke-linecap="round" '
            'stroke-linejoin="round"/>'
            + "".join(bars) + "</svg>")


def write_ico(path, images):
    """PIL 의 ICO 저장은 원본 한 장을 리샘플하므로, 크기별로 따로 그린 PNG 를 직접 묶는다."""
    blobs = []
    for im in images:
        raw = im.tobytes()
        w, h = im.size

        def chunk(tag, data):
            c = tag + data
            return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c))

        rows = b"".join(b"\0" + raw[y * w * 4:(y + 1) * w * 4] for y in range(h))
        png = (b"\x89PNG\r\n\x1a\n"
               + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
               + chunk(b"IDAT", zlib.compress(rows, 9))
               + chunk(b"IEND", b""))
        blobs.append((w, h, png))

    out = struct.pack("<HHH", 0, 1, len(blobs))
    off = 6 + 16 * len(blobs)
    for w, h, png in blobs:
        out += struct.pack("<BBBBHHII", w % 256, h % 256, 0, 0, 1, 32, len(png), off)
        off += len(png)
    path.write_bytes(out + b"".join(p for _, _, p in blobs))


def main():
    ICONS.mkdir(parents=True, exist_ok=True)

    (ROOT / "favicon.svg").write_text(svg(BLOG), encoding="utf-8")
    (ICONS / "insta-icon.svg").write_text(svg(INSTA), encoding="utf-8")

    made = []
    for size in (16, 32, 48, 192, 512):
        p = ICONS / f"blog-{size}.png"
        draw_icon(size, BLOG).save(p)
        made.append(p)
    # iOS 홈화면·마스커블은 바탕이 꽉 차야 한다 (기기가 자기 모양으로 잘라낸다).
    draw_icon(180, BLOG, radius=0).save(ICONS / "blog-apple-180.png")
    draw_icon(512, BLOG, radius=0, mark_scale=0.62).save(ICONS / "blog-maskable-512.png")

    for size in (32, 180, 192, 512):
        rad = 0 if size == 180 else BG_R
        draw_icon(size, INSTA, radius=rad).save(ICONS / f"insta-{size}.png")
    draw_icon(512, INSTA, radius=0, mark_scale=0.62).save(ICONS / "insta-maskable-512.png")

    write_ico(ROOT / "favicon.ico",
              [draw_icon(s, BLOG) for s in (16, 32, 48)])

    print("favicon.svg, favicon.ico, images/icons/*.png 생성 완료")


if __name__ == "__main__":
    main()
