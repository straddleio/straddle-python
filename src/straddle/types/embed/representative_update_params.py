# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.relationship_v1 import RelationshipV1

__all__ = ["RepresentativeUpdateParams"]


class RepresentativeUpdateParams(TypedDict, total=False):
    dob: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The date of birth of the representative, in ISO 8601 format (YYYY-MM-DD)."""

    email: Required[str]
    """The email address of the representative."""

    first_name: Required[str]
    """The first name of the representative."""

    last_name: Required[str]
    """The last name of the representative."""

    mobile_number: Required[str]
    """The mobile phone number of the representative."""

    relationship: Required[RelationshipV1]

    ssn_last4: Required[str]
    """The last 4 digits of the representative's Social Security Number."""

    external_id: Optional[str]
    """
    Unique identifier for the representative in your database, used for
    cross-referencing between Straddle and your systems.
    """

    correlation_id: Annotated[str, PropertyInfo(alias="correlation-id")]

    request_id: Annotated[str, PropertyInfo(alias="request-id")]
