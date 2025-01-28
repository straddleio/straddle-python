# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    page_number: Required[int]
    """Results page number. Starts at page 1. Default value: 1"""

    page_size: Required[int]
    """Page size. Default value: 100. Max value: 1000"""

    sort_order: Required[Literal["asc", "desc"]]
    """Sort Order. Default value: 'asc'."""

    search_text: str

    sort_by: str

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]
