# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.paykey_source_v1 import PaykeySourceV1
from .shared.paykey_status_v1 import PaykeyStatusV1
from .shared.response_metadata import ResponseMetadata
from .shared.status_details_v1 import StatusDetailsV1
from .shared.response_type_enum import ResponseTypeEnum
from .shared.paykey_bank_details_v1 import PaykeyBankDetailsV1

__all__ = ["PaykeyRevealResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the paykey."""

    created_at: datetime
    """Timestamp of when the paykey was created."""

    label: str
    """Human-readable label used to represent this paykey in a UI."""

    paykey: str
    """The tokenized paykey value.

    This value is used to create payments and should be stored securely.
    """

    source: PaykeySourceV1

    status: PaykeyStatusV1

    updated_at: datetime
    """Timestamp of the most recent update to the paykey."""

    bank_data: Optional[PaykeyBankDetailsV1] = None

    customer_id: Optional[str] = None
    """Unique identifier of the related customer object."""

    expires_at: Optional[datetime] = None
    """Expiration date and time of the paykey, if applicable."""

    institution_name: Optional[str] = None
    """Name of the financial institution."""

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 additional user-defined key-value pairs.

    Useful for storing additional information about the paykey in a structured
    format.
    """

    status_details: Optional[StatusDetailsV1] = None


class PaykeyRevealResponse(BaseModel):
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
