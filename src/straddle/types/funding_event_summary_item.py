# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FundingEventSummaryItem", "Data", "Meta"]


class Data(BaseModel):
    id: str
    """Id."""

    amount: int
    """Amount."""

    direction: Literal["deposit", "withdrawal"]

    event_type: Literal["charge_deposit", "charge_reversal", "payout_return", "payout_withdrawal"]

    payment_count: int
    """Payment count."""

    trace_numbers: List[str]
    """Trace number."""

    transfer_date: date
    """Transfer date."""


class Meta(BaseModel):
    api_request_id: str
    """Unique identifier for this API request, useful for troubleshooting."""

    api_request_timestamp: datetime
    """Timestamp for this API request, useful for troubleshooting."""


class FundingEventSummaryItem(BaseModel):
    data: Data

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
