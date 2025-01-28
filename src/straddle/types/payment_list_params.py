# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    customer_id: str
    """Customer id."""

    default_page_size: int

    default_sort: Literal["created_at", "payment_date", "effective_at", "id", "amount"]

    default_sort_order: Literal["asc", "desc"]

    external_id: str
    """External id."""

    funding_id: str
    """Funding id."""

    max_amount: int
    """Maximum amount."""

    max_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Maximum created at."""

    max_effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Maximum effective at."""

    max_payment_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Maximum payment date."""

    min_amount: int
    """Minimum amount."""

    min_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Minimum created at."""

    min_effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Minimum effective at."""

    min_payment_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Minimum payment date."""

    page_number: int
    """Results page number. Starts at page 1. Default value: 1"""

    page_size: int
    """Results page size. Default value: 100. Max value: 1000"""

    paykey: str
    """Paykey."""

    paykey_id: str
    """Paykey id."""

    payment_id: str
    """Payment id."""

    payment_status: List[
        Literal["created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"]
    ]
    """Payment status."""

    payment_type: List[Literal["charge", "payout"]]
    """Payment type."""

    search_text: str
    """Search text."""

    sort_by: Literal["created_at", "payment_date", "effective_at", "id", "amount"]

    sort_order: Literal["asc", "desc"]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
