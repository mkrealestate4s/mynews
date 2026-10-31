# -*- coding: utf-8 -*-
"""리포트 #112 를 등록한다. 전날 #111 은 오후(09:48) 특집이라 07:40 자동등록 전이었으므로 posted 가 아니라 pending."""
import json
import pathlib

ROOT = pathlib.Path("/home/user/mynews")
SLUG, PRE, NO, DATE = "2026-11-01-mokdong9", "mk9", 112, "2026-11-01"
PREV_DATE, PREV_MARK = "2026-10-31", "\n2026-10-31 · #111"
PUBDATE = "Sun, 01 Nov 2026 07:00:00 +0900"
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
KEYWORD = "목동9단지 재건축 시공사 입찰 현설 11/2 · 공사비 2조6,067억(3.3㎡당 980만) · 49층 3,961세대 · 보증금 800억 · 공동도급 불가 · 입찰 마감 2027-01-11 · 목동 5곳 단독 응찰"
CARDTITLE = "목동9단지 재건축 내일 현설, 공사비 2.6조"
FULLTITLE = CARDTITLE
SUMMARY = ("목동9단지 재건축 시공사 입찰 현장설명회가 11월 2일 열립니다. 예정 공사비 2조6,067억원(3.3㎡당 980만원), 최고 49층 3,961세대 계획이고 입찰 마감은 2027년 1월 11일입니다. "
           "목동은 시공사가 정해진 5곳이 모두 단독 응찰이었습니다.")
TITLES = [
    "목동9단지 재건축 내일 현설, 공사비 2.6조",
    "목동9단지 재건축, 첫 경쟁입찰 나올까?",
    "목동9단지 재건축 시공사 입찰 일정·조건 총정리",
]
TAGS = ["목동9단지재건축", "목동9단지", "목동재건축", "목동신시가지", "양천구재건축", "시공사선정", "현장설명회",
        "삼성물산", "GS건설", "재건축입찰"]
CARDFILES = ["01-cover", "02-sched", "03-cost", "04-size", "05-rule", "06-check"]

# ── index.html ────────────────────────────────────────────────
p = ROOT / "index.html"
t = p.read_text(encoding="utf-8")
anchor = "<!-- ⬇ 매일 여기 맨 위에 글 카드를 하나씩 추가 -->\n"
assert t.count(anchor) == 1 and SLUG not in t
card = f'''{anchor}<a class="post" href="posts/{SLUG}.html">
  <div class="date">{DATE.replace("-", ".")} · 키워드 리포트 #{NO}</div>
  <div class="kw gtx">{CARDTITLE}</div>
  <p>{SUMMARY}</p>
  <span class="go">리포트 읽기 →</span>
</a>

'''
p.write_text(t.replace(anchor, card, 1), encoding="utf-8")

# ── sitemap.xml ───────────────────────────────────────────────
p = ROOT / "sitemap.xml"
t = p.read_text(encoding="utf-8")
assert SLUG not in t
t = t.replace(f"    <lastmod>{PREV_DATE}</lastmod>\n    <changefreq>daily</changefreq>",
              f"    <lastmod>{DATE}</lastmod>\n    <changefreq>daily</changefreq>", 1)
head = "  <url>\n    <loc>https://mkrealestate4s.github.io/mynews/posts/"
new = (f"  <url>\n    <loc>{URL}</loc>\n    <lastmod>{DATE}</lastmod>\n"
       f"    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n")
i = t.index(head)
p.write_text(t[:i] + new + t[i:], encoding="utf-8")

# ── feed.xml ──────────────────────────────────────────────────
p = ROOT / "feed.xml"
t = p.read_text(encoding="utf-8")
assert SLUG not in t
item = (f"  <item>\n  <title>{FULLTITLE}</title>\n  <link>{URL}</link>\n"
        f"  <guid>{URL}</guid>\n  <pubDate>{PUBDATE}</pubDate>\n"
        f"  <description>{SUMMARY}</description>\n</item>\n")
i = t.index("  <item>")
p.write_text(t[:i] + item + t[i:], encoding="utf-8")

# ── title.txt (3줄만, 주석·BOM 금지, LF) ───────────────────────
(ROOT / "title.txt").write_bytes(("\n".join(TITLES) + "\n").encode("utf-8"))

# ── titles-archive.txt ────────────────────────────────────────
p = ROOT / "titles-archive.txt"
t = p.read_text(encoding="utf-8")
block = (f"\n{DATE} · #{NO} · {KEYWORD} · posts/{SLUG}.html\n"
         f"  ※ title.txt 반영 완료\n"
         + "".join(f"  {i}) {x}\n" for i, x in enumerate(TITLES, 1)))
i = t.index(PREV_MARK)
p.write_text(t[:i] + block + t[i:], encoding="utf-8")

# ── publish/manifest.json ─────────────────────────────────────
mf = {
    "schema": 1,
    "job_id": f"{SLUG}-01",
    "status": "ready",
    "mode": "draft",
    "requested_at": f"{DATE}T07:05:00+09:00",
    "post": {
        "report_no": NO,
        "slug": SLUG,
        "title": TITLES[0],
        "title_alts": TITLES[1:],
        "body_url": f"https://mkrealestate4s.github.io/mynews/publish/{SLUG}.txt",
        "body_encoding": "utf-8",
        "image_theme": "white",
        "images": [
            {"n": i, "url": f"https://mkrealestate4s.github.io/mynews/images/cards/white/{PRE}-{n}.png"}
            for i, n in enumerate(CARDFILES, 1)],
        "tags": TAGS,
    },
}
(ROOT / "publish/manifest.json").write_text(
    json.dumps(mf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ── publish/queue.json ────────────────────────────────────────
p = ROOT / "publish/queue.json"
q = json.loads(p.read_text(encoding="utf-8"))
q["updated_at"] = f"{DATE}T07:05:00+09:00"
for it in q["items"]:
    if it.get("status") == "designated":
        it["status"] = "pending"
        it["note"] = ((it.get("note", "") + " · ") if it.get("note") else "") + \
            "10/31 오후 특집이라 자동등록 전에 #112 로 교체됨. 사용자 확인 대기(손으로 올렸으면 dropped)."
assert all(it["slug"] != SLUG for it in q["items"])
q["items"].insert(0, {
    "slug": SLUG, "report_no": NO, "date": DATE, "keyword": KEYWORD,
    "status": "designated", "titles": TITLES,
    "body_url": f"https://mkrealestate4s.github.io/mynews/publish/{SLUG}.txt",
})
p.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ── 검증 ──────────────────────────────────────────────────────
raw = (ROOT / "title.txt").read_bytes()
assert not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw
assert len(raw.decode().rstrip("\n").split("\n")) == 3
assert "—" not in raw.decode()
mfj = json.loads((ROOT / "publish/manifest.json").read_text(encoding="utf-8"))
assert mfj["post"]["title"] == raw.decode().split("\n")[0]
for im in mfj["post"]["images"]:
    f = ROOT / "images/cards/white" / im["url"].rsplit("/", 1)[1]
    assert f.exists(), f
qj = json.loads((ROOT / "publish/queue.json").read_text(encoding="utf-8"))
assert [it["status"] for it in qj["items"]].count("designated") == 1
print("index · sitemap · feed · title.txt · archive · manifest · queue 갱신 완료")
print("title.txt 1행 =", raw.decode().split("\n")[0])
