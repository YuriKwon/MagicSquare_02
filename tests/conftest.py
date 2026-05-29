"""Shared pytest fixtures and constants for MagicSquare tests."""

from __future__ import annotations

from typing import Any

import pytest

# PRD §8.1 / AC-FR-01-01 failure contract
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."


@pytest.fixture
def grid_none() -> None:
    """Explicit None grid input."""
    return None


@pytest.fixture
def grid_empty() -> list[list[int]]:
    """Empty list — zero rows."""
    return []


@pytest.fixture
def grid_four_empty_rows() -> list[list[int]]:
    """Four rows with zero columns each."""
    return [[]] * 4


@pytest.fixture
def grid_three_by_four() -> list[list[int]]:
    """3 rows × 4 columns — row count mismatch."""
    return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


@pytest.fixture
def grid_four_by_three() -> list[list[int]]:
    """4 rows × 3 columns — column count mismatch."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


@pytest.fixture
def grid_five_by_five() -> list[list[int]]:
    """5 rows × 5 columns — both dimensions mismatch."""
    return [[1, 2, 3, 4, 5] for _ in range(5)]


@pytest.fixture(params=["grid_none", "grid_empty", "grid_four_empty_rows", "grid_three_by_four"])
def size_fail_grid(request: pytest.FixtureRequest) -> Any:
    """Parametrized invalid-size grids for isolation tests."""
    return request.getfixturevalue(request.param)
