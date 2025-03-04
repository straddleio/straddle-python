# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .response_metadata import ResponseMetadata
from .linked_bank_account_v1 import LinkedBankAccountV1

__all__ = ["ItemResponseOfLinkedBankAccountV1"]


class ItemResponseOfLinkedBankAccountV1(BaseModel):
    data: LinkedBankAccountV1

    meta: ResponseMetadata
    """Metadata about the API request, including an identifier and timestamp."""

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
