# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Charge",
    "Data",
    "DataConfig",
    "DataDevice",
    "DataStatusDetails",
    "DataStatusHistory",
    "DataCustomerDetails",
    "DataPaykeyDetails",
    "Meta",
]


class DataConfig(BaseModel):
    balance_check: Literal["required", "enabled", "disabled"]


class DataDevice(BaseModel):
    ip_address: str
    """Ip address."""


class DataStatusDetails(BaseModel):
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
    ]

    source: Literal["watchtower", "bank_decline", "customer_dispute", "user_action", "system"]

    code: Optional[str] = None
    """The status code if applicable."""


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
    ]

    source: Literal["watchtower", "bank_decline", "customer_dispute", "user_action", "system"]

    status: Literal["created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"]

    code: Optional[str] = None
    """The status code if applicable."""


class DataCustomerDetails(BaseModel):
    id: str
    """Id."""

    customer_type: Literal["unknown", "individual", "business"]

    email: str
    """Email."""

    name: str
    """Name."""

    phone: str
    """Phone."""


class DataPaykeyDetails(BaseModel):
    id: str
    """Id."""

    customer_id: str
    """Customer id."""

    label: str
    """Label."""

    balance: Optional[int] = None
    """Balance."""


class Data(BaseModel):
    id: str
    """Id."""

    amount: int
    """Amount."""

    config: DataConfig

    consent_type: Literal["internet", "signed"]

    created_at: datetime
    """Created at."""

    currency: str
    """Currency."""

    description: str
    """Description."""

    device: DataDevice

    external_id: str
    """External id."""

    paykey: str
    """Paykey."""

    payment_date: date
    """Payment date."""

    status: Literal["created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"]

    status_details: DataStatusDetails

    status_history: List[DataStatusHistory]
    """Status history."""

    updated_at: datetime
    """Updated at."""

    customer_details: Optional[DataCustomerDetails] = None

    effective_at: Optional[datetime] = None
    """Effective at."""

    metadata: Optional[Dict[str, str]] = None
    """Metadata."""

    paykey_details: Optional[DataPaykeyDetails] = None

    payment_rail: Optional[Literal["ach"]] = None

    processed_at: Optional[datetime] = None
    """Processed at."""


class Meta(BaseModel):
    api_request_id: str
    """Unique identifier for this API request, useful for troubleshooting."""

    api_request_timestamp: datetime
    """Timestamp for this API request, useful for troubleshooting."""


class Charge(BaseModel):
    data: Data

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
