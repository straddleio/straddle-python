# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import date
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ComplianceProfileUnmaskedV1", "IndividualComplianceProfile", "BusinessComplianceProfile"]


class IndividualComplianceProfile(BaseModel):
    dob: date
    """Date of birth in YYYY-MM-DD format."""

    ssn: str
    """Social Security Number in the format XXX-XX-XXXX."""

    ein: Optional[str] = None
    """Full 9-digit Employer Identification Number for businesses.

    This data is required to trigger Patriot Act compliant KYB verification. Only
    valid where customer type is 'business'.
    """

    legal_business_name: Optional[str] = None
    """The official name of the business.

    This name should be correlated with the ein value. Only valid where customer
    type is 'business'.
    """

    website: Optional[str] = None
    """URL of the company's official website."""


class BusinessComplianceProfile(BaseModel):
    ein: str
    """Employer Identification Number in the format XX-XXXXXXX."""

    legal_business_name: str
    """The official registered name of the business.

    This name should be correlated with the `ein` value.
    """

    dob: Optional[str] = None
    """Date of birth for individual customers in ISO 8601 format (YYYY-MM-DD).

    This data is required to trigger Patriot Act compliant KYC verification.
    Required if SSN is provided. Only valid where customer type is 'individual'.
    """

    ssn: Optional[str] = None
    """Full 9-digit Social Security Number or government identifier for individuals.

    This data is required to trigger Patriot Act compliant KYC verification.
    Required if DOB is provided. Only valid where customer type is 'individual'.
    """

    website: Optional[str] = None
    """Business website URL."""


ComplianceProfileUnmaskedV1: TypeAlias = Union[IndividualComplianceProfile, BusinessComplianceProfile]
