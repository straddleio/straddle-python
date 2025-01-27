# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import bridge_plaid_params, bridge_initialize_params, bridge_bank_account_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.paykey import Paykey
from ..types.bridge_token import BridgeToken

__all__ = ["BridgeResource", "AsyncBridgeResource"]


class BridgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BridgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/straddle-python#accessing-raw-response-data-eg-headers
        """
        return BridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BridgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/straddle-python#with_streaming_response
        """
        return BridgeResourceWithStreamingResponse(self)

    def bank_account(
        self,
        *,
        account_number: str,
        account_type: Literal["checking", "savings"],
        customer_id: str,
        routing_number: str,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        straddle_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Paykey:
        """
        Use Bridge to create a new paykey using a bank routing and account number as the
        source. This endpoint allows you to create a secure payment token linked to a
        specific bank account.

        Args:
          account_number: The bank account number.

          customer_id: Unique identifier of the related customer object.

          routing_number: The routing number of the bank account.

          metadata: Up to 20 additional user-defined key-value pairs. Useful for storing additional
              information about the paykey in a structured format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Correlation-Id": correlation_id,
                    "Request-Id": request_id,
                    "Straddle-Account-Id": straddle_account_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/bridge/bank_account",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "account_type": account_type,
                    "customer_id": customer_id,
                    "routing_number": routing_number,
                    "metadata": metadata,
                },
                bridge_bank_account_params.BridgeBankAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Paykey,
        )

    def initialize(
        self,
        *,
        customer_id: str,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        straddle_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BridgeToken:
        """
        Use this endpoint to generate a session token for use in the Bridge widget.

        Args:
          customer_id: The Straddle generated unique identifier of the `customer` to create a bridge
              token for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Correlation-Id": correlation_id,
                    "Request-Id": request_id,
                    "Straddle-Account-Id": straddle_account_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/bridge/initialize",
            body=maybe_transform({"customer_id": customer_id}, bridge_initialize_params.BridgeInitializeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeToken,
        )

    def plaid(
        self,
        *,
        customer_id: str,
        plaid_token: str,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        straddle_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Paykey:
        """Use Bridge to create a new paykey using a Plaid token as the source.

        This
        endpoint allows you to create a secure payment token linked to a bank account
        authenticated through Plaid.

        Args:
          customer_id: Unique identifier of the related customer object.

          plaid_token: Plaid processor token generated by your application for use with the Straddle
              API.

          metadata: Up to 20 additional user-defined key-value pairs. Useful for storing additional
              information about the paykey in a structured format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Correlation-Id": correlation_id,
                    "Request-Id": request_id,
                    "Straddle-Account-Id": straddle_account_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/bridge/plaid",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "plaid_token": plaid_token,
                    "metadata": metadata,
                },
                bridge_plaid_params.BridgePlaidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Paykey,
        )


class AsyncBridgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBridgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/straddle-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBridgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/straddle-python#with_streaming_response
        """
        return AsyncBridgeResourceWithStreamingResponse(self)

    async def bank_account(
        self,
        *,
        account_number: str,
        account_type: Literal["checking", "savings"],
        customer_id: str,
        routing_number: str,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        straddle_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Paykey:
        """
        Use Bridge to create a new paykey using a bank routing and account number as the
        source. This endpoint allows you to create a secure payment token linked to a
        specific bank account.

        Args:
          account_number: The bank account number.

          customer_id: Unique identifier of the related customer object.

          routing_number: The routing number of the bank account.

          metadata: Up to 20 additional user-defined key-value pairs. Useful for storing additional
              information about the paykey in a structured format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Correlation-Id": correlation_id,
                    "Request-Id": request_id,
                    "Straddle-Account-Id": straddle_account_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/bridge/bank_account",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "account_type": account_type,
                    "customer_id": customer_id,
                    "routing_number": routing_number,
                    "metadata": metadata,
                },
                bridge_bank_account_params.BridgeBankAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Paykey,
        )

    async def initialize(
        self,
        *,
        customer_id: str,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        straddle_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BridgeToken:
        """
        Use this endpoint to generate a session token for use in the Bridge widget.

        Args:
          customer_id: The Straddle generated unique identifier of the `customer` to create a bridge
              token for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Correlation-Id": correlation_id,
                    "Request-Id": request_id,
                    "Straddle-Account-Id": straddle_account_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/bridge/initialize",
            body=await async_maybe_transform(
                {"customer_id": customer_id}, bridge_initialize_params.BridgeInitializeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeToken,
        )

    async def plaid(
        self,
        *,
        customer_id: str,
        plaid_token: str,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        straddle_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Paykey:
        """Use Bridge to create a new paykey using a Plaid token as the source.

        This
        endpoint allows you to create a secure payment token linked to a bank account
        authenticated through Plaid.

        Args:
          customer_id: Unique identifier of the related customer object.

          plaid_token: Plaid processor token generated by your application for use with the Straddle
              API.

          metadata: Up to 20 additional user-defined key-value pairs. Useful for storing additional
              information about the paykey in a structured format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Correlation-Id": correlation_id,
                    "Request-Id": request_id,
                    "Straddle-Account-Id": straddle_account_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/bridge/plaid",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "plaid_token": plaid_token,
                    "metadata": metadata,
                },
                bridge_plaid_params.BridgePlaidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Paykey,
        )


class BridgeResourceWithRawResponse:
    def __init__(self, bridge: BridgeResource) -> None:
        self._bridge = bridge

        self.bank_account = to_raw_response_wrapper(
            bridge.bank_account,
        )
        self.initialize = to_raw_response_wrapper(
            bridge.initialize,
        )
        self.plaid = to_raw_response_wrapper(
            bridge.plaid,
        )


class AsyncBridgeResourceWithRawResponse:
    def __init__(self, bridge: AsyncBridgeResource) -> None:
        self._bridge = bridge

        self.bank_account = async_to_raw_response_wrapper(
            bridge.bank_account,
        )
        self.initialize = async_to_raw_response_wrapper(
            bridge.initialize,
        )
        self.plaid = async_to_raw_response_wrapper(
            bridge.plaid,
        )


class BridgeResourceWithStreamingResponse:
    def __init__(self, bridge: BridgeResource) -> None:
        self._bridge = bridge

        self.bank_account = to_streamed_response_wrapper(
            bridge.bank_account,
        )
        self.initialize = to_streamed_response_wrapper(
            bridge.initialize,
        )
        self.plaid = to_streamed_response_wrapper(
            bridge.plaid,
        )


class AsyncBridgeResourceWithStreamingResponse:
    def __init__(self, bridge: AsyncBridgeResource) -> None:
        self._bridge = bridge

        self.bank_account = async_to_streamed_response_wrapper(
            bridge.bank_account,
        )
        self.initialize = async_to_streamed_response_wrapper(
            bridge.initialize,
        )
        self.plaid = async_to_streamed_response_wrapper(
            bridge.plaid,
        )
