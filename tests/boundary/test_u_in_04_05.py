"""Track A — U-IN-04~05: value range and duplicate validation (RED skeleton)."""

from __future__ import annotations

import pytest


class TestUIn04ValueRange:
    """U-IN-04; FR-01 value range; AC-FR-01-03."""

    def test_u_in_04_g1_cell_out_of_range_returns_e004(self) -> None:
        """U-IN-04 — G1 with (4,4)=-1 rejects out-of-range values with E004."""
        # Given
        # validator = InputValidator()
        # matrix = copy of G1 with matrix[3][3] = -1

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-04 — G1+(4,4)=-1 returns E004 value range envelope")


class TestUIn05Duplicate:
    """U-IN-05; FR-01 duplicate check; AC-FR-01-04."""

    def test_u_in_05_g1_duplicate_sixteen_returns_e005(self) -> None:
        """U-IN-05 — G1 with (4,4)=16 rejects non-zero duplicate with E005."""
        # Given
        # validator = InputValidator()
        # matrix = copy of G1 with matrix[3][3] = 16  # duplicate 16

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-05 — G1+(4,4)=16 returns E005 duplicate envelope")
