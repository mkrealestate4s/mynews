# -*- coding: utf-8 -*-
"""카드뉴스 렌더링용 웹폰트를 로컬로 내려받아 gf-local.css를 생성한다.
사용법: python3 fetch_fonts.py  (tools/ 디렉터리에서 실행, fonts/ + gf-local.css 생성)
프록시 환경에서는 CA 번들 경로를 CURL_CA에 지정할 수 있다."""
import hashlib
import os
import pathlib
import re
import subprocess

BASE = pathlib.Path(__file__).parent
CSS_URL = ("https://fonts.googleapis.com/css2?"
           "family=Noto+Serif+KR:wght@600;900&family=Noto+Sans+KR:wght@400;500;700&display=swap")
# 인스타(임장로그) 전용 테마 — 고정폭 숫자용 세트. gf2-local.css + fonts2/ 로 분리 저장한다.
CSS_URL2 = ("https://fonts.googleapis.com/css2?"
            "family=IBM+Plex+Sans+KR:wght@400;500;600;700&"
            "family=IBM+Plex+Mono:wght@500;700&display=swap")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
CA = os.environ.get("CURL_CA", "/root/.ccr/ca-bundle.crt")


def curl(url, out=None):
    cmd = ["curl", "-sS", "-A", UA]
    if pathlib.Path(CA).exists():
        cmd += ["--cacert", CA]
    if out:
        cmd += ["-o", str(out)]
    cmd.append(url)
    return subprocess.run(cmd, check=True, capture_output=out is None).stdout


def localize(css_url, subdir, out_css):
    css = curl(css_url).decode()
    (BASE / subdir).mkdir(exist_ok=True)
    urls = sorted(set(re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", css)))
    print(len(urls), "font files ->", subdir)
    for u in urls:
        name = hashlib.md5(u.encode()).hexdigest()[:16] + ".woff2"
        p = BASE / subdir / name
        if not p.exists():
            curl(u, out=p)
        css = css.replace(u, f"{subdir}/{name}")
    (BASE / out_css).write_text(css)
    print("wrote", out_css)


def main():
    localize(CSS_URL, "fonts", "gf-local.css")
    localize(CSS_URL2, "fonts2", "gf2-local.css")


if __name__ == "__main__":
    main()
