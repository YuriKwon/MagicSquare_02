# MagicSquare — 4×4 Magic Square

4×4 마방진(Magic Square)을 다루는 학습·실습 프로젝트입니다.  
**문제 인식·정의**를 마친 뒤, **Dual-Track TDD**와 **ECB 아키텍처**로 구현을 진행 중입니다.

---

## 프로젝트 한 줄 요약

> 4×4 격자에서 **유효 배치가 무엇인지**를 규칙(불변 조건)으로 고정하고, 그에 대한 **판정 책임**(과 필요 시 **도출 책임**)을 일관된 기준으로 수행하도록 훈련하는 문제이다.

“마방진 그림을 한 번 출력한다”가 아니라, **맞음의 정의·검증·(선택) 생성**을 명확히 하는 것이 본 프로젝트의 출발점입니다.

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| 문제 인식·정의 (STEP 1~5) | ✅ 완료 |
| 보고서 (`Report/`) | ✅ 작성됨 |
| ECB 소스 (`src/`) | ✅ Boundary · Control · Entity 스켈레톤 |
| Dual-Track TDD | 🔄 **RED → GREEN** 진행 중 |
| Legacy GREEN (AC-FR-01-01) | ✅ 34건 PASS (`BoundaryValidator`, `ResolveUseCase`) |
| Full RED (U-IN-01~03) | ❌ 7건 FAIL (`InputValidator` E00x 계약) |
| Skeleton RED (U-IN-04~, D-*) | ⚠️ 23건 collection ERROR (import 경로 미정렬) |

### Python · 테스트 환경

- Python `3.10+` (`.python-version` 기준 `3.10`)
- pytest + pytest-cov
- 아키텍처: **ECB** (Boundary → Control → Entity)
- 테스트 전략: **Dual-Track TDD** (RED → GREEN → REFACTOR)
- 커버리지 목표: **80%+**

```powershell
cd c:\Users\usejen_id\Downloads\CursorAI-main\DEV\MagicSquare
python -m pytest tests/boundary/test_boundary_validator_size.py tests/control/test_resolve_use_case_size_guard.py -v
```

---

## TDD 진행 현황

### Legacy GREEN — AC-FR-01-01 (`INVALID_SIZE`)

| 파일 | Test ID / AC | 건수 | 상태 |
|------|--------------|------|------|
| `tests/boundary/test_boundary_validator_size.py` | AC-FR-01-01 (`BoundaryValidator`) | 18 | ✅ PASS |
| `tests/control/test_resolve_use_case_size_guard.py` | AC-FR-01-01 (Control 격리) | 16 | ✅ PASS |

### Full RED — FR-01 Input Validation (`E00x` envelope)

| 파일 | Test ID | 건수 | 상태 |
|------|---------|------|------|
| `tests/boundary/test_ac_fr_01_01_input_validation.py` | U-IN-01~03 | 7 | ❌ FAIL |

### Skeleton RED — Dual-Track (Track A + B)

| 파일 | Test ID | 건수 | 상태 |
|------|---------|------|------|
| `tests/boundary/test_u_in_04_05.py` | U-IN-04, U-IN-05 | 2 | ⚠️ collection ERROR |
| `tests/boundary/test_u_in_06_08.py` | U-IN-06, U-IN-07, U-IN-08 | 3 | ⚠️ collection ERROR |
| `tests/boundary/test_u_out_01_03.py` | U-OUT-01~03 | 3 | ⚠️ collection ERROR |
| `tests/boundary/test_u_flow_02.py` | U-FLOW-02 (+ext×2) | 3 | ⚠️ collection ERROR |
| `tests/entity/test_d_loc_01.py` | D-LOC-01 | 1 | ⚠️ collection ERROR |
| `tests/entity/test_d_mis_01.py` | D-MIS-01 | 1 | ⚠️ collection ERROR |
| `tests/entity/test_d_val_01_06.py` | D-VAL-01~06 | 6 | ⚠️ collection ERROR |
| `tests/entity/test_d_sol_01_04.py` | D-SOL-01~04 | 4 | ⚠️ collection ERROR |
| **합계** | | **23** | |

> Skeleton 파일은 `pytest.fail("RED: …")` 패턴이며, import 경로(`boundary.*` → `src.boundary.*`) 정렬 후 FAIL로 전환됩니다.

---

## RED 커밋 권장 묶음 (Test ID 오름차순)

RED 단계를 **몇 개씩 묶어 커밋**할 때 아래 순서를 권장합니다.

| 커밋 | Test ID | 파일 | 건수 | 커밋 메시지 예시 |
|------|---------|------|------|------------------|
| RED-1 | U-IN-01~03 | `tests/conftest.py`, `tests/boundary/test_ac_fr_01_01_input_validation.py` | 7 | `test(red): add U-IN-01~03 full RED for FR-01 input validation` |
| RED-2 | U-IN-04~05 | `tests/boundary/test_u_in_04_05.py` | 2 | `test(red): add U-IN-04~05 skeleton RED` |
| RED-3 | U-IN-06~08 | `tests/boundary/test_u_in_06_08.py` | 3 | `test(red): add U-IN-06~08 skeleton RED` |
| RED-4 | U-OUT-01~03 | `tests/boundary/test_u_out_01_03.py` | 3 | `test(red): add U-OUT-01~03 skeleton RED` |
| RED-5 | U-FLOW-02 (+ext×2) | `tests/boundary/test_u_flow_02.py` | 3 | `test(red): add U-FLOW-02 skeleton RED` |
| RED-6 | D-LOC-01, D-MIS-01 | `test_d_loc_01.py`, `test_d_mis_01.py` | 2 | `test(red): add D-LOC-01, D-MIS-01 skeleton RED` |
| RED-7 | D-SOL-01~04 | `test_d_sol_01_04.py` | 4 | `test(red): add D-SOL-01~04 skeleton RED` |
| RED-8 | D-VAL-01~06 | `test_d_val_01_06.py` | 6 | `test(red): add D-VAL-01~06 skeleton RED` |

---

## GREEN 처리 순서 (Test ID 오름차순)

FR-01 검증 순서(`null → size → blank → range → duplicate`)와 Test ID 오름차순이 일치합니다.

### Track A — Boundary / Input (U-IN-*)

| # | Test ID | 테스트 함수 | GREEN 구현 포인트 |
|---|---------|-------------|-------------------|
| 1 | U-IN-01 | `test_validate_returns_e003_when_matrix_is_null` | `InputValidator`: null 1순위 → `E003` |
| 2 | U-IN-02 | `test_validate_returns_e001_when_size_not_4x4` (×4) | 4×4 형상 검증 → `E001` |
| 3 | U-IN-03a | `test_validate_returns_e002_when_zero_blank_count_is_0` | blank count == 2 → `E002` |
| 4 | U-IN-03b | `test_validate_returns_e002_when_zero_blank_count_is_3` | 동일 |
| 5 | U-IN-04 | `test_u_in_04_g1_cell_out_of_range_returns_e004` | 값 범위 `0 or 1..16` → `E004` |
| 6 | U-IN-05 | `test_u_in_05_g1_duplicate_sixteen_returns_e005` | non-zero 중복 → `E005` |
| 7 | U-IN-06 | `test_u_in_06_valid_g1_returns_ok_true` | G1 통과 → `ok=true` |
| 8 | U-IN-07 | `test_u_in_07_null_short_circuits_before_blank_count` | null → E003 short-circuit |
| 9 | U-IN-08 | `test_u_in_08_size_fail_short_circuits_before_blank_count` | size fail → E001 short-circuit |

### Track A — Boundary / Output & Flow

| # | Test ID | 선행 GREEN |
|---|---------|------------|
| 10 | U-FLOW-02 (null) | U-IN-01 + `UIBoundary` |
| 11 | U-FLOW-02 ext (size) | U-IN-02 |
| 12 | U-FLOW-02 ext (blank) | U-IN-03 |
| 13 | U-OUT-01 | D-SOL-01 + UIBoundary |
| 14 | U-OUT-02 | D-SOL-04 |
| 15 | U-OUT-03 | D-SOL-01 |

### Track B — Domain / Logic (D-*)

| # | Test ID | Given → Then |
|---|---------|--------------|
| 16 | D-LOC-01 | G1 → `[(2,2),(3,3)]` row-major |
| 17 | D-MIS-01 | G1 → `[7, 10]` 오름차순 |
| 18 | D-SOL-01 | G1 → `[2,2,7,3,3,10]` |
| 19 | D-SOL-02 | G2 PLACEHOLDER → Step B 성공 |
| 20 | D-SOL-03 | G3 PLACEHOLDER → `UnsolvableDomainError` |
| 21 | D-SOL-04 | G1 → len=6, coords ∈ [1,4] |
| 22 | D-VAL-01 | G0 → `True` |
| 23 | D-VAL-02~06 | 행·열·대각·중복·0 위반 → `False` |

> Test ID 문자열 기준으로는 D-SOL이 D-VAL보다 앞이지만, **구현 의존성**상 D-LOC → D-MIS → D-VAL → D-SOL 순이 자연스럽습니다.

### GREEN 커밋 권장 묶음

| GREEN | Test ID | pytest 검증 |
|-------|---------|-------------|
| G-1 | U-IN-01 | `pytest tests/boundary/test_ac_fr_01_01_input_validation.py::TestUIn01NullMatrix -v` |
| G-2 | U-IN-02 | `pytest tests/boundary/test_ac_fr_01_01_input_validation.py::TestUIn02SizeNot4x4 -v` |
| G-3 | U-IN-03a/b | `pytest tests/boundary/test_ac_fr_01_01_input_validation.py::TestUIn03BlankCount -v` |
| G-4 | U-IN-04, U-IN-05 | `pytest tests/boundary/test_u_in_04_05.py -v` |
| G-5 | U-IN-06 | `pytest tests/boundary/test_u_in_06_08.py::TestUIn06ValidationSuccess -v` |
| G-6 | U-IN-07, U-IN-08 | `pytest tests/boundary/test_u_in_06_08.py -k "07 or 08" -v` |
| G-7 | D-LOC-01, D-MIS-01 | `pytest tests/entity/test_d_loc_01.py tests/entity/test_d_mis_01.py -v` |
| G-8 | D-VAL-01~06 | `pytest tests/entity/test_d_val_01_06.py -v` |
| G-9 | D-SOL-01, D-SOL-04 | `pytest tests/entity/test_d_sol_01_04.py -k "01 or 04" -v` |
| G-10 | D-SOL-02, D-SOL-03 | G2/G3 격자 확정 후 |
| G-11 | U-FLOW-02 (×3) | `pytest tests/boundary/test_u_flow_02.py -v` |
| G-12 | U-OUT-01~03 | `pytest tests/boundary/test_u_out_01_03.py -v` |

---

## GREEN 시작 전 필수 결정 — Code Drift

Legacy GREEN과 Full RED 사이에 **에러 코드 불일치**가 있습니다.

| 경로 | null 처리 | size 실패 |
|------|-----------|-----------|
| Legacy (`BoundaryValidator`) | `INVALID_SIZE` | `INVALID_SIZE` |
| Dual-Track RED (`InputValidator`) | `E003` | `E001` |

U-IN-01 GREEN 전에 아래 중 하나를 선택해야 legacy 34건과 충돌하지 않습니다.

1. **`InputValidator`를 E00x SSOT로 통일**하고 legacy 테스트도 E001/E003로 마이그레이션
2. **Legacy `BoundaryValidator`는 유지**, `InputValidator`만 Dual-Track E00x 사용 (두 API 공존)
3. **U-IN-01~03 테스트를 `INVALID_SIZE` 계약으로 수정** (Dual-Track RED 설계와 불일치)

---

## FR-01 Failure Envelope (Dual-Track SSOT)

```text
{ "ok": false, "error": { "code": "E00x", "message": "<exact>" } }
```

| Code | Message (exact) |
|------|-----------------|
| E003 | `Input matrix must not be null.` |
| E001 | `Grid must be 4x4.` |
| E002 | `Exactly two blank cells (value 0) are required.` |
| E004 | `Each cell must be 0 or an integer from 1 to 16.` |
| E005 | `Non-zero cell values must not be duplicated.` |

검증 short-circuit 순서: **null → size → blank count → value range → duplicate**

---

## Given 격자 (G0~G3)

| ID | 격자 | 설명 |
|----|------|------|
| G0 | `[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]` | 완전·유효 마방진 (M=34) |
| G1 | `[[16,3,2,13],[5,0,11,8],[9,6,0,12],[4,15,14,1]]` | 빈칸 (2,2),(3,3); 누락 {7, 10} |
| G2 | PLACEHOLDER | Step A 실패 · Step B 성공 |
| G3 | PLACEHOLDER | Step A·B 모두 실패 |

---

## 왜 이 프로젝트인가 (요약)

| 단계 | 핵심 질문 | 결론 요약 |
|------|-----------|-----------|
| **관찰** | 무엇이 일어나고 있는가? | 1~16을 4×4에 배치하고, 여러 방향의 합이 일치하는지 확인·탐색하는 상황 |
| **Why #1** | 왜 “완성”이 요구되는가? | 외부 판정(과제·채점)의 종료 상태 — 기준 없으면 이분법·모호성 발생 |
| **Why #2** | 왜 프로그램인가? | 반복·전수 검증·규칙 명시 — 손계산만으로는 재현·통제가 어려움 |
| **Why #3** | 왜 TDD 관점인가? | 유효 배치 **계약**·**불변**·**입출력 경계**를 테스트로 먼저 고정 |
| **진짜 문제** | 무엇을 풀어야 하는가? | 유효 배치 규칙 + 판정(·도출) + 단일 기준 |

상세 분석은 [Report/MagicSquare-ProblemDefinition-Report.md](./Report/MagicSquare-ProblemDefinition-Report.md)를 참고하세요.

---

## 핵심 불변 조건 (Invariant)

유효한 **완전 배치**는 아래를 **동시에** 만족해야 합니다.

| 구분 | ID | 내용 |
|------|-----|------|
| 구조 | G1, G2 | 4×4, 16칸 모두 채움 |
| 값 | V1, V2, V3 | 1~16 정수, 서로 다름, 집합 {1,…,16} |
| 합 | S1, S2, S3 | S = 34, 각 행·각 열의 합 = S |
| 합 (선택) | S4 | (확정 시) 대각 합 = S |
| 책임 | C1, C3 | 판정은 일관·무변경; 부분 만족 ≠ 유효 |

---

## 폴더 구조

```
MagicSquare/
├── README.md
├── src/                          ← ECB 구현
│   ├── boundary/                 ← 입력 검증, 응답 포맷 (FR-01)
│   ├── control/                  ← Use-case 오케스트레이션
│   └── entity/                   ← 도메인 모델·순수 로직
├── tests/
│   ├── boundary/                 ← Track A (U-IN, U-OUT, U-FLOW)
│   ├── control/                  ← Control 격리 테스트
│   └── entity/                   ← Track B (D-LOC, D-MIS, D-VAL, D-SOL)
├── Report/                       ← 분석·TDD 실행 보고서
├── Prompt/                       ← 대화형 프롬프트·트랜스크립트
├── .cursor/rules/                ← ECB, TDD, 코드 스타일 규칙
└── defect_list.md                ← TDD 결함 목록
```

---

## 문서 가이드

### Report — 분석·TDD 실행

| 문서 | 설명 |
|------|------|
| [Report/README.md](./Report/README.md) | Report 폴더 안내 |
| [MagicSquare-ProblemDefinition-Report.md](./Report/MagicSquare-ProblemDefinition-Report.md) | STEP 1~5 통합 보고서 |
| [MagicSquare-DualTrack-RED-Design-Report.md](./Report/MagicSquare-DualTrack-RED-Design-Report.md) | FR-01~FR-05 Dual-Track RED 설계표 |
| [MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md](./Report/MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md) | RED Skeleton 23건 실행 보고서 |
| [MagicSquare-AC-FR-01-01-TDD-Execution-Report.md](./Report/MagicSquare-AC-FR-01-01-TDD-Execution-Report.md) | AC-FR-01-01 RED→GREEN 실행 보고서 |
| [MagicSquare-Stabilize-Green-InputValidation-Execution-Report.md](./Report/MagicSquare-Stabilize-Green-InputValidation-Execution-Report.md) | InputValidator GREEN 실행 보고서 |
| [MagicSquare-Green-Roadmap-RED-Commit-Execution-Report.md](./Report/MagicSquare-Green-Roadmap-RED-Commit-Execution-Report.md) | GREEN 로드맵 · RED 커밋 묶음 · README 갱신 실행 보고서 |

### Prompt — 세션 재현·기록

| 문서 | 설명 |
|------|------|
| [Prompt/README.md](./Prompt/README.md) | Prompt 폴더 안내 |
| [Prompt/transcript.md](./Prompt/transcript.md) | User / Assistant 턴별 대화 기록 |

---

## 표면 정의 vs 진짜 정의

| | 표면 (잘못된 정의) | 진짜 (개선된 정의) |
|---|-------------------|-------------------|
| **초점** | 4×4 마방진 프로그램, 합 같게 출력 | 유효 배치 규칙 + 판정·(선택) 도출 |
| **성공** | 뭔가 출력됨 | 무효 거부, 유효 일관 수용 |
| **훈련** | 구현 | 규칙 명시·계약·불변·재현·문제 재정의 |

---

## RED / GREEN 체크리스트

### Track A — Boundary (U-IN)

- [x] U-IN-01~03 Full RED (`test_ac_fr_01_01_input_validation.py`, 7건)
- [x] U-IN-04~05 Skeleton RED
- [x] U-IN-06~08 Skeleton RED
- [x] U-OUT-01~03 Skeleton RED
- [x] U-FLOW-02 Skeleton RED (+ext×2)
- [ ] U-IN-01 GREEN (`E003`)
- [ ] U-IN-02 GREEN (`E001`)
- [ ] U-IN-03 GREEN (`E002`)
- [ ] U-IN-04~05 GREEN (`E004`, `E005`)
- [ ] U-IN-06~08 GREEN (성공 경로 · short-circuit)
- [ ] U-OUT-01~03 GREEN
- [ ] U-FLOW-02 GREEN

### Track B — Domain (D-*)

- [x] D-LOC-01, D-MIS-01 Skeleton RED
- [x] D-VAL-01~06 Skeleton RED
- [x] D-SOL-01~04 Skeleton RED
- [ ] D-LOC-01 GREEN
- [ ] D-MIS-01 GREEN
- [ ] D-VAL-01~06 GREEN
- [ ] D-SOL-01, D-SOL-04 GREEN
- [ ] D-SOL-02, D-SOL-03 GREEN (G2/G3 확정 후)

### Legacy GREEN (유지)

- [x] AC-FR-01-01 Boundary (`test_boundary_validator_size.py`, 18건)
- [x] AC-FR-01-01 Control 격리 (`test_resolve_use_case_size_guard.py`, 16건)

### 커버리지 · 결함

- [ ] 전체 커버리지 80%+
- [x] `defect_list.md` 생성
- [x] AC-FR-01-01 결함 수정 후 legacy 회귀 테스트 통과

---

## 권장 다음 단계

1. **E001/E003 vs `INVALID_SIZE`** code 통일 결정
2. Skeleton RED import 경로 정렬 (`src.boundary.*`)
3. **G-1 ~ G-3**: U-IN-01~03 GREEN (`InputValidator`)
4. **G-4 ~ G-6**: U-IN-04~08 GREEN
5. G2/G3 격자 확정 후 Track B GREEN (D-LOC → D-MIS → D-VAL → D-SOL)
6. U-FLOW-02 · U-OUT-01~03 GREEN

---

## 라이선스·기여

(미정 — 필요 시 추가)

---

*Last updated: 2026-05-29*
