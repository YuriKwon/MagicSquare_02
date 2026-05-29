# MagicSquare 실행 보고서 — Dual-Track RED Skeleton (Track A/B)

| 항목 | 내용 |
|------|------|
| 프로젝트 | `DEV\MagicSquare` |
| 문서 유형 | TDD **RED (Skeleton)** 실행·검증 보고서 |
| TDD Phase | **RED (Skeleton)** — GREEN / REFACTOR 미진입 |
| 범위 | Track A (U-IN-04~08, U-OUT-01~03, U-FLOW-02 확장) + Track B (D-LOC/MIS/VAL/SOL) |
| Traceability | FR-01~FR-05, U-IN/OUT/FLOW-*, D-LOC/MIS/VAL/SOL-*, I1~I11 |
| 작성일 | 2026-05-29 |
| 관련 Transcript | [../Prompt/transcript-dualtrack-red-skeleton-latest.md](../Prompt/transcript-dualtrack-red-skeleton-latest.md) |

---

## 1) 작업 개요

본 세션은 Dual-Track UI + Logic TDD의 **RED Skeleton** 단계를 수행했다. Report/09 설계표(요청 SSOT) 기준으로 **아직 pytest가 없던 Test ID**에 대해 스켈레톤만 작성하고, `src/` 운영 코드는 추가하지 않았다.

| 순서 | 요청 | 산출물 |
|------|------|--------|
| 1 | SSOT·기존 테스트 구조 확인 | Report/09 미존재 → `MagicSquare-DualTrack-RED-Design-Report.md` 대체 참조 |
| 2 | Track A/B RED Skeleton 작성 | `tests/boundary/test_u_*.py` 4파일, `tests/entity/test_d_*.py` 4파일 |
| 3 | G0~G3 fixture placeholder | `tests/conftest.py`, `tests/entity/conftest.py` 주석 |
| 4 | pytest 실행·RED 확인 | 8 collection ERROR (신규), legacy 22건은 동일 스위트 내 미실행 |
| 5 | Report·Transcript Export | 본 보고서, `Prompt/transcript-dualtrack-red-skeleton-latest.md` |

### 금지 준수 확인

| 금지 항목 | 준수 |
|-----------|------|
| `src/` 운영 코드·stub 작성 | ✅ 변경 없음 |
| GREEN / REFACTOR 진입 | ✅ 미진입 |
| skip / xfail / assert 완화 | ✅ 미사용 |
| 실제 기대값 assert | ✅ `pytest.fail()`만 |
| Report/08 `test_ac_fr_01_01_*.py` 수정 | ✅ 해당 파일 없음; `test_boundary_validator_size.py` 미수정 |
| U-IN-01~03 중복 작성 | ✅ 미작성 |

---

## 2) SSOT 참조 상태

| 문서 | 워크스페이스 | 비고 |
|------|-------------|------|
| `Report/09.MagicSquare_DualTrack_RED_TestPlan_Design_Report.md` | ❌ 미존재 | `MagicSquare-DualTrack-RED-Design-Report.md` + 요청 범위로 대체 |
| `docs/PRD_MagicSquare.md` v0.2 | ❌ 미존재 | Level1~5 Report·DualTrack RED 설계 계약 사용 |
| `Report/02.MagicSquare_DualTrack_TDD_Design_Report.md` | ❌ 미존재 | G2/G3 **PLACEHOLDER** |
| `Report/08` (`test_ac_fr_01_01_*.py`) | ❌ 미존재 | AC-FR-01-01 GREEN은 `test_boundary_validator_size.py` (18건) |
| `.cursorrules` | ✅ | ECB, Dual-Track, pytest, AAA |
| `Report/MagicSquare-DualTrack-RED-Design-Report.md` | ✅ | U-IN-04~05, U-OUT-01~02, U-FLOW-02, D-* 설계표 |

### U-IN-06~08 · U-OUT-03 보완 정의 (Report/09 부재)

| Test ID | 설계 요약 | 근거 |
|---------|-----------|------|
| U-IN-06 | G1 valid → `ok=true` envelope | FR-01 통과 경로 |
| U-IN-07 | null → E003 short-circuit (blank count 미도달) | 검증 순서: null → size → … |
| U-IN-08 | size fail → E001 short-circuit | 검증 순서 |
| U-OUT-03 | G1 solve → `[2,2,7,3,3,10]` | FR-05, D-SOL-01과 동형 |

---

## 3) RED Skeleton 산출물

### 3.1 테스트 파일

| 파일 | Test ID | 테스트 수 | Track |
|------|---------|-----------|-------|
| `tests/boundary/test_u_in_04_05.py` | U-IN-04, U-IN-05 | 2 | A |
| `tests/boundary/test_u_in_06_08.py` | U-IN-06, U-IN-07, U-IN-08 | 3 | A |
| `tests/boundary/test_u_out_01_03.py` | U-OUT-01, U-OUT-02, U-OUT-03 | 3 | A |
| `tests/boundary/test_u_flow_02.py` | U-FLOW-02 (+2 확장) | 3 | A |
| `tests/entity/test_d_loc_01.py` | D-LOC-01 | 1 | B |
| `tests/entity/test_d_mis_01.py` | D-MIS-01 | 1 | B |
| `tests/entity/test_d_val_01_06.py` | D-VAL-01~06 | 6 | B |
| `tests/entity/test_d_sol_01_04.py` | D-SOL-01~04 | 4 | B |
| **합계** | | **23** | |

### 3.2 Skeleton 규칙 적용

- AAA 패턴; Given/When/Then은 **주석만**
- naming: `test_<test_id>_<scenario>`
- 본문: `pytest.fail("RED: <Test ID> — <한 줄 설계 요약>")` 단일 실패
- production import (Report/08 동일 스타일):
  - `from boundary.input_validator import InputValidator`
  - `from boundary.ui_boundary import UIBoundary`
  - `from entity.services.* import ...`
  - `from control.solution import solution`
- U-OUT/U-FLOW: Control mock/spy **주석 표시** (`SolvePartialMagicSquare.execute`)
- Track B: **Domain Mock 금지**

### 3.3 Fixture placeholder

| 위치 | 내용 |
|------|------|
| `tests/conftest.py` | G0~G3 격자 주석 추가 |
| `tests/entity/conftest.py` | G0~G3 격자 주석 (신규) |

```text
G0: [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
G1: [[16,3,2,13],[5,0,11,8],[9,6,0,12],[4,15,14,1]]
G2: PLACEHOLDER — Report/02 TBD
G3: PLACEHOLDER — Report/02 TBD
```

---

## 4) pytest 실행 결과

```bash
python -m pytest tests/boundary/ tests/entity/ -v
```

```text
collected 22 items / 8 errors
ERROR tests/boundary/test_u_flow_02.py
ERROR tests/boundary/test_u_in_04_05.py
ERROR tests/boundary/test_u_in_06_08.py
ERROR tests/boundary/test_u_out_01_03.py
ERROR tests/entity/test_d_loc_01.py
ERROR tests/entity/test_d_mis_01.py
ERROR tests/entity/test_d_sol_01_04.py
ERROR tests/entity/test_d_val_01_06.py
```

| 구분 | 결과 | 원인 |
|------|------|------|
| 신규 Skeleton 8파일 (23 tests) | **collection ERROR** | `ModuleNotFoundError: No module named 'boundary.input_validator'` 등 |
| Legacy `test_boundary_validator_size.py` (18) | 미실행 | collection error로 스위트 중단 |
| Legacy `test_user.py` (4) | 미실행 | 동일 |

**대표 ERROR:**

```text
tests/boundary/test_u_in_04_05.py:7: in <module>
    from boundary.input_validator import InputValidator
E   ModuleNotFoundError: No module named 'boundary.input_validator'
```

> 모듈 import 성공 후(GREEN 준비)에는 각 테스트가 `Failed: RED: <Test ID> — …` 로 전환될 것으로 예상.

---

## 5) Test ID ↔ 설계 매핑

| Test ID | 테스트 함수 | Layer | Expected RED |
|---------|-------------|-------|--------------|
| U-IN-04 | `test_u_in_04_g1_cell_out_of_range_returns_e004` | Boundary | ERROR → FAIL |
| U-IN-05 | `test_u_in_05_g1_duplicate_sixteen_returns_e005` | Boundary | ERROR → FAIL |
| U-IN-06 | `test_u_in_06_valid_g1_returns_ok_true` | Boundary | ERROR → FAIL |
| U-IN-07 | `test_u_in_07_null_short_circuits_before_blank_count` | Boundary | ERROR → FAIL |
| U-IN-08 | `test_u_in_08_size_fail_short_circuits_before_blank_count` | Boundary | ERROR → FAIL |
| U-OUT-01 | `test_u_out_01_solve_success_payload_length_is_six` | Boundary | ERROR → FAIL |
| U-OUT-02 | `test_u_out_02_solve_success_coordinates_are_1_indexed_in_1_to_4` | Boundary | ERROR → FAIL |
| U-OUT-03 | `test_u_out_03_solve_success_returns_expected_six_tuple_on_g1` | Boundary | ERROR → FAIL |
| U-FLOW-02 | `test_u_flow_02_null_matrix_execute_not_called` | Boundary | ERROR → FAIL |
| U-FLOW-02 ext | `test_u_flow_02_e001_size_invalid_execute_not_called` | Boundary | ERROR → FAIL |
| U-FLOW-02 ext | `test_u_flow_02_e002_blank_count_invalid_execute_not_called` | Boundary | ERROR → FAIL |
| D-LOC-01 | `test_d_loc_01_find_blank_coords_row_major_on_g1` | Entity | ERROR → FAIL |
| D-MIS-01 | `test_d_mis_01_find_not_exist_nums_on_g1_sorted_ascending` | Entity | ERROR → FAIL |
| D-VAL-01~06 | `test_d_val_0*` (6건) | Entity | ERROR → FAIL |
| D-SOL-01 | `test_d_sol_01_solution_step_a_success_on_g1_returns_six_tuple` | Control | ERROR → FAIL |
| D-SOL-02 | `test_d_sol_02_solution_step_b_success_after_step_a_fails_on_g2` | Control | `RED: D-SOL-02 — G2 TBD` |
| D-SOL-03 | `test_d_sol_03_solution_raises_unsolvable_when_both_steps_fail_on_g3` | Control | `RED: D-SOL-03 — G3 TBD` |
| D-SOL-04 | `test_d_sol_04_solution_success_tuple_enforces_length_and_1_index_coords` | Control | ERROR → FAIL |

---

## 6) 자체 검수

- [x] Skeleton만 작성; assert 기대값 없음
- [x] `src/` 미변경
- [x] U-IN-01~03 중복 없음
- [x] Track B Domain Mock 없음
- [x] D-SOL-02/03 G2/G3 TBD 표시
- [x] pytest 신규 23건 RED (collection ERROR)
- [ ] `tests/boundary/` + `tests/entity/` passed=0 — legacy GREEN 22건과 스위트 공존 시 collection error로 전체 중단

---

## 7) 권장 다음 단계

1. **Report/09·Report/02** 확보 → G2/G3 고정, U-IN-06~08·U-OUT-03 설계 SSOT 확정
2. **Report/08** `test_ac_fr_01_01_*.py` (U-IN-01~03 Full RED) 작성 또는 기존 AC-FR-01-01 스위트와 Test ID 정렬
3. **GREEN Track A:** `boundary.input_validator`, `boundary.ui_boundary` 최소 stub → `pytest.fail` FAIL 전환
4. **GREEN Track B:** `entity.services.*`, `control.solution` 최소 구현
5. **E001 vs INVALID_SIZE** code 통일 결정 (DualTrack RED 설계 vs AC-FR-01-01 GREEN)

---

## 8) 산출물 목록

| 경로 | 설명 |
|------|------|
| `Report/MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md` | 본 보고서 |
| `Prompt/transcript-dualtrack-red-skeleton-latest.md` | 세션 Transcript |
| `tests/boundary/test_u_*.py` | Track A Skeleton 4파일 |
| `tests/entity/test_d_*.py` | Track B Skeleton 4파일 |
| `tests/entity/conftest.py` | G0~G3 placeholder |

---

*End of Report*
