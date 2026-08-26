# -*- coding: utf-8 -*-
"""릴스 스크립트의 씬 초수를 글자 수로 다시 계산하고, 통스크립트 블록을 갱신한다.

- 초수는 **공백 제외 글자 수 ÷ 5.5 + 0.6초**(씬 전환 여유)로 산출한다.
  클로바더빙·VLLO 기본 속도에서 실측에 가까운 값이다. 눈대중으로 적으면
  실제 렌더 길이와 어긋나 편집 때 다시 맞춰야 한다.
- '■ 통스크립트' 블록은 매번 다시 만들어 [나레이션] 본문과 항상 일치시킨다.
  (add_insta_section.py 가 이 [나레이션] 블록을 읽어 포스트 페이지에 심는다)

사용법: python3 tools/sync_reels_script.py publish/reels/<slug>-script.txt
"""
import pathlib, re, sys

RATE = 5.5   # 초당 글자 수 (공백 제외)
PAD = 0.6    # 씬 전환 여유(초)

P = pathlib.Path(sys.argv[1])
s = P.read_text(encoding="utf-8")

SCENE_RE = re.compile(
    r'(씬\s*(\d+)\s*·\s*(\S+?)\s*·\s*)(\d+:\d{2}\s*~\s*\d+:\d{2})'
    r'(\n\n\[나레이션\]\n)(.+?)(\n\n\[자막\])', re.S)  # [자막문장]은 뒤에 있어 영향 없음

matches = list(SCENE_RE.finditer(s))
assert matches, "씬 블록을 찾지 못했습니다 — 파일 형식을 확인하세요"


def ts(x):
    x = int(round(x))
    return f"{x // 60}:{x % 60:02d}"


# 1) 씬별 초수 재계산
narrations, cum, out, last = [], 0.0, [], 0
for m in matches:
    text = m.group(6).strip()
    narrations.append(text)
    dur = len(text.replace(" ", "")) / RATE + PAD
    out.append(s[last:m.start()])
    out.append(m.group(1) + f"{ts(cum)} ~ {ts(cum + dur)}" + m.group(5) + m.group(6) + m.group(7))
    cum += dur
    last = m.end()
out.append(s[last:])
s = "".join(out)

total_chars = sum(len(t.replace(" ", "")) for t in narrations)
s = re.sub(r'■ 총 길이[^\n]*',
           f'■ 총 길이 약 {int(round(cum))}초 · 나레이션 {total_chars}자(공백 제외)'
           f' · 초당 {RATE}자 기준', s, count=1)

# 2) 통스크립트 블록 (있으면 교체, 없으면 캡션 블록 앞에 삽입)
full = "\n".join(narrations)
BLOCK = ("═════════════════════════════════════════════\n"
         "■ 통스크립트 — TTS에 한 번에 넣는 용도 (씬 순서대로 이어붙임)\n"
         f"  {len(narrations)}씬 · {total_chars}자(공백 제외) · 약 {int(round(cum))}초\n"
         "  줄바꿈이 씬 경계입니다. 한 번에 음성으로 뽑은 뒤 씬 길이에 맞춰 자르세요.\n\n"
         + full + "\n\n")

if "■ 통스크립트" in s:
    s = re.sub(r'═+\n■ 통스크립트.*?(?=═+\n■ 인스타 캡션)', BLOCK, s, count=1, flags=re.S)
else:
    s = s.replace("═════════════════════════════════════════════\n■ 인스타 캡션",
                  BLOCK + "═════════════════════════════════════════════\n■ 인스타 캡션", 1)

P.write_text(s, encoding="utf-8")
print(f"{len(narrations)}씬 · {total_chars}자 · 약 {int(round(cum))}초 — 초수 재계산 + 통스크립트 갱신")
