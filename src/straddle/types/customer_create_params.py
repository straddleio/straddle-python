# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerCreateParams", "Device", "Address", "ComplianceProfile"]


class CustomerCreateParams(TypedDict, total=False):
    device: Required[Device]

    email: Required[str]
    """The customer's email address."""

    name: Required[str]
    """Full name of the individual or business name."""

    phone: Required[str]
    """The customer's phone number in E.164 format. Mobile number is preferred."""

    type: Required[Literal["individual", "business"]]

    address: Address

    compliance_profile: ComplianceProfile

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


class Device(TypedDict, total=False):
    ip_address: Required[str]
    """The customer's IP address at the time of profile creation.

    Use '0.0.0.0' to represent an offline customer registration.
    """


class Address(TypedDict, total=False):
    address1: Required[str]
    """Primary address line (e.g., street, PO Box)."""

    city: Required[str]
    """City, district, suburb, town, or village."""

    state: Required[str]
    """Two-letter state code."""

    zip: Required[str]
    """Zip or postal code."""

    address2: Optional[str]
    """Secondary address line (e.g., apartment, suite, unit, or building)."""


class ComplianceProfile(TypedDict, total=False):
    dob: Optional[str]
    """Date of birth for individual customers in ISO 8601 format (YYYY-MM-DD).

    This data is required to trigger Patriot Act compliant KYC verification.
    Required if SSN is provided. Only valid where customer type is 'individual'.
    """

    ein: Optional[str]
    """Full 9-digit Employer Identification Number for businesses.

    This data is required to trigger Patriot Act compliant KYB verification. Only
    valid where customer type is 'business'.
    """

    legal_business_name: Optional[str]
    """The official name of the business.

    This name should be correlated with the ein value. Only valid where customer
    type is 'business'.
    """

    ssn: Optional[str]
    """Full 9-digit Social Security Number or government identifier for individuals.

    This data is required to trigger Patriot Act compliant KYC verification.
    Required if DOB is provided. Only valid where customer type is 'individual'.
    """

    website: Optional[str]
    """URL of the company's official website."""
