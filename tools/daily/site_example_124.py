# -*- coding: utf-8 -*-
"""리포트 #124 를 등록한다. 전날 #123 은 07시 데일리라 posted."""
import json
import pathlib

ROOT = pathlib.Path("/home/user/mynews")
SLUG, PRE, NO, DATE = "2026-11-13-mokdong4", "mk4", 124, "2026-11-13"
PREV_DATE, PREV_MARK = "2026-11-12", "\n2026-11-12 · #123"
PUBDATE = "Fri, 13 Nov 2026 07:00:00 +0900"
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
KEYWORD = "목동4단지 재건축 · 시공사 입찰 마감 11/16 14시(15시 개봉) · 3.3㎡당 1,010만원(목동 최고) · 공사비 1조6,389억 · 1,382→2,436가구 최고 49층 · 현설 4개사 · 현대 단독 관측"
CARDTITLE = "목동4단지 재건축, 16일 입찰 마감 경쟁 붙을까"
FULLTITLE = CARDTITLE
SUMMARY = ("목동4단지 재건축 시공사 입찰이 11월 16일 오후 2시 마감됩니다. 3.3㎡당 1,010만원으로 목동에서 가장 높은 공사비입니다. "
           "일정, 공사비 비교, 현설 4개사와 단독 응찰 관측, 목동 다른 단지 결과를 정리했습니다.")
TITLES = [
    "목동4단지 재건축, 16일 입찰 마감 경쟁 붙을까",
    "목동4단지 재건축, 현대건설 혼자 올까?",
    "목동4단지 재건축 입찰 일정·공사비·후보 총정리",
]
TAGS = ["목동4단지재건축", "목동4단지", "목동재건축", "목동시공사선정", "양천구재건축", "현대건설",
        "목동신시가지", "재건축시공사", "재건축입찰", "목동아파트"]
CARDFILES = ["01-cover", "02-when", "03-cost", "04-bid", "05-vote", "06-check"]

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
        it["status"] = "posted"
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
