# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LinkedBankAccountUnmask", "Data", "DataBankAccount", "DataStatusDetail", "Meta"]


class DataBankAccount(BaseModel):
    account_holder: str

    account_number: str

    institution_name: str

    routing_number: str


class DataStatusDetail(BaseModel):
    code: str

    message: str

    reason: Literal["unverified", "new", "in_review", "pending", "stuck", "verified", "failed_verification", "disabled"]

    source: Literal["watchtower"]


class Data(BaseModel):
    id: str

    account_id: str

    bank_account: DataBankAccount

    created_at: datetime

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]

    status_detail: DataStatusDetail

    updated_at: datetime

    metadata: Optional[Dict[str, Optional[str]]] = None


class Meta(BaseModel):
    api_request_id: str
    """Unique identifier for this API request, useful for troubleshooting."""

    api_request_timestamp: datetime
    """Timestamp for this API request, useful for troubleshooting."""


class LinkedBankAccountUnmask(BaseModel):
    data: Data

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the type of data returned."""
