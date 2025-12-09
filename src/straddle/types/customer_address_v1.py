# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CustomerAddressV1"]


class CustomerAddressV1(BaseModel):
    """An object containing the customer's address.

    This is optional, but if provided, all required fields must be present.
    """

    address1: str
    """Primary address line (e.g., street, PO Box)."""

    city: str
    """City, district, suburb, town, or village."""

    state: str
    """Two-letter state code."""

    zip: str
    """Zip or postal code."""

    address2: Optional[str] = None
    """Secondary address line (e.g., apartment, suite, unit, or building)."""
