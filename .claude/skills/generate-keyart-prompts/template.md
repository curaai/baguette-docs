# 키아트 채팅 출력 템플릿

파일을 만들지 않는다. 아래 블록을 채팅에 그대로 채운다.

## 응답 골격

```markdown
## 확정 범위
- 시점: {원경만 / 절터→원경 / 산길·입구→원경 / …}
- 시리즈/개수: {단일 | 시점 N안 | 낮·폭우밤·새벽}
- 색감·무드: {§0 확정 문구}
- 조명: {포함 | 생략 | 시리즈 교체}

## 사용법 (Nano Banana)
1. (참조 이미지가 있으면) 함께 업로드
2. 아래 영문 프롬프트를 붙여넣기
3. 수정은 레이어·명도·안개 밀도부터

## 컨셉: {짧은 이름}
근거: {foundation/art-direction.md, narrative/…}
⚠️ 미결: {있을 때만}
참조 이미지: {있을 때만 — 경로 + 역할}

### 프롬프트
{레이어 고정}

{장면/구도 — 색감·테마·무드 포함}

{조명 연출 — 포함/시리즈일 때만}

{스타일 앵커}

{기술 조건 — 기본: FHD 1920×1080, 16:9}
```

기술 조건 영문 기본 문구:

```text
Technical: FHD 1920x1080 (16:9) key art, no text, no watermark, …
```


## 시간대 시리즈일 때

```markdown
### 프롬프트
공통 베이스 (모든 버전 동일):
{레이어 + 장면 골격 + 색감·테마 + 스타일 + 기술조건 — 조명만 비움}

--- 낮 ---
{낮 전용 조명·능선 가독}

--- 폭우밤 ---
{능선 은닉·국소광}

--- 새벽 ---
{안개 감소·중성광·잔향}
```

## 레이어 문단 예시 (영문 패턴)

절터 → 원경:

```text
Depth layers, locked: sparse near silhouettes of temple courtyard wall and stone base only;
mid-ground hillside hardwood clusters and low canopy masses in mist, not filling the sky;
far background 2–3 soft mountain ridge layers with low-density tree silhouettes, one value step darker than any temple massing;
open highland sky as the main clear plane above the yard.
```

원경만:

```text
Depth layers, locked: almost no playable foreground; mid only as soft forest mass under mist;
far 2–3 ridge silhouettes with sparse canopy; sky dominant; not an explorable trail scene.
```

산길 → 원경:

```text
Depth layers, locked: near = wet path and sparse trail markers only; mid = close canopy and trunks creating isolation;
far = 1–2 ridge hints often veiled in cold mist — background for disorientation, not a destination vista.
```

## 스타일·팔레트 앵커 (문서 기본, §0이 덮어쓰면 그쪽 우선)

```text
Late-summer monsoon Korean mountain temple, near-photoreal / grounded photographic look (not semi-stylized cartoon, not cozy pastel fantasy);
palette anchored in deep teal, black-brown, granite gray; ochre and faded dancheong only as sparse accent points;
highland isolation with open sky over the yard.
```

정본: `foundation/art-direction.md`
