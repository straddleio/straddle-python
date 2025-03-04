# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel
from .customer_v1 import CustomerV1
from .response_metadata import ResponseMetadata
from .response_type_enum import ResponseTypeEnum

__all__ = ["CustomerV1ItemResponse"]


class CustomerV1ItemResponse(BaseModel):
    data: CustomerV1

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
