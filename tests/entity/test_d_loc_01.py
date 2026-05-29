"""Track B — D-LOC-01: blank coordinate finder (RED skeleton)."""

from __future__ import annotations

import pytest


class TestDLoc01BlankCoords:
    """D-LOC-01; I6 blank coords row-major 1-index on G1."""

    def test_d_loc_01_find_blank_coords_row_major_on_g1(self) -> None:
        """D-LOC-01 — G1 yields [(2,2),(3,3)] in row-major 1-index order."""
        # Given
        # matrix = G1

        # When
        # coords = find_blank_coords(matrix)

        # Then
        pytest.fail("RED: D-LOC-01 — G1 blank coords row-major [(2,2),(3,3)]")
