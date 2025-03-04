# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChargeConfigurationV1"]


class ChargeConfigurationV1(TypedDict, total=False):
    balance_check: Required[Literal["required", "enabled", "disabled"]]
    """Defines whether to check the customer's balance before processing the charge."""
