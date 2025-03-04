# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .identity_decision_v1 import IdentityDecisionV1

__all__ = ["IdentityVerificationBreakdownV1"]


class IdentityVerificationBreakdownV1(BaseModel):
    codes: Optional[List[str]] = None
    """List of specific result codes from the fraud and risk screening."""

    correlation_score: Optional[float] = None
    """
    Represents the strength of the correlation between provided and known
    information. A higher score indicates a stronger correlation.
    """

    decision: Optional[IdentityDecisionV1] = None

    risk_score: Optional[float] = None
    """Predicts the inherent risk associated with the customer for a given module.

    A higher score indicates a greater likelihood of fraud.
    """
