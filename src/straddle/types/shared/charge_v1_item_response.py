# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from ..._models import BaseModel
from .device_info_v1 import DeviceInfoV1
from .consent_type_v1 import ConsentTypeV1
from .payment_rail_v1 import PaymentRailV1
from .paykey_details_v1 import PaykeyDetailsV1
from .payment_status_v1 import PaymentStatusV1
from .response_metadata import ResponseMetadata
from .status_details_v1 import StatusDetailsV1
from .status_history_v1 import StatusHistoryV1
from .response_type_enum import ResponseTypeEnum
from .customer_details_v1 import CustomerDetailsV1
from .charge_configuration_v1 import ChargeConfigurationV1

__all__ = ["ChargeV1ItemResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the charge."""

    amount: int
    """The amount of the charge in cents."""

    config: ChargeConfigurationV1
    """Configuration options for the charge."""

    consent_type: ConsentTypeV1
    """The channel or mechanism through which the payment was authorized.

    Use `internet` for payments made online or through a mobile app and `signed` for
    signed agreements where there is a consent form or contract. Use `signed` for
    PDF signatures.
    """

    created_at: Optional[datetime] = None
    """Timestamp of when the charge was created."""

    currency: str
    """The currency of the charge. Only USD is supported."""

    description: str
    """An arbitrary description for the charge."""

    device: DeviceInfoV1
    """Information about the device used when the customer authorized the payment."""

    external_id: str
    """Unique identifier for the charge in your database.

    This value must be unique across all charges.
    """

    paykey: str
    """Value of the `paykey` used for the charge."""

    payment_date: date
    """The desired date on which the payment should be occur.

    For charges, this means the date you want the customer to be debited on.
    """

    status: PaymentStatusV1
    """The current status of the charge."""

    status_details: StatusDetailsV1
    """Additional details about the current status of the charge."""

    status_history: List[StatusHistoryV1]
    """Status history."""

    updated_at: Optional[datetime] = None
    """Timestamp of when the charge was last updated."""

    customer_details: Optional[CustomerDetailsV1] = None
    """Information about the customer associated with the charge."""

    effective_at: Optional[datetime] = None
    """
    Timestamp of when the charge was effective in the customer's bank account,
    otherwise known as the date on which the customer is debited.
    """

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the charge in a structured
    format.
    """

    paykey_details: Optional[PaykeyDetailsV1] = None
    """Information about the paykey used for the charge."""

    payment_rail: Optional[PaymentRailV1] = None
    """The payment rail that the charge will be processed through."""

    processed_at: Optional[datetime] = None
    """
    Timestamp of when the charge was processed by Straddle and originated to the
    payment rail.
    """


class ChargeV1ItemResponse(BaseModel):
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
