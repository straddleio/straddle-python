# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.sort_order import SortOrder
from .shared.payment_type_v1 import PaymentTypeV1
from .shared.payment_status_v1 import PaymentStatusV1
from .shared.payment_sort_by_v1 import PaymentSortByV1

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    customer_id: str
    """Search using the `customer_id` of a `charge` or `payout`."""

    default_page_size: int

    default_sort: PaymentSortByV1
    """The field to sort the results by."""

    default_sort_order: SortOrder

    external_id: str
    """Search using the `external_id` of a `charge` or `payout`."""

    funding_id: str
    """Search using the `funding_id` of a `charge` or `payout`."""

    max_amount: int
    """Search using a maximum `amount` of a `charge` or `payout`."""

    max_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Search using the latest `created_at` date of a `charge` or `payout`."""

    max_effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Search using the latest `effective_date` of a `charge` or `payout`."""

    max_payment_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Search using the latest `payment_date` of a `charge` or `payout`."""

    min_amount: int
    """Search using the minimum `amount of a `charge`or`payout`."""

    min_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Search using the earliest `created_at` date of a `charge` or `payout`."""

    min_effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Search using the earliest `effective_date` of a `charge` or `payout`."""

    min_payment_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Search using the earliest ` `of a `charge` or `payout`."""

    page_number: int
    """Results page number. Starts at page 1."""

    page_size: int
    """Results page size. Max value: 1000"""

    paykey: str
    """Search using the `paykey` of a `charge` or `payout`."""

    paykey_id: str
    """Search using the `paykey_id` of a `charge` or `payout`."""

    payment_id: str
    """Search using the `id` of a `charge` or `payout`."""

    payment_status: List[PaymentStatusV1]
    """Search by the status of a `charge` or `payout`."""

    payment_type: List[PaymentTypeV1]
    """Search by the type of a `charge` or `payout`."""

    search_text: str
    """Search using a text string associated with a `charge` or `payout`."""

    sort_by: PaymentSortByV1
    """The field to sort the results by."""

    sort_order: SortOrder

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]
