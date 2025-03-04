# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import date, datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .address_v11 import AddressV11
from .customer_type_v1 import CustomerTypeV1
from .customer_status_v1 import CustomerStatusV1

__all__ = [
    "CustomerV1",
    "ComplianceProfile",
    "ComplianceProfileIndividualComplianceProfile",
    "ComplianceProfileBusinessComplianceProfile",
    "Device",
]


class ComplianceProfileIndividualComplianceProfile(BaseModel):
    dob: date
    """Date of birth in YYYY-MM-DD format."""

    ssn: str
    """Social Security Number in the format XXX-XX-XXXX."""

    ein: Optional[str] = None
    """Full 9-digit Employer Identification Number for businesses.

    This data is required to trigger Patriot Act compliant Know Your Business (KYB)
    verification. Only valid where customer type is 'business'.
    """

    legal_business_name: Optional[str] = None
    """The official name of the business.

    This name should be correlated with the ein value. Only valid where customer
    type is 'business'.
    """

    website: Optional[str] = None
    """URL of the company's official website.

    Only valid where customer type is 'business'.
    """


class ComplianceProfileBusinessComplianceProfile(BaseModel):
    ein: str
    """Employer Identification Number in the format XX-XXXXXXX."""

    legal_business_name: str
    """The official registered name of the business.

    This name should be correlated with the `ein` value.
    """

    dob: Optional[str] = None
    """Date of birth for individual customers in ISO 8601 format (YYYY-MM-DD).

    This data is required to trigger Patriot Act compliant Know Your Customer (KYC)
    verification. Required if SSN is provided. Only valid where customer type is
    'individual'.
    """

    ssn: Optional[str] = None
    """Full 9-digit Social Security Number or government identifier for individuals.

    This data is required to trigger Patriot Act compliant KYC verification.
    Required if DOB is provided. Only valid where customer type is 'individual'.
    """

    website: Optional[str] = None
    """Business website URL."""


ComplianceProfile: TypeAlias = Union[
    ComplianceProfileIndividualComplianceProfile, ComplianceProfileBusinessComplianceProfile
]


class Device(BaseModel):
    ip_address: str
    """The customer's IP address at the time of profile creation.

    Use `0.0.0.0` to represent an offline customer registration.
    """


class CustomerV1(BaseModel):
    id: str
    """Unique identifier for the customer."""

    created_at: datetime
    """Timestamp of when the customer record was created."""

    email: str
    """The customer's email address."""

    name: str
    """Full name of the individual or business name."""

    phone: str
    """The customer's phone number in E.164 format."""

    status: CustomerStatusV1

    type: CustomerTypeV1

    updated_at: datetime
    """Timestamp of the most recent update to the customer record."""

    address: Optional[AddressV11] = None

    compliance_profile: Optional[ComplianceProfile] = None
    """Compliance profile for individual customers"""

    device: Optional[Device] = None

    external_id: Optional[str] = None
    """
    Unique identifier for the customer in your database, used for cross-referencing
    between Straddle and your systems.
    """

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the customer in a structured
    format.
    """
