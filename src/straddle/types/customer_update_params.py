# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.address_v11 import AddressV11
from .shared_params.device_unmasked_v1 import DeviceUnmaskedV1
from .shared_params.compliance_profile_unmasked_v1 import ComplianceProfileUnmaskedV1

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    device: Required[DeviceUnmaskedV1]

    email: Required[str]
    """The customer's email address."""

    name: Required[str]
    """The customer's full name or business name."""

    phone: Required[str]
    """The customer's phone number in E.164 format."""

    status: Required[Literal["pending", "review", "verified", "inactive", "rejected"]]

    address: Optional[AddressV11]
    """An object containing the customer's address.

    This is optional, but if provided, all required fields must be present.
    """

    compliance_profile: ComplianceProfileUnmaskedV1
    """Compliance profile for individual customers"""

    external_id: Optional[str]
    """
    Unique identifier for the customer in your database, used for cross-referencing
    between Straddle and your systems.
    """

    metadata: Optional[Dict[str, str]]
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the customer in a structured
    format.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
