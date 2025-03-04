# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["PaymentStatusV1"]

PaymentStatusV1: TypeAlias = Literal[
    "created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"
]
