# Prompt — 대화형 프롬프트 Export

이 폴더는 **4×4 Magic Square 문제 인식·정의** 세션의 프롬프트·응답을 대화형으로 재사용·재현할 수 있도록보낸 산출물입니다.

## 파일

| 파일 | 용도 |
|------|------|
| [transcript.md](./transcript.md) | 전체 대화 트랜스크립트 (User / Assistant 턴 순서) |
| [transcript-latest.md](./transcript-latest.md) | Cursor Rule + User Entity 세션 Transcript |
| [transcript-ac-fr-01-01-tdd-latest.md](./transcript-ac-fr-01-01-tdd-latest.md) | AC-FR-01-01 TDD (RED→GREEN) 세션 Transcript |
| [transcript-dualtrack-red-design-latest.md](./transcript-dualtrack-red-design-latest.md) | FR-01~FR-05 Dual-Track RED 설계 세션 Transcript |
| [transcript-dualtrack-red-skeleton-latest.md](./transcript-dualtrack-red-skeleton-latest.md) | Dual-Track RED Skeleton pytest 세션 Transcript |
| [interactive-prompt-chain.md](./interactive-prompt-chain.md) | 턴별 **User 프롬프트만** 복사·재실행용 체인 |
| [system-context.md](./system-context.md) | 세션 전제·역할·제약 (문제 정의 전문가 모드) |

## 사용 방법

1. **처음부터 같은 흐름 재현:** `system-context.md` → `interactive-prompt-chain.md`의 Turn 1부터 순서대로 붙여 넣기  
2. **기록 확인:** `transcript.md`에서 User·Assistant 전체 내용 검토  
3. **보고서와 연계:**
   - 문제 정의: [../Report/MagicSquare-ProblemDefinition-Report.md](../Report/MagicSquare-ProblemDefinition-Report.md)
   - TDD 프롬프트 설계: [../Report/MagicSquare-TDDPrompt-Design-Report.md](../Report/MagicSquare-TDDPrompt-Design-Report.md)
   - AC-FR-01-01 실행: [../Report/MagicSquare-AC-FR-01-01-TDD-Execution-Report.md](../Report/MagicSquare-AC-FR-01-01-TDD-Execution-Report.md)
   - Dual-Track RED 설계: [../Report/MagicSquare-DualTrack-RED-Design-Report.md](../Report/MagicSquare-DualTrack-RED-Design-Report.md)
   - Dual-Track RED Skeleton: [../Report/MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md](../Report/MagicSquare-DualTrack-RED-Skeleton-Execution-Report.md)

## 범위

- Turn 1 ~ Turn 10 (문제 정의 STEP + 실행 프롬프트 설계 + 최신 Export)
- 구현 코드 작성 요청은 배제, 설계 프롬프트 중심 세션

## Export 정보

| 항목 | 값 |
|------|-----|
| Export 일자 | 2026-05-28 |
| 프로젝트 | `DEV\MagicSquare` |
| 모드 | 문제 정의 전문가 (관찰 → Why → 진짜 문제 정의) |
