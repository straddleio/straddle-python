# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.linked_bank_account_v1 import LinkedBankAccountV1
from ..shared.paged_response_metadata import PagedResponseMetadata

__all__ = ["LinkedBankAccountPagedV1"]


class LinkedBankAccountPagedV1(BaseModel):
    data: List[LinkedBankAccountV1]

    meta: PagedResponseMetadata
    """
    Metadata about the API request, including an identifier, timestamp, and
    pagination details.
    """

    response_type: Literal["object", "array", "error", "none"]
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
