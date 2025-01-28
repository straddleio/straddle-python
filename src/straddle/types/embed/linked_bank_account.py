# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LinkedBankAccount", "Data", "DataBankAccount", "DataStatusDetail", "Meta"]


class DataBankAccount(BaseModel):
    account_holder: str

    account_mask: str

    institution_name: str

    routing_number: str


class DataStatusDetail(BaseModel):
    code: str

    message: str

    reason: Literal["unverified", "new", "in_review", "pending", "stuck", "verified", "failed_verification", "disabled"]

    source: Literal["watchtower"]


class Data(BaseModel):
    id: str
    """Unique identifier for the linked bank account."""

    account_id: str
    """The unique identifier of the Straddle account relatd to this bank account."""

    bank_account: DataBankAccount

    created_at: datetime
    """Timestamp of when the bank account object was created."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """The current status of the linked bank account.

    Possible values: 'created', 'onboarding', 'active', 'inactive', 'rejected'.
    """

    status_detail: DataStatusDetail

    updated_at: datetime
    """Timestamp of the most recent update to the linked bank account."""

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the linked bank account in a
    structured format.
    """


class Meta(BaseModel):
    api_request_id: str
    """Unique identifier for this API request, useful for troubleshooting."""

    api_request_timestamp: datetime
    """Timestamp for this API request, useful for troubleshooting."""


class LinkedBankAccount(BaseModel):
    data: Data

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the type of data returned."""
