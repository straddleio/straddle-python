# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Representative", "Data", "DataRelationship", "DataStatusDetail", "Meta"]


class DataRelationship(BaseModel):
    control: bool

    owner: bool

    primary: bool

    percent_ownership: Optional[float] = None

    title: Optional[str] = None


class DataStatusDetail(BaseModel):
    code: str

    message: str

    reason: Literal["unverified", "new", "in_review", "pending", "stuck", "verified", "failed_verification", "disabled"]

    source: Literal["watchtower"]


class Data(BaseModel):
    id: str
    """Unique identifier for the representative."""

    account_id: str
    """The unique identifier of the account this representative is associated with."""

    created_at: datetime
    """Timestamp of when the representative was created."""

    dob: date
    """The date of birth of the representative, in ISO 8601 format (YYYY-MM-DD)."""

    email: str
    """The email address of the representative."""

    first_name: str
    """The first name of the representative."""

    last_name: str
    """The last name of the representative."""

    mobile_number: str
    """The mobile phone number of the representative."""

    relationship: DataRelationship

    ssn_last4: str
    """The last 4 digits of the representative's Social Security Number."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """The current status of the representative."""

    status_detail: DataStatusDetail

    updated_at: datetime
    """Timestamp of the most recent update to the representative."""

    external_id: Optional[str] = None
    """
    Unique identifier for the representative in your database, used for
    cross-referencing between Straddle and your systems.
    """

    user_id: Optional[str] = None
    """
    The unique identifier of the user account associated with this representative,
    if applicable.
    """


class Meta(BaseModel):
    api_request_id: str
    """Unique identifier for this API request, useful for troubleshooting."""

    api_request_timestamp: datetime
    """Timestamp for this API request, useful for troubleshooting."""


class Representative(BaseModel):
    data: Data

    meta: Meta

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the type of data returned."""
