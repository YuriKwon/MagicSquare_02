"""Track B — D-MIS-01: missing number finder (RED skeleton)."""

from __future__ import annotations

import pytest

from entity.services.missing_number_finder import find_not_exist_nums


class TestDMis01MissingNumbers:
    """D-MIS-01; I7, I11 missing numbers sorted ascending on G1."""

    def test_d_mis_01_find_not_exist_nums_on_g1_sorted_ascending(self) -> None:
        """D-MIS-01 — G1 yields missing numbers [7, 10] in ascending order."""
        # Given
        # matrix = G1

        # When
        # missing = find_not_exist_nums(matrix)

        # Then
        pytest.fail("RED: D-MIS-01 — G1 missing numbers [7,10] ascending")
