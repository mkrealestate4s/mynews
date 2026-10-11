# 인수인계 · 부동산 인사이트 데일리 운영 (2026-10-11 작성)

로그인 계정을 옮기면서 남기는 문서다. 새 계정에서 Claude Code를 처음 열면 **이 파일과 `CLAUDE.md`를 먼저 읽힌다.**
규칙 원본은 `CLAUDE.md`이고, 이 문서는 "지금 어디까지 와 있고, 옮길 때 무엇이 끊기는지"만 담는다.

---

## 1. 계정을 옮기면 끊기는 것 (가장 먼저 처리)

| 항목 | 지금 상태 | 새 계정에서 할 일 |
|---|---|---|
| **매일 아침 루틴** | `데일리 부동산 리포트 (세션 직결)` (trigger `trig_01NzBVFPB1A3ZVvx5BQngZam`) 가 옛 계정의 이 세션에 묶여 매일 07:07 KST 에 발화 | 옛 계정이 해지되면 같이 멈춘다. **새 계정에서 루틴을 새로 만든다.** 아래 2절 프롬프트를 그대로 쓴다. 시각은 `CRON_TZ=Asia/Seoul 7 7 * * *` |
| GitHub 연결 | 옛 계정이 `mkrealestate4s/mynews` 에 접근 | 새 계정 claude.ai 설정 → Connectors → GitHub 에서 같은 저장소 권한을 준다. 브랜치 `claude/github-pages-deploy-lzb2mq` 를 그대로 쓴다 |
| 작업 폴더(스크래치패드) | 세션마다 비어 있다. 폰트·playwright·헬퍼 스크립트가 다 사라진다 | 4절 복구 순서대로 3~5분이면 복구된다 |
| 로컬 자동포스팅 프로그램 | PC에서 `title.txt`·`publish/manifest.json` 을 07:40 이후 받아간다 | **영향 없음.** 깃페이지 주소가 그대로라 계정과 무관하다 |
| 인스타 예약 발행 | 폰 홈화면 `insta.html` 바로가기 | 영향 없음 |
| 노션 | 인수인계 페이지를 옛 계정 노션에 남겼다 | 새 계정에서 같은 워크스페이스를 쓰면 그대로 보인다 |

**옛 계정 해지 전 마지막 데일리:** 2026-10-11 #92 (이번 주 청약 일정). 10/12(월) 아침 루틴이 옛 계정에서 돌지 않으면 그날 글이 빠진다.
그러면 07:40 프로그램이 #92 를 한 번 더 받아갈 수 있으니, **새 계정 첫 세션은 07:40 전에 #93 을 올리거나 `publish/manifest.json` 의 status 를 `hold` 로 내린다.**

---

## 2. 새 루틴에 넣을 프롬프트 (그대로 복사)

```
아침 7시 데일리 리포트 작성 시간이다. 이 세션에서 지금까지 해온 방식 그대로, 오늘의 부동산 키워드 리포트를 작성해 배포하라: (1) WebSearch로 오늘 이슈 검색 후 실측 데이터가 풍부한 키워드 1개 선정 (직전 리포트와 주제 중복 회피), (2) posts/의 최신 포스트를 복제해 새 리포트 작성 (CLAUDE.md 표준: SEO 메타·data-img 매핑·data-tags 교체), (3) 스크래치패드 cards/의 최신 make_cards_*.py를 참고해 카드 6장×3테마 생성·렌더(크롬 1080x1167→1080 크롭)·검수, (4) index.html/sitemap.xml/feed.xml 갱신, (5) 복사 텍스트 [이미지1~6]과 모바일 390px 검증, (6) main 푸시 + claude/github-pages-deploy-lzb2mq 미러, gh-pages 배포 success 확인, (7) 사용자에게 리포트 URL·키워드·핵심 수치 보고. 어떤 단계가 실패하면 축소해서라도 본문을 배포하고 실패 내용을 보고에 포함하라.
```

새 계정은 이전 대화 맥락이 없다. 첫 세션에서 한 번 이렇게 덧붙인다:
"`ops/HANDOVER.md` 와 `CLAUDE.md`, `ops/calendar.md` 를 먼저 읽고, `tools/daily/` 예시 스크립트를 스크래치패드로 복사해 쓰라."

---

## 3. 지금 상태 (2026-10-11 07:14 기준)

- **최신 리포트: #92** `posts/2026-10-11-weekcal.html` · 다음 번호는 **#93** (index.html 맨 위 카드에서 읽는다)
- `title.txt` · `publish/manifest.json` = #92 (designated)
- `publish/queue.json` 에서 사용자 확인 대기:
  - **#90 한글날 특집 (아파트 이름)** `pending`: 오후 특집이라 다음 날 07:40 전에 #91 로 교체돼 자동등록되지 않았다
  - **#85 송파 ICT 보안 클러스터 특집** `pending`: 같은 이유
  - 손으로 올렸으면 `dropped` + `dropped_reason`, 안 올릴 거면 `dropped`, 올릴 거면 `pending` 유지
  - **#73** `hold` (9/26 통계 글, 발행 여부 미정)
- 그 밖의 항목은 `posted` 또는 `dropped` 로 정리돼 있다

## 4. 앞으로 쓸 날 (`ops/calendar.md` 요약)

| 날짜 | 글 | 비고 |
|---|---|---|
| **10/12(월)** | **SH 신혼·신생아 매입임대 "내일부터 접수"** (Ⅰ 서울 347호 + Ⅱ, 접수 10/13 10시~10/15 17시) | #83 에서 "접수 전날 다시 알려 드린다"고 약속함. Ⅰ·Ⅱ 중복 신청 결격 |
| **10/14(수)** | **청담르엘 장기전세 서류심사 대상자 발표** (SH 51차) · 서류 우편 10/19~21 · 당첨 2027-03-05 | 9월 1위 글의 후속. 반드시 쓴다 |
| 10/20(화) | 향남역 그로브 스위첸 당첨자 발표 | #91 후속(선택) |
| 10/23(금) | SH 재개발임대 서류심사 대상자 발표 | 2순위 |
| 10/25(일) | 인천계양 A17 신혼희망타운 "내일부터 접수" (10/26~27, 309가구) | |
| 공고 뜨는 날 | 고덕강일3단지 토지임대부 본청약 · 반포 디에이치 클래스트 | 10/9 기준 아직 공고 없음 |
| 11/19 · 11/21 · 11/23 · 11/30 | 마천1구역 입찰 마감 · 성수2지구 총회 · 청담현대1차 마감 · 여의도 진주아파트 입찰 마감 | 결과 글 |
| 연내 | 신규택지 7.3만가구 발표 · 토지거래허가구역 연장 결정(12/31 만료) | #88·#89 후속 |

매주 월요일 아침 "찾아도 못 찾은 것"(SH 장기전세 52차, 행복주택 3차, 미리내집 다음 차수, LH 11월 공공분양)을 다시 검색해 표에 올린다.

---

## 5. 매일 작업 흐름 (요약 · 자세한 규칙은 CLAUDE.md)

1. **주제 고르기**: `ops/calendar.md` 오늘 줄 → 없으면 우선순위
   공공임대·공공분양 접수 D-1 > 대표 단지(은마·잠실·압구정·목동·성수·여의도) > 마감 걸린 제도 > 통계(단독 금지).
   사건일이 1주일 넘게 지났으면 버린다. 메인 검색어 1개를 정하고 제목 맨 앞, 첫 문장, H3 2개 이상, 정리, data-tags 첫째에 넣는다.
2. **본문**: `tools/daily/gen_example_92.py` 를 복사해 HEAD·HEADER·DASH·CARDNAMES·ARTICLE·FOOTER·검산 assert 를 교체 → 실행하면 어제 글을 복제해 `posts/<slug>.html` 생성.
3. **카드**: `tools/daily/make_cards_example_wk1011.py` 를 스크래치패드 `cards/` 에 복사해 문안 교체(블로그 `cards` 6장 + 인스타 `insta` 6장) →
   ```
   python3 make_cards_X.py && for t in report white editorial insta; do node ../shot_cards.js $t png-$t 1080 1080 X; done | grep -v "over v0 h0"
   python3 make_carousel.py X insta && node ../shot_cards.js insta-car pngc 1080 1350 X
   ```
   `images/cards/{report,white,editorial}/` 와 `images/cards/carousel/` 로 복사.
4. **캡션**: `publish/insta/<slug>-caption.txt` (어제 것 복제, 첫 줄에 메인 검색어, 해시태그 10개).
5. **등록**: `tools/daily/site_example_92.py` 복사해 SLUG·제목·태그 교체 → index·sitemap·feed·title.txt·titles-archive·manifest·queue 한 번에 갱신.
   전날 designated 는 `posted` 로 내린다(전날 오후 특집이었다면 `pending`).
6. `python3 tools/add_insta_section.py posts/<slug>.html <카드접두어>`
7. `node grab_body.js $PWD/posts/<slug>.html $PWD/publish/<slug>.txt` → "1~6 true · 줄표 0 · 깃페이지 false · 태그줄 false" 확인
8. `python3 -m http.server 8899 &` 후 `node verify_mobile.js <slug>` → over 0, instaImgs 6
9. 확인: `grep -c '—'` 0 · `grep -c '<img'` 7 · `grep -c 'data-all="theme"'` 1
10. 푸시: `git push origin HEAD:main; git push -f origin HEAD:claude/github-pages-deploy-lzb2mq; git branch -f main HEAD`
11. gh-pages `pages build and deployment` success 확인 → 사용자 보고

**07:40 이 마감이다.** 평소 07:12 푸시, 07:14 배포 완료.

## 6. 스크래치패드 복구 순서 (새 세션·컨테이너 재생성 때)

```
S=<스크래치패드>
mkdir -p $S/cards
cp tools/make_cards.py tools/make_carousel.py tools/fetch_fonts.py $S/cards/
cp tools/shot_cards.js tools/daily/grab_body.js tools/daily/verify_mobile.js $S/
(cd $S/cards && python3 fetch_fonts.py)          # 두 세트, 약 1~3분
(cd $S && npm init -y && npm install playwright-core)
python3 -m pip install pillow                     # 대조 시트용 (pip 가 아니라 python3 -m pip)
```
`tools/daily/` 의 예시 스크립트는 경로가 `/home/user/mynews` 와 옛 스크래치패드로 박혀 있다. 새 환경 경로로 바꿔 쓴다.

## 7. 꼭 지킬 것 (사용자 지시 · 실수에서 나온 규칙)

- 줄표 `—` 금지 (가운뎃점·쉼표·마침표로 다시 쓴다)
- 확인 못 한 것은 단정하지 않는다: "유력·우협"은 관측, 현설 참석은 입찰 아님, 계획 가구수는 확정 전, 정책은 "검토"와 "확정"을 구분
- 인스타 카드는 블로그와 다른 글: 일반인 말투, 비율은 100명 기준, 전문용어 금지
- 사용자가 "손으로 올렸다"고 하면 queue `dropped` + manifest `hold`
- 원문(깃페이지) 링크를 블로그 본문에 넣지 않는다
