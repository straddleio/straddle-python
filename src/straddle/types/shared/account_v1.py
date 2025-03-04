# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .capability import Capability
from .business_profile_v1 import BusinessProfileV1
from .terms_of_service_v1 import TermsOfServiceV1

__all__ = [
    "AccountV1",
    "StatusDetail",
    "Capabilities",
    "CapabilitiesConsentTypes",
    "CapabilitiesCustomerTypes",
    "CapabilitiesPaymentTypes",
    "Settings",
    "SettingsCharges",
    "SettingsPayouts",
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
        "unverified",
        "in_review",
        "pending",
        "stuck",
        "verified",
        "failed_verification",
        "disabled",
        "terminated",
        "new",
    ]
    """
    A machine-readable identifier for the specific status, useful for programmatic
    handling.
    """

    source: Literal["watchtower"]
    """Identifies the origin of the status change (e.g., `bank_decline`, `watchtower`).

    This helps in tracking the cause of status updates.
    """


class CapabilitiesConsentTypes(BaseModel):
    internet: Capability
    """
    Whether the internet payment authorization capability is enabled for the
    account.
    """

    signed_agreement: Capability
    """
    Whether the signed agreement payment authorization capability is enabled for the
    account.
    """


class CapabilitiesCustomerTypes(BaseModel):
    businesses: Capability

    individuals: Capability


class CapabilitiesPaymentTypes(BaseModel):
    charges: Capability

    payouts: Capability


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


class AccountV1(BaseModel):
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

    business_profile: Optional[BusinessProfileV1] = None

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

    terms_of_service: Optional[TermsOfServiceV1] = None

    updated_at: Optional[datetime] = None
    """Timestamp of the most recent update to the account."""
