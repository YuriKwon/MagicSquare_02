# Report

4×4 Magic Square 프로젝트의 **문제 인식·정의** 단계 산출물입니다.

## 문서

| 파일 | 설명 |
|------|------|
| [MagicSquare-ProblemDefinition-Report.md](./MagicSquare-ProblemDefinition-Report.md) | STEP 1~5 통합 보고서 (관찰, Why #1~#3, 진짜 문제 정의) |
| [MagicSquare-TDDPrompt-Design-Report.md](./MagicSquare-TDDPrompt-Design-Report.md) | TDD 설계 문서 생성용 실행 프롬프트 설계/Export 보고서 |
| [MagicSquare-Level1to5-Verification-Report.md](./MagicSquare-Level1to5-Verification-Report.md) | Level 1~5 Epic→Scenario 검증 보고서 |
| [MagicSquare-AC-FR-01-01-TDD-Execution-Report.md](./MagicSquare-AC-FR-01-01-TDD-Execution-Report.md) | AC-FR-01-01 RED→GREEN TDD 실행 보고서 |
| [MagicSquare-DualTrack-RED-Design-Report.md](./MagicSquare-DualTrack-RED-Design-Report.md) | FR-01~FR-05 Dual-Track RED 테스트 설계표 (코드 없음) |
| [MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md](./MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md) | Dual-Track RED Skeleton pytest 실행 보고서 (Track A/B, 23건) |

## 범위

- 포함: 문제 관찰, 가정·구조 분석, TDD 관점, 불변 조건, 사고 능력 정의, AC-FR-01-01 TDD 실행 요약, Dual-Track RED 설계표, **RED Skeleton pytest 23건**
- 미포함: FR-02~05 Domain GREEN 구현 (별도 세션)

## 다음 단계 (권장, 본 폴더 외 작업)

1. 대각 포함 여부 등 **미결 항목** 확정
2. Given/When/Then **테스트 시나리오 목록** 작성 (코드 없이)
3. 이후 TDD 기반 구현 단계 진입
