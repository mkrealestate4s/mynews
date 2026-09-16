# 인수인계 · mynews 데일리 리포트 운영

작성 2026-09-16 (리포트 #62 배포 직후) · 이 문서는 운영 메모다. 규칙의 정본은 `CLAUDE.md`,
이 문서는 "지금 어디까지 왔고 다음에 뭘 보면 되는지"를 적는다.

---

## 1. 지금 상태 한 줄

리포트 **#62까지 발행 완료**(2026-09-16). 매일 아침 07:00 KST 트리거가 이 세션을 깨우고,
**07:40까지** 깃페이지 배포를 끝내면 로컬 자동 포스팅 프로그램이 받아간다. 마지막 배포는
07:13:04 KST에 success.

- 사이트 https://mkrealestate4s.github.io/mynews/
- 폰 인스타 입구 https://mkrealestate4s.github.io/mynews/insta.html
- 큐 상태: designated 1건(`2026-09-16-ipju`), pending 0건, posted 26, dropped 3

---

## 2. 매일 아침 절차 (실제로 치는 순서)

스크래치패드는 `/tmp/claude-0/-home-user-mynews/<세션id>/scratchpad`.
`SP=` 로 잡아 두고 쓴다. 어제 스크립트를 복제해 오늘 것을 만드는 방식이다.

```bash
# 0. 상태 확인 (컨테이너가 재생성됐을 수 있다. 4절 참조)
cd /home/user/mynews && git log --oneline -2 && git branch --show-current
ls $SP/cards/gf2-local.css $SP/node_modules >/dev/null   # 없으면 4절 복구

# 1. 주제: WebSearch. CLAUDE.md '주제 배분'을 먼저 본다 (주 3편은 단지·구역 뉴스)

# 2. 본문: 어제 gen 스크립트를 복제해 gen<N>.py 작성 후 실행
cd $SP && python3 gen<N>.py

# 3. 카드: 어제 make_cards_*.py 를 복제
cd $SP/cards && python3 make_cards_<pre>.py
export NODE_PATH=$SP/node_modules
for t in report white editorial insta; do
  node /home/user/mynews/tools/shot_cards.js $t png-$t 1080 1080 <pre> | grep -v "v0 h0"; done
for t in report white editorial; do cp png-$t/<pre>-*.png /home/user/mynews/images/cards/$t/; done
python3 make_carousel.py <pre> insta
node /home/user/mynews/tools/shot_cards.js insta-car pngc 1080 1350 <pre>
cp pngc/<pre>-*.png /home/user/mynews/images/cards/carousel/

# 4. 인스타 캡션 작성 → publish/insta/<slug>-caption.txt
cd /home/user/mynews && python3 tools/add_insta_section.py posts/<slug>.html <pre>

# 5. 사이트 등록 + 발행 본문
cd $SP && python3 site<N>.py
node grab_body.js /home/user/mynews/posts/<slug>.html /home/user/mynews/publish/<slug>.txt

# 6. 푸시 (HEAD: 를 쓴다. main: 을 쓰지 말 것. 4절 참조)
cd /home/user/mynews && git add -A && git commit -F - <<'EOF' ... EOF
git push origin HEAD:main
git push -f origin HEAD:claude/github-pages-deploy-lzb2mq

# 7. 검증 + 배포 확인
cd /home/user/mynews && nohup python3 -m http.server 8899 >/dev/null 2>&1 &
cd $SP && node verify<N>.js
# GitHub Actions 'pages build and deployment' 가 success 인지 확인
```

`over`가 0이면 오버플로 없음. `shot_cards.js` 출력에서 `over v0 h0`가 아닌 줄만 걸러 보면 된다.

---

## 3. 이번 세션에서 낸 리포트 (#50 ~ #62)

| # | 날짜 | slug | 주제 | 성격 |
|---|---|---|---|---|
| 50 | 09-05 | palleok | 강북 8억 미만 매물 감소 | 통계 |
| 51 | 09-06 | jeonse9 | 9월 입주 1만4,174가구 | 통계 |
| 52 | 09-06 | songpa | 송파 재건축 3곳 8,768 → 13,976세대 | 단지 |
| 53 | 09-07 | mokdong | 목동윤슬자이 651실은 아파트가 아니다 | 단지 |
| 54 | 09-08 | eunma | 은마 세대수, 세 번 바뀌었다 | 단지 |
| 55 | 09-09 | nakchalga | 낙찰가율 97.0%, 감정가 아래로 | 통계 |
| 56 | 09-10 | moa | 모아주택 112곳 중 준공은 1곳 | 제도·단지 |
| 57 | 09-11 | wolgok | 월곡 59.7 대 1, 목동윤슬자이 32 대 1 | 단지 |
| 58 | 09-12 | gap | 강북구 +0.46%, 강남구 −0.35% | 통계 |
| 59 | 09-13 | sh51 | SH 제51차 장기전세 마감 임박 (특집) | 특집 |
| 60 | 09-14 | jangmi | 잠실 장미1·2·3차 이달 입찰공고 | 단지 |
| 61 | 09-15 | hyeonseol | 이번 주 서울 7곳 시공사 현설 | 단지 |
| 62 | 09-16 | ipju | 서울 9월 입주 88%가 디에이치방배 | 통계·단지 |

**9/6 사용자 지적으로 주제 배분을 바꿨다.** 그 전 20편 중 14편이 통계 해설이었고 단지명이
제목에 들어간 글은 하나뿐이었다. 지금은 **주 3편 이상 단지·구역 뉴스**, 제목에 고유명사를
반드시 넣는다. 지역은 강남3구 + 강북 주요구(성북·노원·중랑·강북·도봉).

**리포트끼리 엮인 실이 있다.** 강북 중저가 강세가 #50(매물 감소) → #51(KB 중랑 1위) →
#55(경매 중랑 115.2%) → #57(성북 8억대 59.7 대 1) → #58(강북구 +0.46%)로 다섯 편에 걸쳐
같은 방향을 가리켰다. #62에서는 #56의 모아주택 1호와 #59의 디에이치방배가 실제 입주
단지로 다시 나왔다. 새 글을 쓸 때 **지난 글과 이어 붙일 곳이 있는지 먼저 본다.**

---

## 4. 이번 세션에서 실제로 터진 사고 5건 (같은 걸 또 밟지 말 것)

### (1) 컨테이너 재생성 + 잘못된 브랜치 푸시 (9/15, 가장 위험했던 건)
재클론된 컨테이너는 **지정 브랜치를 HEAD로 잡고 로컬 `main`은 클론 시점 커밋에 멈춰 있다.**
늘 쓰던 `git push origin main:main`을 그대로 써서 #54 시점의 낡은 main을 밀었다.
main 푸시는 거부됐지만 뒤이은 `push -f origin main:<미러>`가 **미러 브랜치를 #54로 되돌렸다.**

- **`HEAD:main`을 쓴다.** 푸시 전 `git log --oneline -2`로 HEAD가 오늘 커밋인지 본다.
- `git push ... | tail -2`는 **파이프라 exit status가 tail 것**이라 `&&` 체인이 실패를 못 잡는다.
- 복구: `git push origin HEAD:main` + `git push -f origin HEAD:<미러>` + `git branch -f main HEAD`
- 스크래치패드도 함께 비었다. 복구: `tools/`에서 make_cards.py·make_carousel.py·fetch_fonts.py
  복사 → `python3 fetch_fonts.py`(약 3분) → `npm install playwright-core` → grab_body.js·
  site\<N\>.py·verify\<N\>.js 재작성. 이 절차로 30분 안에 복구했고 산출물에는 영향 없었다.

### (2) 자동 포스팅이 하루 헛돌았다 (9/5)
#50 배포가 11:16에 끝나 **07:40 마감을 넘겼다.** 프로그램은 어제 파일을 받아갔는데,
그때 title.txt가 9/4 오후에 특집 #49로 덮여 있어서 **#49가 한 번 더 올라갔다.**
사용자에게는 "자동 포스팅이 안 됐다 · title.txt가 갱신되지 않는다"로 보였다.
(확인해 보니 8/21~9/4는 매일 07:17~07:23에 정상 갱신됐다. 캐시 문제가 아니었다.)

→ **07:40은 목표가 아니라 마감이다.** 늦어질 것 같으면 먼저 알린다.

### (3) 큐가 영원히 pending으로 쌓였다 (9/5 정리)
`fetch_queue()`는 중복을 **slug**로 보는데 `fetch_job()`은 **job_id(`<slug>-01`)**를
posted.log에 적는다. 키가 달라서 당일 manifest로 발행한 글이 큐에서는 계속 pending이었다.
8/21 이후 15편이 그렇게 쌓여 있었고, 큐 경로를 한 번 돌리면 지난 글이 줄줄이 재발행될
상태였다. → **다음 날 designated를 내릴 때 pending이 아니라 `posted`로 내린다.**

### (4) '전체 저장' 버튼이 매일 두 개씩 생겼다 (9/6 사용자 스크린샷 제보)
일일 생성기 CARDS 블록에 `.ilabel` 줄이 굳어 들어간 뒤로 `add_insta_section.py`가 같은 줄을
한 번 더 넣었다. 13편을 되돌리고 스크립트를 `data-all="theme"`가 없을 때만 넣도록 고쳤다.
→ 푸시 전 `grep -c 'data-all="theme"' posts/<slug>.html` 이 **1**이어야 한다.

### (5) 확인 못 한 걸 단정했다 (9/4, 사용자가 물어서 잡힘)
"청약통장을 전환하면 국민주택 회차가 0으로 초기화된다"고 #46·#49 두 편에 걸쳐 단정했는데
공고문 원문은 **"인정 실적이 달라질 수 있으니 순위(가입)확인서로 확인하라"**고만 쓴다.
원문에는 내가 놓친 더 정확한 근거가 있었다: **자격·순위 산정은 공고일 기준, 전환은 공고일
전일까지 완료해야 반영.** #59에서는 이 근거로 다시 썼고 "초기화"를 코드 assert로 막았다.

→ 이 환경은 WebFetch가 막혀 **검색 요약만 본다.** 요약에는 기자 해석이 섞인다.
1차 출처를 못 읽었으면 단정하지 말고 "확인 필요" 또는 원문 인용으로 처리한다.

**그 밖에 내가 직접 잡은 것**: #60에서 `<span class="imgslot">`를 닫지 않아 바로 뒤 첫 문단이
hidden span 안으로 들어갈 뻔했다(본문과 복사 텍스트에서 사라진다). 고치고 gen 스크립트에
imgslot마다 `</span>`가 뒤따르는지 검사하는 assert를 넣었다. 복제되니 계속 이어진다.

---

## 5. 추적 중인 후속 (날짜가 있는 것부터)

| 언제 | 무엇 | 어디서 나온 건가 |
|---|---|---|
| 9월 30일 | 청약예금·부금 → 종합저축 **전환 마감** | #59 |
| 10월 14일 | SH 51차 장기전세 **서류심사 대상자 발표** | #59 |
| 11월 2일 14시 | 무지개아파트 **입찰 마감** | #61 |
| 2027년 1월 | 잠실 장미1·2·3차 **시공사 선정 총회** | #52, #60 |
| 2027년 3월 5일 | SH 51차 장기전세 **당첨자 발표** | #59 |
| 날짜 미정 | 잠실 장미 **입찰 마감에 몇 곳이 들어오는지** (경쟁 성립 여부) | #60 |
| 날짜 미정 | 디에이치방배 입주 뒤 **인근 전월세 매물이 실제로 얼마나 느는지** | #62 |
| 날짜 미정 | 은마 **강남구 인가 고시 확정 세대수** (지금은 5,778/5,893/5,962로 갈림) | #54 |
| 날짜 미정 | 모아주택 **착공 8곳이 두 자리로 오르는 시점** | #56 |
| 날짜 미정 | 송파 **오금현대 시공사 입찰** | #60, #61 |
| 매주 목요일 | 부동산원 주간동향. **송파가 한 주 더 마이너스인지** | #58 |

---

## 6. 절대 건드리면 안 되는 것

로컬 자동 포스팅 프로그램이 이 계약에 묶여 있다. 깨면 아침에 글이 안 올라간다.

- `title.txt` **3줄만**, 주석·빈줄 없음, UTF-8 BOM 없음, LF. 프로그램은 **첫 줄만** 쓴다.
- `title.txt`와 `publish/manifest.json`은 **항상 같은 글**을 가리킨다.
- 서빙 HTML의 `<img>` 개수는 **7개**(카드 6 + figure 1). 인스타 섹션 이미지는 JS가 만든다.
- 복사 텍스트에 `[이미지1]`~`[이미지6]`이 **전부** 나와야 한다. N은 순번이 아니라 **카드 번호**다.
- 복사 텍스트에 **깃페이지 링크를 넣지 않는다**(블로그 글 원본성 보호).
- `grep -c 'data-all="theme"'` 는 **1**.
- 줄표 `—` 는 **0**. 가운뎃점 `·`, 화살표 `→`, 마이너스 `−` 는 그대로 쓴다.
- 캐러셀 저장은 **6번부터 거꾸로, 1.1초 간격**. 실기기(안드로이드)에서 검증된 조합이라
  간격을 줄이거나 순서를 되돌리지 말 것.

---

## 7. 파일 지도

**저장소**
- `CLAUDE.md` 규칙 정본. 사고가 나면 여기에 규칙으로 남긴다
- `index.html` 홈. 새 글 카드는 맨 위 앵커 주석 아래
- `posts/YYYY-MM-DD-slug.html` 본문. 어제 글을 복제해 만든다
- `images/cards/{report,white,editorial}/` 블로그 카드 · `carousel/` 인스타 4:5
- `publish/manifest.json` 발행 지시서 · `queue.json` 후보 목록 · `<slug>.txt` 발행 본문
- `publish/insta/<slug>-caption.txt` 인스타 캡션
- `title.txt` 오늘 제목 3줄 · `titles-archive.txt` 누적 기록
- `tools/` make_cards.py, make_carousel.py, shot_cards.js, add_insta_section.py, fetch_fonts.py

**스크래치패드** (컨테이너 회수되면 사라진다. 저장소에 커밋하지 않는다)
- `gen<N>.py` 본문 생성기. 맨 위 docstring에 **출처·검산·단정하지 않은 것**을 적는다
- `cards/make_cards_<pre>.py` 카드 생성기 (블로그 dict + 인스타 dict, render 두 번)
- `site<N>.py` index·sitemap·feed·title.txt·archive·manifest·queue 등록
- `grab_body.js` 발행 본문 추출 · `verify<N>.js` 390px 검증

---

## 8. 다음 사람이 아침에 먼저 볼 것

1. `git log --oneline -2` 와 `git branch --show-current` (컨테이너 재생성 여부)
2. `CLAUDE.md`의 **주제 배분** 절 (최근 3편이 전부 통계면 오늘은 단지 뉴스)
3. 위 5절 **추적 중인 후속** 표에서 오늘 날짜에 걸리는 것
4. 시계. **07:40 마감**이고 배포까지 보통 10분 걸린다

그리고 사용자가 "손으로 발행했다"고 하면 그 자리에서 `queue.json` → `dropped`,
`manifest.json` → `hold` 두 줄을 내린다. 안 내리면 프로그램이 같은 글을 또 올린다.
