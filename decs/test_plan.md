# Magic Square 4×4 — Test Plan

| 항목 | 내용 |
|------|------|
| 문서 유형 | 단위 테스트 계획서 (Unit Test Plan) |
| 기준 AC | **AC-FR-01-01** — 4×4가 아니면 `INVALID_SIZE` 반환 |
| 기준 FR | **FR-01** Input Verification (Boundary), §10 |
| 관련 BR | **BR-01** — 입력은 항상 4행 4열 정수 매트릭스여야 한다 |
| Technical Scenario | **SC-BND-VAL-004** — Reject non-4x4 matrix shape |
| Traceability | Concept(G1) → BR-01 → FR-01 → AC-FR-01-01 → TC-BND-001 |
| 대상 스택 | Python 3.11+, pytest, pydantic, unittest.mock |
| 작성 관점 | Senior QA Lead / Dual-Track TDD (Track A: Boundary) |

---

## 1. 목적 및 범위

본 계획서는 **AC-FR-01-01**을 중심으로 Boundary 계층의 **4×4 형상(size) 검증** 단위 테스트 범위·우선순위·검증 전략을 정의한다.

### 1.1 In-Scope

- BoundaryValidator(또는 동등 컴포넌트)의 **행·열 크기 검증**
- Control 계층의 **입력 검증 실패 시 Domain 해 결정 진입점 미호출** 보장
- 표준 실패 응답 계약: `{ code: "INVALID_SIZE", message: "Grid must be 4x4." }`
- pytest 기반 RED → GREEN → REFACTOR 사이클에 따른 Track A 테스트

### 1.2 Out-of-Scope (본 AC 범위 외 — 테스트 포함 금지)

| 항목 | 관련 AC | 사유 |
|------|---------|------|
| 빈칸 개수 검증 | AC-FR-01-02 | FR-01 후속 AC |
| 값 범위 검증 (`0` 또는 `1..16`) | AC-FR-01-03 | FR-01 후속 AC |
| 중복 숫자 검증 | AC-FR-01-04 | FR-01 후속 AC |
| **4×4 정상 입력** | — | AC-FR-01-01 통과 케이스; 본 계획 범위 외 |
| Solver / BlankFinder / MissingNumberFinder | FR-02~FR-05 | Domain Track B; 별도 계획 |

---

## 2. pytest 단위 테스트 범위 및 우선순위

### 2.1 테스트 레이어 매핑

| 우선순위 | 레이어 | 테스트 대상 | 테스트 파일 (예정) | Track |
|----------|--------|-------------|-------------------|-------|
| **P0** | Boundary | `BoundaryValidator.validate_size(grid)` | `tests/boundary/test_boundary_validator_size.py` | A |
| **P0** | Control | `ResolveUseCase.execute(grid)` — 검증 실패 시 Domain 미위임 | `tests/control/test_resolve_use_case_size_guard.py` | A |
| **P1** | Boundary | pydantic 입력 모델(선택) — `None`/비정형 grid 거부 | `tests/boundary/test_grid_input_model.py` | A |
| **P2** | Integration | Boundary → Control → Domain 전체 경로 smoke (size fail only) | `tests/integration/test_size_validation_guard.py` | A |

> **P0**는 AC-FR-01-01 GREEN 달성에 필수. **P1/P2**는 회귀 보호 및 계층 간 계약 강화용.

### 2.2 실행 우선순위 (RED 순서)

1. **RED-BND-SIZE-001** — `grid=None` → `INVALID_SIZE` (대표 샘플, 최우선)
2. **RED-BND-SIZE-002** — `grid=[]` → `INVALID_SIZE`
3. **RED-BND-SIZE-003** — `grid=[[]]*4` → `INVALID_SIZE`
4. **RED-BND-SIZE-004** — 3×4, 4×3, 5×5 → 각각 `INVALID_SIZE`
5. **RED-CTL-GUARD-001** — 위 모든 케이스에서 Domain resolver 호출 0회

### 2.3 AAA 패턴 적용 규칙

모든 테스트는 pytest AAA(Arrange–Act–Assert)를 따른다.

```text
Arrange : grid 입력값, mock/spy 설정
Act     : BoundaryValidator.validate_size(grid) 또는 ResolveUseCase.execute(grid)
Assert  : 반환 code/message, Domain 진입점 call_count == 0
```

### 2.4 테스트 네이밍 규칙

- 파일: `test_<layer>_<feature>.py`
- 함수: `test_<behavior>_when_<condition>`
- 예: `test_returns_invalid_size_when_grid_is_none`

---

## 3. 경계값 케이스 목록 (AC-FR-01-01)

> **공통 기대 결과:** `{ "code": "INVALID_SIZE", "message": "Grid must be 4x4." }`  
> **공통 부수 조건:** Domain 해 결정 진입점(Solver/Resolve) 호출 **0회**

| TC ID | 입력 (`grid`) | 검증 포인트 | 우선순위 |
|-------|---------------|-------------|----------|
| TC-BND-SIZE-001 | `None` | 명시적 `None` 입력 거부 | P0 |
| TC-BND-SIZE-002 | `[]` | 빈 리스트(행 0) 거부 | P0 |
| TC-BND-SIZE-003 | `[[]] * 4` | 행 4개 존재, 열 0(빈 행) 거부 | P0 |
| TC-BND-SIZE-004a | 3×4 행렬 (3행, 각 행 길이 4) | 행 수 불일치 거부 | P0 |
| TC-BND-SIZE-004b | 4×3 행렬 (4행, 각 행 길이 3) | 열 수 불일치 거부 | P0 |
| TC-BND-SIZE-004c | 5×5 행렬 | 행·열 모두 불일치 거부 | P0 |

### 3.1 경계값 케이스 상세

#### TC-BND-SIZE-001 — `grid = None`

| 항목 | 값 |
|------|-----|
| Arrange | `grid = None` |
| Act | `BoundaryValidator.validate_size(None)` |
| Assert | `result.code == "INVALID_SIZE"`, `result.message == "Grid must be 4x4."` |

#### TC-BND-SIZE-002 — `grid = []`

| 항목 | 값 |
|------|-----|
| Arrange | `grid = []` |
| Act | `BoundaryValidator.validate_size([])` |
| Assert | 동일 실패 응답 |

#### TC-BND-SIZE-003 — `grid = [[]] * 4`

| 항목 | 값 |
|------|-----|
| Arrange | `grid = [[]] * 4` (4행, 각 행 길이 0) |
| Act | `BoundaryValidator.validate_size(grid)` |
| Assert | 동일 실패 응답; `len(grid)==4`이지만 열 길이 0으로 4×4 아님 |

#### TC-BND-SIZE-004 — 크기 불일치 행렬

| 변형 | Arrange 예시 | 불일치 유형 |
|------|--------------|-------------|
| 004a | `[[1]*4]*3` | 3×4 (행 부족) |
| 004b | `[[1]*3]*4` | 4×3 (열 부족) |
| 004c | `[[1]*5]*5` | 5×5 (양방향 초과) |

### 3.2 명시적 제외 케이스

| 입력 | 제외 사유 |
|------|-----------|
| 유효한 4×4 정상 행렬 | AC-FR-01-01 **통과** 케이스; 본 AC 테스트 범위 외 |
| 빈칸 2개인 4×4 | 형상은 유효 → AC-FR-01-02 이후 검증 대상 |

---

## 4. 예외/특이 케이스 목록

AC-FR-01-01 형상 검증과 직접 연관된 예외·특이 입력. P1 이상에서 커버.

| TC ID | 입력 / 조건 | 기대 동작 | 비고 |
|-------|-------------|-----------|------|
| TC-BND-SIZE-EX-001 | `grid`가 `list`가 아닌 타입 (예: `"4x4"`, `42`, `{}`) | `INVALID_SIZE` 반환 | 타입 계약 위반 |
| TC-BND-SIZE-EX-002 | `grid = [[1,2,3,4], [5,6,7], [9,10,11,12], [13,14,15,16]]` | `INVALID_SIZE` 반환 | **가변 길이 행**(ragged row) |
| TC-BND-SIZE-EX-003 | `grid = None` 반복 호출 2회 | 매 호출 동일 `INVALID_SIZE` | NFR-03 결정성 |
| TC-BND-SIZE-EX-004 | 검증 실패 후 원본 `grid` 참조 불변 | 입력 객체 변경 없음 | NFR-04 불변 입력 |
| TC-BND-SIZE-EX-005 | pydantic `GridInput` 모델에 `None` 주입 | ValidationError 또는 `INVALID_SIZE` 매핑 | Boundary DTO 계층 |
| TC-BND-SIZE-EX-006 | Control 경로에서 size fail | 예외 throw 없이 에러 객체 반환 | FR-01 실패 정책 |

---

## 5. Domain 해 결정 진입점 호출 횟수 검증 전략 (mock/spy)

### 5.1 검증 대상

| 진입점 (spy 대상) | 레이어 | 역할 |
|-------------------|--------|------|
| `Solver.resolve(...)` | Domain | 두 조합 시도 후 결과 반환 |
| `ResolveUseCase._invoke_domain(...)` (내부) | Control | Domain 위임 게이트 |

> FR-01 Error Policy: **입력 검증 실패 시 Domain resolver를 호출하지 않는다.**

### 5.2 검증 패턴

#### Pattern A — Boundary 단독 (순수 함수)

BoundaryValidator는 Domain을 import하지 않는다.  
→ **spy 불필요**. 반환값만 Assert.

#### Pattern B — Control orchestration (필수 P0)

```python
from unittest.mock import MagicMock

def test_domain_resolver_not_called_when_grid_is_none():
    # Arrange
    domain_resolver = MagicMock()
    use_case = ResolveUseCase(domain_resolver=domain_resolver)
    grid = None

    # Act
    result = use_case.execute(grid)

    # Assert
    assert result.code == "INVALID_SIZE"
    assert result.message == "Grid must be 4x4."
    domain_resolver.resolve.assert_not_called()
    assert domain_resolver.resolve.call_count == 0
```

#### Pattern C — `@patch` 데코레이터 (통합 smoke)

```python
from unittest.mock import patch

@patch("src.control.resolve_use_case.Solver.resolve")
def test_size_fail_short_circuits_before_solver(mock_resolve):
    # Arrange / Act
    result = ResolveUseCase(...).execute([])

    # Assert
    assert result.code == "INVALID_SIZE"
    mock_resolve.assert_not_called()
```

### 5.3 케이스별 spy 적용 매트릭스

| TC ID | spy 대상 | 기대 `call_count` |
|-------|----------|-------------------|
| TC-BND-SIZE-001 ~ 004c | `domain_resolver.resolve` | **0** |
| TC-BND-SIZE-EX-001 ~ 006 | `domain_resolver.resolve` | **0** |
| (향후) AC-FR-01-01 통과 4×4 | `domain_resolver.resolve` | ≥ 1 (별도 AC) |

### 5.4 실패 시 진단 기준

| 관측 | 판정 | 조치 |
|------|------|------|
| `call_count == 0` & `INVALID_SIZE` | PASS | — |
| `call_count >= 1` & size invalid | **FAIL** — 계층 누수 | Control 가드 로직 수정 |
| 예외 throw & Domain 호출됨 | **FAIL** — 실패 정책 위반 | 에러 객체 반환으로 통일 |

---

## 6. 커버리지 목표

| 레이어 | 목표 | 측정 대상 (예정) | 본 AC 기여 |
|--------|------|------------------|------------|
| **Domain** | **95%+** | `src/entity/`, Domain services | AC-FR-01-01 범위에서는 Domain 코드 미실행; Track B 별도 계획으로 달성 |
| **Boundary** | **85%+** | `src/boundary/` | BoundaryValidator size 분기 **100%** 목표 |
| **Control** | **85%+** (Boundary와 동일 Track A 기준) | `src/control/` | size fail short-circuit 경로 **100%** 목표 |
| **프로젝트 전체** | **80%+** (workspace baseline) | `src/` | Dual-Track 누적 |

### 6.1 AC-FR-01-01 관련 커버리지 체크리스트

- [ ] `validate_size`: `None` 분기 covered
- [ ] `validate_size`: empty list 분기 covered
- [ ] `validate_size`: ragged / non-4x4 분기 covered
- [ ] `ResolveUseCase.execute`: size fail early-return 분기 covered
- [ ] Domain resolver 미호출 경로 covered (spy 테스트)

---

## 7. pytest-cov 측정 전략

### 7.1 설치

```bash
pip install pytest-cov
```

### 7.2 기본 실행 (전체)

```bash
pytest --cov=src --cov-report=term-missing
```

### 7.3 AC-FR-01-01 집중 실행 (Track A — Boundary/Control)

```bash
pytest tests/boundary/test_boundary_validator_size.py \
       tests/control/test_resolve_use_case_size_guard.py \
       --cov=src/boundary \
       --cov=src/control \
       --cov-report=term-missing \
       --cov-fail-under=85
```

### 7.4 레이어별 분리 측정

```bash
# Boundary only
pytest tests/boundary/ --cov=src/boundary --cov-report=term-missing --cov-fail-under=85

# Domain only (Track B — 별도 스위트)
pytest tests/entity/ tests/domain/ --cov=src/entity --cov-report=term-missing --cov-fail-under=95
```

### 7.5 CI 권장 옵션

```bash
pytest --cov=src \
       --cov-report=term-missing \
       --cov-report=xml:coverage.xml \
       --cov-fail-under=80
```

| 옵션 | 용도 |
|------|------|
| `--cov-report=term-missing` | 미커버 라인 즉시 확인 |
| `--cov-report=xml` | CI/CD 커버리지 게이트 연동 |
| `--cov-fail-under=N` | 레이어별 최소 커버리지 강제 |

### 7.6 측정 시 주의사항

- **Boundary spy 테스트**는 Domain 코드를 실행하지 않으므로, Domain 95%는 Track B 테스트와 **분리 측정**한다.
- `tests/` 및 `__init__.py` only 파일은 `--cov=src`로 한정하여 측정 노이즈를 줄인다.
- REFACTOR 단계마다 `--cov-report=term-missing`으로 size 검증 분기 누락을 확인한다.

---

## 8. Traceability Matrix (본 AC)

| Concept | BR | FR | AC | TC ID | RED Test ID | Component |
|---------|----|----|-----|-------|-------------|-----------|
| 4×4 입력 (G1) | BR-01 | FR-01 | AC-FR-01-01 | TC-BND-SIZE-001~004c | RED-BND-SIZE-001~004 | BoundaryValidator |
| Domain 미호출 | FR-01 Error Policy | FR-01 | AC-FR-01-01 | TC-CTL-GUARD-001 | RED-CTL-GUARD-001 | ResolveUseCase |

---

## 9. 완료 기준 (Exit Criteria)

1. §3 경계값 케이스 **6건**(001~004c) 전부 GREEN
2. §4 예외/특이 케이스 **6건**(EX-001~006) GREEN
3. 모든 size-fail 케이스에서 Domain resolver **`call_count == 0`** 확인
4. Boundary/Control `--cov-fail-under=85` 통과
5. 4×4 정상 입력 테스트가 **본 AC 스위트에 포함되지 않음** 확인

---

## 10. 후속 계획 (별도 문서)

| AC | 내용 | Track |
|----|------|-------|
| AC-FR-01-02 | 빈칸 2개 검증 | A |
| AC-FR-01-03 | 값 범위 검증 | A |
| AC-FR-01-04 | 중복 숫자 검증 | A |
| AC-FR-02~05 | BlankFinder, Solver 등 | B |

---

*End of Test Plan*
