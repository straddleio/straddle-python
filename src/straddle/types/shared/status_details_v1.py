# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .status_reason_v1 import StatusReasonV1
from .status_source_v1 import StatusSourceV1

__all__ = ["StatusDetailsV1"]


class StatusDetailsV1(BaseModel):
    changed_at: datetime
    """The time the status change occurred."""

    message: str
    """A human-readable description of the current status."""

    reason: StatusReasonV1
    """
    A machine-readable identifier for the specific status, useful for programmatic
    handling.
    """

    source: StatusSourceV1
    """Identifies the origin of the status change (e.g., `bank_decline`, `watchtower`).

    This helps in tracking the cause of status updates.
    """

    code: Optional[str] = None
    """The status code if applicable."""
