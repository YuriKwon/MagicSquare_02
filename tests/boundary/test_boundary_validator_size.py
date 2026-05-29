"""Boundary size-validation tests for AC-FR-01-01.

AC-FR-01-01; PRD §8.1 INVALID_SIZE — 4×4 shape rejection at Boundary layer.
"""

from __future__ import annotations

import inspect

import pytest

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.validation_result import ValidationResult
from tests.conftest import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE


class TestNormalFailureReturn:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — normal failure return path."""

    def test_grid_none_returns_invalid_size_code(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — None grid returns failure code."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate_size(grid)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_grid_none_returns_invalid_size_message(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — None grid returns failure message."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate_size(grid)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE

    def test_grid_none_returns_validation_result_type(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — failure is ValidationResult."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate_size(grid)

        # Then
        assert isinstance(result, ValidationResult)

    def test_grid_none_failure_is_not_success_flag(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — size failure is not a pass signal."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate_size(grid)

        # Then
        assert result.is_valid is False

    def test_grid_none_failure_has_code_and_message_fields(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — failure exposes code and message."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate_size(grid)

        # Then
        assert hasattr(result, "code")
        assert hasattr(result, "message")
        assert result.code == INVALID_SIZE_CODE
        assert result.message == INVALID_SIZE_MESSAGE


class TestBoundaryValueInputs:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — boundary value size rejection."""

    def test_grid_empty_returns_invalid_size_code(
        self, grid_empty: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — empty list rejected."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_empty)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_grid_four_empty_rows_returns_invalid_size_code(
        self, grid_four_empty_rows: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — four empty rows rejected."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_four_empty_rows)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_grid_three_by_four_returns_invalid_size_code(
        self, grid_three_by_four: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — 3×4 matrix rejected."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_three_by_four)

        # Then
        assert result.code == INVALID_SIZE_CODE

    def test_grid_four_by_three_returns_invalid_size_message(
        self, grid_four_by_three: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — 4×3 matrix returns PRD message."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_four_by_three)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE

    def test_grid_five_by_five_returns_invalid_size_contract(
        self, grid_five_by_five: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — 5×5 matrix returns full contract."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_five_by_five)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert result.message == INVALID_SIZE_MESSAGE


class TestMessageExactMatch:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — character-level message identity."""

    def test_grid_none_message_exact_prd_wording(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — message matches PRD verbatim."""
        # Given
        validator = BoundaryValidator()
        expected = "Grid must be 4x4."

        # When
        result = validator.validate_size(None)

        # Then
        assert result.message == expected

    def test_grid_empty_message_exact_prd_wording(
        self, grid_empty: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — empty grid message is verbatim."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_empty)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE

    def test_grid_none_code_exact_invalid_size_literal(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — code is exact INVALID_SIZE string."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(None)

        # Then
        assert result.code == "INVALID_SIZE"

    def test_grid_none_message_length_matches_prd_spec(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — message length is fixed."""
        # Given
        validator = BoundaryValidator()
        prd_message = "Grid must be 4x4."

        # When
        result = validator.validate_size(None)

        # Then
        assert len(result.message) == len(prd_message)

    def test_grid_three_by_four_message_ends_with_period(
        self, grid_three_by_four: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — message ends with period."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_three_by_four)

        # Then
        assert result.message.endswith(".")
        assert result.message == INVALID_SIZE_MESSAGE


class TestScopeExclusion:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — AC-FR-01-02~05 / FR-02~05 out of scope."""

    def test_boundary_validator_exposes_validate_size_only(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — no blank-count API on validator."""
        # Given
        forbidden_methods = (
            "validate_blank_count",
            "validate_value_range",
            "validate_duplicates",
            "resolve",
        )

        # When
        public_methods = {
            name
            for name, _ in inspect.getmembers(BoundaryValidator, predicate=inspect.isfunction)
            if not name.startswith("_")
        }

        # Then
        for method_name in forbidden_methods:
            assert method_name not in public_methods

    def test_size_fail_does_not_return_blank_count_error_code(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — not a blank-count failure code."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(None)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert result.code != "INVALID_BLANK_COUNT"
        assert result.code != "E-BND-002"

    def test_size_fail_does_not_return_duplicate_error_code(
        self, grid_three_by_four: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — not a duplicate-value failure."""
        # Given
        validator = BoundaryValidator()

        # When
        result = validator.validate_size(grid_three_by_four)

        # Then
        assert result.code != "INVALID_DUPLICATE"
        assert result.code != "E-BND-004"
