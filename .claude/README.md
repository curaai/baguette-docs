# 기획 에이전트·스킬 안내
이 폴더는 Baguette 기획·서사·분석 에이전트와 스킬의 기준이다.

## 사용 원칙
새 기획은 `planning-kickoff`로 시작한다. 승인된 방향의 후속 수정은 해당 스킬에서 이어간다.
공통 승인·질문·기록 원칙은 루트 작업 규칙을 따른다. 세부 절차는 각 스킬에서 관리한다.
이 vault를 단독으로 열면 문서 경로는 vault 루트 기준이다. 게임 저장소에서 보이는 `Docs/` 접두사를 이 안에 다시 만들지 않는다.
태스크 경로와 속성은 TaskNotes 안내에서 확인한다.

## 연결 구성
원본은 항상 `docs/.claude/`다. 아래 경로는 Windows junction이나 등록 파일이므로 따로 수정하지 않는다.
**junction으로 연결한 경로는 모두 해당 저장소의 `.git/info/exclude`(로컬 exclude)에 등록한다.** 새 junction을 만들면 같은 때 exclude에도 추가한다. 로컬 설정이라 새 PC·새 checkout에서는 junction과 함께 다시 만든다.

| 경로 | 종류 | 가리키는 곳 |
|------|------|------|
| `docs/.claude-plugin/plugin.json` | 플러그인 정의 | 플러그인 `docs`, 스킬 경로 `./.claude/skills` |
| `docs/.codex-plugin` | junction | `docs/.claude/integrations/codex` (Codex용 `plugin.json`, Git 추적은 원본만) |
| `docs/.agents/skills/generate-asset-image` | junction | `docs/.claude/skills/generate-asset-image` (Codex용 스킬 노출) |
| 게임 저장소 `.claude-plugin` | junction | 게임 저장소 `.claude/integrations/claude` (marketplace가 `./docs`를 `docs` 플러그인으로 등록) |
| 게임 저장소 `.codex-plugin` | junction | 게임 저장소 `.claude/integrations/codex` |
| 게임 저장소 `.agents/plugins` | junction | 게임 저장소 `.claude/integrations/agents` |
| 게임 저장소 `.codex` | junction | 게임 저장소 `.claude` (이 폴더가 아님) |

## 역할이 겹칠 때

| 다루는 문제 | 담당 | 사용하는 절차 |
|------|------|------|
| 행동·게임 규칙·피드백 | 게임 디자이너 | game-planning과 플레이 경험 검토 |
| 반복·세션·복귀 흐름 | 게임 디자이너 | game-loop-planning |
| 구역 배치·동선·시야 | 게임 디자이너 | level-design |
| 사건·인물·분기의 의미 | 내러티브 디렉터 | planning-content-narrative와 인터랙티브 서사 검토 |
| 실제 대사·게임 안 문장 | 라이터 | 승인된 서사 방향에 따른 집필 |
| 공간의 미술·색·조명 기준 | 아트 디렉터 | art-bible |
| 문서의 배치·중복·목차 | 문서 정리 요청을 받은 담당 | knowledge-ops |

## rsc 선별 도입
2026-10-30~31에 npm `@ericrisco/rsc` 3.6.0 전체 도입을 검토하고, 필요한 절차만 기존 체계에 통합했다.
전체 설치는 보류했다. 스킬·관리 경로가 과도하고, 별도 위키·세션 기록이 TaskNotes와 겹치며, 매 응답 마무리 블록·자동 업데이트·원격 동기화·main 직접 작업 정규화가 현재 방식과 맞지 않았다.
`decision-challenge`와 `level-design`, `knowledge-ops`는 별도 스킬로, 서사·게임 디자인 절차는 기존 스킬의 참고 자료로 넣었다. 기획서 형식·목차·승인 방식·TaskNotes는 기존 규칙을 유지한다.

## 출처·라이선스

| 원본 | 반영 위치·라이선스 |
|------|------|
| [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | art-bible 스킬 |
| [decision-challenge](https://github.com/ericrisco/rsc-harness/blob/main/skills/decision-challenge/SKILL.md) | 결정 검토 스킬 · [MIT 고지](skills/decision-challenge/LICENSE.txt) |
| [level-design](https://github.com/ericrisco/rsc-harness/blob/main/skills/level-design/SKILL.md) | 공간 설계 스킬 · [MIT 고지](skills/level-design/LICENSE.txt) |
| [game-storytelling](https://github.com/ericrisco/rsc-harness/blob/main/skills/game-storytelling/SKILL.md) | 인터랙티브 서사 검토 자료 · [MIT 고지](skills/planning-content-narrative/LICENSE.txt) |
| [game-design](https://github.com/ericrisco/rsc-harness/blob/main/skills/game-design/SKILL.md) | 플레이 경험 검토 자료 · [MIT 고지](skills/game-planning/LICENSE.txt) |
| [knowledge-ops](https://github.com/ericrisco/rsc-harness/blob/main/skills/knowledge-ops/SKILL.md) | 기존 문서 정리 스킬 · [MIT 고지](skills/knowledge-ops/LICENSE.txt) |
