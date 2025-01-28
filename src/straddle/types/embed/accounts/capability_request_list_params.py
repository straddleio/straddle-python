# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CapabilityRequestListParams"]


class CapabilityRequestListParams(TypedDict, total=False):
    page_number: Required[int]
    """Results page number. Starts at page 1. Default value: 1"""

    page_size: Required[int]
    """Page size. Default value: 100. Max value: 1000"""

    sort_by: Required[str]
    """Sort By. Default value: 'id'."""

    sort_order: Required[Literal["asc", "desc"]]
    """Sort Order. Default value: 'asc'."""

    category: Literal["payment_type", "customer_type", "consent_type"]
    """Filter capability requests by category.

    Possible values: 'payment_type', 'customer_type', 'consent_type'.
    """

    status: Literal["approved", "rejected", "reviewing"]
    """Filter capability requests by their current status.

    Possible values: 'active', 'inactive', 'in_review', 'rejected'.
    """

    type: Literal["charges", "payouts", "individuals", "businesses", "signed_agreement", "internet"]
    """Filter capability requests by the specific type of capability.

    Possible values: 'charges', 'payouts', 'individuals', 'businesses',
    'signed_agreement', 'internet'.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]
