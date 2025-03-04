# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BankAccountV1Request"]


class BankAccountV1Request(TypedDict, total=False):
    account_holder: Required[str]
    """The name of the account holder as it appears on the bank account.

    Typically, this is the legal name of the business associated with the account.
    """

    account_number: Required[str]
    """The bank account number."""

    routing_number: Required[str]
    """The routing number of the bank account."""
