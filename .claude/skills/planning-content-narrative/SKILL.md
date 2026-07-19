---
name: planning-content-narrative
description: >
  세계관·설정·용어·로어·톤 등 **narrative 관련 컨텐츠**를 `Docs/narrative/**` 에 작성하기 위한 스킬.
  메카닉·루프·수치·UI 흐름은 다루지 않는다(그쪽은 `Docs/planning/` + game-designer 담당).
user-invocable: true
argument-hint: "[narrative 주제 또는 파일명 힌트]"
---

# Narrative 컨텐츠 작성 스킬 (Docs/narrative 전용)

이 스킬은 **`Docs/narrative/**` 에 들어갈 narrative 문서**(세계관 시트, 용어표 항목, 캐릭터 스냅샷, 로어 단편, 톤 가이드 등)를 쓰기 위한 가이드와 템플릿이다.

## 적용 범위 (반드시 준수)

- **출력 경로:** `Docs/narrative/**` 만 사용한다. `Docs/planning/`·`Docs/specs/` 에는 쓰지 않는다.
- **다루는 내용:** 세계관, 설정, 용어, 캐릭터·존재, 장소, 시대·연표, 로어 단편, 톤·금지어 등 **narrative만**.
- **다루지 않는 내용:** 코어루프, 메카닉, 수식, 시스템 다이어그램, UI 흐름, 데이터 스키마, 코드 델타.
- 메카닉이 narrative와 관련될 때는 “세계 안에서 어떻게 보이는가”의 **프레이밍**까지만 적고, 메카닉 본문은 `Docs/planning/`(마나) 으로 링크만 남긴다.

## 언제 쓰나

- `Docs/narrative/` 에 새 세계관·용어·로어·캐릭터 문서가 필요할 때
- 기존 narrative 초안이 톤·용어가 흩어져 있어 정본 한 장으로 정리해야 할 때
- 메카닉 문서가 “세계 톤”과 어긋나는 표현을 쓰고 있어 narrative 쪽 정본이 필요할 때

## 출력 규칙

- 본문은 **세계 안에서 읽히는 글**(서술·앵커·톤)로 쓴다. 표/명세형 문체는 최소화.
- 새로운 용어는 **용어표 항목**으로 따로 박는다(중복 방지).
- 톤·금지어는 **명확한 예시 1개 이상**과 함께 둔다.
- narrative 외 주제(메카닉·UI·수치)가 보이면 그 자리에서 멈추고 “해당 부분은 `Docs/planning/` 정본 참조”라고 링크만.

## 작업 절차

1. `Docs/narrative/README.md` 와 기존 `Docs/narrative/**` 문서를 먼저 읽어 톤·용어 충돌을 확인한다.
2. `template.md` 스켈레톤을 대상 파일에 깔고, **상단(요지·세계 위치·톤)부터** 채운다.
3. 새 용어가 생기면 **용어표 항목**을 같이 추가하거나, 기존 용어표에 1줄 반영.
4. 마지막에 “열린 질문(결정 필요)”과 “충돌·확인 필요”를 정리한다.

## 위임·연동

- 메인 위임 대상: **narrative-game-designer**(렉시) — 설정·용어·캐논 정리.
- 후속: **writer**(나나) — 위 정본을 기반으로 대사·플레이어 향 카피.
- 메카닉 충돌이 보이면 **game-designer**(마나) 와 정렬한다(메카닉 쪽 정본은 `Docs/planning/`).

## 템플릿

- 스켈레톤: `Docs/.claude/skills/planning-content-narrative/template.md`
