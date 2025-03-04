# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .status_reason_v1 import StatusReasonV1
from .status_source_v1 import StatusSourceV1
from .payment_status_v1 import PaymentStatusV1

__all__ = ["StatusHistoryV1"]


class StatusHistoryV1(BaseModel):
    changed_at: datetime
    """The time the status change occurred."""

    message: str
    """A human-readable description of the status."""

    reason: StatusReasonV1
    """
    A machine-readable identifier for the specific status, useful for programmatic
    handling.
    """

    source: StatusSourceV1
    """Identifies the origin of the status change (e.g., `bank_decline`, `watchtower`).

    This helps in tracking the cause of status updates.
    """

    status: PaymentStatusV1
    """The current status of the `charge` or `payout`."""

    code: Optional[str] = None
    """The status code if applicable."""
