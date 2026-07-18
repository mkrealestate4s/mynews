---
name: theme-preset
description: 사이트 디자인 테마 프리셋을 조회·적용한다. 사용자가 "테마 목록", "프리셋 보여줘", "OO 테마 적용/추가해줘"(예: 스너그 심플, 레조넌트 스타크), "새 테마 만들어줘", "/theme-preset"을 요청할 때 사용한다. 프리셋 팔레트로 페이지 테마와 테마별 카드뉴스 이미지 세트까지 함께 생성한다.
---

# 테마 프리셋 시스템

이 저장소(mynews)는 CSS 변수 기반 3-테마 시스템(report / white / editorial)을 쓴다.
프리셋 라이브러리는 `themes/design-library.json`, 시각 카탈로그는 `themes/preview.html`
(배포: https://mkrealestate4s.github.io/mynews/themes/preview.html).

## 프리셋 조회 요청 시
`themes/design-library.json`을 읽고 presets의 label/mood를 표로 요약해준다.
미리보기 URL도 함께 안내한다.

## 프리셋을 라이브 테마로 추가/교체할 때 (전체 절차)

1. **페이지 CSS**: `index.html`과 `posts/*.html`의 `<style>`에
   `:root[data-theme="<키>"]{...}` 블록을 프리셋 vars로 추가.
   변수 이름 매핑: bg→(post에서는 --navy, index에서는 --bg), panel, ink, mute,
   accent→--teal, accent2→--peri, line, rail, fillgray, onfill, body→--body-ink,
   typography.heading→--head-font, headSpace→--head-space.
   gradientText=false면 화이트 테마처럼 `.gtx`/헤드라인 단색 오버라이드 블록도 추가.
2. **스위처 버튼**: 두 페이지의 `.themes`에
   `<button class="tbtn" data-set="<키>" title="<라벨>" style="--sa:<bg>;--sb:<accent>">` 추가.
3. **카드뉴스 재생성**: `tools/make_cards.py`의 THEMES 딕셔너리에 프리셋 추가.
   - 최초 1회 `tools/`에서 `python3 fetch_fonts.py` (fonts/ 9.9MB는 저장소에 커밋하지 않음)
   - 렌더: chromium headless, **창 크기 1080x1167** (헤드리스 UI가 87px 차지 → 뷰포트 1080),
     `--virtual-time-budget=15000`, 렌더 후 PIL로 상단 1080x1080 크롭.
   - 결과를 `images/cards/<키>/banse-*.png`로 커밋.
4. **검증**: playwright-core(+ executablePath /opt/pw-browsers/chromium)로 각 테마 클릭 후
   스크린샷 — 게이지 회색이 트랙과 구분되는지, 제목 폰트/단색 처리, 푸터 잘림 확인.
5. **배포**: main에 push하면 워크플로우가 gh-pages로 미러링 → Pages 자동 배포.
   `localStorage['mynews-theme']` 키로 두 페이지가 선택을 공유한다.

## 주의
- 회색 게이지(fillgray)는 rail과 명확히 구분되는 값이어야 함 (과거 버그).
- 이미지 `<img>`에 width/height 속성이 있으므로 CSS에 `height:auto;aspect-ratio:1/1` 필수.
- 새 프리셋을 라이브러리에 추가할 때는 이미지 복제가 아니라 스타일 요소(색·타이포·무드)만 기록.
- 99designs 등 외부 갤러리 수집은 직접 접속이 막혀 있으니 Apify MCP(rag-web-browser)를 사용.
