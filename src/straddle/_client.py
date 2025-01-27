# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    charges,
    paykeys,
    payouts,
    reports,
    payments,
    organizations,
    funding_events,
    representatives,
    linked_bank_accounts,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import StraddleError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.bridge import bridge
from .resources.accounts import accounts
from .resources.customers import customers

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Straddle",
    "AsyncStraddle",
    "Client",
    "AsyncClient",
]


class Straddle(SyncAPIClient):
    accounts: accounts.AccountsResource
    linked_bank_accounts: linked_bank_accounts.LinkedBankAccountsResource
    organizations: organizations.OrganizationsResource
    representatives: representatives.RepresentativesResource
    bridge: bridge.BridgeResource
    customers: customers.CustomersResource
    paykeys: paykeys.PaykeysResource
    reports: reports.ReportsResource
    charges: charges.ChargesResource
    funding_events: funding_events.FundingEventsResource
    payments: payments.PaymentsResource
    payouts: payouts.PayoutsResource
    with_raw_response: StraddleWithRawResponse
    with_streaming_response: StraddleWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous straddle client instance.

        This automatically infers the `bearer_token` argument from the `STRADDLE_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("STRADDLE_BEARER_TOKEN")
        if bearer_token is None:
            raise StraddleError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the STRADDLE_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("STRADDLE_BASE_URL")
        if base_url is None:
            base_url = f"https://{environment}.straddle.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AccountsResource(self)
        self.linked_bank_accounts = linked_bank_accounts.LinkedBankAccountsResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.representatives = representatives.RepresentativesResource(self)
        self.bridge = bridge.BridgeResource(self)
        self.customers = customers.CustomersResource(self)
        self.paykeys = paykeys.PaykeysResource(self)
        self.reports = reports.ReportsResource(self)
        self.charges = charges.ChargesResource(self)
        self.funding_events = funding_events.FundingEventsResource(self)
        self.payments = payments.PaymentsResource(self)
        self.payouts = payouts.PayoutsResource(self)
        self.with_raw_response = StraddleWithRawResponse(self)
        self.with_streaming_response = StraddleWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncStraddle(AsyncAPIClient):
    accounts: accounts.AsyncAccountsResource
    linked_bank_accounts: linked_bank_accounts.AsyncLinkedBankAccountsResource
    organizations: organizations.AsyncOrganizationsResource
    representatives: representatives.AsyncRepresentativesResource
    bridge: bridge.AsyncBridgeResource
    customers: customers.AsyncCustomersResource
    paykeys: paykeys.AsyncPaykeysResource
    reports: reports.AsyncReportsResource
    charges: charges.AsyncChargesResource
    funding_events: funding_events.AsyncFundingEventsResource
    payments: payments.AsyncPaymentsResource
    payouts: payouts.AsyncPayoutsResource
    with_raw_response: AsyncStraddleWithRawResponse
    with_streaming_response: AsyncStraddleWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async straddle client instance.

        This automatically infers the `bearer_token` argument from the `STRADDLE_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("STRADDLE_BEARER_TOKEN")
        if bearer_token is None:
            raise StraddleError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the STRADDLE_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("STRADDLE_BASE_URL")
        if base_url is None:
            base_url = f"https://{environment}.straddle.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AsyncAccountsResource(self)
        self.linked_bank_accounts = linked_bank_accounts.AsyncLinkedBankAccountsResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.representatives = representatives.AsyncRepresentativesResource(self)
        self.bridge = bridge.AsyncBridgeResource(self)
        self.customers = customers.AsyncCustomersResource(self)
        self.paykeys = paykeys.AsyncPaykeysResource(self)
        self.reports = reports.AsyncReportsResource(self)
        self.charges = charges.AsyncChargesResource(self)
        self.funding_events = funding_events.AsyncFundingEventsResource(self)
        self.payments = payments.AsyncPaymentsResource(self)
        self.payouts = payouts.AsyncPayoutsResource(self)
        self.with_raw_response = AsyncStraddleWithRawResponse(self)
        self.with_streaming_response = AsyncStraddleWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class StraddleWithRawResponse:
    def __init__(self, client: Straddle) -> None:
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.linked_bank_accounts = linked_bank_accounts.LinkedBankAccountsResourceWithRawResponse(
            client.linked_bank_accounts
        )
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.representatives = representatives.RepresentativesResourceWithRawResponse(client.representatives)
        self.bridge = bridge.BridgeResourceWithRawResponse(client.bridge)
        self.customers = customers.CustomersResourceWithRawResponse(client.customers)
        self.paykeys = paykeys.PaykeysResourceWithRawResponse(client.paykeys)
        self.reports = reports.ReportsResourceWithRawResponse(client.reports)
        self.charges = charges.ChargesResourceWithRawResponse(client.charges)
        self.funding_events = funding_events.FundingEventsResourceWithRawResponse(client.funding_events)
        self.payments = payments.PaymentsResourceWithRawResponse(client.payments)
        self.payouts = payouts.PayoutsResourceWithRawResponse(client.payouts)


class AsyncStraddleWithRawResponse:
    def __init__(self, client: AsyncStraddle) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.linked_bank_accounts = linked_bank_accounts.AsyncLinkedBankAccountsResourceWithRawResponse(
            client.linked_bank_accounts
        )
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.representatives = representatives.AsyncRepresentativesResourceWithRawResponse(client.representatives)
        self.bridge = bridge.AsyncBridgeResourceWithRawResponse(client.bridge)
        self.customers = customers.AsyncCustomersResourceWithRawResponse(client.customers)
        self.paykeys = paykeys.AsyncPaykeysResourceWithRawResponse(client.paykeys)
        self.reports = reports.AsyncReportsResourceWithRawResponse(client.reports)
        self.charges = charges.AsyncChargesResourceWithRawResponse(client.charges)
        self.funding_events = funding_events.AsyncFundingEventsResourceWithRawResponse(client.funding_events)
        self.payments = payments.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.payouts = payouts.AsyncPayoutsResourceWithRawResponse(client.payouts)


class StraddleWithStreamedResponse:
    def __init__(self, client: Straddle) -> None:
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.linked_bank_accounts = linked_bank_accounts.LinkedBankAccountsResourceWithStreamingResponse(
            client.linked_bank_accounts
        )
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.representatives = representatives.RepresentativesResourceWithStreamingResponse(client.representatives)
        self.bridge = bridge.BridgeResourceWithStreamingResponse(client.bridge)
        self.customers = customers.CustomersResourceWithStreamingResponse(client.customers)
        self.paykeys = paykeys.PaykeysResourceWithStreamingResponse(client.paykeys)
        self.reports = reports.ReportsResourceWithStreamingResponse(client.reports)
        self.charges = charges.ChargesResourceWithStreamingResponse(client.charges)
        self.funding_events = funding_events.FundingEventsResourceWithStreamingResponse(client.funding_events)
        self.payments = payments.PaymentsResourceWithStreamingResponse(client.payments)
        self.payouts = payouts.PayoutsResourceWithStreamingResponse(client.payouts)


class AsyncStraddleWithStreamedResponse:
    def __init__(self, client: AsyncStraddle) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.linked_bank_accounts = linked_bank_accounts.AsyncLinkedBankAccountsResourceWithStreamingResponse(
            client.linked_bank_accounts
        )
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.representatives = representatives.AsyncRepresentativesResourceWithStreamingResponse(client.representatives)
        self.bridge = bridge.AsyncBridgeResourceWithStreamingResponse(client.bridge)
        self.customers = customers.AsyncCustomersResourceWithStreamingResponse(client.customers)
        self.paykeys = paykeys.AsyncPaykeysResourceWithStreamingResponse(client.paykeys)
        self.reports = reports.AsyncReportsResourceWithStreamingResponse(client.reports)
        self.charges = charges.AsyncChargesResourceWithStreamingResponse(client.charges)
        self.funding_events = funding_events.AsyncFundingEventsResourceWithStreamingResponse(client.funding_events)
        self.payments = payments.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.payouts = payouts.AsyncPayoutsResourceWithStreamingResponse(client.payouts)


Client = Straddle

AsyncClient = AsyncStraddle
