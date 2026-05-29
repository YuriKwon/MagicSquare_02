# MagicSquare — Dual-Track RED 설계 보고서 (FR-01~FR-05)

| 항목 | 내용 |
|------|------|
| 프로젝트 | `DEV\MagicSquare` |
| 문서 유형 | Dual-Track TDD **RED 단계** 테스트 설계표 (코드 없음) |
| TDD Phase | **RED** (설계만; GREEN/REFACTOR 미진입) |
| 범위 | Track A (Boundary/UI) + Track B (Domain/Logic) |
| Traceability | FR-01~FR-05, AC-FR-01-*, U-IN/OUT/FLOW-*, D-LOC/MIS/VAL/SOL-* |
| 작성일 | 2026-05-29 |
| 관련 Transcript | [../Prompt/transcript-dualtrack-red-design-latest.md](../Prompt/transcript-dualtrack-red-design-latest.md) |

---

## 1) 작업 개요

본 세션은 **구현·테스트 코드·pytest 실행 없이** Dual-Track UI + Logic TDD의 RED 테스트 설계표만 산출했다.

| 순서 | 요청 | 산출물 |
|------|------|--------|
| 1 | FR-01~FR-05 전체 Dual-Track RED 설계표 작성 | 본 보고서 §3~§4 |
| 2 | Report·Prompt Export | 본 보고서, `Prompt/transcript-dualtrack-red-design-latest.md` |

### 금지 준수 확인

- 구현 코드·테스트 코드·스켈레톤 코드: **미작성**
- 클래스/파일 구조 확정: **미수행**
- GREEN / REFACTOR: **미진입**
- pytest 실행: **미실행**

---

## 2) SSOT 및 격자 상수

### 2.1 SSOT 참조 상태

| 문서 | 워크스페이스 | 비고 |
|------|-------------|------|
| `docs/PRD_MagicSquare.md` v0.2 | ❌ 미존재 | 요청 계약·Level1~5 Report로 대체 |
| `Report/02.MagicSquare_DualTrack_TDD_Design_Report.md` | ❌ 미존재 | G2/G3 **PLACEHOLDER** |
| `.cursorrules` | ✅ | ECB, Dual-Track, RED→GREEN→REFACTOR |
| `Report/MagicSquare-Level1to5-Verification-Report.md` | ✅ | 입출력·M=34 규칙 확인 |

### 2.2 프로젝트 계약 (요약)

| 항목 | 계약 |
|------|------|
| 입력 | 4×4 `int[][]`, `0`=빈칸(정확히 2개), 값 `0` 또는 `1..16`, non-zero 중복 금지 |
| 출력 | `int[6]` = `[r1,c1,n1,r2,c2,n2]`, 좌표 **1-index** |
| 마방진 상수 | 4×4 → **M = 34** (`MagicConstant` SSOT) |
| 검증 순서 (short-circuit) | null → size → empty count → value range → duplicate |
| Boundary invalid | Failure envelope (Python 예외 아님); E003/E001/E002/E004/E005 |
| U-FLOW-02 | invalid 시 `SolvePartialMagicSquare.execute` **0회** |

### 2.3 Given 격자 (G0~G3)

| ID | 격자 | 설명 |
|----|------|------|
| **G0** | `[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]` | 완전·유효 마방진 (M=34) |
| **G1** | `[[16,3,2,13],[5,0,11,8],[9,6,0,12],[4,15,14,1]]` | 빈칸 (2,2),(3,3); 누락 {7,10} |
| **G2** | **PLACEHOLDER** | Report/02 부록 확정 후 고정 — Step A 실패·Step B 성공 |
| **G3** | **PLACEHOLDER** | Report/02 부록 확정 후 고정 — Step A·B 모두 실패 |

### 2.4 Failure envelope (Boundary)

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

> **주의:** AC-FR-01-01 GREEN 구현은 `INVALID_SIZE`를 사용 중. 본 RED 설계는 **E001** SSOT 기준이며, GREEN 시 code 통일 리팩터가 필요할 수 있음.

---

## 3) Track A — UI / Boundary RED Tests

| Test ID | Layer | 테스트 이름 | Given | When | Then | Expected RED Failure | 실패 이유 | Boundary 계약 | Invariant/AC |
|---------|-------|-------------|-------|------|------|----------------------|-----------|-----------------|--------------|
| U-IN-01 | Boundary | `test_validate_returns_e003_when_matrix_is_null` | `matrix = null` | `InputValidator.validate(matrix)` | `ok=false`, `error.code="E003"`, `error.message="Input matrix must not be null."` | `AttributeError` / `AssertionError` | null·E003 미구현 | FR-01 null 1순위 | AC-FR-01-05 |
| U-IN-02 | Boundary | `test_validate_returns_e001_when_size_not_4x4` | A:`[]` B:3×4 C:4×3 D:5×5 | `InputValidator.validate(matrix)` | `E001`, message exact | `AssertionError` (`INVALID_SIZE` drift) | size 검증·E001 | FR-01 형상 | AC-FR-01-01 |
| U-IN-03a | Boundary | `test_validate_returns_e002_when_zero_blank_count_is_0` | G0 (빈칸 0) | `InputValidator.validate(matrix)` | `E002`, message exact | `AssertionError` / `AttributeError` | 빈칸≠2 | FR-01 | AC-FR-01-02 |
| U-IN-03b | Boundary | `test_validate_returns_e002_when_zero_blank_count_is_3` | G1+(1,1)=0 → 0 세 개 | `InputValidator.validate(matrix)` | `E002`, message exact | 동 U-IN-03a | 3빈칸 거부 | FR-01 | AC-FR-01-02 |
| U-IN-04 | Boundary | `test_validate_returns_e004_when_value_out_of_range` | G1+(4,4)=-1 등 | `InputValidator.validate(matrix)` | `E004`, message exact | `AssertionError` | 범위 검증 없음 | FR-01 | AC-FR-01-03 |
| U-IN-05 | Boundary | `test_validate_returns_e005_when_nonzero_duplicate` | G1+(4,4)=16 (16 중복) | `InputValidator.validate(matrix)` | `E005`, message exact | `AssertionError` | 중복 검증 없음 | FR-01 | AC-FR-01-04 |
| U-OUT-01 | Boundary | `test_solve_success_payload_length_is_six` | G1 (+ stub 가능) | `UIBoundary.solve(matrix)` | `ok=true`, `len(result)==6` | `AssertionError` / `AttributeError` | 출력 길이 6 | FR-05 | AC-FR-05, I8 |
| U-OUT-02 | Boundary | `test_solve_success_coordinates_are_1_indexed_in_1_to_4` | G1, `[2,2,7,3,3,10]` | `UIBoundary.solve(matrix)` | r,c ∈ [1,4] | `AssertionError` | 1-index 계약 | FR-05 | AC-FR-05, I8 |
| U-FLOW-02 | Boundary | `test_solve_does_not_call_execute_when_validation_fails` | `matrix=null`, spy on `execute` | `UIBoundary.solve(matrix)` | E003; `execute.call_count==0` | `AssertionError` (call≥1) | Domain 격리 | U-FLOW-02 | AC-FR-01-* |

---

## 4) Track B — Domain / Logic RED Tests

**Domain Mock 금지:** Entity/Control 대상 함수에 mock/spy 대체 호출 금지. Given은 G0/G1/(확정 후)G2/G3 실데이터만.

| Test ID | Layer | 테스트 이름 | Given | When | Then | Expected RED Failure | Logic Invariant | 필요성 |
|---------|-------|-------------|-------|------|------|----------------------|-----------------|--------|
| D-LOC-01 | Entity | `test_find_blank_coords_row_major_on_g1` | G1 | `find_blank_coords(matrix)` | `[(2,2),(3,3)]` 1-index | `ModuleNotFoundError` | I6 | 빈칸·순서 SSOT |
| D-MIS-01 | Entity | `test_find_not_exist_nums_on_g1_sorted_ascending` | G1 | `find_not_exist_nums(matrix)` | `[7,10]` | `ModuleNotFoundError` | I7, I11 | 누락·정렬 |
| D-VAL-01 | Entity | `test_is_magic_square_true_on_g0` | G0 | `is_magic_square(matrix)` | `True` | `ModuleNotFoundError` | I1~I5 | baseline |
| D-VAL-02 | Entity | `test_is_magic_square_false_when_row_sum_mismatch` | G0 행합 깨기 | `is_magic_square(matrix)` | `False` | `AssertionError` | I1 | 행 합 분리 |
| D-VAL-03 | Entity | `test_is_magic_square_false_when_col_sum_mismatch` | G0 열합 깨기 | `is_magic_square(matrix)` | `False` | `AssertionError` | I2 | 열 합 분리 |
| D-VAL-04 | Entity | `test_is_magic_square_false_when_diagonal_sum_mismatch` | G0 대각 깨기 | `is_magic_square(matrix)` | `False` | `AssertionError` | I3 | 대각 분리 |
| D-VAL-05 | Entity | `test_is_magic_square_false_when_duplicate_or_out_of_1_to_16` | G0 중복 | `is_magic_square(matrix)` | `False` | `AssertionError` | I4, I5 | 값 집합 |
| D-VAL-06 | Entity | `test_is_magic_square_false_when_zero_in_filled_grid` | G0+0 포함 | `is_magic_square(matrix)` | `False` | `AssertionError` | I4 | 0 불가 |
| D-SOL-01 | Control | `test_solution_step_a_success_on_g1_returns_six_tuple` | G1 | `solution(matrix)` | `[2,2,7,3,3,10]` | `ModuleNotFoundError` | I8 | Step A happy |
| D-SOL-02 | Control | `test_solution_step_b_success_after_step_a_fails_on_g2` | G2 PLACEHOLDER | `solution(matrix)` | Step B `int[6]` | `ModuleNotFoundError` | I9 | 역순 성공 |
| D-SOL-03 | Control | `test_solution_raises_unsolvable_when_both_steps_fail_on_g3` | G3 PLACEHOLDER | `solution(matrix)` | `UnsolvableDomainError` | `Failed: DID NOT RAISE` | I10 | 해 없음 |
| D-SOL-04 | Control | `test_solution_success_tuple_enforces_length_and_1_index_coords` | G1 | `solution(matrix)` | len=6, coords ∈ [1,4] | `AssertionError` | I8 | 형식 계약 |

---

## 5) Invariant ↔ Test ID 매핑

| Invariant | 요약 | Test ID |
|-----------|------|---------|
| I1~I3 | 행·열·대각 = M(34) | D-VAL-01~04 |
| I4~I5 | 완전 시 1~16, 0 없음 | D-VAL-05~06 |
| I6 | 빈칸 2·좌표 | D-LOC-01, U-IN-03* |
| I7, I11 | 누락 2·오름차순 | D-MIS-01 |
| I8~I10 | Step A/B/Unsolvable | D-SOL-01~03 |
| I8 | 출력 6·1-index | D-SOL-04, U-OUT-* |

---

## 6) RED 설계 자체 검수

- [x] Boundary는 E00x Failure schema (generic Exception 아님)
- [x] invalid → `execute` 0회 (U-FLOW-02)
- [x] U-IN vs U-OUT 분리
- [x] Logic Track Domain Mock 없음
- [x] I1~I11·AC-FR* 추적 가능
- [x] 코드/스켈레톤/구현 미작성

---

## 7) 권장 다음 단계

1. **Report/02** 또는 PRD v0.2 확보 → G2/G3 PLACEHOLDER 격자 상수 고정
2. **E001** vs `INVALID_SIZE` code 통일 결정 후 AC-FR-01-01 회귀 영향 분석
3. Track A: U-IN-01~05 RED 테스트 작성 (pytest, 실패 확인)
4. Track B: D-LOC-01 → D-MIS-01 → D-VAL-* → D-SOL-* 순 RED
5. U-FLOW-02 Control spy 테스트를 Boundary 통합 경로에 연결

---

## 8) 산출물 목록

| 경로 | 설명 |
|------|------|
| `Report/MagicSquare-DualTrack-RED-Design-Report.md` | 본 보고서 |
| `Prompt/transcript-dualtrack-red-design-latest.md` | 세션 Transcript |

---

*End of Report*
