# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FundingEventSummaryPaged", "Data", "Meta"]


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

    max_page_size: int
    """Maximum allowed page size for this endpoint."""

    page_number: int
    """Page number for paginated results."""

    page_size: int
    """Number of items per page in this response."""

    sort_by: str
    """The field that the results were sorted by."""

    sort_order: Literal["asc", "desc"]

    total_items: int

    total_pages: int
    """The number of pages available."""


class FundingEventSummaryPaged(BaseModel):
    data: List[Data]

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
