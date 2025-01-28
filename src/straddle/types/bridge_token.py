# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeToken", "Data", "Meta"]


class Data(BaseModel):
    bridge_token: str
    """JWT Token to use in the bridge widget."""


class Meta(BaseModel):
    api_request_id: str
    """Unique identifier for this API request, useful for troubleshooting."""

    api_request_timestamp: datetime
    """Timestamp for this API request, useful for troubleshooting."""


class BridgeToken(BaseModel):
    data: Data

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
