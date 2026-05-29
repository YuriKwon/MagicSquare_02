# Magic Square 4x4 — TDD 실행 프롬프트 설계 보고서

| 항목 | 내용 |
|------|------|
| 프로젝트 | `DEV\MagicSquare` |
| 문서 유형 | 프롬프트 설계/Export 보고서 |
| 목적 | 설계 문서를 직접 작성하지 않고, 설계 문서를 생성할 수 있는 실행 프롬프트를 확정 |
| 작성일 | 2026-05-28 |

---

## 1) 요청 배경

- 사용자 목표는 `Magic Square 4x4`의 **TDD 설계 문서 작성용 프롬프트** 확보였다.
- 핵심 제약은 **구현 코드 금지**, **설계/계약/테스트/통합 계획 중심**이다.
- 추가 요구로 Dual-Track(`UI Boundary + Logic`) 및 Clean Architecture 관점이 포함되었다.

## 2) 이번 세션 산출물

### 2.1 실행용 프롬프트 v1 (기본형)

- 역할: 시니어 아키텍트 + TDD 코치
- 목적: `Magic Square 4x4 TDD 설계 문서`를 Markdown으로 산출
- 포함 섹션:
  - 문제 정의
  - 요구사항 명세(기능/비기능/예외)
  - 도메인 모델/설계
  - TDD 전략(Red-Green-Refactor 단계화)
  - 테스트 설계(20+ 시나리오)
  - 알고리즘 대안 비교
  - 품질/검증 계획
  - 다음 단계 + Open Questions

### 2.2 실행용 프롬프트 v2 (Dual-Track 강화형)

- 고정 계약이 명시된 구조적 프롬프트로 확장:
  - 입력 계약: `4x4 int[][]`, `0=빈칸`, 빈칸 정확히 2개, 범위/중복 규칙
  - 출력 계약: `int[6] = [r1,c1,n1,r2,c2,n2]`, 1-index, 두 조합 순서 규칙
- 고정 출력 구조(1~4장) 강제:
  - Logic Layer
  - Screen(UI Boundary) Layer
  - Data Layer
  - Integration & Verification
- 필수 검증:
  - Traceability Matrix
  - 커버리지 목표(Domain 95%+, UI 85%+, Data 80%+)
  - 문서 말미 자체 검증 체크리스트

## 3) 품질 기준(프롬프트 관점)

- 모호 표현 금지(예: “적절히”, “충분히”)
- 테스트로 검증 가능한 규칙만 허용
- 구현 코드 출력 금지
- 표/체크리스트 중심 문서화

## 4) Export 실행 결과

- `Prompt/transcript.md`: 최신 대화 턴까지 반영한 대화형 기록
- `Prompt/interactive-prompt-chain.md`: 재실행 가능한 User Prompt 체인(기본형 + 강화형)
- 본 보고서: 프롬프트 설계 의도와 산출물 요약

## 5) 결론

이번 세션은 구현 단계로 넘어가지 않고, **TDD 설계 문서를 안정적으로 생성하는 실행 프롬프트 자체를 제품화**하는 데 초점을 맞췄다.  
특히 v2는 입력/출력 계약과 레이어별 테스트 책임을 고정해, 후속 설계 문서 품질 편차를 줄이도록 구성됐다.

---

*End of Report*
