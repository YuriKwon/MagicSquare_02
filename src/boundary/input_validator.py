"""FR-01 unified input validation at the Boundary layer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.boundary.schemas import (
    FailureResponse,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    RESPONSE_TYPE_ERROR,
)


@dataclass(frozen=True)
class ValidationError:
    """Machine-readable failure payload for invalid input."""

    code: str
    message: str


@dataclass(frozen=True)
class ValidationEnvelope:
    """Boundary response contract for input validation."""

    ok: bool
    error: ValidationError | None = None


class InputValidator:
    """Validate FR-01 input rules through a single entry point."""

    def validate(
        self, matrix: Any
    ) -> FailureResponse | ValidationEnvelope:
        """Validate matrix against FR-01 short-circuit rules.

        Args:
            matrix: Candidate 4x4 input grid.

        Returns:
            FailureResponse on size-null failure; ValidationEnvelope otherwise.
        """
        if matrix is None:
            return FailureResponse(
                type=RESPONSE_TYPE_ERROR,
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        return ValidationEnvelope(ok=True, error=None)
