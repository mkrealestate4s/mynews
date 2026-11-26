# -*- coding: utf-8 -*-
"""리포트 #140 (2026-11-27 금 데일리) 를 등록한다. 전날 추가 발행 #139(designated) 은 posted 로 내린다."""
import json
import pathlib

ROOT = pathlib.Path("/home/user/mynews")
SLUG, PRE, NO, DATE = "2026-11-27-hanan67-ipark", "h67", 140, "2026-11-27"
PREV_DATE, PREV_MARK = "2026-11-26", "\n2026-11-26 · #139"
PUBDATE = "Fri, 27 Nov 2026 07:00:00 +0900"
REQ = "2026-11-27T07:00:00+09:00"
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
KEYWORD = "하안주공6·7단지 재건축 시공사 IPARK현대산업개발 · 총회 2,092명 중 1,813표(86.7%) · 예정 공사비 1조1,549억 · 2,603→3,240가구 44층 · 5단지(한화 11/18)에 이어 두 번째"
CARDTITLE = "하안주공6·7단지 재건축, 시공사 IPARK현산 찬성 87%"
FULLTITLE = CARDTITLE
SUMMARY = ("광명 하안주공6·7단지 통합 재건축 시공사로 IPARK현대산업개발이 선정됐습니다. 총회에서 2,092명 중 1,813명이 찬성했습니다. "
           "예정 공사비 약 1조1,549억원, 2,603가구를 3,240가구로 다시 짓는 계획과 착공까지 남은 단계를 정리했습니다.")
TITLES = [
    "하안주공6·7단지 재건축, 시공사 IPARK현산 찬성 87%",
    "하안주공6·7단지 시공사 확정, 착공은 언제쯤?",
    "하안주공6·7단지 재건축 공사비·가구수·남은 일정 정리",
]
TAGS = ["하안주공6·7단지", "하안주공재건축", "광명재건축", "하안주공", "IPARK현대산업개발", "아이파크",
        "광명하안동", "신탁방식재건축", "재건축시공사", "광명아파트"]
CARDFILES = ["01-cover", "02-size", "03-homes", "04-vote", "05-next", "06-check"]

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
    "requested_at": REQ,
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
q["updated_at"] = REQ
for it in q["items"]:
    if it.get("status") == "designated":
        it["status"] = "posted"
assert all(it["slug"] != SLUG for it in q["items"])
q["items"].insert(0, {
    "slug": SLUG, "report_no": NO, "date": DATE, "keyword": KEYWORD,
    "status": "designated", "titles": TITLES, "job_id": f"{SLUG}-01",
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
assert mfj["job_id"].endswith("-01") and len(mfj["post"]["images"]) == 6
