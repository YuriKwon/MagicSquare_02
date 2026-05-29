"""Track B — D-SOL-01~04: solution orchestration (RED skeleton)."""

from __future__ import annotations

import pytest

from control.solution import solution


class TestDSol01StepASuccess:
    """D-SOL-01; I8 Step A happy path on G1."""

    def test_d_sol_01_solution_step_a_success_on_g1_returns_six_tuple(self) -> None:
        """D-SOL-01 — G1 solution returns [2,2,7,3,3,10]."""
        # Given
        # matrix = G1

        # When
        # result = solution(matrix)

        # Then
        pytest.fail("RED: D-SOL-01 — G1 Step A returns six-tuple [2,2,7,3,3,10]")


class TestDSol02StepBSuccess:
    """D-SOL-02; I9 Step B after Step A fails on G2 (TBD)."""

    def test_d_sol_02_solution_step_b_success_after_step_a_fails_on_g2(self) -> None:
        """D-SOL-02 — G2 PLACEHOLDER: Step B returns int[6]."""
        # Given
        # matrix = G2  # PLACEHOLDER — Report/02 TBD

        # When
        # result = solution(matrix)

        # Then
        pytest.fail("RED: D-SOL-02 — G2 TBD")


class TestDSol03Unsolvable:
    """D-SOL-03; I10 both steps fail on G3 (TBD)."""

    def test_d_sol_03_solution_raises_unsolvable_when_both_steps_fail_on_g3(
        self,
    ) -> None:
        """D-SOL-03 — G3 PLACEHOLDER: raises UnsolvableDomainError."""
        # Given
        # matrix = G3  # PLACEHOLDER — Report/02 TBD

        # When / Then
        pytest.fail("RED: D-SOL-03 — G3 TBD raises UnsolvableDomainError")


class TestDSol04TupleContract:
    """D-SOL-04; I8 output length and 1-index coordinate contract on G1."""

    def test_d_sol_04_solution_success_tuple_enforces_length_and_1_index_coords(
        self,
    ) -> None:
        """D-SOL-04 — G1 solution len=6 and coords in [1,4]."""
        # Given
        # matrix = G1

        # When
        # result = solution(matrix)

        # Then
        pytest.fail("RED: D-SOL-04 — G1 solution len=6 with 1-index coords in 1..4")
