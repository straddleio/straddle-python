# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "AccountGetResponse",
    "StatusDetail",
    "BusinessProfile",
    "BusinessProfileAddress",
    "BusinessProfileIndustry",
    "BusinessProfileSupportChannels",
    "Capabilities",
    "CapabilitiesConsentTypes",
    "CapabilitiesConsentTypesInternet",
    "CapabilitiesConsentTypesSignedAgreement",
    "CapabilitiesCustomerTypes",
    "CapabilitiesCustomerTypesBusinesses",
    "CapabilitiesCustomerTypesIndividuals",
    "CapabilitiesPaymentTypes",
    "CapabilitiesPaymentTypesCharges",
    "CapabilitiesPaymentTypesPayouts",
    "Settings",
    "SettingsCharges",
    "SettingsPayouts",
    "TermsOfService",
]


class StatusDetail(BaseModel):
    code: str
    """
    A machine-readable code for the specific status, useful for programmatic
    handling.
    """

    message: str
    """A human-readable message describing the current status."""

    reason: Literal[
        "unverified", "in_review", "pending", "stuck", "verified", "failed_verification", "disabled", "terminated"
    ]
    """
    A machine-readable identifier for the specific status, useful for programmatic
    handling.
    """

    source: Literal["watchtower"]
    """Identifies the origin of the status change (e.g., `bank_decline`, `watchtower`).

    This helps in tracking the cause of status updates.
    """


class BusinessProfileAddress(BaseModel):
    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    country: Optional[str] = None
    """The country of the address, in ISO 3166-1 alpha-2 format."""

    line1: Optional[str] = None
    """Primary address line (e.g., street, PO Box)."""

    line2: Optional[str] = None
    """Secondary address line (e.g., apartment, suite, unit, or building)."""

    postal_code: Optional[str] = None
    """Postal or ZIP code."""

    state: Optional[str] = None
    """Two-letter state code."""


class BusinessProfileIndustry(BaseModel):
    category: Optional[str] = None
    """The general category of the industry. Required if not providing MCC."""

    mcc: Optional[str] = None
    """The Merchant Category Code (MCC) that best describes the business. Optional."""

    sector: Optional[str] = None
    """The specific sector within the industry category.

    Required if not providing MCC.
    """


class BusinessProfileSupportChannels(BaseModel):
    email: Optional[str] = None
    """The email address for customer support inquiries."""

    phone: Optional[str] = None
    """The phone number for customer support."""

    url: Optional[str] = None
    """The URL of the business's customer support page or contact form."""


class BusinessProfile(BaseModel):
    name: str
    """The operating or trade name of the business."""

    website: str
    """URL of the business's primary marketing website."""

    address: Optional[BusinessProfileAddress] = None
    """The address object is optional. If provided, it must be a valid address."""

    description: Optional[str] = None
    """A brief description of the business and its products or services."""

    industry: Optional[BusinessProfileIndustry] = None

    legal_name: Optional[str] = None
    """The official registered name of the business."""

    phone: Optional[str] = None
    """The primary contact phone number for the business."""

    support_channels: Optional[BusinessProfileSupportChannels] = None

    tax_id: Optional[str] = None
    """The business's tax identification number (e.g., EIN in the US)."""

    use_case: Optional[str] = None
    """A description of how the business intends to use Straddle's services."""


class CapabilitiesConsentTypesInternet(BaseModel):
    capability_status: Literal["active", "inactive"]


class CapabilitiesConsentTypesSignedAgreement(BaseModel):
    capability_status: Literal["active", "inactive"]


class CapabilitiesConsentTypes(BaseModel):
    internet: CapabilitiesConsentTypesInternet
    """
    Whether the internet payment authorization capability is enabled for the
    account.
    """

    signed_agreement: CapabilitiesConsentTypesSignedAgreement
    """
    Whether the signed agreement payment authorization capability is enabled for the
    account.
    """


class CapabilitiesCustomerTypesBusinesses(BaseModel):
    capability_status: Literal["active", "inactive"]


class CapabilitiesCustomerTypesIndividuals(BaseModel):
    capability_status: Literal["active", "inactive"]


class CapabilitiesCustomerTypes(BaseModel):
    businesses: CapabilitiesCustomerTypesBusinesses

    individuals: CapabilitiesCustomerTypesIndividuals


class CapabilitiesPaymentTypesCharges(BaseModel):
    capability_status: Literal["active", "inactive"]


class CapabilitiesPaymentTypesPayouts(BaseModel):
    capability_status: Literal["active", "inactive"]


class CapabilitiesPaymentTypes(BaseModel):
    charges: CapabilitiesPaymentTypesCharges

    payouts: CapabilitiesPaymentTypesPayouts


class Capabilities(BaseModel):
    consent_types: CapabilitiesConsentTypes

    customer_types: CapabilitiesCustomerTypes

    payment_types: CapabilitiesPaymentTypes


class SettingsCharges(BaseModel):
    daily_amount: int
    """The maximum dollar amount of charges in a calendar day."""

    funding_time: Literal["immediate", "next_day", "one_day", "two_day", "three_day"]
    """The amount of time it takes for a charge to be funded.

    This value is defined by Straddle.
    """

    linked_bank_account_id: str
    """The unique identifier of the linked bank account associated with charges.

    This value is defined by Straddle.
    """

    max_amount: int
    """The maximum amount of a single charge."""

    monthly_amount: int
    """The maximum dollar amount of charges in a calendar month."""

    monthly_count: int
    """The maximum number of charges in a calendar month."""


class SettingsPayouts(BaseModel):
    daily_amount: int
    """The maximum dollar amount of payouts in a day."""

    funding_time: Literal["immediate", "next_day", "one_day", "two_day", "three_day"]
    """The amount of time it takes for a payout to be funded.

    This value is defined by Straddle.
    """

    linked_bank_account_id: str
    """The unique identifier of the linked bank account to use for payouts."""

    max_amount: int
    """The maximum amount of a single payout."""

    monthly_amount: int
    """The maximum dollar amount of payouts in a month."""

    monthly_count: int
    """The maximum number of payouts in a month."""


class Settings(BaseModel):
    charges: SettingsCharges

    payouts: SettingsPayouts


class TermsOfService(BaseModel):
    accepted_date: datetime
    """The datetime of when the terms of service were accepted, in ISO 8601 format."""

    agreement_type: Literal["embedded", "direct"]
    """The type or version of the agreement accepted.

    Use `embedded` unless your platform was specifically enabled for `direct`
    agreements.
    """

    accepted_ip: Optional[str] = None
    """The IP address from which the terms of service were accepted."""

    accepted_user_agent: Optional[str] = None
    """The user agent string of the browser or application used to accept the terms."""

    agreement_url: Optional[str] = None
    """The URL where the full text of the accepted agreement can be found."""


class AccountGetResponse(BaseModel):
    id: str
    """Unique identifier for the account."""

    access_level: Literal["standard", "managed"]
    """The access level granted to the account.

    This is determined by your platform configuration. Use `standard` unless
    instructed otherwise by Straddle.
    """

    organization_id: str
    """The unique identifier of the organization this account belongs to."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """The current status of the account (e.g., 'active', 'inactive', 'pending')."""

    status_detail: StatusDetail

    type: Literal["business"]
    """The type of account (e.g., 'individual', 'business')."""

    business_profile: Optional[BusinessProfile] = None

    capabilities: Optional[Capabilities] = None

    created_at: Optional[datetime] = None
    """Timestamp of when the account was created."""

    external_id: Optional[str] = None
    """
    Unique identifier for the account in your database, used for cross-referencing
    between Straddle and your systems.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the account in a structured
    format.
    """

    settings: Optional[Settings] = None

    terms_of_service: Optional[TermsOfService] = None

    updated_at: Optional[datetime] = None
    """Timestamp of the most recent update to the account."""
