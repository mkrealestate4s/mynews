# -*- coding: utf-8 -*-
"""리포트 #109 를 등록한다. 전날 designated(#108) → posted."""
import json
import pathlib

ROOT = pathlib.Path("/home/user/mynews")
SLUG, PRE, NO, DATE = "2026-10-30-cheongna-arkone", "arw1030", 109, "2026-10-30"
PREV_DATE, PREV_MARK = "2026-10-29", "\n2026-10-29 · #108"
PUBDATE = "Fri, 30 Oct 2026 07:00:00 +0900"
URL = f"https://mkrealestate4s.github.io/mynews/posts/{SLUG}.html"
KEYWORD = "청라 아크원 푸르지오 · 견본주택 10/30 · 아파트 868가구(특공 514·일반 354) · 84㎡ 8억3,780만~9억2,070만 · 특공 11/2·1순위 11/3·당첨 11/10"
CARDTITLE = "청라 아크원 푸르지오, 오늘 견본주택"
FULLTITLE = "청라 아크원 푸르지오 오늘 견본주택, 분양가 8억대"
SUMMARY = ("청라 아크원 푸르지오가 10월 30일 견본주택을 엽니다. 아파트 868가구(일반공급 354)에 분양가상한제가 적용되고 "
           "84㎡ 분양가는 8억3,780만~9억2,070만원 선입니다. 특공 11월 2일, 1순위 3일, 당첨 발표 10일입니다.")
TITLES = [
    "청라 아크원 푸르지오 오늘 견본주택, 분양가 8억대",
    "청라 아크원 푸르지오 분상제 청약, 넣어도 될까?",
    "청라 아크원 푸르지오 분양가·청약 일정·자격 총정리",
]
TAGS = ["청라아크원푸르지오", "아크원푸르지오", "청라아크원푸르지오분양가", "청라아크원푸르지오견본주택", "청라국제도시",
        "청라분양", "인천분양", "분양가상한제", "아파트청약", "11월청약"]
CARDFILES = ["01-cover", "02-supply", "03-date", "04-price", "05-cash", "06-tips"]

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
    "requested_at": f"{DATE}T07:15:00+09:00",
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
q["updated_at"] = f"{DATE}T07:15:00+09:00"
for it in q["items"]:
    if it.get("status") == "designated":
        it["status"] = "posted"
        it["note"] = ((it.get("note", "") + " · ") if it.get("note") else "") + \
            "다음 날 자동등록 처리 완료로 보고 posted. 큐 재발행 금지."
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
