# 기획 에이전트·스킬 안내
이 폴더는 Baguette 기획·서사·분석 에이전트와 스킬의 기준이다.

## 사용 원칙
새 기획은 `planning-kickoff`로 시작한다. 승인된 방향의 후속 수정은 해당 스킬에서 이어간다.
공통 승인·질문·기록 원칙은 루트 작업 규칙을 따른다. 세부 절차는 각 스킬에서 관리한다.
이 vault를 단독으로 열면 문서 경로는 vault 루트 기준이다. 게임 저장소에서 보이는 `Docs/` 접두사를 이 안에 다시 만들지 않는다.
태스크 경로와 속성은 TaskNotes 안내에서 확인한다. `.codex`는 이 폴더를 가리키므로 두 곳을 따로 수정하지 않는다.

## 에이전트

| 문서 | 역할 |
|------|------|
| [제니스](agents/zenith-orchestrator.md) | 요청을 담당자와 스킬에 연결 |
| [게임 디자이너](agents/game-designer.md) | 플레이 장면·규칙·컨텐츠 기획 |
| [내러티브 디렉터](agents/narrative-director.md) | 세계관·용어·서사 정합 |
| [라이터](agents/writer.md) | 대사·로어·게임 안의 문장 |
| [아트 디렉터](agents/art-director.md) | 아트 방향·비주얼 규칙 |

## 스킬

| 문서 | 역할 |
|------|------|
| [planning-kickoff](skills/planning-kickoff/SKILL.md) | 새 컨텐츠의 요소와 방향 선택 |
| [brainstorm](skills/brainstorm/SKILL.md) | 아이디어 후보를 채팅에서 정리 |
| [decision-challenge](skills/decision-challenge/SKILL.md) | 중요한 결정의 가정·반례·제작 부담 검토 |
| [game-planning](skills/game-planning/SKILL.md) | 순수 게임 기획서 |
| [game-loop-planning](skills/game-loop-planning/SKILL.md) | 게임 전체 흐름과 세션 |
| [level-design](skills/level-design/SKILL.md) | 구역 배치·동선·시야와 공간 안의 긴장 흐름 |
| [knowledge-ops](skills/knowledge-ops/SKILL.md) | 기존 문서의 중복·분산·오래된 초안과 목차 정리 |
| [analyze-game](skills/analyze-game/SKILL.md) | 방향 선택용 외부 사례 브리핑 |
| [analyze-deep-game](skills/analyze-deep-game/SKILL.md) | 외부 게임 심층 분석 |
| [planning-content-narrative](skills/planning-content-narrative/SKILL.md) | 세계관·설정·용어와 선택·분기의 서사 |
| [create-tasknote](skills/create-tasknote/SKILL.md) | 태스크 초안·기획의 작업 분해 |
| [generate-spec](skills/generate-spec/SKILL.md) | 기존 스펙 요청을 TaskNotes 초안으로 연결 |
| [art-bible](skills/art-bible/SKILL.md) | 아트 디렉션 작성·보강 |
| [generate-asset-prompts](skills/generate-asset-prompts/SKILL.md) | 에셋 원화 프롬프트 파일 |
| [generate-keyart-prompts](skills/generate-keyart-prompts/SKILL.md) | 실내외 장면·키아트 프롬프트 |
| [auto-commit](skills/auto-commit/SKILL.md) | 요청받은 변경 사항 커밋 |

## 템플릿·작성 자료

| 문서 | 내용 |
|------|------|
| [서사 템플릿](skills/planning-content-narrative/template.md) | 세계관·설정 문서의 구성 |
| [플레이 경험 검토](skills/game-planning/references/play-experience.md) | 행동·선택·피드백·반복과 작은 검증 |
| [인터랙티브 서사 검토](skills/planning-content-narrative/references/interactive-story.md) | 선택·분기·행동과 이야기 전달의 조화 |
| [에셋 프롬프트 템플릿](skills/generate-asset-prompts/template.md) | 프롬프트 파일 구성 |
| [키아트 프롬프트 템플릿](skills/generate-keyart-prompts/template.md) | 실내외 장면 프롬프트 구성 |
| [실내 배경 규칙](skills/generate-keyart-prompts/indoor-background.md) | 공간·시점·광원과 예시 |
| [아트 바이블의 원본 스킬](https://github.com/Donchitos/Claude-Code-Game-Studios) | 프로젝트에 맞춰 조정한 원본 출처 |
| [결정 검토의 원본 스킬](https://github.com/ericrisco/rsc-harness/blob/main/skills/decision-challenge/SKILL.md) | npm `@ericrisco/rsc` 3.6.0 배포본의 검토 절차를 게임 기획용으로 조정 |
| [결정 검토 라이선스](skills/decision-challenge/LICENSE.txt) | 원본의 MIT 저작권·사용 허가 고지 |

## 역할이 겹칠 때

| 다루는 문제 | 담당 | 사용하는 절차 |
|------|------|------|
| 행동·게임 규칙·피드백 | 게임 디자이너 | game-planning과 플레이 경험 검토 |
| 반복·세션·복귀 흐름 | 게임 디자이너 | game-loop-planning |
| 구역 배치·동선·시야 | 게임 디자이너 | level-design |
| 사건·인물·분기의 의미 | 내러티브 디렉터 | planning-content-narrative와 인터랙티브 서사 검토 |
| 실제 대사·게임 안 문장 | 라이터 | 승인된 서사 방향에 따른 집필 |
| 공간의 미술·색·조명 기준 | 아트 디렉터 | art-bible |
| 문서의 배치·중복·목차 | 문서 정리 작업의 실행 담당 | knowledge-ops |

## 추가로 조정한 원본
npm `@ericrisco/rsc` 3.6.0 배포본에서 필요한 설계·정리 절차를 가져왔다.

| 원본 | 반영 위치·라이선스 |
|------|------|
| [level-design](https://github.com/ericrisco/rsc-harness/blob/main/skills/level-design/SKILL.md) | 공간 설계 스킬 · [MIT 고지](skills/level-design/LICENSE.txt) |
| [game-storytelling](https://github.com/ericrisco/rsc-harness/blob/main/skills/game-storytelling/SKILL.md) | 인터랙티브 서사 검토 자료 · [MIT 고지](skills/planning-content-narrative/LICENSE.txt) |
| [game-design](https://github.com/ericrisco/rsc-harness/blob/main/skills/game-design/SKILL.md) | 플레이 경험 검토 자료 · [MIT 고지](skills/game-planning/LICENSE.txt) |
| [knowledge-ops](https://github.com/ericrisco/rsc-harness/blob/main/skills/knowledge-ops/SKILL.md) | 기존 문서 정리 스킬 · [MIT 고지](skills/knowledge-ops/LICENSE.txt) |
