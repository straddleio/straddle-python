# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutCreateParams", "Device"]


class PayoutCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount."""

    currency: Required[str]
    """Currency."""

    description: Required[str]
    """Description."""

    device: Required[Device]

    external_id: Required[str]
    """External id."""

    paykey: Required[str]
    """Paykey."""

    payment_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Payment date."""

    config: object

    metadata: Optional[Dict[str, str]]
    """Metadata."""

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]


class Device(TypedDict, total=False):
    ip_address: Required[str]
    """Ip address."""
