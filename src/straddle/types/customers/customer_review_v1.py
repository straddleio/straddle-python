# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..shared.customer_v1 import CustomerV1
from ..shared.response_metadata import ResponseMetadata
from ..shared.response_type_enum import ResponseTypeEnum
from ..shared.identity_decision_v1 import IdentityDecisionV1
from ..shared.identity_verification_breakdown_v1 import IdentityVerificationBreakdownV1

__all__ = [
    "CustomerReviewV1",
    "Data",
    "DataIdentityDetails",
    "DataIdentityDetailsBreakdown",
    "DataIdentityDetailsKYC",
    "DataIdentityDetailsKYCValidations",
    "DataIdentityDetailsNetworkAlerts",
    "DataIdentityDetailsWatchList",
]


class DataIdentityDetailsBreakdown(BaseModel):
    address: Optional[IdentityVerificationBreakdownV1] = None

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

    decision: Optional[IdentityDecisionV1] = None


class DataIdentityDetailsNetworkAlerts(BaseModel):
    alerts: Optional[List[str]] = None
    """Any alerts or flags raised during the consortium alert screening."""

    codes: Optional[List[str]] = None
    """List of specific result codes from the consortium alert screening."""

    decision: Optional[IdentityDecisionV1] = None


class DataIdentityDetailsWatchList(BaseModel):
    codes: Optional[List[str]] = None
    """Specific codes related to the Straddle watchlist screening results."""

    decision: Optional[IdentityDecisionV1] = None

    matched: Optional[List[str]] = None
    """Information about any matches found during screening."""


class DataIdentityDetails(BaseModel):
    breakdown: DataIdentityDetailsBreakdown
    """
    Detailed breakdown of the customer verification results, including decisions,
    risk scores, correlation score, and more.
    """

    created_at: datetime
    """Timestamp of when the review was initiated."""

    decision: IdentityDecisionV1

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
    customer_details: CustomerV1

    identity_details: Optional[DataIdentityDetails] = None


class CustomerReviewV1(BaseModel):
    data: Data

    meta: ResponseMetadata
    """Metadata about the API request, including an identifier and timestamp."""

    response_type: ResponseTypeEnum
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
