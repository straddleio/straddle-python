# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.address_v11 import AddressV11
from .shared.customer_type_v1 import CustomerTypeV1
from .shared.response_metadata import ResponseMetadata
from .shared.customer_status_v1 import CustomerStatusV1
from .shared.device_unmasked_v1 import DeviceUnmaskedV1
from .shared.response_type_enum import ResponseTypeEnum
from .shared.compliance_profile_unmasked_v1 import ComplianceProfileUnmaskedV1

__all__ = ["CustomerUnmaskedV1", "Data"]


class Data(BaseModel):
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

    compliance_profile: Optional[ComplianceProfileUnmaskedV1] = None
    """Compliance profile for individual customers"""

    device: Optional[DeviceUnmaskedV1] = None

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


class CustomerUnmaskedV1(BaseModel):
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
