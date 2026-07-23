# baguette-docs/.claude (기획 Agent·Skill 정본)

이 폴더가 Baguette 기획·서사·분석 Agent/Skill 의 정본이다 (`baguette-docs`).

## 기획 킥오프 (제니스 기본 진입)

새 주제·「기획 시작」→ **`skills/planning-kickoff/`** Phase **1→2→3** (스킵·마나 숏컷 금지).

| Phase | 내용 | 담당 |
|-------|------|------|
| 1 | 최초 아이템/요소 제안·잠금 | PD ↔ Zenith (AskUserQuestion). planning 본문 금지 |
| 2 | 아이디어 2~3 + 필요할 때 레퍼런스 브리핑 | Zenith + `game-designer`. 방향 선택 후 |
| 3 | 기획 구체화 (PD 승인 후) | 컨텐츠→마나 / 흐름→`game-loop-planning` / 비주얼→art |

`brainstorm` = 기획서용 아이디어를 채팅에 정리. 컨텐츠 단위 **시작**은 kickoff.

## Agents

| 경로 | 역할 |
|------|------|
| `agents/zenith-orchestrator.md` | 오케스트레이터 — 킥오프 1→2→3 후 위임 |
| `agents/game-designer.md` (마나) | `Docs/planning/**` 컨텐츠 기획서 (킥오프 Phase 3+) |
| `agents/narrative-game-designer.md` | 세계관·용어·설정 정합 |
| `agents/writer.md` | 대사·로어·플레이어 향 텍스트 |
| `agents/art-director.md` | 아트 바이블·비주얼 스펙 문서 |

## Skills

| 경로 | 역할 |
|------|------|
| `skills/planning-kickoff/` | 컨텐츠 단위 기획 시작 Phase 1→2→3 |
| `skills/analyze-game/` | 방향 선택용 한 페이지 레퍼런스 브리핑 |
| `skills/analyze-deep-game/` | 게임 자체 심층 분석 + 선택한 항목의 별도 우리 게임 비교 |
| `skills/brainstorm/` | 컨셉·컨텐츠 기획용 아이디어를 채팅에 정리 |
| `skills/game-planning/` | 순수 게임 기획서 작성 |
| `skills/game-loop-planning/` | 게임 전체 흐름과 세션 구성 |
| `skills/generate-spec/` | 프로그래머 스펙 |
| `skills/planning-content-narrative/` | narrative 컨텐츠 |
| `skills/create-tasknote/` | TaskNotes 초안 |
| `skills/generate-asset-prompts/` | 에셋 프롬프트 |

## 경로 규칙

스킬·에이전트 문서의 `Docs/...` 는 **이 vault가 게임 레포의 `Docs/` submodule로 붙을 때** 기준이다.  
Cursor에서 `baguette-docs`만 단독으로 열면 vault 루트 = 여기이므로, 실제 파일 쓰기는 `planning/`, `Tasks/` 등 **루트 상대 경로**를 쓴다.
