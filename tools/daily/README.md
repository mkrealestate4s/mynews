# tools/daily · 데일리 리포트 헬퍼 (2026-10-11 스크래치패드에서 옮김)

세션마다 스크래치패드가 비어서 잃어버리던 스크립트를 저장소에 보관한다. 쓰는 법은 `ops/HANDOVER.md` 5·6절.

- `gen_example_92.py` : 어제 포스트를 복제해 새 포스트를 만드는 생성기 예시(#92). 블록·검산 assert 를 바꿔 쓴다.
- `site_example_92.py` : index·sitemap·feed·title.txt·titles-archive·manifest·queue 등록 예시.
- `make_cards_example_wk1011.py` : 카드 스크립트 예시(공용 헤더 top/foot/hb/tlrows/checks + 블로그·인스타 문안).
- `grab_body.js` : 복사 버튼 텍스트를 받아 `publish/<slug>.txt` 발행본을 쓴다.
- `verify_mobile.js` : 390px 가로 오버플로·이미지·인스타 섹션 검증 (localhost:8899).

경로가 `/home/user/mynews` 와 옛 스크래치패드로 박혀 있으니 새 환경에 맞게 바꾼다.
- `gen_example_98.py` · `site_example_98.py` · `make_cards_example_mkd1019.py` : 2026-10-19 #98 최신 예시(경로 /home/claude/mynews, 6열 대시보드·가로막대 hb 카드).
- `gen_example_99.py` · `site_example_99.py` · `make_cards_example_hng1020.py` : 2026-10-20 #99 최신 예시(경로 /home/user/mynews, 청약 결과 글: 가로막대·statrow 교대).
- `gen_example_100.py` · `site_example_100.py` · `make_cards_example_gdk1021.py` : 2026-10-21 #100 최신 예시(경로 /home/user/mynews, 공공분양 본청약 글: 공급·분양가 가로막대 + 일정·임대료 statrow).
- `gen_example_101.py` · `site_example_101.py` · `make_cards_example_shd1022.py` : 2026-10-22 #101 최신 예시(경로 /home/user/mynews, 공공임대 발표 D-1 글: 일정 statrow + 날 수 가로막대 + 자격 statrow + 물량 가로막대).
- `gen_example_102.py` · `site_example_102.py` · `make_cards_example_gya1023.py` : 2026-10-23 #102 최신 예시(경로 /home/user/mynews, 공공분양 접수 D-3 글: 물량 세로 컬럼 + 일정 statrow + 물량·분양가 가로막대 + 조건 statrow).
- `gen_example_103.py` · `site_example_103.py` · `make_cards_example_dhb1024.py` : 2026-10-24 #103 최신 예시(경로 /home/user/mynews, 대표 단지 공고 전 글: 물량 세로 컬럼 + 일정 statrow + 평형 가로막대(railval) + 가정 분양가 가로막대 + 미확정 statrow).
- `gen_example_104.py` · `site_example_104.py` · `make_cards_example_akm1025.py` : 2026-10-25 #104 최신 예시(경로 /home/user/mynews, 민영 청약 D-1 글: 이번 주 물량 세로 컬럼 + 일정 statrow + 주간 단지 가로막대 + 분양가·계약금 가정 가로막대 + 확인 statrow).
- `gen_example_105.py` · `site_example_105.py` · `make_cards_example_trv1026.py` : 2026-10-26 #105 최신 예시(경로 /home/user/mynews, 민영 청약 D-day 글: 물량 세로 컬럼 + 일정 타임라인 + 주간·단지 가로막대 + 타입별 분양가 가로막대 + 확인 statrow).
- `gen_example_106.py` · `site_example_106.py` · `make_cards_example_gyd1027.py` : 2026-10-27 #106 최신 예시(경로 /home/user/mynews, 공공분양 접수 마감일 글: #102 수치 재사용 + 마감·다음 일정 statrow 2개 + 물량·분양가 가로막대).
- `gen_example_107.py` · `site_example_107.py` · `make_cards_example_akm1028.py` : 2026-10-28 #107 최신 예시(경로 /home/user/mynews, 민영 청약 결과 후속 D-day 글: 특공 모집·접수 세로 컬럼 + 가로막대 + 일정 statrow + 분양가 가로막대 + 확인 statrow).
- `gen_example_108.py` · `site_example_108.py` · `make_cards_example_shh1029.py` : 2026-10-29 #108 최신 예시(경로 /home/user/mynews, 공공임대 당첨 발표 D-1 글: 모집 구성 세로 컬럼 + 구성 가로막대(railval) + 일정 statrow + 면적별 임대료 가로막대 + 확인 statrow).
- `gen_example_109.py` · `site_example_109.py` · `make_cards_example_arw1030.py` : 2026-10-30 #109 최신 예시(경로 /home/user/mynews, 민영 분상제 단지 견본주택 개관일 글: 공급 구성 세로 컬럼 + 특공·일반 가로막대 + 일정 statrow + 분양가 범위 가로막대 + 계약금·지역 statrow).
