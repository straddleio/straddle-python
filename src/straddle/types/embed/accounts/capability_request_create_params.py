# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "CapabilityRequestCreateParams",
    "Businesses",
    "Charges",
    "Individuals",
    "Internet",
    "Payouts",
    "SignedAgreement",
]


class CapabilityRequestCreateParams(TypedDict, total=False):
    businesses: Businesses

    charges: Charges

    individuals: Individuals

    internet: Internet

    payouts: Payouts

    signed_agreement: SignedAgreement

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]


class Businesses(TypedDict, total=False):
    enable: Required[bool]


class Charges(TypedDict, total=False):
    daily_amount: Required[float]

    enable: Required[bool]

    max_amount: Required[float]

    monthly_amount: Required[float]

    monthly_count: Required[int]


class Individuals(TypedDict, total=False):
    enable: Required[bool]


class Internet(TypedDict, total=False):
    enable: Required[bool]


class Payouts(TypedDict, total=False):
    daily_amount: Required[float]

    enable: Required[bool]

    max_amount: Required[float]

    monthly_amount: Required[float]

    monthly_count: Required[int]


class SignedAgreement(TypedDict, total=False):
    enable: Required[bool]
