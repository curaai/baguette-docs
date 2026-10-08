# 키아트 채팅 출력 템플릿

파일을 만들지 않는다. 아래 블록을 채팅에 그대로 채운다.

## 응답 골격

```markdown
## 확정 범위
- 장면·시점: {실외 장면과 시점 / 실내 공간과 시점}
- 시리즈/개수: {단일 | 시점 N안 | 낮·폭우밤·새벽}
- 색감·무드: {§0 확정 문구}
- 조명: {포함 | 생략 | 시리즈 교체}

## 사용법 (Nano Banana)
1. (참조 이미지가 있으면) 함께 업로드
2. 아래 영문 프롬프트를 붙여넣기
3. 수정은 공간 구조·구도·레이어·명도부터

## 컨셉: {짧은 이름}
근거: {foundation/art-direction.md, narrative/…}
⚠️ 미결: {있을 때만}
참조 이미지: {있을 때만 — 경로 + 역할}

### 프롬프트
{실외: 레이어 고정 / 실내: 방의 구조·시선 축 고정}

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

실내 시리즈라면 공통 베이스에서 방 구조·카메라·주요 소품 위치를 고정하고, 버전별 문단에서는 광원·명도·분위기만 바꾼다. 바깥 능선·하늘 레이어는 넣지 않는다.

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

## 실내 공간·시선 문단 예시

실내 프롬프트는 산·하늘 대신 입구에서 방 안쪽 초점까지 이어지는 공간 관계를 고정한다. 세부 규칙과 대웅전 예시는 [indoor-background.md](indoor-background.md)를 따른다.

기본값을 적용할 때는 아래 두 프롬프트를 별도로 출력한다. 각각 독립된 이미지 1장을 생성하기 위한 프롬프트다.

```markdown
### 프롬프트 1 — 메인: 배경 설정 보드
{큰 아이소메트릭 컷어웨이 + 공간에 맞는 소품 콜아웃 + 정면/측면 뷰}

### 프롬프트 2 — 서브: 단일 실내 배경
{입구 안쪽에서 초점을 향하는 풀프레임 단일 장면, 도면·콜아웃 없음}
```

두 프롬프트는 방 구조·재료·소품 위치·팔레트를 맞춘다. 사용자가 다른 장수나 구도를 지정했다면 지정한 출력만 사용한다.

```text
Interior composition, locked: a clearly enclosed room with a readable floor, walls, posts, beams, and ceiling;
camera just inside the entrance, looking along the clear central floor toward the focal objects at the far end;
keep the entrance-side floor open, supporting props sparse and secondary, and the doorway/window light direction physically consistent;
no exterior landscape layers, no open-sky ceiling, no invented rooms or doors.
```

## 스타일·팔레트 앵커 (문서 기본, §0이 덮어쓰면 그쪽 우선)

```text
Late-summer monsoon Korean mountain temple, near-photoreal / grounded photographic look (not semi-stylized cartoon, not cozy pastel fantasy);
palette anchored in deep teal, black-brown, granite gray; ochre and faded dancheong only as sparse accent points;
highland isolation with open sky over the yard.
```

정본: `foundation/art-direction.md`

실내 장면은 해당 건물 문서의 분위기와 [indoor-background.md](indoor-background.md)를 함께 따른다. 외부의 열린 하늘·능선 문구는 실내에 복사하지 않는다.
