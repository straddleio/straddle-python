# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaykeyListParams"]


class PaykeyListParams(TypedDict, total=False):
    customer_id: str
    """Filter paykeys by related customer ID."""

    page_number: int
    """Page number for paginated results. Starts at 1."""

    page_size: int
    """Number of results per page. Maximum: 1000."""

    sort_by: Literal["institution_name", "expires_at", "created_at"]

    sort_order: Literal["asc", "desc"]

    source: List[Literal["bank_account", "straddle", "mx", "plaid", "tan", "quiltt"]]
    """Filter paykeys by their source."""

    status: List[Literal["pending", "active", "inactive", "rejected", "review", "blocked"]]
    """Filter paykeys by their current status."""

    unblock_eligible: bool
    """Filter paykeys by unblock eligibility.

    When true, returns only blocked paykeys eligible for client-initiated unblocking
    (blocked due to R29 returns and not previously unblocked). When false, returns
    only blocked paykeys that are not eligible for unblocking.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
