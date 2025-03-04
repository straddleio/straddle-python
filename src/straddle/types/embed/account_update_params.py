# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.business_profile_v1 import BusinessProfileV1

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    business_profile: Required[BusinessProfileV1]

    external_id: Optional[str]
    """
    Unique identifier for the account in your database, used for cross-referencing
    between Straddle and your systems.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the account in a structured
    format.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]
