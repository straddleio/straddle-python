# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UpdateChargeStatusV1Request"]


class UpdateChargeStatusV1Request(BaseModel):
    reason: Optional[str] = None
    """Details about why the charge status was updated."""
