# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .device_unmasked_v1_param import DeviceUnmaskedV1Param
from .customer_address_v1_param import CustomerAddressV1Param

__all__ = [
    "CustomerCreateParams",
    "ComplianceProfile",
    "ComplianceProfileIndividualComplianceProfile",
    "ComplianceProfileBusinessComplianceProfile",
]


class CustomerCreateParams(TypedDict, total=False):
    device: Required[DeviceUnmaskedV1Param]

    email: Required[str]
    """The customer's email address."""

    name: Required[str]
    """Full name of the individual or business name."""

    phone: Required[str]
    """The customer's phone number in E.164 format. Mobile number is preferred."""

    type: Required[Literal["individual", "business"]]

    address: Optional[CustomerAddressV1Param]
    """An object containing the customer's address.

    This is optional, but if provided, all required fields must be present.
    """

    compliance_profile: ComplianceProfile
    """An object containing the customer's compliance profile.

    This is optional, but if provided, all required fields must be present for the
    appropriate customer type.
    """

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


class ComplianceProfileIndividualComplianceProfile(TypedDict, total=False):
    dob: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date of birth in YYYY-MM-DD format."""

    ssn: Required[str]
    """Social Security Number in the format XXX-XX-XXXX."""


class ComplianceProfileBusinessComplianceProfile(TypedDict, total=False):
    ein: Required[str]
    """Employer Identification Number in the format XX-XXXXXXX."""

    legal_business_name: Required[str]
    """The official registered name of the business.

    This name should be correlated with the `ein` value.
    """

    website: str
    """Business website URL."""


ComplianceProfile: TypeAlias = Union[
    ComplianceProfileIndividualComplianceProfile, ComplianceProfileBusinessComplianceProfile
]
