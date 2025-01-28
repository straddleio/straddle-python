# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FundingEventListParams"]


class FundingEventListParams(TypedDict, total=False):
    created_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Created from."""

    created_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Created to."""

    direction: Literal["deposit", "withdrawal"]

    event_type: Literal["charge_deposit", "charge_reversal", "payout_return", "payout_withdrawal"]

    page_number: int
    """Results page number. Starts at page 1. Default value: 1"""

    page_size: int
    """Results page size. Default value: 100. Max value: 1000"""

    sort_by: Literal["transfer_date", "id", "amount"]

    sort_order: Literal["asc", "desc"]

    trace_number: Optional[str]
    """Trace number."""

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
