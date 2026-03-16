# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FundingEventListParams"]


class FundingEventListParams(TypedDict, total=False):
    created_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The start date of the range to filter by using the `YYYY-MM-DD` format."""

    created_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The end date of the range to filter by using the `YYYY-MM-DD` format."""

    direction: Literal["deposit", "withdrawal"]
    """
    Describes the direction of the funding event from the perspective of the
    `linked_bank_account`.
    """

    event_type: Literal["charge_deposit", "charge_reversal", "payout_return", "payout_withdrawal"]
    """
    The funding event types describes the direction and reason for the funding
    event.
    """

    page_number: int
    """Results page number. Starts at page 1."""

    page_size: int
    """Results page size. Max value: 1000"""

    search_text: Optional[str]
    """Search text."""

    sort_by: Literal["transfer_date", "id", "amount"]
    """The field to sort the results by."""

    sort_order: Literal["asc", "desc"]
    """The order in which to sort the results."""

    status: Optional[
        List[
            Literal[
                "created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed", "validating"
            ]
        ]
    ]
    """Funding Event status."""

    status_reason: Optional[
        List[
            Literal[
                "insufficient_funds",
                "closed_bank_account",
                "invalid_bank_account",
                "invalid_routing",
                "disputed",
                "payment_stopped",
                "owner_deceased",
                "frozen_bank_account",
                "risk_review",
                "fraudulent",
                "duplicate_entry",
                "invalid_paykey",
                "payment_blocked",
                "amount_too_large",
                "too_many_attempts",
                "internal_system_error",
                "user_request",
                "ok",
                "other_network_return",
                "payout_refused",
                "cancel_request",
                "failed_verification",
                "require_review",
                "blocked_by_system",
                "watchtower_review",
                "validating",
            ]
        ]
    ]
    """Reason for latest payment status change."""

    status_source: Optional[List[Literal["watchtower", "bank_decline", "customer_dispute", "user_action", "system"]]]
    """Source of latest payment status change."""

    trace_id: Optional[str]
    """Trace Id."""

    trace_number: Optional[str]
    """Trace number."""

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
