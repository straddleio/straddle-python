# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["BankAccountV1Request"]


class BankAccountV1Request(BaseModel):
    account_holder: str
    """The name of the account holder as it appears on the bank account.

    Typically, this is the legal name of the business associated with the account.
    """

    account_number: str
    """The bank account number."""

    routing_number: str
    """The routing number of the bank account."""
