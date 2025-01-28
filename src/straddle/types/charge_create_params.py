# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChargeCreateParams", "Config", "Device"]


class ChargeCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount."""

    config: Required[Config]

    consent_type: Required[Literal["internet", "signed"]]

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

    metadata: Optional[Dict[str, str]]
    """Metadata."""

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]


class Config(TypedDict, total=False):
    balance_check: Required[Literal["required", "enabled", "disabled"]]


class Device(TypedDict, total=False):
    ip_address: Required[str]
    """Ip address."""
