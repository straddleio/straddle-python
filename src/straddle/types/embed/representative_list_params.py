# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RepresentativeListParams"]


class RepresentativeListParams(TypedDict, total=False):
    page_number: Required[int]
    """Results page number. Starts at page 1. Default value: 1"""

    page_size: Required[int]
    """Page size. Default value: 100. Max value: 1000"""

    sort_by: Required[str]
    """Sort By. Default value: 'id'."""

    sort_order: Required[Literal["asc", "desc"]]
    """Sort Order. Default value: 'asc'."""

    account_id: str
    """The unique identifier of the account to list representatives for."""

    organization_id: str

    platform_id: str

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]
