# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.response_type_enum import ResponseTypeEnum
from .shared.funding_event_summary_v1 import FundingEventSummaryV1
from .shared.paged_response_metadata_2 import PagedResponseMetadata2

__all__ = ["FundingEventSummaryPagedV1"]


class FundingEventSummaryPagedV1(BaseModel):
    data: List[FundingEventSummaryV1]

    meta: PagedResponseMetadata2

    response_type: ResponseTypeEnum
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
