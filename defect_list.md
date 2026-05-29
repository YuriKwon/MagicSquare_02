# Magic Square 4×4 — Defect List

| 항목 | 내용 |
|------|------|
| 문서 유형 | 결함 추적 목록 (Defect Log) |
| 기준 AC | AC-FR-01-01 (FR-01 Input Verification — Boundary) |
| 관련 테스트 | `tests/boundary/test_boundary_validator_size.py`, `tests/control/test_resolve_use_case_size_guard.py` |
| 관련 계획 | [decs/test_plan.md](./decs/test_plan.md) |
| 최종 갱신 | 2026-05-29 |
| 회귀 상태 | **34 passed** (`pytest` AC-FR-01-01 스위트) |

---

## 결함 목록

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|----|----------|-------|-----------|--------|--------|-----------|-----------|
| DEF-001 | Critical | AC-FR-01-01 | `pytest tests/boundary/test_boundary_validator_size.py` 실행 | `BoundaryValidator` import 성공 후 `grid=None` → `code="INVALID_SIZE"` | `ModuleNotFoundError: No module named 'src.boundary'` (`test_boundary_validator_size.py:13`) | `src/boundary` 패키지 및 `BoundaryValidator` 미구현 | `src/boundary/validation_result.py`, `boundary_validator.py` 추가. `validate_size()`에 `grid is None` 및 4×4 형상 분기 구현 ✅ |
| DEF-002 | Critical | AC-FR-01-01 | `pytest tests/control/test_resolve_use_case_size_guard.py` 실행 | `grid=None` 시 `resolve()` 호출 0회, `INVALID_SIZE` 반환 | `ModuleNotFoundError: No module named 'src.control'` (`test_resolve_use_case_size_guard.py:12`) | `src/control` 패키지 및 `ResolveUseCase` 미구현 | `src/control/resolve_use_case.py` 추가. size 검증 실패 시 early-return, Domain `resolve()` 미호출 ✅ |
| DEF-003 | Minor | AC-FR-01-01 | GREEN 구현 후 동일 스위트 실행 | 범위 제한 메타 테스트 PASS | `AssertionError`: `assert 'AC-FR-01-02' not in source` 등 4건 — 금지 토큰이 테스트 docstring/함수명에 포함 | 소스 전체 문자열 스캔 방식 오류(자기 참조) | 자기 참조 메타 테스트 4건 제거. 행동 기반 범위 검증(`validate_size_only`, FR-02~03 미호출) 유지 ✅ |
| DEF-004 | Info | AC-FR-01-01 | (잠재) 유효 4×4 `grid`로 `BoundaryValidator.validate_size()` 호출 | 통과 시 `is_valid=True` 및 성공 code(또는 별도 pass 계약) | `is_valid=True`이나 `code="INVALID_SIZE"`, `message="Grid must be 4x4."` 유지 | 성공/실패 응답 계약 미분리(실패 전용 상수 재사용) | **미수정 (범위 외).** AC-FR-01-01 스위트는 실패 경로만 검증. 후속 AC 또는 GREEN 확장 시 성공 code 분리 예정 |
| DEF-005 | Info | AC-FR-01-01 | RED 단계에서 `tests/entity/test_user.py`와 AC 스위트 동시 실행 | AC-FR-01-01 34건 + entity 테스트 전체 GREEN | AC 스위트만 34 passed; entity 테스트는 별도 스위트 | AC-FR-01-01과 User 엔티티 테스트 범위 분리 | 결함 아님 — 스위트 분리 유지. 회귀 시 AC 스위트 명령을 README/defect_list에 고정 ✅ |

---

## 심각도 정의

| Severity | 기준 |
|----------|------|
| **Critical** | 테스트 수집/실행 불가, 또는 `None`/잘못된 입력 시 예외·크래시 |
| **Major** | `code` / `message`가 PRD §8.1과 불일치, Domain 격리 위반 |
| **Minor** | 테스트 설계 오류, 반환 타입/구조체 불일치(동작은 맞음) |
| **Info** | 잠재 결함, 문서/범위 이슈, 미래 AC 대비 개선 항목 |

---

## 수정 이력 요약

| 단계 | 조치 | 결과 |
|------|------|------|
| RED | AC-FR-01-01 테스트 38건 작성 | Collection ERROR 2건 (DEF-001, DEF-002) |
| GREEN | Boundary/Control 최소 구현 | 동작 테스트 34건 PASS |
| REFACTOR | 메타 테스트 자기 참조 제거 (DEF-003) | 전체 34건 PASS |
| 잔여 | DEF-004 성공 응답 계약 | AC-FR-01-01 범위 외 — 추적만 유지 |

---

## 회귀 테스트 명령

```powershell
cd c:\Users\usejen_id\Downloads\CursorAI-main\DEV\MagicSquare
python -m pytest tests/boundary/test_boundary_validator_size.py tests/control/test_resolve_use_case_size_guard.py -v
```

**기대:** `34 passed`

---

*End of Defect List*
