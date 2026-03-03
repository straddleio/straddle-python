# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import StraddleError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import embed, bridge, charges, paykeys, payouts, reports, payments, customers, funding_events
    from .resources.charges import ChargesResource, AsyncChargesResource
    from .resources.payouts import PayoutsResource, AsyncPayoutsResource
    from .resources.reports import ReportsResource, AsyncReportsResource
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.embed.embed import EmbedResource, AsyncEmbedResource
    from .resources.bridge.bridge import BridgeResource, AsyncBridgeResource
    from .resources.funding_events import FundingEventsResource, AsyncFundingEventsResource
    from .resources.paykeys.paykeys import PaykeysResource, AsyncPaykeysResource
    from .resources.customers.customers import CustomersResource, AsyncCustomersResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Straddle",
    "AsyncStraddle",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "sandbox": "https://sandbox.straddle.com",
    "production": "https://production.straddle.com",
}


class Straddle(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["sandbox", "production"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["sandbox", "production"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Straddle client instance.

        This automatically infers the `api_key` argument from the `STRADDLE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STRADDLE_API_KEY")
        if api_key is None:
            raise StraddleError(
                "The api_key client option must be set either by passing api_key to the client or by setting the STRADDLE_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("STRADDLE_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `STRADDLE_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "sandbox"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

    @cached_property
    def embed(self) -> EmbedResource:
        from .resources.embed import EmbedResource

        return EmbedResource(self)

    @cached_property
    def bridge(self) -> BridgeResource:
        """
        Bridge provides a comprehensive suite of tools for connecting customer bank accounts. Use it to generate secure widget sessions for instant account verification, accept tokens from major providers like Plaid and Finicity, or verify accounts directly via our API. Bridge handles all sensitive banking credentials and ensures secure, compliant connections with support for 90% of US bank accounts.
        """
        from .resources.bridge import BridgeResource

        return BridgeResource(self)

    @cached_property
    def customers(self) -> CustomersResource:
        """
        Customers represent the end users who send or receive payments through your integration. Each customer undergoes automatic identity verification and fraud screening upon creation. Use customers to track payment history, manage bank account connections, and maintain a secure record of all transactions associated with a user. Customers can be either individuals or businesses with appropriate compliance checks for each type.
        """
        from .resources.customers import CustomersResource

        return CustomersResource(self)

    @cached_property
    def paykeys(self) -> PaykeysResource:
        """
        Paykeys are secure tokens that link verified customer identities to their bank accounts. Each Paykey includes built-in balance checking, fraud detection through LSTM machine learning models, and can be reused for subscriptions and recurring payments without storing sensitive data. Paykeys eliminate fraud by ensuring the person initiating payment owns the funding account.
        """
        from .resources.paykeys import PaykeysResource

        return PaykeysResource(self)

    @cached_property
    def charges(self) -> ChargesResource:
        """
        Charges represent attempts to debit money from a customer's bank account using a Paykey. Each charge includes automatic balance verification, real-time fraud screening, and multi-rail optimization and detailed status tracking throughout the payment lifecycle. Use charges to accept bank payments with confidence knowing every transaction is protected.
        """
        from .resources.charges import ChargesResource

        return ChargesResource(self)

    @cached_property
    def funding_events(self) -> FundingEventsResource:
        """
        Funding events represent all money movement between Straddle and an Account's external bank accounts. They are automatically generated when charges settle or payouts are initiated. Each event provides detailed tracking of settlement status, fee breakdowns, and reconciliation data across both incoming and outgoing transfers. Use funding events to monitor your platform's entire money movement lifecycle.
        """
        from .resources.funding_events import FundingEventsResource

        return FundingEventsResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        """
        Payments provide endpoints to filter both Charges and Payouts with multiple different parameters.
        """
        from .resources.payments import PaymentsResource

        return PaymentsResource(self)

    @cached_property
    def payouts(self) -> PayoutsResource:
        """Payouts represent transfers from Straddle to customer bank accounts.

        Create payouts to handle disbursements, process refunds, or manage marketplace settlements. Use payouts to send money quickly and securely with the most cost-effective rail automatically selected.
        """
        from .resources.payouts import PayoutsResource

        return PayoutsResource(self)

    @cached_property
    def reports(self) -> ReportsResource:
        from .resources.reports import ReportsResource

        return ReportsResource(self)

    @cached_property
    def with_raw_response(self) -> StraddleWithRawResponse:
        return StraddleWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StraddleWithStreamedResponse:
        return StraddleWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
        api_key: str | None = None,
        environment: Literal["sandbox", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
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
    # client options
    api_key: str

    _environment: Literal["sandbox", "production"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["sandbox", "production"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncStraddle client instance.

        This automatically infers the `api_key` argument from the `STRADDLE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STRADDLE_API_KEY")
        if api_key is None:
            raise StraddleError(
                "The api_key client option must be set either by passing api_key to the client or by setting the STRADDLE_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("STRADDLE_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `STRADDLE_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "sandbox"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

    @cached_property
    def embed(self) -> AsyncEmbedResource:
        from .resources.embed import AsyncEmbedResource

        return AsyncEmbedResource(self)

    @cached_property
    def bridge(self) -> AsyncBridgeResource:
        """
        Bridge provides a comprehensive suite of tools for connecting customer bank accounts. Use it to generate secure widget sessions for instant account verification, accept tokens from major providers like Plaid and Finicity, or verify accounts directly via our API. Bridge handles all sensitive banking credentials and ensures secure, compliant connections with support for 90% of US bank accounts.
        """
        from .resources.bridge import AsyncBridgeResource

        return AsyncBridgeResource(self)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        """
        Customers represent the end users who send or receive payments through your integration. Each customer undergoes automatic identity verification and fraud screening upon creation. Use customers to track payment history, manage bank account connections, and maintain a secure record of all transactions associated with a user. Customers can be either individuals or businesses with appropriate compliance checks for each type.
        """
        from .resources.customers import AsyncCustomersResource

        return AsyncCustomersResource(self)

    @cached_property
    def paykeys(self) -> AsyncPaykeysResource:
        """
        Paykeys are secure tokens that link verified customer identities to their bank accounts. Each Paykey includes built-in balance checking, fraud detection through LSTM machine learning models, and can be reused for subscriptions and recurring payments without storing sensitive data. Paykeys eliminate fraud by ensuring the person initiating payment owns the funding account.
        """
        from .resources.paykeys import AsyncPaykeysResource

        return AsyncPaykeysResource(self)

    @cached_property
    def charges(self) -> AsyncChargesResource:
        """
        Charges represent attempts to debit money from a customer's bank account using a Paykey. Each charge includes automatic balance verification, real-time fraud screening, and multi-rail optimization and detailed status tracking throughout the payment lifecycle. Use charges to accept bank payments with confidence knowing every transaction is protected.
        """
        from .resources.charges import AsyncChargesResource

        return AsyncChargesResource(self)

    @cached_property
    def funding_events(self) -> AsyncFundingEventsResource:
        """
        Funding events represent all money movement between Straddle and an Account's external bank accounts. They are automatically generated when charges settle or payouts are initiated. Each event provides detailed tracking of settlement status, fee breakdowns, and reconciliation data across both incoming and outgoing transfers. Use funding events to monitor your platform's entire money movement lifecycle.
        """
        from .resources.funding_events import AsyncFundingEventsResource

        return AsyncFundingEventsResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        """
        Payments provide endpoints to filter both Charges and Payouts with multiple different parameters.
        """
        from .resources.payments import AsyncPaymentsResource

        return AsyncPaymentsResource(self)

    @cached_property
    def payouts(self) -> AsyncPayoutsResource:
        """Payouts represent transfers from Straddle to customer bank accounts.

        Create payouts to handle disbursements, process refunds, or manage marketplace settlements. Use payouts to send money quickly and securely with the most cost-effective rail automatically selected.
        """
        from .resources.payouts import AsyncPayoutsResource

        return AsyncPayoutsResource(self)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        from .resources.reports import AsyncReportsResource

        return AsyncReportsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncStraddleWithRawResponse:
        return AsyncStraddleWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStraddleWithStreamedResponse:
        return AsyncStraddleWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
        api_key: str | None = None,
        environment: Literal["sandbox", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
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
    _client: Straddle

    def __init__(self, client: Straddle) -> None:
        self._client = client

    @cached_property
    def embed(self) -> embed.EmbedResourceWithRawResponse:
        from .resources.embed import EmbedResourceWithRawResponse

        return EmbedResourceWithRawResponse(self._client.embed)

    @cached_property
    def bridge(self) -> bridge.BridgeResourceWithRawResponse:
        """
        Bridge provides a comprehensive suite of tools for connecting customer bank accounts. Use it to generate secure widget sessions for instant account verification, accept tokens from major providers like Plaid and Finicity, or verify accounts directly via our API. Bridge handles all sensitive banking credentials and ensures secure, compliant connections with support for 90% of US bank accounts.
        """
        from .resources.bridge import BridgeResourceWithRawResponse

        return BridgeResourceWithRawResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithRawResponse:
        """
        Customers represent the end users who send or receive payments through your integration. Each customer undergoes automatic identity verification and fraud screening upon creation. Use customers to track payment history, manage bank account connections, and maintain a secure record of all transactions associated with a user. Customers can be either individuals or businesses with appropriate compliance checks for each type.
        """
        from .resources.customers import CustomersResourceWithRawResponse

        return CustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.PaykeysResourceWithRawResponse:
        """
        Paykeys are secure tokens that link verified customer identities to their bank accounts. Each Paykey includes built-in balance checking, fraud detection through LSTM machine learning models, and can be reused for subscriptions and recurring payments without storing sensitive data. Paykeys eliminate fraud by ensuring the person initiating payment owns the funding account.
        """
        from .resources.paykeys import PaykeysResourceWithRawResponse

        return PaykeysResourceWithRawResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.ChargesResourceWithRawResponse:
        """
        Charges represent attempts to debit money from a customer's bank account using a Paykey. Each charge includes automatic balance verification, real-time fraud screening, and multi-rail optimization and detailed status tracking throughout the payment lifecycle. Use charges to accept bank payments with confidence knowing every transaction is protected.
        """
        from .resources.charges import ChargesResourceWithRawResponse

        return ChargesResourceWithRawResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.FundingEventsResourceWithRawResponse:
        """
        Funding events represent all money movement between Straddle and an Account's external bank accounts. They are automatically generated when charges settle or payouts are initiated. Each event provides detailed tracking of settlement status, fee breakdowns, and reconciliation data across both incoming and outgoing transfers. Use funding events to monitor your platform's entire money movement lifecycle.
        """
        from .resources.funding_events import FundingEventsResourceWithRawResponse

        return FundingEventsResourceWithRawResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        """
        Payments provide endpoints to filter both Charges and Payouts with multiple different parameters.
        """
        from .resources.payments import PaymentsResourceWithRawResponse

        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithRawResponse:
        """Payouts represent transfers from Straddle to customer bank accounts.

        Create payouts to handle disbursements, process refunds, or manage marketplace settlements. Use payouts to send money quickly and securely with the most cost-effective rail automatically selected.
        """
        from .resources.payouts import PayoutsResourceWithRawResponse

        return PayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithRawResponse:
        from .resources.reports import ReportsResourceWithRawResponse

        return ReportsResourceWithRawResponse(self._client.reports)


class AsyncStraddleWithRawResponse:
    _client: AsyncStraddle

    def __init__(self, client: AsyncStraddle) -> None:
        self._client = client

    @cached_property
    def embed(self) -> embed.AsyncEmbedResourceWithRawResponse:
        from .resources.embed import AsyncEmbedResourceWithRawResponse

        return AsyncEmbedResourceWithRawResponse(self._client.embed)

    @cached_property
    def bridge(self) -> bridge.AsyncBridgeResourceWithRawResponse:
        """
        Bridge provides a comprehensive suite of tools for connecting customer bank accounts. Use it to generate secure widget sessions for instant account verification, accept tokens from major providers like Plaid and Finicity, or verify accounts directly via our API. Bridge handles all sensitive banking credentials and ensures secure, compliant connections with support for 90% of US bank accounts.
        """
        from .resources.bridge import AsyncBridgeResourceWithRawResponse

        return AsyncBridgeResourceWithRawResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithRawResponse:
        """
        Customers represent the end users who send or receive payments through your integration. Each customer undergoes automatic identity verification and fraud screening upon creation. Use customers to track payment history, manage bank account connections, and maintain a secure record of all transactions associated with a user. Customers can be either individuals or businesses with appropriate compliance checks for each type.
        """
        from .resources.customers import AsyncCustomersResourceWithRawResponse

        return AsyncCustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.AsyncPaykeysResourceWithRawResponse:
        """
        Paykeys are secure tokens that link verified customer identities to their bank accounts. Each Paykey includes built-in balance checking, fraud detection through LSTM machine learning models, and can be reused for subscriptions and recurring payments without storing sensitive data. Paykeys eliminate fraud by ensuring the person initiating payment owns the funding account.
        """
        from .resources.paykeys import AsyncPaykeysResourceWithRawResponse

        return AsyncPaykeysResourceWithRawResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.AsyncChargesResourceWithRawResponse:
        """
        Charges represent attempts to debit money from a customer's bank account using a Paykey. Each charge includes automatic balance verification, real-time fraud screening, and multi-rail optimization and detailed status tracking throughout the payment lifecycle. Use charges to accept bank payments with confidence knowing every transaction is protected.
        """
        from .resources.charges import AsyncChargesResourceWithRawResponse

        return AsyncChargesResourceWithRawResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.AsyncFundingEventsResourceWithRawResponse:
        """
        Funding events represent all money movement between Straddle and an Account's external bank accounts. They are automatically generated when charges settle or payouts are initiated. Each event provides detailed tracking of settlement status, fee breakdowns, and reconciliation data across both incoming and outgoing transfers. Use funding events to monitor your platform's entire money movement lifecycle.
        """
        from .resources.funding_events import AsyncFundingEventsResourceWithRawResponse

        return AsyncFundingEventsResourceWithRawResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        """
        Payments provide endpoints to filter both Charges and Payouts with multiple different parameters.
        """
        from .resources.payments import AsyncPaymentsResourceWithRawResponse

        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithRawResponse:
        """Payouts represent transfers from Straddle to customer bank accounts.

        Create payouts to handle disbursements, process refunds, or manage marketplace settlements. Use payouts to send money quickly and securely with the most cost-effective rail automatically selected.
        """
        from .resources.payouts import AsyncPayoutsResourceWithRawResponse

        return AsyncPayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithRawResponse:
        from .resources.reports import AsyncReportsResourceWithRawResponse

        return AsyncReportsResourceWithRawResponse(self._client.reports)


class StraddleWithStreamedResponse:
    _client: Straddle

    def __init__(self, client: Straddle) -> None:
        self._client = client

    @cached_property
    def embed(self) -> embed.EmbedResourceWithStreamingResponse:
        from .resources.embed import EmbedResourceWithStreamingResponse

        return EmbedResourceWithStreamingResponse(self._client.embed)

    @cached_property
    def bridge(self) -> bridge.BridgeResourceWithStreamingResponse:
        """
        Bridge provides a comprehensive suite of tools for connecting customer bank accounts. Use it to generate secure widget sessions for instant account verification, accept tokens from major providers like Plaid and Finicity, or verify accounts directly via our API. Bridge handles all sensitive banking credentials and ensures secure, compliant connections with support for 90% of US bank accounts.
        """
        from .resources.bridge import BridgeResourceWithStreamingResponse

        return BridgeResourceWithStreamingResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithStreamingResponse:
        """
        Customers represent the end users who send or receive payments through your integration. Each customer undergoes automatic identity verification and fraud screening upon creation. Use customers to track payment history, manage bank account connections, and maintain a secure record of all transactions associated with a user. Customers can be either individuals or businesses with appropriate compliance checks for each type.
        """
        from .resources.customers import CustomersResourceWithStreamingResponse

        return CustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.PaykeysResourceWithStreamingResponse:
        """
        Paykeys are secure tokens that link verified customer identities to their bank accounts. Each Paykey includes built-in balance checking, fraud detection through LSTM machine learning models, and can be reused for subscriptions and recurring payments without storing sensitive data. Paykeys eliminate fraud by ensuring the person initiating payment owns the funding account.
        """
        from .resources.paykeys import PaykeysResourceWithStreamingResponse

        return PaykeysResourceWithStreamingResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.ChargesResourceWithStreamingResponse:
        """
        Charges represent attempts to debit money from a customer's bank account using a Paykey. Each charge includes automatic balance verification, real-time fraud screening, and multi-rail optimization and detailed status tracking throughout the payment lifecycle. Use charges to accept bank payments with confidence knowing every transaction is protected.
        """
        from .resources.charges import ChargesResourceWithStreamingResponse

        return ChargesResourceWithStreamingResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.FundingEventsResourceWithStreamingResponse:
        """
        Funding events represent all money movement between Straddle and an Account's external bank accounts. They are automatically generated when charges settle or payouts are initiated. Each event provides detailed tracking of settlement status, fee breakdowns, and reconciliation data across both incoming and outgoing transfers. Use funding events to monitor your platform's entire money movement lifecycle.
        """
        from .resources.funding_events import FundingEventsResourceWithStreamingResponse

        return FundingEventsResourceWithStreamingResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        """
        Payments provide endpoints to filter both Charges and Payouts with multiple different parameters.
        """
        from .resources.payments import PaymentsResourceWithStreamingResponse

        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithStreamingResponse:
        """Payouts represent transfers from Straddle to customer bank accounts.

        Create payouts to handle disbursements, process refunds, or manage marketplace settlements. Use payouts to send money quickly and securely with the most cost-effective rail automatically selected.
        """
        from .resources.payouts import PayoutsResourceWithStreamingResponse

        return PayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithStreamingResponse:
        from .resources.reports import ReportsResourceWithStreamingResponse

        return ReportsResourceWithStreamingResponse(self._client.reports)


class AsyncStraddleWithStreamedResponse:
    _client: AsyncStraddle

    def __init__(self, client: AsyncStraddle) -> None:
        self._client = client

    @cached_property
    def embed(self) -> embed.AsyncEmbedResourceWithStreamingResponse:
        from .resources.embed import AsyncEmbedResourceWithStreamingResponse

        return AsyncEmbedResourceWithStreamingResponse(self._client.embed)

    @cached_property
    def bridge(self) -> bridge.AsyncBridgeResourceWithStreamingResponse:
        """
        Bridge provides a comprehensive suite of tools for connecting customer bank accounts. Use it to generate secure widget sessions for instant account verification, accept tokens from major providers like Plaid and Finicity, or verify accounts directly via our API. Bridge handles all sensitive banking credentials and ensures secure, compliant connections with support for 90% of US bank accounts.
        """
        from .resources.bridge import AsyncBridgeResourceWithStreamingResponse

        return AsyncBridgeResourceWithStreamingResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithStreamingResponse:
        """
        Customers represent the end users who send or receive payments through your integration. Each customer undergoes automatic identity verification and fraud screening upon creation. Use customers to track payment history, manage bank account connections, and maintain a secure record of all transactions associated with a user. Customers can be either individuals or businesses with appropriate compliance checks for each type.
        """
        from .resources.customers import AsyncCustomersResourceWithStreamingResponse

        return AsyncCustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.AsyncPaykeysResourceWithStreamingResponse:
        """
        Paykeys are secure tokens that link verified customer identities to their bank accounts. Each Paykey includes built-in balance checking, fraud detection through LSTM machine learning models, and can be reused for subscriptions and recurring payments without storing sensitive data. Paykeys eliminate fraud by ensuring the person initiating payment owns the funding account.
        """
        from .resources.paykeys import AsyncPaykeysResourceWithStreamingResponse

        return AsyncPaykeysResourceWithStreamingResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.AsyncChargesResourceWithStreamingResponse:
        """
        Charges represent attempts to debit money from a customer's bank account using a Paykey. Each charge includes automatic balance verification, real-time fraud screening, and multi-rail optimization and detailed status tracking throughout the payment lifecycle. Use charges to accept bank payments with confidence knowing every transaction is protected.
        """
        from .resources.charges import AsyncChargesResourceWithStreamingResponse

        return AsyncChargesResourceWithStreamingResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.AsyncFundingEventsResourceWithStreamingResponse:
        """
        Funding events represent all money movement between Straddle and an Account's external bank accounts. They are automatically generated when charges settle or payouts are initiated. Each event provides detailed tracking of settlement status, fee breakdowns, and reconciliation data across both incoming and outgoing transfers. Use funding events to monitor your platform's entire money movement lifecycle.
        """
        from .resources.funding_events import AsyncFundingEventsResourceWithStreamingResponse

        return AsyncFundingEventsResourceWithStreamingResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        """
        Payments provide endpoints to filter both Charges and Payouts with multiple different parameters.
        """
        from .resources.payments import AsyncPaymentsResourceWithStreamingResponse

        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithStreamingResponse:
        """Payouts represent transfers from Straddle to customer bank accounts.

        Create payouts to handle disbursements, process refunds, or manage marketplace settlements. Use payouts to send money quickly and securely with the most cost-effective rail automatically selected.
        """
        from .resources.payouts import AsyncPayoutsResourceWithStreamingResponse

        return AsyncPayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithStreamingResponse:
        from .resources.reports import AsyncReportsResourceWithStreamingResponse

        return AsyncReportsResourceWithStreamingResponse(self._client.reports)


Client = Straddle

AsyncClient = AsyncStraddle
