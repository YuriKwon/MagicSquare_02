# MagicSquare — 4×4 Magic Square

4×4 마방진(Magic Square)을 다루는 학습·실습 프로젝트입니다.  
현재는 **구현 이전** 단계로, **문제 인식·문제 정의**까지 완료된 상태입니다.

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
| 대화형 프롬프트 (`Prompt/`) | ✅ Export 완료 |
| 소스 코드·테스트·실행 환경 | ❌ 없음 (의도적) |

## Python 버전

- 프로젝트 기본 Python 버전은 `3.10`으로 고정 (`.python-version`).

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

## 아직 확정하지 않은 항목

구현·테스트 설계에 들어가기 **전에** 문서로 고정할 것:

1. **대각**을 제약에 포함할지 (S4)
2. **입력:** 완전 격자만 vs 부분 채움·사용자 입력
3. **출력:** 통과/실패만 vs 위반 항목 진단
4. **동치:** 특정 배치 고정 vs 회전·대칭 허용 vs `validate`만
5. **범위:** 판정만 vs 유효 배치 **도출**까지 포함

---

## 폴더 구조

```
MagicSquare/
├── README.md                 ← 이 파일 (프로젝트 개요)
├── Report/                   ← 문제 정의 보고서
│   ├── README.md
│   └── MagicSquare-ProblemDefinition-Report.md
└── Prompt/                   ← 대화형 프롬프트·트랜스크립트
    ├── README.md
    ├── transcript.md
    ├── interactive-prompt-chain.md
    └── system-context.md
```

---

## 문서 가이드

### Report — 분석·정의 본문

| 문서 | 설명 |
|------|------|
| [Report/MagicSquare-ProblemDefinition-Report.md](./Report/MagicSquare-ProblemDefinition-Report.md) | STEP 1~5 통합 보고서 (관찰, Why, TDD, 진짜 문제 정의) |
| [Report/README.md](./Report/README.md) | Report 폴더 안내 |

### Prompt — 세션 재현·기록

| 문서 | 설명 |
|------|------|
| [Prompt/transcript.md](./Prompt/transcript.md) | User / Assistant 턴별 대화 기록 |
| [Prompt/interactive-prompt-chain.md](./Prompt/interactive-prompt-chain.md) | Turn별 User 프롬프트만 (복사·재실행용) |
| [Prompt/system-context.md](./Prompt/system-context.md) | 역할·제약·단계 전제 |
| [Prompt/README.md](./Prompt/README.md) | Prompt 폴더 안내 |

**같은 문제 정의 흐름을 다시 돌리려면:**  
`Prompt/system-context.md` → `Prompt/interactive-prompt-chain.md` (Turn 1부터 순서대로)

---

## 표면 정의 vs 진짜 정의

| | 표면 (잘못된 정의) | 진짜 (개선된 정의) |
|---|-------------------|-------------------|
| **초점** | 4×4 마방진 프로그램, 합 같게 출력 | 유효 배치 규칙 + 판정·(선택) 도출 |
| **성공** | 뭔가 출력됨 | 무효 거부, 유효 일관 수용 |
| **훈련** | 구현 | 규칙 명시·계약·불변·재현·문제 재정의 |

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 test_plan.md 기반으로 생성되었습니다.
> 각 항목은 RED(실패 테스트 작성) 완료 시 체크합니다.

### Track A — UI / Boundary 테스트
- [ ] TC-A-01: grid=None 입력 → 실패 결과 반환 (Happy Path of Failure)
- [ ] TC-A-02: code가 정확히 "INVALID_SIZE" 문자열인지 검증
- [ ] TC-A-03: message가 "Grid must be 4x4." 와 문자 단위 동일한지 검증
- [ ] TC-A-04: grid=None 시 Domain 진입점 0회 호출 (mock/spy 검증)
- [ ] TC-A-05: grid=[] 빈 리스트 → 실패 결과 반환
- [ ] TC-A-06: grid=3×4 크기 불일치 → 실패 결과 반환
- [ ] TC-A-07: 반환 객체 타입이 지정 실패 결과 구조체인지 검증

### Track B — Domain / Logic 테스트
- [ ] TC-B-01: resolve()가 None grid를 직접 받지 않음을 격리 검증
- [ ] TC-B-02: Boundary가 None 분기를 처리 후 resolve() 미호출 확인
- [ ] TC-B-03: resolve() mock이 호출됐을 경우 테스트 실패 처리
- [ ] TC-B-04: AC-FR-01-02~05 범위의 케이스는 이 커밋에 포함하지 않음 확인

### 커버리지 목표
- [ ] Domain Logic: 95%+ (pip install pytest-cov)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결
- [x] defect_list.md 생성 및 발견 결함 기록
- [x] 모든 결함 수정 후 회귀 테스트 통과 확인

---

## 권장 다음 단계

1. 위 **미결 항목** 확정 (특히 대각·도출 범위)
2. Given / When / Then 형식의 **테스트 시나리오 목록** 작성 (코드 없이)
3. TDD 기반으로 **검증(validate)** 부터 구현
4. 범위에 포함되면 **도출(generate)** 구현

---

## 세션 제약 (문제 정의 단계)

다음은 의도적으로 다루지 않았습니다.

- 구현 설계
- 소스 코드
- 알고리즘 설명

이후 단계에서 별도로 추가합니다.

---

## 라이선스·기여

(미정 — 필요 시 추가)

---

*Last updated: 2026-05-28*
