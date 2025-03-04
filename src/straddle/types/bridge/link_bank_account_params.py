# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.account_type_v1 import AccountTypeV1

__all__ = ["LinkBankAccountParams"]


class LinkBankAccountParams(TypedDict, total=False):
    account_number: Required[str]
    """The bank account number."""

    account_type: Required[AccountTypeV1]

    customer_id: Required[str]
    """Unique identifier of the related customer object."""

    routing_number: Required[str]
    """The routing number of the bank account."""

    metadata: Optional[Dict[str, str]]
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the paykey in a structured
    format.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
