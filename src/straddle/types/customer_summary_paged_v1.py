# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.customer_type_v1 import CustomerTypeV1
from .shared.customer_status_v1 import CustomerStatusV1
from .shared.response_type_enum import ResponseTypeEnum
from .shared.paged_response_metadata_1 import PagedResponseMetadata1

__all__ = ["CustomerSummaryPagedV1", "Data"]


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

    external_id: Optional[str] = None
    """
    Unique identifier for the customer in your database, used for cross-referencing
    between Straddle and your systems.
    """


class CustomerSummaryPagedV1(BaseModel):
    data: List[Data]

    meta: PagedResponseMetadata1

    response_type: ResponseTypeEnum
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
