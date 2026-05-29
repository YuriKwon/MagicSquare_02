"""Control orchestration tests for AC-FR-01-01 domain-entry isolation.

AC-FR-01-01; PRD §8.1 INVALID_SIZE — resolve() must not run on size-invalid input.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.control.resolve_use_case import ResolveUseCase
from tests.conftest import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE


class TestDomainEntryIsolation:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — resolve() call-count guard."""

    def test_grid_none_resolve_call_count_zero(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — None grid blocks resolve()."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)
        grid = None

        # When
        result = use_case.execute(grid)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert domain_resolver.resolve.call_count == 0

    def test_grid_none_resolve_assert_not_called(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — resolve() assert_not_called."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(None)

        # Then
        domain_resolver.resolve.assert_not_called()

    def test_grid_empty_resolve_call_count_zero(
        self, grid_empty: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — empty grid blocks resolve()."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        result = use_case.execute(grid_empty)

        # Then
        assert result.message == INVALID_SIZE_MESSAGE
        assert domain_resolver.resolve.call_count == 0

    def test_grid_four_empty_rows_resolve_call_count_zero(
        self, grid_four_empty_rows: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — four empty rows block resolve()."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(grid_four_empty_rows)

        # Then
        assert domain_resolver.resolve.call_count == 0

    def test_grid_three_by_four_resolve_call_count_zero(
        self, grid_three_by_four: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — 3×4 grid blocks resolve()."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(grid_three_by_four)

        # Then
        domain_resolver.resolve.assert_not_called()
        assert domain_resolver.resolve.call_count == 0


class TestIsolationFailureContract:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — isolation path still returns failure."""

    def test_grid_none_returns_invalid_size_before_resolve(
        self,
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — failure returned without resolve."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        result = use_case.execute(None)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert result.message == INVALID_SIZE_MESSAGE
        domain_resolver.resolve.assert_not_called()

    @pytest.mark.parametrize(
        "fixture_name",
        ["grid_none", "grid_empty", "grid_four_empty_rows", "grid_three_by_four"],
    )
    def test_size_fail_grids_resolve_never_invoked(
        self, request: pytest.FixtureRequest, fixture_name: str
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — parametrized isolation guard."""
        # Given
        grid = request.getfixturevalue(fixture_name)
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(grid)

        # Then
        assert domain_resolver.resolve.call_count == 0

    def test_resolve_mock_failure_when_called_on_none_grid(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — resolve must not be reachable."""
        # Given
        domain_resolver = MagicMock()
        domain_resolver.resolve.side_effect = AssertionError(
            "resolve() must not be called for size-invalid grid"
        )
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        result = use_case.execute(None)

        # Then
        assert result.code == INVALID_SIZE_CODE
        domain_resolver.resolve.assert_not_called()

    def test_grid_none_domain_resolver_never_receives_grid_argument(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — resolve receives no grid on None."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(None)

        # Then
        domain_resolver.resolve.assert_not_called()
        assert domain_resolver.resolve.call_args_list == []

    def test_grid_empty_short_circuits_without_domain_side_effects(
        self, grid_empty: list[list[int]]
    ) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — empty list has zero domain calls."""
        # Given
        domain_resolver = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        result = use_case.execute(grid_empty)

        # Then
        assert result.code == INVALID_SIZE_CODE
        assert domain_resolver.resolve.call_count == 0


class TestIsolationScopeExclusion:
    """AC-FR-01-01; PRD §8.1 INVALID_SIZE — guard tests exclude FR-02~05 paths."""

    def test_execute_does_not_invoke_blank_finder_on_none(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — BlankFinder not invoked (FR-02)."""
        # Given
        domain_resolver = MagicMock()
        domain_resolver.find_blanks = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(None)

        # Then
        assert not hasattr(domain_resolver, "find_blanks") or (
            domain_resolver.find_blanks.call_count == 0
        )

    def test_execute_does_not_invoke_missing_number_finder_on_none(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — MissingNumberFinder not invoked (FR-03)."""
        # Given
        domain_resolver = MagicMock()
        domain_resolver.find_missing_numbers = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(None)

        # Then
        assert domain_resolver.find_missing_numbers.call_count == 0

    def test_execute_does_not_invoke_magic_validator_on_none(self) -> None:
        """AC-FR-01-01; PRD §8.1 INVALID_SIZE — MagicSquareValidator not invoked (FR-04)."""
        # Given
        domain_resolver = MagicMock()
        domain_resolver.validate_magic_square = MagicMock()
        use_case = ResolveUseCase(domain_resolver=domain_resolver)

        # When
        use_case.execute(None)

        # Then
        assert domain_resolver.validate_magic_square.call_count == 0
