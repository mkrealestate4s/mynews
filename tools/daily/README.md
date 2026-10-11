# tools/daily · 데일리 리포트 헬퍼 (2026-10-11 스크래치패드에서 옮김)

세션마다 스크래치패드가 비어서 잃어버리던 스크립트를 저장소에 보관한다. 쓰는 법은 `ops/HANDOVER.md` 5·6절.

- `gen_example_92.py` : 어제 포스트를 복제해 새 포스트를 만드는 생성기 예시(#92). 블록·검산 assert 를 바꿔 쓴다.
- `site_example_92.py` : index·sitemap·feed·title.txt·titles-archive·manifest·queue 등록 예시.
- `make_cards_example_wk1011.py` : 카드 스크립트 예시(공용 헤더 top/foot/hb/tlrows/checks + 블로그·인스타 문안).
- `grab_body.js` : 복사 버튼 텍스트를 받아 `publish/<slug>.txt` 발행본을 쓴다.
- `verify_mobile.js` : 390px 가로 오버플로·이미지·인스타 섹션 검증 (localhost:8899).

경로가 `/home/user/mynews` 와 옛 스크래치패드로 박혀 있으니 새 환경에 맞게 바꾼다.
