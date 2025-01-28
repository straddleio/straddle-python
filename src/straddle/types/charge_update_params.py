# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChargeUpdateParams"]


class ChargeUpdateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount."""

    description: Required[str]
    """Description."""

    payment_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Payment date."""

    metadata: Optional[Dict[str, str]]
    """Metadata."""

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
