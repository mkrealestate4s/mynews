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


def main():
    css = curl(CSS_URL).decode()
    (BASE / "fonts").mkdir(exist_ok=True)
    urls = sorted(set(re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", css)))
    print(len(urls), "font files")
    for u in urls:
        name = hashlib.md5(u.encode()).hexdigest()[:16] + ".woff2"
        p = BASE / "fonts" / name
        if not p.exists():
            curl(u, out=p)
        css = css.replace(u, f"fonts/{name}")
    (BASE / "gf-local.css").write_text(css)
    print("wrote gf-local.css")


if __name__ == "__main__":
    main()
