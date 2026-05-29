"""Report/08 — U-IN-01~03: FR-01 input validation (Full RED).

Traceability:
  U-IN-01 → AC-FR-01-05 (null → E003)
  U-IN-02 → AC-FR-01-01 (size → E001)
  U-IN-03 → AC-FR-01-02 (blank count → E002)
"""

from __future__ import annotations

from typing import Any

import pytest

from src.boundary.input_validator import InputValidator, ValidationEnvelope
from tests.conftest import (
    E001_CODE,
    E001_MESSAGE,
    E002_CODE,
    E002_MESSAGE,
    E003_CODE,
    E003_MESSAGE,
)


class TestUIn01NullMatrix:
    """U-IN-01; FR-01 null check (1st priority); AC-FR-01-05."""

    def test_validate_returns_e003_when_matrix_is_null(self) -> None:
        """U-IN-01 — null matrix returns E003 failure envelope."""
        # Given
        validator = InputValidator()
        matrix = None

        # When
        result = validator.validate(matrix)

        # Then
        assert isinstance(result, ValidationEnvelope)
        assert result.ok is False
        assert result.error is not None
        assert result.error.code == E003_CODE
        assert result.error.message == E003_MESSAGE


class TestUIn02SizeNot4x4:
    """U-IN-02; FR-01 4x4 shape; AC-FR-01-01."""

    @pytest.mark.parametrize(
        "matrix",
        [
            pytest.param([], id="empty_list"),
            pytest.param(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                id="three_by_four",
            ),
            pytest.param(
                [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                id="four_by_three",
            ),
            pytest.param([[1, 2, 3, 4, 5] for _ in range(5)], id="five_by_five"),
        ],
    )
    def test_validate_returns_e001_when_size_not_4x4(self, matrix: Any) -> None:
        """U-IN-02 — non-4x4 matrix returns E001 failure envelope."""
        # Given
        validator = InputValidator()

        # When
        result = validator.validate(matrix)

        # Then
        assert result.ok is False
        assert result.error is not None
        assert result.error.code == E001_CODE
        assert result.error.message == E001_MESSAGE


class TestUIn03BlankCount:
    """U-IN-03; FR-01 blank count; AC-FR-01-02."""

    def test_validate_returns_e002_when_zero_blank_count_is_0(
        self, grid_g0: list[list[int]]
    ) -> None:
        """U-IN-03a — G0 (zero blanks) returns E002 failure envelope."""
        # Given
        validator = InputValidator()

        # When
        result = validator.validate(grid_g0)

        # Then
        assert result.ok is False
        assert result.error is not None
        assert result.error.code == E002_CODE
        assert result.error.message == E002_MESSAGE

    def test_validate_returns_e002_when_zero_blank_count_is_3(
        self, grid_g1_three_blanks: list[list[int]]
    ) -> None:
        """U-IN-03b — G1+(1,1)=0 (three blanks) returns E002 failure envelope."""
        # Given
        validator = InputValidator()

        # When
        result = validator.validate(grid_g1_three_blanks)

        # Then
        assert result.ok is False
        assert result.error is not None
        assert result.error.code == E002_CODE
        assert result.error.message == E002_MESSAGE
