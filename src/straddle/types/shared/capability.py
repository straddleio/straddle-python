# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Capability"]


class Capability(BaseModel):
    capability_status: Literal["active", "inactive"]
