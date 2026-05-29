"""Boundary input validation for Magic Square 4x4."""

from __future__ import annotations

from typing import Any

from src.boundary.validation_result import ValidationResult

EXPECTED_GRID_DIMENSION = 4
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."


class BoundaryValidator:
    """Validate 4x4 grid shape at the Boundary layer (AC-FR-01-01)."""

    def validate_size(self, grid: Any) -> ValidationResult:
        """Return INVALID_SIZE when grid is not a 4x4 matrix.

        Args:
            grid: Candidate input matrix.

        Returns:
            ValidationResult with is_valid=True only for 4x4 shape.
        """
        if not _is_valid_size(grid):
            return ValidationResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
                is_valid=False,
            )
        return ValidationResult(
            code=INVALID_SIZE_CODE,
            message=INVALID_SIZE_MESSAGE,
            is_valid=True,
        )


def _is_valid_size(grid: Any) -> bool:
    """Check whether grid is a 4x4 list-of-lists."""
    if grid is None or not isinstance(grid, list):
        return False
    if len(grid) != EXPECTED_GRID_DIMENSION:
        return False
    for row in grid:
        if not isinstance(row, list) or len(row) != EXPECTED_GRID_DIMENSION:
            return False
    return True
