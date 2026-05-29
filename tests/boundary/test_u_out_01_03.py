"""Track A — U-OUT-01~03: solve success output contract (RED skeleton)."""

from __future__ import annotations

import pytest


class TestUOut01PayloadLength:
    """U-OUT-01; FR-05 output length; AC-FR-05, I8."""

    def test_u_out_01_solve_success_payload_length_is_six(self) -> None:
        """U-OUT-01 — G1 solve returns ok=true with len(result)==6."""
        # Given
        # boundary = UIBoundary()
        # matrix = G1

        # When
        # response = boundary.solve(matrix)

        # Then
        pytest.fail("RED: U-OUT-01 — solve success payload length is six")


class TestUOut02OneIndexedCoords:
    """U-OUT-02; FR-05 1-index coordinates; AC-FR-05, I8."""

    def test_u_out_02_solve_success_coordinates_are_1_indexed_in_1_to_4(self) -> None:
        """U-OUT-02 — G1 solve returns r,c coordinates in [1,4] (1-index)."""
        # Given
        # boundary = UIBoundary()
        # matrix = G1

        # When
        # response = boundary.solve(matrix)

        # Then
        pytest.fail("RED: U-OUT-02 — success coordinates are 1-indexed in 1..4")


class TestUOut03ExpectedTuple:
    """U-OUT-03; FR-05 exact success tuple on G1; AC-FR-05, I8."""

    def test_u_out_03_solve_success_returns_expected_six_tuple_on_g1(self) -> None:
        """U-OUT-03 — G1 solve returns [2,2,7,3,3,10]."""
        # Given
        # boundary = UIBoundary()
        # matrix = G1

        # When
        # response = boundary.solve(matrix)

        # Then
        pytest.fail("RED: U-OUT-03 — G1 solve returns [2,2,7,3,3,10]")
