# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChargeConfigurationV1"]


class ChargeConfigurationV1(BaseModel):
    balance_check: Literal["required", "enabled", "disabled"]
    """Defines whether to check the customer's balance before processing the charge."""
