"""Data contract owned by Validator.

Per 02_ARCHITECTURE.md, Section 15, Step 1.1 and
04_RENDERING_SPECIFICATION.md, Section 4:

    Validator
        Input:  raw rendering request
        Output: ValidatedPayload (immutable)
        Raises: ValidationError
        Depends on no other subsystem.

This module currently defines only the ValidatedPayload data contract
(Phase 1 -- Immutable Data Contracts). The Validator class itself,
which performs the actual validation logic and raises
ValidationError, is implemented in Phase 2 (Pre-Render Pipeline
Stages) per the incremental implementation plan.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping


@dataclass(frozen=True)
class ValidatedPayload:
    """Immutable output of Validator.

    Contains data only -- no validation or rendering logic. The exact
    field schema of a validated rendering request is an implementation
    detail left open by the frozen specification; ``data`` holds the
    validated request fields as an immutable mapping, which is the
    smallest structure sufficient to satisfy the contract.
    """

    data: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "data", MappingProxyType(dict(self.data)))
