# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel
from .account_type_v1 import AccountTypeV1

__all__ = ["PaykeyBankDetailsV1"]


class PaykeyBankDetailsV1(BaseModel):
    account_number: str
    """Bank account number.

    This value is masked by default for security reasons. Use the /unmask endpoint
    to access the unmasked value.
    """

    account_type: AccountTypeV1

    routing_number: str
    """The routing number of the bank account."""
