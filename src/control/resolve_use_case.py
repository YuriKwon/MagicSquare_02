"""Resolve use-case orchestration with Boundary size guard."""

from __future__ import annotations

from typing import Any, Protocol

from src.boundary.boundary_validator import BoundaryValidator
from src.boundary.validation_result import ValidationResult


class DomainResolver(Protocol):
    """Domain entry point for magic-square resolution."""

    def resolve(self, grid: Any) -> Any:
        """Resolve a valid 4x4 grid into a solution."""
        ...


class ResolveUseCase:
    """Orchestrate boundary validation before domain resolution."""

    def __init__(
        self,
        domain_resolver: DomainResolver,
        validator: BoundaryValidator | None = None,
    ) -> None:
        """Initialize the use case with a domain resolver dependency.

        Args:
            domain_resolver: Domain-layer resolver (mocked in tests).
            validator: Optional boundary validator (defaults to new instance).
        """
        self._domain_resolver = domain_resolver
        self._validator = validator or BoundaryValidator()

    def execute(self, grid: Any) -> ValidationResult | Any:
        """Run size validation; delegate to domain only when shape is valid.

        Args:
            grid: Input matrix from the boundary.

        Returns:
            ValidationResult on size failure, otherwise domain resolver output.
        """
        size_result = self._validator.validate_size(grid)
        if not size_result.is_valid:
            return size_result
        return self._domain_resolver.resolve(grid)
