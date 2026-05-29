"""Boundary response schemas for input validation."""

from __future__ import annotations

from dataclasses import dataclass

RESPONSE_TYPE_ERROR = "ERROR"
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."


@dataclass(frozen=True)
class FailureResponse:
    """Failure envelope returned for invalid Boundary input.

    Attributes:
        type: Response category (ERROR for validation failures).
        code: Machine-readable failure code.
        message: Human-readable failure message aligned with PRD §8.1.
    """

    type: str
    code: str
    message: str
