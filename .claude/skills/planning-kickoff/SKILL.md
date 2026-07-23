---
name: planning-kickoff
description: >
  기존 게임 안 컨텐츠 단위 기획을 Phase 1→2→3 순으로 시작한다.
  요소 제안 → 아이디어 2~3개+레퍼런스 브리핑 → PD 승인 후 기획 구체화.
  트리거: "기획 시작", "킥오프", "요소 제안", "zenith 시작", "새 주제 기획",
  "컨텐츠 기획 시작". 아이디어만 고민할 때는 brainstorm 스킬을 쓴다.
---

# 기획 킥오프 (컨텐츠 단위)

**zenith-orchestrator** 가 기존 Baguette 안 **컨텐츠/시스템 한 덩어리**를 새로 기획할 때 **기본 진입**.  
아이디어만 막혀서 후보를 좁힐 때는 `brainstorm`(이 스킬 대체 아님).

순서는 **1 → 2 → 3 강제**. 앞 단계 PD 잠금 없이 다음으로 가지 않는다.

## Phase 1 — 요소 제안 (PD ↔ Zenith)

**목표:** 다룰 **최초 아이템/요소** 후보를 제안·좁힘. 문서 본문 Write 전.

1. 주제 키워드만 와도 foundation·기존 planning을 짧게 훑고 **요소 후보**를 낸다.
2. **AskUserQuestion**으로 범위 잠금 (텍스트만 "어때요?" 금지). 도구 없으면 옵션 라벨을 구조화해 부모가 고르게.
3. **산출:** 잠긴 요소 목록 ≤1페이지 (채팅 또는 짧은 memo).

**금지:** `Docs/planning/**` 본문 Write. 마나에게 풀 기획서 위임 금지.

## Phase 2 — 아이디어 + 레퍼런스 브리핑

**목표:** 방향 선택용 짧은 제안 + 레퍼런스 맥락. 풀 기획서 아님.

1. Zenith가 **간단한 아이디어 2~3개** (컨텐츠 단위만). 여기서 막히면 `brainstorm`으로 채팅 정리를 받고 돌아온다.
2. 외부 사례가 선택에 필요하면 `game-designer`가 `analyze-game` 스킬로 한 페이지 브리핑 작성.
   - 기존 `Docs/reference/reference-game-*.md` 우선 Read.
   - 부족하면 `analyze-game` → `planning/references/<주제-kebab>.md`.
   - 실제 장면·핵심 차이·우리 선택지 2~3개만 작성.
   - 외부 사례가 필요 없으면 생략.
3. Phase 2 끝: **AskUserQuestion**으로 PD가 방향 선택.

**금지:** `Docs/planning/**` 풀 기획서 Write. Phase 3 승인 전 마나 풀 본문 위임 금지.

## Phase 3 — 기획 구체화

PD가 Phase 2 방향을 **명시 승인**한 뒤에만.

| 대상 | 위임 |
|------|------|
| 컨텐츠 단위 기획서 | `game-designer`(마나)가 `game-planning` 스킬로 작성 |
| 게임 전체 흐름과 세션 | `game-loop-planning` 스킬 |
| 비주얼 앵커 | `art-director` 병행 가능 |

## brainstorm 와의 구분

| | planning-kickoff | brainstorm |
|--|------------------|------------|
| 언제 | 컨텐츠 단위 **기획 시작** Phase 1→2→3 | 기획 중 **아이디어만** 고민·좁히기 |
| 산출 | 요소 잠금 → 방향 선택 → 기획 위임 | 채팅에 고른 방향·후보 정리 (파일 없음) |
| 본문 | Phase 1–2 planning Write **금지** | 풀 기획서 Write **금지** |

## 체크리스트

```
Kickoff:
- [ ] Phase 1: 요소 잠금 (AskUserQuestion) — planning Write 없음
- [ ] Phase 2: 아이디어 2~3 + 필요할 때만 레퍼런스 브리핑 — 방향 선택
- [ ] Phase 3: PD 승인 후에만 마나/art 위임
```
