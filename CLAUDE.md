# mynews — 부동산 인사이트 (데일리 키워드 리포트)

GitHub Pages 사이트. main 푸시 → 워크플로우가 gh-pages로 미러링 → 자동 배포.
URL: https://mkrealestate4s.github.io/mynews/

## 구조
- `index.html` — 홈(리포트 목록). 새 글은 목록 맨 위에 카드 추가.
- `posts/YYYY-MM-DD-slug.html` — 리포트 본문. 기존 포스트를 복제해 스타일 유지.
- `images/cards/{report,white,editorial}/<slug>-*.png` — 카드뉴스 (테마별 동일 파일명).
- `themes/design-library.json` + `themes/preview.html` — 디자인 프리셋 라이브러리/카탈로그.
- `tools/make_cards.py`, `tools/fetch_fonts.py` — 카드뉴스 생성 (스킬 `.claude/skills/theme-preset` 참조).
- 테마 3종(report/white/editorial)은 CSS 변수 + `localStorage['mynews-theme']` 공유.

## 데일리 리포트 작성 절차
1. WebSearch로 당일 부동산 이슈 검색 → 데이터가 풍부한 키워드 1개 선정.
2. 본문: 대시보드(kcard 4 + 차트) → 카드뉴스 갤러리 → 기사(섹션별 차트) → 체크포인트 3 → 출처.
3. 카드뉴스 6장 × 3테마 생성(스킬 참조), 인덱스에 글 카드 추가, 커밋·푸시, 배포 success 확인.

## 데이터 시각화 표준 (중요 — 사용자 요구사항)
- **촘촘하게**: 헤드라인 숫자 2개 비교로 끝내지 않는다. 가능하면
  **시계열(4+ 데이터 포인트)**, **다중 지표(매매/전세/월세 등)**, **전기 대비 병기**를 쓴다.
- 모든 수치는 **보도·통계 출처가 있는 실제 값만** 사용(임의 보간·창작 금지). 출처는 푸터에 표기.
- 차트 컴포넌트: 가로 막대(.chart/.bar/.rail/.fill), 세로 컬럼 시계열(.colchart/.cols/.col, 눈금
  repeating-gradient), 대형 스탯(.statrow). 회색 막대는 --fillgray(트랙과 구분), 값 라벨은 짧은
  막대 밖에 배치(.railval).
- 단위·기간이 다른 수치를 한 축에 섞지 않는다(주간/분기/연간 분리).
- 카드뉴스도 그래프 우선: 표지+흐름+데이터 3~4장+체크리스트, 6장 구성 기본.

## 검증 체크리스트 (푸시 전)
- playwright-core(executablePath /opt/pw-browsers/chromium)로 모바일 390px 확인:
  가로 오버플로 없음, 이미지 1:1(aspect-ratio), 게이지 라벨 안 잘림.
- 카드 렌더는 창 1080x1167 → 상단 1080 크롭 (헤드리스 UI 87px 보정).
- 세 테마 모두 스크린샷 확인 후 커밋. 배포는 gh-pages 'pages build and deployment' success 확인.
