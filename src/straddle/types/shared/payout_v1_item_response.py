# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from ..._models import BaseModel
from .device_info_v1 import DeviceInfoV1
from .payment_rail_v1 import PaymentRailV1
from .paykey_details_v1 import PaykeyDetailsV1
from .payment_status_v1 import PaymentStatusV1
from .response_metadata import ResponseMetadata
from .status_details_v1 import StatusDetailsV1
from .status_history_v1 import StatusHistoryV1
from .response_type_enum import ResponseTypeEnum
from .customer_details_v1 import CustomerDetailsV1

__all__ = ["PayoutV1ItemResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the payout."""

    amount: int
    """The amount of the payout in cents."""

    config: object
    """Configuration for the payout."""

    currency: str
    """The currency of the payout. Only USD is supported."""

    description: str
    """An arbitrary description for the payout."""

    device: DeviceInfoV1
    """Information about the device used when the customer authorized the payout."""

    external_id: str
    """Unique identifier for the payout in your database.

    This value must be unique across all payouts.
    """

    paykey: str
    """Value of the `paykey` used for the payout."""

    payment_date: date
    """The desired date on which the payment should be occur.

    For payouts, this means the date you want the funds to be sent from your bank
    account.
    """

    status: PaymentStatusV1
    """The current status of the payout."""

    status_details: StatusDetailsV1
    """Details about the current status of the payout."""

    status_history: List[StatusHistoryV1]
    """History of the status changes for the payout."""

    created_at: Optional[datetime] = None
    """The time the payout was created."""

    customer_details: Optional[CustomerDetailsV1] = None
    """Information about the customer associated with the payout."""

    effective_at: Optional[datetime] = None
    """The actual date on which the payment occurred.

    For payouts, this is the date the funds were sent from your bank account.
    """

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the payout in a structured
    format.
    """

    paykey_details: Optional[PaykeyDetailsV1] = None
    """Information about the paykey used for the payout."""

    payment_rail: Optional[PaymentRailV1] = None
    """The payment rail used for the payout."""

    processed_at: Optional[datetime] = None
    """
    The time the payout was processed by Straddle and originated to the payment
    rail.
    """

    updated_at: Optional[datetime] = None
    """The time the payout was last updated."""


class PayoutV1ItemResponse(BaseModel):
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
