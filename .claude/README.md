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
| [game-planning](skills/game-planning/SKILL.md) | 순수 게임 기획서 |
| [game-loop-planning](skills/game-loop-planning/SKILL.md) | 게임 전체 흐름과 세션 |
| [analyze-game](skills/analyze-game/SKILL.md) | 방향 선택용 외부 사례 브리핑 |
| [analyze-deep-game](skills/analyze-deep-game/SKILL.md) | 외부 게임 심층 분석 |
| [planning-content-narrative](skills/planning-content-narrative/SKILL.md) | 세계관·설정·용어 |
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
| [에셋 프롬프트 템플릿](skills/generate-asset-prompts/template.md) | 프롬프트 파일 구성 |
| [키아트 프롬프트 템플릿](skills/generate-keyart-prompts/template.md) | 실내외 장면 프롬프트 구성 |
| [실내 배경 규칙](skills/generate-keyart-prompts/indoor-background.md) | 공간·시점·광원과 예시 |
| [아트 바이블의 원본 스킬](https://github.com/Donchitos/Claude-Code-Game-Studios) | 프로젝트에 맞춰 조정한 원본 출처 |
