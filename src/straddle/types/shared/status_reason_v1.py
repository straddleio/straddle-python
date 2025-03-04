# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["StatusReasonV1"]

StatusReasonV1: TypeAlias = Literal[
    "insufficient_funds",
    "closed_bank_account",
    "invalid_bank_account",
    "invalid_routing",
    "disputed",
    "payment_stopped",
    "owner_deceased",
    "frozen_bank_account",
    "risk_review",
    "fraudulent",
    "duplicate_entry",
    "invalid_paykey",
    "payment_blocked",
    "amount_too_large",
    "too_many_attempts",
    "internal_system_error",
    "user_request",
    "ok",
    "other_network_return",
    "payout_refused",
]
