# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPageNumberSchema, AsyncPageNumberSchema
from ...._base_client import AsyncPaginator, make_request_options
from ....types.embed.accounts import capability_request_list_params, capability_request_create_params
from ....types.embed.accounts.capability_request_paged import Data, CapabilityRequestPaged

__all__ = ["CapabilityRequestsResource", "AsyncCapabilityRequestsResource"]


class CapabilityRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CapabilityRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/straddleio/straddle-python#accessing-raw-response-data-eg-headers
        """
        return CapabilityRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilityRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/straddleio/straddle-python#with_streaming_response
        """
        return CapabilityRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        businesses: capability_request_create_params.Businesses | NotGiven = NOT_GIVEN,
        charges: capability_request_create_params.Charges | NotGiven = NOT_GIVEN,
        individuals: capability_request_create_params.Individuals | NotGiven = NOT_GIVEN,
        internet: capability_request_create_params.Internet | NotGiven = NOT_GIVEN,
        payouts: capability_request_create_params.Payouts | NotGiven = NOT_GIVEN,
        signed_agreement: capability_request_create_params.SignedAgreement | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CapabilityRequestPaged:
        """Submits a new request to enable a specific capability for an account.

        Use this
        endpoint to request additional features or services for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "correlation-id": correlation_id,
                    "request-id": request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            f"/v1/accounts/{account_id}/capability_requests",
            body=maybe_transform(
                {
                    "businesses": businesses,
                    "charges": charges,
                    "individuals": individuals,
                    "internet": internet,
                    "payouts": payouts,
                    "signed_agreement": signed_agreement,
                },
                capability_request_create_params.CapabilityRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRequestPaged,
        )

    def list(
        self,
        account_id: str,
        *,
        page_number: int,
        page_size: int,
        sort_by: str,
        sort_order: Literal["asc", "desc"],
        category: Literal["payment_type", "customer_type", "consent_type"] | NotGiven = NOT_GIVEN,
        status: Literal["approved", "rejected", "reviewing"] | NotGiven = NOT_GIVEN,
        type: Literal["charges", "payouts", "individuals", "businesses", "signed_agreement", "internet"]
        | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageNumberSchema[Data]:
        """Retrieves a list of capability requests associated with an account.

        The requests
        are returned sorted by creation date, with the most recent requests appearing
        first. This endpoint supports filtering options to help you track the status of
        various capability requests.

        Args:
          page_number: Results page number. Starts at page 1. Default value: 1

          page_size: Page size. Default value: 100. Max value: 1000

          sort_by: Sort By. Default value: 'id'.

          sort_order: Sort Order. Default value: 'asc'.

          category: Filter capability requests by category. Possible values: 'payment_type',
              'customer_type', 'consent_type'.

          status: Filter capability requests by their current status. Possible values: 'active',
              'inactive', 'in_review', 'rejected'.

          type:
              Filter capability requests by the specific type of capability. Possible values:
              'charges', 'payouts', 'individuals', 'businesses', 'signed_agreement',
              'internet'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "correlation-id": correlation_id,
                    "request-id": request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            f"/v1/accounts/{account_id}/capability_requests",
            page=SyncPageNumberSchema[Data],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "category": category,
                        "status": status,
                        "type": type,
                    },
                    capability_request_list_params.CapabilityRequestListParams,
                ),
            ),
            model=Data,
        )


class AsyncCapabilityRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCapabilityRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/straddleio/straddle-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilityRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilityRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/straddleio/straddle-python#with_streaming_response
        """
        return AsyncCapabilityRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        businesses: capability_request_create_params.Businesses | NotGiven = NOT_GIVEN,
        charges: capability_request_create_params.Charges | NotGiven = NOT_GIVEN,
        individuals: capability_request_create_params.Individuals | NotGiven = NOT_GIVEN,
        internet: capability_request_create_params.Internet | NotGiven = NOT_GIVEN,
        payouts: capability_request_create_params.Payouts | NotGiven = NOT_GIVEN,
        signed_agreement: capability_request_create_params.SignedAgreement | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CapabilityRequestPaged:
        """Submits a new request to enable a specific capability for an account.

        Use this
        endpoint to request additional features or services for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "correlation-id": correlation_id,
                    "request-id": request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/v1/accounts/{account_id}/capability_requests",
            body=await async_maybe_transform(
                {
                    "businesses": businesses,
                    "charges": charges,
                    "individuals": individuals,
                    "internet": internet,
                    "payouts": payouts,
                    "signed_agreement": signed_agreement,
                },
                capability_request_create_params.CapabilityRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRequestPaged,
        )

    def list(
        self,
        account_id: str,
        *,
        page_number: int,
        page_size: int,
        sort_by: str,
        sort_order: Literal["asc", "desc"],
        category: Literal["payment_type", "customer_type", "consent_type"] | NotGiven = NOT_GIVEN,
        status: Literal["approved", "rejected", "reviewing"] | NotGiven = NOT_GIVEN,
        type: Literal["charges", "payouts", "individuals", "businesses", "signed_agreement", "internet"]
        | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Data, AsyncPageNumberSchema[Data]]:
        """Retrieves a list of capability requests associated with an account.

        The requests
        are returned sorted by creation date, with the most recent requests appearing
        first. This endpoint supports filtering options to help you track the status of
        various capability requests.

        Args:
          page_number: Results page number. Starts at page 1. Default value: 1

          page_size: Page size. Default value: 100. Max value: 1000

          sort_by: Sort By. Default value: 'id'.

          sort_order: Sort Order. Default value: 'asc'.

          category: Filter capability requests by category. Possible values: 'payment_type',
              'customer_type', 'consent_type'.

          status: Filter capability requests by their current status. Possible values: 'active',
              'inactive', 'in_review', 'rejected'.

          type:
              Filter capability requests by the specific type of capability. Possible values:
              'charges', 'payouts', 'individuals', 'businesses', 'signed_agreement',
              'internet'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "correlation-id": correlation_id,
                    "request-id": request_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            f"/v1/accounts/{account_id}/capability_requests",
            page=AsyncPageNumberSchema[Data],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "category": category,
                        "status": status,
                        "type": type,
                    },
                    capability_request_list_params.CapabilityRequestListParams,
                ),
            ),
            model=Data,
        )


class CapabilityRequestsResourceWithRawResponse:
    def __init__(self, capability_requests: CapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = to_raw_response_wrapper(
            capability_requests.create,
        )
        self.list = to_raw_response_wrapper(
            capability_requests.list,
        )


class AsyncCapabilityRequestsResourceWithRawResponse:
    def __init__(self, capability_requests: AsyncCapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = async_to_raw_response_wrapper(
            capability_requests.create,
        )
        self.list = async_to_raw_response_wrapper(
            capability_requests.list,
        )


class CapabilityRequestsResourceWithStreamingResponse:
    def __init__(self, capability_requests: CapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = to_streamed_response_wrapper(
            capability_requests.create,
        )
        self.list = to_streamed_response_wrapper(
            capability_requests.list,
        )


class AsyncCapabilityRequestsResourceWithStreamingResponse:
    def __init__(self, capability_requests: AsyncCapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = async_to_streamed_response_wrapper(
            capability_requests.create,
        )
        self.list = async_to_streamed_response_wrapper(
            capability_requests.list,
        )
