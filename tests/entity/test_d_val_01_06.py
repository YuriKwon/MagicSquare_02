"""Track B — D-VAL-01~06: magic square validator (RED skeleton)."""

from __future__ import annotations

import pytest

from entity.services.magic_validator import is_magic_square


class TestDVal01Baseline:
    """D-VAL-01; I1~I5 baseline valid complete grid G0."""

    def test_d_val_01_is_magic_square_true_on_g0(self) -> None:
        """D-VAL-01 — G0 complete grid returns True."""
        # Given
        # matrix = G0

        # When
        # result = is_magic_square(matrix)

        # Then
        pytest.fail("RED: D-VAL-01 — G0 is_magic_square returns True")


class TestDVal02RowSum:
    """D-VAL-02; I1 row sum mismatch."""

    def test_d_val_02_is_magic_square_false_when_row_sum_mismatch(self) -> None:
        """D-VAL-02 — G0 with broken row sum returns False."""
        # Given
        # matrix = copy of G0 with one row sum != M(34)

        # When
        # result = is_magic_square(matrix)

        # Then
        pytest.fail("RED: D-VAL-02 — row sum mismatch returns False")


class TestDVal03ColSum:
    """D-VAL-03; I2 column sum mismatch."""

    def test_d_val_03_is_magic_square_false_when_col_sum_mismatch(self) -> None:
        """D-VAL-03 — G0 with broken column sum returns False."""
        # Given
        # matrix = copy of G0 with one column sum != M(34)

        # When
        # result = is_magic_square(matrix)

        # Then
        pytest.fail("RED: D-VAL-03 — column sum mismatch returns False")


class TestDVal04DiagonalSum:
    """D-VAL-04; I3 diagonal sum mismatch."""

    def test_d_val_04_is_magic_square_false_when_diagonal_sum_mismatch(self) -> None:
        """D-VAL-04 — G0 with broken diagonal sum returns False."""
        # Given
        # matrix = copy of G0 with diagonal sum != M(34)

        # When
        # result = is_magic_square(matrix)

        # Then
        pytest.fail("RED: D-VAL-04 — diagonal sum mismatch returns False")


class TestDVal05DuplicateOrRange:
    """D-VAL-05; I4, I5 duplicate or out-of-range in filled grid."""

    def test_d_val_05_is_magic_square_false_when_duplicate_or_out_of_1_to_16(
        self,
    ) -> None:
        """D-VAL-05 — G0 with duplicate non-zero value returns False."""
        # Given
        # matrix = copy of G0 with duplicate values

        # When
        # result = is_magic_square(matrix)

        # Then
        pytest.fail("RED: D-VAL-05 — duplicate/out-of-range returns False")


class TestDVal06ZeroInFilledGrid:
    """D-VAL-06; I4 zero not allowed in complete grid."""

    def test_d_val_06_is_magic_square_false_when_zero_in_filled_grid(self) -> None:
        """D-VAL-06 — G0 with a zero cell returns False."""
        # Given
        # matrix = copy of G0 with one cell set to 0

        # When
        # result = is_magic_square(matrix)

        # Then
        pytest.fail("RED: D-VAL-06 — zero in filled grid returns False")
