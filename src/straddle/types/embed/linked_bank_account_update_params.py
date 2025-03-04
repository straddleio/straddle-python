# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.bank_account_v1_request import BankAccountV1Request

__all__ = ["LinkedBankAccountUpdateParams"]


class LinkedBankAccountUpdateParams(TypedDict, total=False):
    bank_account: Required[BankAccountV1Request]

    metadata: Optional[Dict[str, Optional[str]]]
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the linked bank account in a
    structured format.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]
