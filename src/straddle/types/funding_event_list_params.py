# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.sort_order import SortOrder
from .shared.funding_event_type_v1 import FundingEventTypeV1
from .shared.transfer_direction_v1 import TransferDirectionV1

__all__ = ["FundingEventListParams"]


class FundingEventListParams(TypedDict, total=False):
    created_from: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The start date of the range to filter by using the `YYYY-MM-DD` format."""

    created_to: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The end date of the range to filter by using the `YYYY-MM-DD` format."""

    direction: TransferDirectionV1
    """
    Describes the direction of the funding event from the perspective of the
    `linked_bank_account`.
    """

    event_type: FundingEventTypeV1
    """
    The funding event types describes the direction and reason for the funding
    event.
    """

    page_number: int
    """Results page number. Starts at page 1."""

    page_size: int
    """Results page size. Max value: 1000"""

    sort_by: Literal["transfer_date", "id", "amount"]
    """The field to sort the results by."""

    sort_order: SortOrder
    """The order in which to sort the results."""

    trace_number: Optional[str]
    """Trace number."""

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
