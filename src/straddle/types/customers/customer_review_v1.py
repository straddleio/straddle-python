# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..customer_address_v1 import CustomerAddressV1
from ..shared.response_metadata import ResponseMetadata
from .identity_verification_breakdown_v1 import IdentityVerificationBreakdownV1

__all__ = [
    "CustomerReviewV1",
    "Data",
    "DataCustomerDetails",
    "DataCustomerDetailsComplianceProfile",
    "DataCustomerDetailsComplianceProfileIndividualComplianceProfile",
    "DataCustomerDetailsComplianceProfileIndividualComplianceProfileRepresentative",
    "DataCustomerDetailsComplianceProfileBusinessComplianceProfile",
    "DataCustomerDetailsComplianceProfileBusinessComplianceProfileRepresentative",
    "DataCustomerDetailsDevice",
    "DataIdentityDetails",
    "DataIdentityDetailsBreakdown",
    "DataIdentityDetailsKYC",
    "DataIdentityDetailsKYCValidations",
    "DataIdentityDetailsNetworkAlerts",
    "DataIdentityDetailsWatchList",
    "DataIdentityDetailsWatchListMatch",
]


class DataCustomerDetailsComplianceProfileIndividualComplianceProfileRepresentative(BaseModel):
    name: str

    email: Optional[str] = None

    phone: Optional[str] = None


class DataCustomerDetailsComplianceProfileIndividualComplianceProfile(BaseModel):
    dob: Optional[date] = None
    """Masked date of birth in \\****\\**-**-\\**\\** format."""

    ssn: Optional[str] = None
    """Masked Social Security Number in the format **\\**-**-\\**\\**\\**\\**."""

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

    representatives: Optional[List[DataCustomerDetailsComplianceProfileIndividualComplianceProfileRepresentative]] = (
        None
    )
    """A list of people related to the company.

    Only valid where customer type is 'business'.
    """

    website: Optional[str] = None
    """URL of the company's official website.

    Only valid where customer type is 'business'.
    """


class DataCustomerDetailsComplianceProfileBusinessComplianceProfileRepresentative(BaseModel):
    name: str

    email: Optional[str] = None

    phone: Optional[str] = None


class DataCustomerDetailsComplianceProfileBusinessComplianceProfile(BaseModel):
    ein: Optional[str] = None
    """Masked Employer Identification Number in the format **-**\\******"""

    legal_business_name: Optional[str] = None
    """The official registered name of the business.

    This name should be correlated with the `ein` value.
    """

    dob: Optional[str] = None
    """Date of birth for individual customers in ISO 8601 format (YYYY-MM-DD).

    This data is required to trigger Patriot Act compliant Know Your Customer (KYC)
    verification. Required if SSN is provided. Only valid where customer type is
    'individual'.
    """

    representatives: Optional[List[DataCustomerDetailsComplianceProfileBusinessComplianceProfileRepresentative]] = None
    """A list of people related to the company.

    Only valid where customer type is 'business'.
    """

    ssn: Optional[str] = None
    """Full 9-digit Social Security Number or government identifier for individuals.

    This data is required to trigger Patriot Act compliant KYC verification.
    Required if DOB is provided. Only valid where customer type is 'individual'.
    """

    website: Optional[str] = None
    """Official business website URL. Optional but recommended for enhanced KYB."""


DataCustomerDetailsComplianceProfile: TypeAlias = Union[
    DataCustomerDetailsComplianceProfileIndividualComplianceProfile,
    DataCustomerDetailsComplianceProfileBusinessComplianceProfile,
    None,
]


class DataCustomerDetailsDevice(BaseModel):
    ip_address: str
    """The customer's IP address at the time of profile creation.

    Use `0.0.0.0` to represent an offline customer registration.
    """


class DataCustomerDetails(BaseModel):
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

    status: Literal["pending", "review", "verified", "inactive", "rejected"]

    type: Literal["individual", "business"]

    updated_at: datetime
    """Timestamp of the most recent update to the customer record."""

    address: Optional[CustomerAddressV1] = None
    """An object containing the customer's address.

    This is optional, but if provided, all required fields must be present.
    """

    compliance_profile: Optional[DataCustomerDetailsComplianceProfile] = None
    """PII required to trigger Patriot Act compliant KYC verification."""

    device: Optional[DataCustomerDetailsDevice] = None

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


class DataIdentityDetailsBreakdown(BaseModel):
    address: Optional[IdentityVerificationBreakdownV1] = None

    business_evaluation: Optional[IdentityVerificationBreakdownV1] = None

    business_identification: Optional[IdentityVerificationBreakdownV1] = None

    business_validation: Optional[IdentityVerificationBreakdownV1] = None

    email: Optional[IdentityVerificationBreakdownV1] = None

    fraud: Optional[IdentityVerificationBreakdownV1] = None

    phone: Optional[IdentityVerificationBreakdownV1] = None

    synthetic: Optional[IdentityVerificationBreakdownV1] = None


class DataIdentityDetailsKYCValidations(BaseModel):
    address: Optional[bool] = None

    city: Optional[bool] = None

    dob: Optional[bool] = None

    email: Optional[bool] = None

    first_name: Optional[bool] = None

    last_name: Optional[bool] = None

    phone: Optional[bool] = None

    ssn: Optional[bool] = None

    state: Optional[bool] = None

    zip: Optional[bool] = None


class DataIdentityDetailsKYC(BaseModel):
    validations: DataIdentityDetailsKYCValidations
    """Boolean values indicating the result of each validation in the KYC process."""

    codes: Optional[List[str]] = None
    """List of specific result codes from the KYC screening process."""

    decision: Optional[Literal["accept", "reject", "review"]] = None


class DataIdentityDetailsNetworkAlerts(BaseModel):
    alerts: Optional[List[str]] = None
    """Any alerts or flags raised during the consortium alert screening."""

    codes: Optional[List[str]] = None
    """List of specific result codes from the consortium alert screening."""

    decision: Optional[Literal["accept", "reject", "review"]] = None


class DataIdentityDetailsWatchListMatch(BaseModel):
    correlation: Literal["low_confidence", "potential_match", "likely_match", "high_confidence", "unknown"]

    list_name: str
    """The name of the list the match was found."""

    match_fields: List[str]
    """Data fields that matched."""

    urls: List[str]
    """Relevent Urls to review."""


class DataIdentityDetailsWatchList(BaseModel):
    codes: Optional[List[str]] = None
    """Specific codes related to the Straddle watchlist screening results."""

    decision: Optional[Literal["accept", "reject", "review"]] = None

    matched: Optional[List[str]] = None
    """Information about any matches found during screening."""

    matches: Optional[List[DataIdentityDetailsWatchListMatch]] = None
    """Information about any matches found during screening."""


class DataIdentityDetails(BaseModel):
    breakdown: DataIdentityDetailsBreakdown
    """
    Detailed breakdown of the customer verification results, including decisions,
    risk scores, correlation score, and more.
    """

    created_at: datetime
    """Timestamp of when the review was initiated."""

    decision: Literal["accept", "reject", "review"]

    review_id: str
    """Unique identifier for the review."""

    updated_at: datetime
    """Timestamp of the most recent update to the review."""

    kyc: Optional[DataIdentityDetailsKYC] = None

    messages: Optional[Dict[str, str]] = None
    """Dictionary of all messages from the customer verification process."""

    network_alerts: Optional[DataIdentityDetailsNetworkAlerts] = None

    watch_list: Optional[DataIdentityDetailsWatchList] = None


class Data(BaseModel):
    customer_details: DataCustomerDetails

    identity_details: Optional[DataIdentityDetails] = None


class CustomerReviewV1(BaseModel):
    data: Data

    meta: ResponseMetadata
    """Metadata about the API request, including an identifier and timestamp."""

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
