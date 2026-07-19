#baguette

# TaskNotes — 작업 트래킹 정본

PD·에이전트의 **프로젝트 작업(태스크) 트래킹**은 이 문서 규칙을 따른다.

> **정본**: 프로젝트 할 일은 전부 Obsidian vault `Docs/` 안 **TaskNotes** 태스크 노트로 관리한다. 기획서 본문에 할 일을 흩뿌리지 않는다. **`Docs/specs/` 는 쓰지 않는다** — 구현 델타·`~ 현재` 스냅샷은 코드와 어긋나 context를 오염시킨다.

## 요약

- **작업 트래킹 = TaskNotes.** 태스크는 각각 하나의 Markdown 노트 (`Tasks/`).
- **뷰(칸반·목록)로 본다.** 뷰 파일: `Docs/TaskNotes/Views/*.base`.
- **문서(기획서)는 트래킹 도구가 아니다.** 체크리스트를 문서에 대량으로 쌓지 말고, 태스크는 TaskNotes에 만들고 문서에서는 **링크만** 건다.
- **태스크 = 임시 실행층.** `todo`/`in-progress` 태스크만 “지금 무엇을 할지”의 정본. `done`/`archived` 는 이력·칸반용이며, **구현 진실은 코드** + **체험 진실은 `planning/`**.

## Vault·경로

| 항목 | 값 |
|------|-----|
| Vault 루트 | `baguette-docs/` (Obsidian은 이 폴더를 vault로 연다. `.obsidian`은 여기) |
| 태스크 노트 폴더 | `Tasks/` (vault 루트 기준) — TaskNotes 설정의 task folder |
| 뷰(.base) 폴더 | `TaskNotes/Views/` |
| 임베드 경로 기준 | **vault 루트** — 예: `![[TaskNotes/Views/kanban-default.base]]` |

### 열기

1. Obsidian에서 **`baguette-docs/` 폴더를 vault로 연다.**
2. 코어 플러그인 **Bases** 활성화, 커뮤니티 플러그인 **TaskNotes** 활성화.
3. TaskNotes 설정에서 **task folder = `Tasks/`** 확인.
4. 아래 칸반을 쓰거나, 아무 노트에 `![[TaskNotes/Views/kanban-default.base]]` 임베드.

## 칸반 (상태별·타입별·우선순위별)

![[TaskNotes/Views/kanban-default.base]]

## 태스크 생성

- 명령 팔레트 **TaskNotes: Create new task** — 노트는 `Tasks/` 에 생성.
- 에이전트·PD가 제목만 던질 때: 스킬 **`create-tasknote`** — 초안 → PD 검수 → 승인 후 저장. 본문 참조는 `[[planning/…]]` 등 Obsidian 위키링크.
- 인라인 체크박스 → 그 줄에서 **Convert to TaskNote**.
- 태스크 노트 YAML(properties)이 뷰 필터·정렬·그룹 기준.

### 태그 규칙 (필수)

모든 태스크에 **분야 태그 1개**. 칸반 "타입별 보드" 열 구분.

| 태그 | 분야 |
|------|------|
| `기획` | 기획서·루프·문서 작업 |
| `아트` | 팔레트·에셋·비주얼·아트 바이블 |
| `프로그래밍` | Unity 구현·시스템·툴 |

- 태그 없으면 타입별 보드 **`미분류`**. **`tags`는 카테고리만** — 반드시 `task` + 분야(`기획` \| `아트` \| `프로그래밍`) **딱 이 두 개**(분야는 하나). 주제·시스템·도구 맥락은 **tags에 넣지 않는다**. 맥락은 **`projects`**·본문 `[[planning/…]]`·`[[에픽 태스크]]` 위키링크로.

### 프로젝트 · 슬라이스 (맥락)

TaskNotes에서 **`projects` = 부모 태스크 링크**이면 칸반 `hideTopLevelSubtasks` 시 **하위로 숨겨져** 루트만 보일 수 있다. **슬라이스 묶음에는 `projects` 쓰지 않는다.**

| 필드 | 용도 |
|------|------|
| **`contexts`** | 슬라이스·실행 묶음 |
| **`projects`** | (선택) **다른 태스크 노트**를 부모로 둘 때만 — 칸반에서 접히는 계층 |
| **본문 위키링크** | 에픽·서브태스크 |

- 칸반: `TaskNotes/Views/kanban-default.base` — `hideTopLevelSubtasks: false` (전 태스크 카드 노출)

### 상태·우선순위

- **status** (하나): `todo` | `in-progress` | `done` | `archived`. (`open` 등 사용 안 함)
- **priority**: `lowest` / `low` / `medium` / `high` / `highest`

## 뷰 목록

`TaskNotes/Views/kanban-default.base`:

| 뷰 | 그룹 기준 |
|------|-----------|
| 상태별 보드 | status |
| 타입별 보드 | 분야 태그 |
| 우선순위별 보드 | priority |
| 전체 목록 | 우선순위 정렬 |

- `tasks-default.base` — 오늘/이번주/지연/미예약 등
- `relationships.base` — 하위·blocking (태스크 노트 임베드용)

## planning / Tasks / foundation / 코드

| 트리 | 다루는 것 | 진실? |
|------|-----------|--------|
| **TaskNotes** (`Tasks/` + Views) | 지금 할 일 — 목표·작업·완료 기준·범위 밖 | 실행 정본 (`todo`/`in-progress`) |
| `planning/` | 체험·의도, 코어루프, 포함/비포함 | 체험 정본 |
| `foundation/` | PD 방향·기조·욕구 | 방향 초안 |
| **코드** | 동작·아키텍처 | 구현 정본 |

- 파이프라인: planning → TaskNotes(슬라이스) → 코드.
- 구현 전 **코드 1패스**. 문서에 “현재 구현” 스냅샷 금지.

### 태스크 본문 권장

- **목표**, **작업** 3~7개, **완료 기준**, 필요 시 **범위 밖**.
- 링크: `[[planning/<폴더>/…]]` 위키링크. 규칙: [[planning/README]]. 클래스명·파일 델타 목록 금지.
- `done`/`archived` 를 미완 작업 컨텍스트로 쓰지 않음.

## 에이전트·PD 규칙

- 기획서 본문에 체크리스트 대량 금지 → TaskNotes + 링크.
- 인라인 `- [ ]` 는 임시만. 트래킹 전환 시 **Convert to TaskNote**.
