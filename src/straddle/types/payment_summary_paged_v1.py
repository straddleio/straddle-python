# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel
from .shared.payment_type_v1 import PaymentTypeV1
from .shared.paykey_details_v1 import PaykeyDetailsV1
from .shared.payment_status_v1 import PaymentStatusV1
from .shared.status_details_v1 import StatusDetailsV1
from .shared.response_type_enum import ResponseTypeEnum
from .shared.customer_details_v1 import CustomerDetailsV1
from .shared.paged_response_metadata_2 import PagedResponseMetadata2

__all__ = ["PaymentSummaryPagedV1", "Data"]


class Data(BaseModel):
    id: str
    """Unique identifier for the `charge` or `payout`."""

    amount: int
    """The amount of the `charge` or `payout` in cents."""

    created_at: datetime
    """The time the `charge` or `payout` was created."""

    currency: str
    """The currency of the `charge` or `payout`. Only USD is supported."""

    description: str
    """An arbitrary description for the `charge` or `payout`."""

    external_id: str
    """Unique identifier for the `charge` or `payout` in your database.

    This value must be unique across all charges or payouts.
    """

    paykey: str
    """Value of the `paykey` used for the `charge` or `payout`."""

    payment_date: date
    """The desired date on which the payment should be occur.

    For charges, this means the date you want the customer to be debited on. For
    payouts, this means the date you want the funds to be sent from your bank
    account.
    """

    payment_type: PaymentTypeV1
    """The type of payment. Valid values are `charge` or `payout`."""

    status: PaymentStatusV1
    """The current status of the `charge` or `payout`."""

    status_details: StatusDetailsV1
    """Details about the current status of the `charge` or `payout`."""

    updated_at: datetime
    """The time the `charge` or `payout` was last updated."""

    customer_details: Optional[CustomerDetailsV1] = None
    """Information about the customer associated with the charge or payout."""

    effective_at: Optional[datetime] = None
    """The actual date on which the payment occurred.

    For charges, this is the date the customer was debited. For payouts, this is the
    date the funds were sent from your bank account.
    """

    funding_id: Optional[str] = None
    """
    Unique identifier for the funding event associated with the `charge` or
    `payout`.
    """

    paykey_details: Optional[PaykeyDetailsV1] = None
    """Information about the paykey used for the `charge` or `payout`."""


class PaymentSummaryPagedV1(BaseModel):
    data: List[Data]

    meta: PagedResponseMetadata2

    response_type: ResponseTypeEnum
    """Indicates the structure of the returned content.

    - "object" means the `data` field contains a single JSON object.
    - "array" means the `data` field contains an array of objects.
    - "error" means the `data` field contains an error object with details of the
      issue.
    - "none" means no data is returned.
    """
