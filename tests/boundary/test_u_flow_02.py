"""Track A — U-FLOW-02 (extended): invalid input must not invoke Domain execute."""

from __future__ import annotations

import pytest


class TestUFlow02DomainIsolation:
    """U-FLOW-02; invalid validation blocks SolvePartialMagicSquare.execute."""

    def test_u_flow_02_null_matrix_execute_not_called(self) -> None:
        """U-FLOW-02 — matrix=null returns E003; execute call_count==0."""
        # Given
        # boundary = UIBoundary()
        # matrix = None
        # spy: patch SolvePartialMagicSquare.execute and assert call_count==0

        # When
        # response = boundary.solve(matrix)

        # Then
        pytest.fail("RED: U-FLOW-02 — null matrix must not call execute")

    def test_u_flow_02_e001_size_invalid_execute_not_called(self) -> None:
        """U-FLOW-02 ext — non-4x4 returns E001; execute call_count==0."""
        # Given
        # boundary = UIBoundary()
        # matrix = []  # size invalid
        # spy: patch SolvePartialMagicSquare.execute and assert call_count==0

        # When
        # response = boundary.solve(matrix)

        # Then
        pytest.fail("RED: U-FLOW-02 ext — size invalid must not call execute")

    def test_u_flow_02_e002_blank_count_invalid_execute_not_called(self) -> None:
        """U-FLOW-02 ext — blank count != 2 returns E002; execute call_count==0."""
        # Given
        # boundary = UIBoundary()
        # matrix = G0  # zero blanks
        # spy: patch SolvePartialMagicSquare.execute and assert call_count==0

        # When
        # response = boundary.solve(matrix)

        # Then
        pytest.fail("RED: U-FLOW-02 ext — blank count invalid must not call execute")
