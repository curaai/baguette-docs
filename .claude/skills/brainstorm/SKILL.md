---
name: brainstorm
description: "가이드형 게임 컨셉 발상 — 아이디어 제로에서 구조화된 게임 컨셉 문서까지. 스튜디오식 브레인스토밍, 플레이어 심리 틀, 단계적 탐색을 사용한다. 기존 게임 안 컨텐츠 단위 시작은 planning-kickoff를 쓴다(이 스킬 대체 아님)."
argument-hint: "[장르·테마 힌트 또는 open] [--review full|lean|solo]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Write, WebSearch, Task, AskUserQuestion
---

이 스킬이 호출되면:

1. **인자 파싱**: 선택적 장르·테마 힌트(예: `roguelike`, `space survival`, `cozy farming`). `open` 이거나 인자 없으면 백지에서 시작. 리뷰 모드도 한 번 정해 이번 실행의 모든 게이트에 재사용:
   1. `--review [full|lean|solo]` 가 있으면 그 값 사용
   2. 아니면 `.claude/review-mode.txt` 가 있으면 첫 토큰을 `full` \| `lean` \| `solo` 로 읽기
   3. 아니면 기본 `lean`

2. **기존 컨셉 작업 확인**:
   - `Docs/planning/game-concept.md` 있으면 읽기(이어가기, 처음부터 다시 하지 않음)
   - `Docs/planning/game-pillars.md` 있으면 읽기(확정 필러 위에 쌓기)

3. **발상 단계를 대화형으로 진행** — 매 단계 사용자에게 질문. 전부 조용히 생성하지 말 것. 목표는 **협업 탐색**이며, AI는 인간의 비전을 대체하는 게 아니라 촉진 역할.

   브레인스토밍 전반의 **핵심 결정점**에서 **`AskUserQuestion`** 사용:
   - 취향 제한 질문(장르 선호, 범위, 팀 규모)
   - 옵션 제시 뒤 컨셉 선택("어떤 2~3개가 와닿나?")
   - 방향 선택("더 파고들기 / 더 탐색 / 프로토타입?")
   - 컨셉 다듬은 뒤 필러 순위
   먼저 대화에 창의적 분석을 **전부** 쓰고, 이어서 `AskUserQuestion`으로 짧은 라벨로 결정을 캡처한다.

   스튜디오식 브레인스토밍 원칙:
   - 판단 유보 — 탐색 중엔 나쁜 아이디어 없음
   - 기발한 아이디어 장려 — 상자 밖 사고가 더 나은 컨셉을 낳음
   - 서로 위에 쌓기 — "yes, and..." 가 아니라 "but..." 금지
   - 제약을 연료로 — 제한이 최선의 아이디어를 자주 만든다
   - 단계마다 타임박스 — 초반 과도한 숙고로 속도 죽이지 않기

---

### Phase 1: 크리에이티브 디스커버리

게임보다 **사람**을 먼저 이해한다. 아래는 대화로 묻는다(체크리스트처럼 한꺼번에 금지).

**감정 앵커**:
- 게임에서 진심으로 감동했거나, 짜릿했거나, 시간 가는 줄 몰랐던 순간은? 그 느낌을 만든 구체는?
- 게임에서 항상 찾았지만 제대로 못 찾았던 판타지나 파워 트립이 있는가?

**취향 프로필**:
- 가장 오래 붙잡은 게임 3개는? 무엇이 다시 켜게 했는가?
  *(이건 **일반 대화**로 묻는다 — 사용자가 특정 타이틀을 자유 타이핑해야 한다. AskUserQuestion 프리셋 옵션에 넣지 말 것.)*
- 좋아하는 장르? 피하는 장르? 이유?
- 도전·휴식·스토리·자기표현 중 무엇을 선호하는가? *(이건 `AskUserQuestion` — 제한 선택.)*

**실무 제약** (브레인스토밍 전에 샌드박스 형태를 잡는다).
아래를 **하나의 multi-tab `AskUserQuestion`** 으로 묶되, 탭 라벨은 **정확히** 이 문자열을 쓴다:
- Tab "Experience" — "What kind of experience do you most want players to have?" (Challenge & Mastery / Story & Discovery / Expression & Creativity / Relaxation & Flow)
- Tab "Timeline" — "What's your realistic development timeline?" (Weeks / Months / 1-2 years / Multi-year)
- Tab "Dev level" — "Where are you in your dev journey?" (First game / Shipped before / Professional background)

탭 이름을 바꾸거나 중복하지 말 것.

답을 **크리에이티브 브리프**로 압축 — 감정 목표·취향·제약을 3~5문장으로. 브리프를 다시 읽어 주고 의도를 잡았는지 확인.

---

### Phase 2: 컨셉 생성

크리에이티브 브리프를 바탕으로 서로 다른 방향의 **컨셉 3개**를 낸다. 기법:

**기법 1: 동사 우선**
핵심 플레이어 동사(짓다, 싸우다, 탐험하다, 풀다, 살아남다, 창조하다, 관리하다, 발견하다)에서 바깥으로 확장. 동사가 곧 게임이다.

**기법 2: 매시업**
뜻밖의 둘을 합친다: [장르 A] + [테마 B]. 둘 사이 긴장이 훅이 된다. (예: "농장 시뮘 + 코스믹 호러", "로그라이크 + 연애 시뮘", "시티 빌더 + 실시간 전투")

**기법 3: 경험 우선(MDA 역방향)**
원하는 플레이어 감정(MDA 미학: 감각, 판타지, 내러티브, 도전, 동료성, 발견, 표현, 몰입)에서 출발해, 그걸 만드는 다이내믹스·메카닉으로 거슬러 올라간다.

컨셉마다 제시:
- **가제목**
- **엘리베이터 피치** (1~2문장 — "10초 테스트" 통과)
- **코어 동사** (가장 자주 하는 행동 하나)
- **코어 판타지** (감정적 약속)
- **유니크 훅** ("X 같은데, 거기에 Y까지" 테스트)
- **주된 MDA 미학** (어떤 감정이 지배하는가)
- **추정 스코프** (small / medium / large)
- **통할 수 있는 이유** (시장·오디언스 한 문장)
- **최대 리스크** (가장 어렵게 남은 질문 한 문장)

셋 다 보여 준 뒤 `AskUserQuestion`으로 선택을 캡처한다.

**중요**: 여기서는 **반드시 평범한 prompt + options 호출** — tabs·폼 필드 금지. 구조는 아래와 같이:

```
AskUserQuestion(
  prompt: "Which concept resonates with you? You can pick one, combine elements, or ask for fresh directions.",
  options: [
    "Concept 1 — [Title]",
    "Concept 2 — [Title]",
    "Concept 3 — [Title]",
    "Combine elements across concepts",
    "Generate fresh directions"
  ]
)
```

여기서 `tabs` 필드를 쓰지 말 것. `tabs`는 다중 필드 입력 전용 — 여기 쓰면 "Invalid tool parameters" 오류. 순수 `prompt` + `options` 호출만.

선택을 재촉하지 말고 생각할 시간을 준다.

---

### Phase 3: 코어 루프 설계

선택된 컨셉에 대해 구조화된 질문으로 코어 루프를 쌓는다. 코어 루프는 게임의 심장 — 단독으로 재미없으면 콘텐츠·폴리시로 구할 수 없다.

**30초 루프** (모멘트 투 모멘트):

아래는 `AskUserQuestion` 호출로 — 옵션은 선택된 컨셉에서 **유도**하고 하드코딩하지 말 것:

1. **코어 액션 느낌** — 프롬프트: "What's the primary feel of the core action?" 장르·톤에 맞는 옵션 3~4개 + 자유 서술 탈출구(`I'll describe it`).

2. **핵심 설계 차원** — 이 컨셉에서 가장 중요한 설계 변수(예: 세계 반응성, 페이싱, 플레이어 에이전시)를 집고 질문. 컨셉에 맞는 옵션 생성. 항상 자유 서술 탈출구 포함.

답을 받은 뒤 분석: 이 행동이 본질적으로 만족스러운가? 무엇이 좋게 느껴지게 하는가? (오디오 피드백, 비주얼 쥬스, 타이밍 만족, 전술 깊이?)

**5분 루프** (단기 목표):
- 모멘트 플레이를 주기로 묶는 구조는?
- "한 판 더" 심리가 어디서 도는가?
- 이 레벨에서 플레이어 선택은?

**세션 루프** (30~120분):
- 한 세션의 완결 모습은?
- 자연스러운 멈춤 지점은?
- 플레이하지 않을 때 생각나게 하는 훅은?

**진행 루프** (일/주):
- 플레이어는 어떻게 성장하는가? (파워? 지식? 선택지? 스토리?)
- 장기 목표는? 게임이 "끝났다"고 할 때는?

**플레이어 동기 분석** (자기결정이론):
- **자율성**: 의미 있는 선택이 얼마나 있는가?
- **유능감**: 기술 성장을 어떻게 느끼게 하는가?
- **관계성**: 캐릭터·다른 플레이어·세계와 어떻게 연결되는가?

---

### Phase 4: 필러와 경계

게임 필러는 God of War, Hades, The Last of Us 같은 AAA에서 수백 명이 같은 방향으로 결정하도록 쓴다. 솔로 개발에도 필러는 스코프 크립을 막고 비전을 날카롭게 유지한다.

협업으로 **필러 3~5개** 정의:
- 필러마다 **이름** + **한 문장 정의**
- 필러마다 **디자인 테스트**: "X와 Y 사이에서 논쟁이면 이 필러는 __ 쪽"
- 필러끼리 **긴장**이 느껴져야 한다 — 전부 같은 방향이면 일이 덜 된다

이어 **안티필러 3개 이상**(이 게임이 **아닌 것**):
- 안티필러는 가장 흔한 스코프 크립을 막는다: 비전에 안 서는 "재밌지 않을까..." 기능
- 문장 형식: "[일]은 하지 않는다 — [필러]를 해치기 때문"

**필러 확정**: 전체 필러 세트를 보여 준 뒤 `AskUserQuestion`:
- Prompt: "Do these pillars feel right for your game?"
- Options: `[A] Lock these in` / `[B] Rename or reframe one` / `[C] Swap a pillar out` / `[D] Something else`

사용자가 B/C/D면 수정 후 다시 `AskUserQuestion`:
- Prompt: "Pillars updated. Ready to lock these in?"
- Options: `[A] Lock these in` / `[B] Revise another pillar` / `[C] Something else`

`[A] Lock these in` 선택될 때까지 반복.

**리뷰 모드 확인** — `art-director` 스폰 **전**: `solo`/`lean` → 생략, 메모 "Visual anchor skipped — [Mode] mode." 후 Visual Identity Anchor는 비워두고 Phase 5로. `full` → 정상 스폰.

**필러·안티필러는 위에서 이미 PD가 직접 Lock 했다** — 별도 검증 없음. `full` 모드면 Phase 5로 가기 전에 `art-director` 를 Task로 스폰해 비주얼 방향을 받는다.

넘길 것: 게임 컨셉 엘리베이터 피치, 디자인 테스트 포함 전체 필러, 타깃 플랫폼(알면), 사용자가 말한 레퍼런스 게임·비주얼 터치스톤.

결과(이름 붙은 비주얼 방향 2~3개)를 `AskUserQuestion`으로 제시: 방향마다 하나씩 + `Combine elements across directions` + `Describe my own direction`.

사용자가 고른 비주얼 앵커(이름 붙은 방향 또는 사용자 서술)를 **Visual Identity Anchor**로 저장 — 게임 컨셉 문서에 쓰이고 아트 바이블의 씨앗이 된다.

---

### Phase 5: 플레이어 유형 검증

Bartle 분류와 Quantic Foundry 동기 모델로 **이 게임이 실제로 누구를 위한지** 검증:

- **1차 플레이어 유형**: 누가 이 게임을 **사랑**할까? (Achievers, Explorers, Socializers, Competitors, Creators, Storytellers)
- **2차 호소**: 또 누가 즐길 수 있나?
- **이 게임이 아닌 사람**: 싫어할 사람을 밝히는 것도, 좋아할 사람을 아는 것만큼 중요
- **시장 검증**: 비슷한 플레이어 유형을 노린 성공작이 있는가? 오디언스 규모에서 배울 점은?

---

### Phase 6: 스코프와 실현 가능성

컨셉을 현실에 붙인다:

- **타깃 플랫폼**: `AskUserQuestion` — "What platforms are you targeting for this game?"
  Options: `PC (Steam / Epic)` / `Mobile (iOS / Android)` / `Console` / `Web / Browser` / `Multiple platforms`
  답을 기록 — 이후 엔진 판단에 직결. 관련 시 플랫폼 함의 메모(예: 모바일은 Unity 선호 강함; 콘솔은 Godot 제약; 웹은 Godot 유리 등).

- **엔진 경험**: `AskUserQuestion` — "Do you already have an engine you work in?"
  Options: `Godot` / `Unity` / `Unreal Engine 5` / `No preference — help me decide`
  - 엔진을 고르면 → 선호로 기록하고 진행. **재반박하지 말 것.**
  - "No preference"면 컨셉·플랫폼에 맞는 Godot/Unity/Unreal 트레이드오프를 이 자리에서 짧게 요약해 바로 고르게 한다(별도 엔진설정 스킬 없음).
- **아트 파이프라인**: 스타일과 공수는?
- **콘텐츠 스코프**: 레벨/에리어 수, 아이템 수, 플레이 시간 추정
- **MVP 정의**: "코어 루프가 재미있는가"를 검증하는 **최소** 빌드는?
- **최대 리스크**: 기술·디자인·시장
- **스코프 티어**: 풀 비전 vs 시간이 부족할 때 출하분

**가장 큰 기술 리스크를 짚은 뒤, 스코프 티어를 정하기 전에** 지금까지 모은 정보(코어 루프, 플랫폼, 엔진, 기술 리스크)로 실현 가능성을 직접 종합한다(전담 기술 디렉터 에이전트 없음 — Claude가 평가하고 PD가 최종 판단). 리스크가 크면 명시하고 `AskUserQuestion`으로 확인:
- Prompt: "Given [핵심 기술 리스크], does the current direction still feel feasible?"
- Options: `[A] Yes — proceed` / `[B] Reconsider scope or platform` / `[C] Something else`

**스코프 티어 정의 후**, 같은 방식으로 스코프 현실성(풀 비전 vs MVP vs 일정·팀 규모)을 종합해 `AskUserQuestion`으로 확인:
- Prompt: "Does this scope feel realistic given your timeline and team size?"
- Options: `[A] Yes — lock this scope` / `[B] Adjust MVP or scope tier` / `[C] Something else`

---

4. **게임 컨셉 문서 생성** — `Docs/planning/game-concept.md` 에 브레인스토밍 대화 내용으로 아래 섹션을 **모두** 채운다(전용 템플릿 파일 없음 — 이 목록이 곧 구조):
   - Core Identity (엘리베이터 피치, 코어 동사, 코어 판타지, 유니크 훅, 추정 스코프)
   - MDA 분석, 플레이어 동기 프로필(자기결정이론 + Bartle/Quantic Foundry 유형)
   - 필러·안티필러(디자인 테스트 포함), 코어 루프(30초/5분/세션/진행)
   - MVP 정의·스코프 티어·최대 리스크

   문서에 **Visual Identity Anchor** 섹션을 포함:
   - 선택된 비주얼 방향 이름
   - 한 줄 비주얼 규칙
   - 디자인 테스트가 붙은 지원 비주얼 원칙 2~3개
   - 색 철학 요약

   이 섹션은 아트 바이블의 씨앗 — 세션 사이에 잊히기 전에 "전부 움직여야 한다"는 결정을 고정한다.

5. 쓰기 승인은 `AskUserQuestion`:
- Prompt: "Game concept is ready. May I write it to `Docs/planning/game-concept.md`?"
- Options: `[A] Yes — write it` / `[B] Not yet — revise a section first`

[B]이면 어떤 섹션을 고칠지 `AskUserQuestion`으로: `Elevator Pitch` / `Core Fantasy & Unique Hook` / `Pillars` / `Core Loop` / `MVP Definition` / `Scope Tiers` / `Risks` / `Something else — I'll describe`

수정 뒤에는 갱신 섹션을 diff 또는 명확한 전후로 보여 주고 `AskUserQuestion` — "Ready to write the updated concept document?"
Options: `[A] Yes — write it` / `[B] Revise another section`
`[A]` 선택될 때까지 반복.

예이면 템플릿으로 문서 생성·전 섹션 채우기·필요 시 디렉터리 생성까지 Write.

**스코프 일관 규칙**: Core Identity 표의 "Estimated Scope" 는 Scope Tiers의 풀 비전 타임라인과 **맞아야** 한다 — "Large (9+ months)"만 쓰지 말고 "Large (X–Y개월, solo)" 또는 "Large (X–Y개월, 팀 N명)"처럼 요약 표가 정확하게.

6. **다음 단계 제안** (이 저장소에 실제로 있는 스킬·에이전트만):
   1. "다음 컨텐츠/시스템은 `planning-kickoff` 로 시작 — 요소 제안 → 아이디어+레퍼런스 브리핑 → PD 승인 후 구체화"
   2. "컨텐츠 기획서는 `game-designer`가 `game-planning` 스킬로 작성한다. 스펙은 `generate-spec` 스킬로 작성한다"
   3. "게임 전체 흐름과 세션은 `game-loop-planning` 스킬, 컨텐츠 단위 기획서는 `game-designer`, 비주얼은 `art-director`, 세계관·용어는 `narrative-game-designer` 에게 위임"

7. **요약 출력**: 선택 컨셉 엘리베이터 피치, 필러, 1차 플레이어 유형, 엔진 권장(있다면), 최대 리스크, 파일 경로.

판정: **COMPLETE** — 게임 컨셉 생성·다음 단계 인계 완료.

---

## 컨텍스트 창 인지

다단계 스킬이다. 어느 Phase에서든 컨텍스트가 70% 이상이면, 계속하기 **전에** 현재 응답에 아래 알림을 덧붙인다:

> **Context is approaching the limit (≥70%).** The game concept document is saved
> to `Docs/planning/game-concept.md`. Open a fresh Claude Code session to continue
> if needed — progress is not lost.
