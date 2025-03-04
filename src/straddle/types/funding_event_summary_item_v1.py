# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .shared.response_metadata import ResponseMetadata
from .shared.response_type_enum import ResponseTypeEnum
from .shared.funding_event_summary_v1 import FundingEventSummaryV1

__all__ = ["FundingEventSummaryItemV1"]


class FundingEventSummaryItemV1(BaseModel):
    data: FundingEventSummaryV1

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
