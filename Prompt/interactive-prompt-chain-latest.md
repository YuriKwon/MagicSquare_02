# Interactive Prompt Chain (Latest)

아래 User 프롬프트를 순서대로 실행하면 이번 세션 흐름을 재현할 수 있습니다.

---

## Turn 1

```text
MagicSquare Python 프로젝트용 Cursor Rule을 만들고 싶습니다.

조건:
- Python 3.10+
- PEP8
- type hints 필수
- pytest + AAA 패턴
- ECB 아키텍처(boundary/control/entity)
- Dual-Track TDD
- print() 디버깅 금지
- 테스트 약화 금지
- RED 없이 구현 금지

지금 규칙 파일을 바로 만들지 말고,
먼저 Cursor Rule을 어떤 파일 구조와 섹션으로 설계해야 하는지 설명해 주세요.

특히 .cursorrules 방식과 .cursor/rules/*.mdc 방식 중 무엇을 선택해야 하는지,
그리고 MagicSquare 프로젝트에서는 규칙 파일을 어떻게 나누면 좋은지 알려주세요.
```

## Turn 2

```text
MagicSquare 프로젝트의 .cursorrules YAML 파일 뼈대를 만들어줘.
아래 최상위 키만 포함하고 값은 비워둬:
project, code_style, architecture, tdd_rules, testing, forbidden, file_structure, ai_behavior
각 키 앞에 80자짜리 # 구분선 주석을 추가해.
YAML 내용만 출력해.
```

## Turn 3

```text
계속
```

## Turn 4

```text
위 .cursorrules 파일의 tdd_rules 섹션을 채워줘.
  - red_phase: 테스트 먼저 작성, 실패 확인 후 다음 단계 진행 조건
  - green_phase: 최소 코드로만 테스트 통과, 이 단계에서 리팩터링 금지
  - refactor_phase: 기능 변경 없이 구조 개선, 커버리지 유지 조건
YAML 형식 유지. tdd_rules 블록만 출력해.
```

## Turn 5

```text
방금 완성한 .cursorrules 파일을 검토해줘.
아래 항목을 확인해:
1. YAML 문법 오류
2. 누락된 필수 섹션
3. tdd_rules와 forbidden 규칙 간의 충돌
4. Cursor AI가 실제로 따를 수 없는 ai_behavior 규칙
문제점만 보고해줘. 수정은 내가 요청할 때만 해.
```

## Turn 6

```text
위에서 만든 .cursorrules 뼈대의 빈 섹션을 모두 채워줘.
MagicSquare 프로젝트 기준으로 작성해.
각 섹션 작성 규칙:
code_style:
  - python_version: "3.10+"
  - style_guide: PEP8 엄격 준수
  - type_hints: 모든 함수 파라미터와 반환값에 필수
  - docstring: Google 스타일, 모든 public 메서드에 필수
  - max_line_length: 88 (Black 기준)
architecture:
  ECB 패턴 3 레이어를 각각 정의해줘:
  - boundary: 외부 입출력 담당 (UI, API, CLI)
  - control: 비즈니스 로직 담당
  - entity: 도메인 데이터 및 규칙 담당
  레이어 간 의존성 방향도 명시해줘.
tdd_rules:
  지금은 문자열 1줄인데, 하위 항목으로 세분화해줘.
  각 phase마다:
    - description: 단계 설명
    - rules: 지켜야 할 규칙 목록
    - must_not: 이 단계에서 하면 안 되는 것
testing:
  - framework: pytest
  - pattern: AAA (Arrange-Act-Assert)
  - coverage_minimum: "80%"
  - fixture_scope: 규칙 정의
  - naming_convention: test_ 접두사 필수
forbidden:
  항목마다 아래 구조로 작성:
    pattern: 금지 패턴
    reason: 금지 이유
    alternative: 대신 써야 할 것
  최소 포함 항목: print(), 하드코딩 상수, except 단독 사용
file_structure:
  ECB 기준 폴더 구조를 트리 형태 주석으로 작성해줘.
  boundary/, control/, entity/, tests/ 포함.
ai_behavior:
  Cursor AI가 코드 생성 전·중·후에 반드시 따라야 할 규칙.
  최소 포함:
    - 코드 작성 전 관련 테스트 파일 확인
    - ECB 레이어 경계 위반 금지
    - 타입힌트 없는 함수 생성 금지
    - tdd_rules 위반 시 경고 출력
완성된 .cursorrules 전체 파일을 출력해줘.
```

## Turn 7

```text
어딨어? cursorrules가
```

## Turn 8

```text
응. 만들어.
```

## Turn 9

```text
.cursorrules를 읽고
MagicSquare의 User 엔티티 클래스를 ECB 패턴으로 작성해줘.
타입힌트, Google docstring, pytest 테스트 파일도 함께 만들어줘.
```

## Turn 10

```text
다음의 순서로 실행해줘
1. Report 폴더에 보고서 생성해줘
2. 현재까지의 프롬프트 전체를 대화형 프롬프트로 Prompt 폴더에 Export transcript 해줘
```

## Turn 11

```text
다음처럼 확장해 보세요.
. D:. 1-3-2..MagicSquare_개선
│  .cursorrules
│
└─.cursor
    └─rules
            magicsquare-ecb-architecture.mdc
            magicsquare-forbidden.mdc
            magicsquare-project.mdc
            magicsquare-python-code-style.mdc
            magicsquare-tdd-testing.mdc
```

## Turn 12

```text
보고서를 내보내주는 것과 프롬프트 저장을 해줘
```
