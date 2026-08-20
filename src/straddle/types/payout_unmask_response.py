# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.paykey_details_v1 import PaykeyDetailsV1
from .shared.response_metadata import ResponseMetadata
from .shared.status_details_v1 import StatusDetailsV1
from .shared.customer_details_v1 import CustomerDetailsV1

__all__ = [
    "PayoutUnmaskResponse",
    "Data",
    "DataConfig",
    "DataDevice",
    "DataStatusHistory",
    "DataDocument",
    "DataRelatedPayment",
]


class DataConfig(BaseModel):
    auto_hold: Optional[bool] = None
    """Defines whether to automatically place this charge on hold after being created."""

    auto_hold_message: Optional[str] = None
    """The reason the payout is being automatically held on creation."""

    sandbox_outcome: Optional[
        Literal[
            "standard",
            "paid",
            "on_hold_daily_limit",
            "cancelled_for_fraud_risk",
            "cancelled_for_balance_check",
            "failed_insufficient_funds",
            "reversed_insufficient_funds",
            "failed_customer_dispute",
            "reversed_customer_dispute",
            "failed_closed_bank_account",
            "reversed_closed_bank_account",
            "failed_not_authorized",
            "reversed_not_authorized",
        ]
    ] = None
    """Payment will simulate processing if not Standard."""


class DataDevice(BaseModel):
    ip_address: str
    """Ip address."""


class DataStatusHistory(BaseModel):
    changed_at: datetime
    """The time the status change occurred."""

    message: str
    """A human-readable description of the status."""

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
        "validating",
        "auto_hold",
    ]
    """
    A machine-readable identifier for the specific status, useful for programmatic
    handling.
    """

    source: Literal["watchtower", "bank_decline", "customer_dispute", "user_action", "system"]
    """Identifies the origin of the status change (e.g., `bank_decline`, `watchtower`).

    This helps in tracking the cause of status updates.
    """

    status: Literal[
        "created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed", "validating"
    ]
    """The current status of the `charge` or `payout`."""

    code: Optional[str] = None
    """The status code if applicable."""


class DataDocument(BaseModel):
    document_id: str
    """Unique identifier for this document."""

    document_name: str
    """The file name of this document as uploaded."""

    document_size: int
    """The size of this document in bytes."""

    document_type: Literal["payment_authorization"]

    uploaded_at: datetime
    """The UTC timestamp when this document was uploaded."""


class DataRelatedPayment(BaseModel):
    id: str
    """The ID of the related payment."""

    payment_type: Literal["charge", "payout"]
    """The type of payment."""

    relationship: Literal["original", "resubmit", "refund"]


class Data(BaseModel):
    id: str
    """Id."""

    amount: int
    """Amount."""

    config: DataConfig

    currency: str
    """Currency."""

    description: Optional[str] = None
    """Description."""

    device: DataDevice

    external_id: str
    """External id."""

    funding_ids: List[str]
    """Funding Ids"""

    has_resubmit: bool
    """Has the payout been resubmitted."""

    is_refund: bool
    """Is the payout a refund of an original charge."""

    is_resubmit: bool
    """Is the payout a resubmit of an original payout."""

    paykey: str
    """Paykey."""

    payment_date: date
    """Payment date."""

    status: Literal[
        "created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed", "validating"
    ]
    """The current status of the `charge` or `payout`."""

    status_details: StatusDetailsV1

    status_history: List[DataStatusHistory]
    """Status history."""

    trace_ids: Dict[str, str]
    """Trace Ids."""

    created_at: Optional[datetime] = None
    """Created at."""

    customer_details: Optional[CustomerDetailsV1] = None
    """Information about the customer associated with the charge or payout."""

    documents: Optional[List[DataDocument]] = None
    """Documents uploaded for this payout (e.g.

    proof of authorization), in the order they were uploaded.
    """

    effective_at: Optional[datetime] = None
    """Effective at."""

    metadata: Optional[Dict[str, str]] = None
    """Metadata."""

    paykey_details: Optional[PaykeyDetailsV1] = None

    payment_rail: Optional[Literal["ach"]] = None
    """The payment rail used for the charge or payout."""

    processed_at: Optional[datetime] = None
    """Processed at."""

    related_payments: Optional[List[DataRelatedPayment]] = None
    """Related payments."""

    updated_at: Optional[datetime] = None
    """Updated at."""


class PayoutUnmaskResponse(BaseModel):
    data: Data

    meta: ResponseMetadata
    """Metadata about the API request, including an identifier and timestamp."""

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
