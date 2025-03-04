# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RelationshipV1"]


class RelationshipV1(TypedDict, total=False):
    control: Required[bool]
    """
    Whether the representative has significant responsibility to control, manage, or
    direct the organization. One representative must be identified under the control
    prong for each legal entity.
    """

    owner: Required[bool]
    """
    Whether the representative owns any percentage of of the equity interests of the
    legal entity.
    """

    primary: Required[bool]
    """Whether the person is authorized as the primary representative of the account.

    This is the person chosen by the business to provide information about
    themselves, general information about the account, and who consented to the
    services agreement.

    There can be only one primary representative for an account at a time.
    """

    percent_ownership: Optional[float]
    """The percentage of ownership the representative has.

    Required if 'Owner' is true.
    """

    title: Optional[str]
    """The job title of the representative."""
