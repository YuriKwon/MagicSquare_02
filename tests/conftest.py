"""Shared pytest fixtures and constants for MagicSquare tests."""

from __future__ import annotations

from typing import Any

import pytest

# Dual-Track RED grid placeholders (G0~G3) — Report/09 / Report/02
# G0: [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]  — complete valid (M=34)
# G1: [[16,3,2,13],[5,0,11,8],[9,6,0,12],[4,15,14,1]]   — blanks (2,2),(3,3)
# G2: PLACEHOLDER — Report/02 TBD (Step A fail, Step B success)
# G3: PLACEHOLDER — Report/02 TBD (Step A and B both fail)

# PRD §8.1 / AC-FR-01-01 failure contract
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."

# Dual-Track RED failure envelope (Report/09 §2.4)
E003_CODE = "E003"
E003_MESSAGE = "Input matrix must not be null."
E001_CODE = "E001"
E001_MESSAGE = "Grid must be 4x4."
E002_CODE = "E002"
E002_MESSAGE = "Exactly two blank cells (value 0) are required."


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


@pytest.fixture
def grid_g0() -> list[list[int]]:
    """G0 — complete valid magic square (zero blanks)."""
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1 — two blanks at (2,2) and (3,3); missing {7, 10}."""
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_g1_three_blanks(grid_g1: list[list[int]]) -> list[list[int]]:
    """G1 with (1,1)=0 — three blank cells."""
    matrix = [row[:] for row in grid_g1]
    matrix[0][0] = 0
    return matrix
