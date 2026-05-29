"""Validation result contract for Boundary layer responses."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationResult:
    """Represent the outcome of a boundary validation check.

    Attributes:
        code: Machine-readable result code (e.g. INVALID_SIZE).
        message: Human-readable explanation aligned with PRD §8.1.
        is_valid: True when the input passes the validated contract.
    """

    code: str
    message: str
    is_valid: bool
