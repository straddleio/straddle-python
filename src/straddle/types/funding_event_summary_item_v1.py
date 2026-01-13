# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.response_metadata import ResponseMetadata

__all__ = ["FundingEventSummaryItemV1", "Data", "DataStatusDetails"]


class DataStatusDetails(BaseModel):
    changed_at: datetime
    """The time the status change occurred."""

    message: str
    """A human-readable description of the current status."""

    reason: Literal[
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
        "InsufficientFunds",
        "ClosedBankAccount",
        "InvalidBankAccount",
        "InvalidRouting",
        "Disputed",
        "PaymentStopped",
        "OwnerDeceased",
        "FrozenBankAccount",
        "RiskReview",
        "Fraudulent",
        "DuplicateEntry",
        "InvalidPaykey",
        "PaymentBlocked",
        "AmountTooLarge",
        "TooManyAttempts",
        "InternalSystemError",
        "UserRequest",
        "Ok",
        "OtherNetworkReturn",
        "PayoutRefused",
    ]

    source: Literal[
        "watchtower",
        "bank_decline",
        "customer_dispute",
        "user_action",
        "system",
        "Watchtower",
        "BankDecline",
        "CustomerDispute",
        "UserAction",
        "System",
    ]

    code: Optional[str] = None
    """The status code if applicable."""


class Data(BaseModel):
    id: str
    """Unique identifier for the funding event."""

    amount: int
    """The amount of the funding event in cents."""

    created_at: datetime
    """Created at."""

    direction: Literal["deposit", "withdrawal"]
    """
    Describes the direction of the funding event from the perspective of the
    `linked_bank_account`.
    """

    event_type: Literal[
        "charge_deposit",
        "charge_reversal",
        "payout_return",
        "payout_withdrawal",
        "ChargeDeposit",
        "ChargeReversal",
        "PayoutReturn",
        "PayoutWithdrawal",
    ]
    """
    The funding event types describes the direction and reason for the funding
    event.
    """

    payment_count: int
    """The number of payments associated with the funding event."""

    trace_ids: Dict[str, str]
    """Trace Ids."""

    trace_numbers: List[str]
    """Trace number."""

    transfer_date: date
    """The date on which the funding event occurred.

    For `deposits` and `returns`, this is the date the funds were credited to your
    bank account. For `withdrawals` and `reversals`, this is the date the funds were
    debited from your bank account.
    """

    updated_at: datetime
    """Updated at."""

    status: Optional[
        Literal[
            "created",
            "scheduled",
            "failed",
            "cancelled",
            "on_hold",
            "pending",
            "paid",
            "reversed",
            "Created",
            "Scheduled",
            "Failed",
            "Cancelled",
            "OnHold",
            "Pending",
            "Paid",
            "Reversed",
        ]
    ] = None
    """The current status of the `charge` or `payout`."""

    status_details: Optional[DataStatusDetails] = None

    trace_number: Optional[str] = None
    """The trace number of the funding event."""


class FundingEventSummaryItemV1(BaseModel):
    data: Data

    meta: ResponseMetadata
    """Metadata about the API request, including an identifier and timestamp."""

    response_type: Literal["object", "array", "error", "none", "Object", "Array", "Error", "None"]
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
