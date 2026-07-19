---
name: create-tasknote
description: PD가 제안한 짧은 태스크 제목으로 TaskNotes용 `Docs/Tasks/*.md` 초안(태그·priority·본문)을 채우고 승인 후에만 파일을 쓴다. 트리거: 태스크 생성, TaskNotes 할일, 할일 추가, create tasknote, 태스크 초안.
---

# TaskNote 생성 (검수 후 저장)

PD가 **간략한 타이틀**만 주면, 에이전트가 TaskNotes 규칙에 맞게 **초안을 채워 검수를 받은 뒤** `Docs/Tasks/` 에 저장한다.

정본: [`Docs/TaskNotes/README.md`](../../TaskNotes/README.md) — 먼저 Read.

## 금지

- PD 승인 전 `Docs/Tasks/` 에 Write/Edit 하지 않는다.
- 기획서·스펙 본문에 할일 체크리스트를 새로 쌓지 않는다.

## 워크플로

### 1. 입력

- PD 타이틀(한 줄). 맥락(급함, 연관 스펙)이 있으면 반영.

### 2. 초안 작성 (채팅에만)

아래 필드를 채워 **한 블록**으로 보여준다.

| 필드 | 규칙 |
|------|------|
| **파일명** | `Docs/Tasks/{타이틀}.md` — 타이틀은 PD 제안을 기본, 파일명에 쓸 수 없는 문자만 정리 |
| **status** | 신규는 `todo` |
| **priority** | `lowest` / `low` / `medium` / `high` / `highest` — PD가 “최우선”이면 `highest` |
| **tags** | **`task` + 분야 하나만** (`기획` \| `아트` \| `프로그래밍`). 주제 맥락 태그 금지 |
| **contexts** | 슬라이스 v0: **`Prototype.V0`** (`projects`에 슬라이스 총괄 넣지 말 것 — 칸반에서 숨김) |
| **본문** | 목표 1~2문장, 불릿 작업 3~7개, 완료 기준 1~3개. 관련 문서는 **Obsidian 위키링크** (아래 절) |

### 본문 링크 (Obsidian)

태스크 본문·표 안의 문서 참조는 **Markdown 상대경로 링크 대신** vault 기준 위키링크를 쓴다. Obsidian에서 클릭·백링크·섹션 점프가 된다.

| 대상 | 형식 | 예 |
|------|------|-----|
| vault 루트의 노트 | `[[경로/파일명]]` (확장자 없음) | `[[planning/direction/art-direction]]`, `[[planning/content/proto-v0-play]]`, `[[TaskNotes/README]]` |
| 같은 폴더 `Tasks/` 태스크 | `[[노트 제목]]` | `[[버티컬 슬라이스 숲 마당 1컷]]`, `[[쉐이더 R&D]]` |
| 특정 헤딩 | `[[경로/파일명#헤딩 텍스트]]` | `[[planning/direction/art-direction#4. 렌더링 파이프라인]]` |
| 표시 텍스트 다를 때 | `[[경로#헤딩|보이는 글자]]` | `[[foundation/레퍼런스 게임#Mobile|AFK Journey]]` |

규칙:

- 경로는 **vault 루트(`Docs/`)** 기준. `Tasks/` 안에서도 `../foundation/…` Markdown 링크는 쓰지 않는다.
- `#` 뒤 헤딩은 해당 `.md`의 **헤딩 문자열과 동일**하게 (Obsidian “Copy link to heading” 기준).
- 외부 URL만 `https://…` 일반 링크.
- 초안(채팅)에도 본문 예시는 위키링크로 보여 PD가 그대로 검수한다.

**분야 태그 힌트**

- Mixamo·스프라이트·팔레트·쉐이더·에셋 → `아트`
- Unity·시스템·리팩터·버그 → `프로그래밍`
- 기획서·루프·문서·스펙 정리 → `기획`

### 3. 검수 (필수)

**AskUserQuestion** 으로 PD에게 묻는다. 텍스트로만 “괜찮아요?” 금지.

옵션 예:

- (Recommended) 승인 — 이대로 `Docs/Tasks/` 저장
- 타이틀/파일명 수정
- priority·태그 수정
- 본문만 수정
- 취소 — 파일 쓰지 않음

수정 요청이 오면 초안을 고친 뒤 **다시 3단계** (승인될 때까지).

### 4. 저장

승인 후에만 파일 생성. frontmatter 형식:

```yaml
---
status: todo
priority: medium
tags:
  - task
  - 기획
contexts:
  - Prototype.V0
---

(본문 Markdown)
```

기존 태스크와 같은 톤·깊이. XML 문서 주석 없음.

### 5. 끝

저장 경로 한 줄 + Obsidian에서 칸반 **타입별 보드**로 확인 안내(한 문장).

## 초안 출력 템플릿 (채팅용)

```markdown
## TaskNote 초안 (미저장)

**파일**: `Docs/Tasks/….md`

| status | priority | tags |
|--------|----------|------|
| todo | … | task, … |

### 본문
…
```

## 예시

**PD**: `캐릭터 기본 애니메이션 mixamo`

**에이전트**: priority `highest`, tags `task`, `아트`만 — Mixamo 맥락은 본문·`[[planning/…]]` — → AskUserQuestion → 승인 후 저장.
