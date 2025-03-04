# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["UpdatePayoutStatusV1Request"]


class UpdatePayoutStatusV1Request(BaseModel):
    reason: str
    """Details about why the payout status was updated."""
