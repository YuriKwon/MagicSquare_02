# MagicSquare 실행 보고서 — GREEN 로드맵 · RED 커밋 묶음 · README 갱신

| 항목 | 내용 |
|------|------|
| 프로젝트 | `DEV\MagicSquare` |
| 브랜치 | `stabilize/green` |
| 문서 유형 | TDD GREEN 로드맵·RED 커밋 전략·문서 갱신 실행 보고서 |
| 기준 FR | **FR-01** Input Verification (Boundary) |
| Traceability | U-IN-01~08, U-OUT-01~03, U-FLOW-02, D-LOC/MIS/VAL/SOL-*, AC-FR-01-* |
| 작성일 | 2026-05-29 |
| 관련 Transcript | [../Prompt/transcript-green-roadmap-red-commit-latest.md](../Prompt/transcript-green-roadmap-red-commit-latest.md) |

---

## 1) 작업 개요

본 세션은 TDD **GREEN 단계 진입 전** RED 테스트를 **몇 개씩 묶어 커밋**할 수 있도록 Test ID 오름차순 기준으로 RED/GREEN 로드맵을 정리하고, `README.md`에 반영한 뒤 Report·Transcript를 Export했다.

| 순서 | 요청 | 산출물 |
|------|------|--------|
| 1 | GREEN 처리 TC를 Test ID 오름차순으로 정리, RED 커밋 묶음 제안 | RED-1~RED-8, G-1~G-12 로드맵 |
| 2 | 위 내용을 `README.md`에 반영 | 프로젝트 README 전면 갱신 |
| 3 | Report·Transcript Export | 본 보고서, `Prompt/transcript-green-roadmap-red-commit-latest.md` |

### 금지 준수 확인

- GREEN 구현 코드 추가: **미수행** (로드맵·문서만)
- 테스트 코드 수정: **미수행**
- `src/` 변경: **미수행**

---

## 2) 세션 전 테스트 현황 (pytest 검증)

```powershell
python -m pytest tests/boundary/test_ac_fr_01_01_input_validation.py `
  tests/boundary/test_boundary_validator_size.py `
  tests/control/test_resolve_use_case_size_guard.py -v
```

| 스위트 | passed | failed | 비고 |
|--------|--------|--------|------|
| `test_boundary_validator_size.py` | 18 | 0 | Legacy GREEN (`INVALID_SIZE`) |
| `test_resolve_use_case_size_guard.py` | 16 | 0 | Legacy GREEN (Control 격리) |
| `test_ac_fr_01_01_input_validation.py` | 0 | 7 | Full RED (U-IN-01~03, E00x) |
| **합계** | **34** | **7** | |

Skeleton RED 23건 (`test_u_in_04_05.py` 등 8파일)은 `ModuleNotFoundError: boundary.input_validator`로 **collection ERROR** — 전체 `tests/` 스위트 실행 시 8 errors.

---

## 3) RED 커밋 권장 묶음 (Test ID 오름차순)

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

**합계:** Full RED 7 + Skeleton 23 = **30건** (Legacy GREEN 34건은 기존 커밋 가정)

---

## 4) GREEN 처리 순서 (Test ID 오름차순)

FR-01 검증 short-circuit: **null → size → blank count → value range → duplicate**

### 4.1 Track A — Boundary / Input (U-IN-*)

| # | Test ID | 테스트 함수 | 파일 | GREEN 구현 포인트 |
|---|---------|-------------|------|-------------------|
| 1 | U-IN-01 | `test_validate_returns_e003_when_matrix_is_null` | `test_ac_fr_01_01_input_validation.py` | null 1순위 → `E003` |
| 2 | U-IN-02 | `test_validate_returns_e001_when_size_not_4x4` (×4) | 동일 | 4×4 형상 → `E001` |
| 3 | U-IN-03a | `test_validate_returns_e002_when_zero_blank_count_is_0` | 동일 | blank count == 2 → `E002` |
| 4 | U-IN-03b | `test_validate_returns_e002_when_zero_blank_count_is_3` | 동일 | 동일 |
| 5 | U-IN-04 | `test_u_in_04_g1_cell_out_of_range_returns_e004` | `test_u_in_04_05.py` | 값 범위 → `E004` |
| 6 | U-IN-05 | `test_u_in_05_g1_duplicate_sixteen_returns_e005` | `test_u_in_04_05.py` | non-zero 중복 → `E005` |
| 7 | U-IN-06 | `test_u_in_06_valid_g1_returns_ok_true` | `test_u_in_06_08.py` | G1 통과 → `ok=true` |
| 8 | U-IN-07 | `test_u_in_07_null_short_circuits_before_blank_count` | `test_u_in_06_08.py` | null → E003 short-circuit |
| 9 | U-IN-08 | `test_u_in_08_size_fail_short_circuits_before_blank_count` | `test_u_in_06_08.py` | size fail → E001 short-circuit |

### 4.2 Track A — Boundary / Output & Flow

| # | Test ID | 선행 GREEN |
|---|---------|------------|
| 10 | U-FLOW-02 (null) | U-IN-01 + `UIBoundary` |
| 11 | U-FLOW-02 ext (size) | U-IN-02 |
| 12 | U-FLOW-02 ext (blank) | U-IN-03 |
| 13 | U-OUT-01 | D-SOL-01 + UIBoundary |
| 14 | U-OUT-02 | D-SOL-04 |
| 15 | U-OUT-03 | D-SOL-01 |

### 4.3 Track B — Domain / Logic (D-*)

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

> Test ID 문자열 오름차순: D-SOL이 D-VAL보다 앞. **구현 의존성**상 D-LOC → D-MIS → D-VAL → D-SOL 순 권장.

### 4.4 GREEN 커밋 권장 묶음

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
| G-10 | D-SOL-02, D-SOL-03 | G2/G3 확정 후 |
| G-11 | U-FLOW-02 (×3) | `pytest tests/boundary/test_u_flow_02.py -v` |
| G-12 | U-OUT-01~03 | `pytest tests/boundary/test_u_out_01_03.py -v` |

---

## 5) GREEN 시작 전 필수 결정 — Code Drift

| 경로 | null 처리 | size 실패 |
|------|-----------|-----------|
| Legacy (`BoundaryValidator`) | `INVALID_SIZE` | `INVALID_SIZE` |
| Dual-Track RED (`InputValidator`) | `E003` | `E001` |

U-IN-01 GREEN 전 선택 필요:

1. **`InputValidator`를 E00x SSOT로 통일** + legacy 테스트 마이그레이션
2. **Legacy `BoundaryValidator` 유지** + `InputValidator`만 E00x (두 API 공존)
3. **U-IN-01~03을 `INVALID_SIZE` 계약으로 수정** (Dual-Track RED 설계와 불일치)

현재 `InputValidator.validate()`는 `None` → `FailureResponse(INVALID_SIZE)` 부분 GREEN 상태이며, U-IN-01은 `ValidationEnvelope` + `E003`을 기대 → **7건 전부 FAIL**.

---

## 6) README.md 갱신 요약

`README.md`를 TDD 진행 현황 문서로 전면 갱신했다.

| 섹션 | 변경 내용 |
|------|-----------|
| 현재 상태 | ECB·Dual-Track TDD·테스트 PASS/FAIL/ERROR 현황 |
| TDD 진행 현황 | Legacy / Full RED / Skeleton RED 표 |
| RED 커밋 권장 묶음 | RED-1~RED-8 |
| GREEN 처리 순서 | U-IN → U-FLOW/U-OUT → D-* + G-1~G-12 |
| Code Drift | E00x vs `INVALID_SIZE` 결정 항목 |
| FR-01 Failure Envelope | E003~E005 메시지 SSOT |
| 폴더 구조 | `src/`, `tests/` 실제 구조 |
| 체크리스트 | TC-A/B → U-IN/D-* RED/GREEN 체크리스트 |

---

## 7) 산출물 목록

| 경로 | 설명 |
|------|------|
| `README.md` | GREEN 로드맵·RED 커밋·체크리스트 반영 |
| `Report/MagicSquare-Green-Roadmap-RED-Commit-Execution-Report.md` | 본 보고서 |
| `Prompt/transcript-green-roadmap-red-commit-latest.md` | 세션 Transcript |

---

## 8) 권장 다음 단계

1. **E001/E003 vs `INVALID_SIZE`** code 통일 결정
2. RED-1~RED-8 순서로 RED 커밋 (미커밋 파일 정리)
3. Skeleton import 경로 정렬 (`boundary.*` → `src.boundary.*`)
4. **G-1(U-IN-01)** GREEN 구현 시작
5. G2/G3 격자 확정 후 D-SOL-02/03 GREEN

---

## 9) 회귀 테스트 명령

```powershell
cd c:\Users\usejen_id\Downloads\CursorAI-main\DEV\MagicSquare
python -m pytest tests/boundary/test_boundary_validator_size.py tests/control/test_resolve_use_case_size_guard.py -v
```

---

*End of Report*
