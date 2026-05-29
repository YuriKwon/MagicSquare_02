"""Track A — U-IN-06~08: validation success and short-circuit order (RED skeleton)."""

from __future__ import annotations

import pytest


class TestUIn06ValidationSuccess:
    """U-IN-06; FR-01 pass path on valid partial grid G1."""

    def test_u_in_06_valid_g1_returns_ok_true(self) -> None:
        """U-IN-06 — G1 passes all FR-01 checks and returns ok=true envelope."""
        # Given
        # validator = InputValidator()
        # matrix = G1

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-06 — valid G1 returns ok=true success envelope")


class TestUIn07ShortCircuitNull:
    """U-IN-07; FR-01 short-circuit: null before blank count."""

    def test_u_in_07_null_short_circuits_before_blank_count(self) -> None:
        """U-IN-07 — matrix=null yields E003 without reaching blank-count check."""
        # Given
        # validator = InputValidator()
        # matrix = None

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-07 — null input short-circuits to E003 only")


class TestUIn08ShortCircuitSize:
    """U-IN-08; FR-01 short-circuit: size before blank count."""

    def test_u_in_08_size_fail_short_circuits_before_blank_count(self) -> None:
        """U-IN-08 — non-4x4 matrix yields E001 without reaching blank-count check."""
        # Given
        # validator = InputValidator()
        # matrix = []  # or 3x4 / 4x3 / 5x5

        # When
        # result = validator.validate(matrix)

        # Then
        pytest.fail("RED: U-IN-08 — size invalid short-circuits to E001 only")
