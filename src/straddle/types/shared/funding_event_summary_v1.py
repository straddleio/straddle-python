# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel
from .funding_event_type_v1 import FundingEventTypeV1
from .transfer_direction_v1 import TransferDirectionV1

__all__ = ["FundingEventSummaryV1"]


class FundingEventSummaryV1(BaseModel):
    id: str
    """Unique identifier for the funding event."""

    amount: int
    """The amount of the funding event in cents."""

    direction: TransferDirectionV1
    """
    Describes the direction of the funding event from the perspective of the
    `linked_bank_account`.
    """

    event_type: FundingEventTypeV1
    """
    The funding event types describes the direction and reason for the funding
    event.
    """

    payment_count: int
    """The number of payments associated with the funding event."""

    trace_numbers: List[str]
    """Trace number."""

    transfer_date: date
    """The date on which the funding event occurred.

    For `deposits` and `returns`, this is the date the funds were credited to your
    bank account. For `withdrawals` and `reversals`, this is the date the funds were
    debited from your bank account.
    """

    trace_number: Optional[str] = None
    """The trace number of the funding event."""
