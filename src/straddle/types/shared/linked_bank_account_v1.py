# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .status_detail_of_linked_bank_account_status_detail_enum import StatusDetailOfLinkedBankAccountStatusDetailEnum

__all__ = ["LinkedBankAccountV1", "BankAccount"]


class BankAccount(BaseModel):
    account_holder: str

    account_mask: str

    institution_name: str

    routing_number: str


class LinkedBankAccountV1(BaseModel):
    id: str
    """Unique identifier for the linked bank account."""

    account_id: str
    """The unique identifier of the Straddle account related to this bank account."""

    bank_account: BankAccount

    created_at: datetime
    """Timestamp of when the bank account object was created."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """The current status of the linked bank account."""

    status_detail: StatusDetailOfLinkedBankAccountStatusDetailEnum

    updated_at: datetime
    """Timestamp of the most recent update to the linked bank account."""

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the linked bank account in a
    structured format.
    """
