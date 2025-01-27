# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from straddle import Straddle, AsyncStraddle
from tests.utils import assert_matches_type
from straddle.types import Customer
from straddle.types.customers import CustomerReview

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Straddle) -> None:
        review = client.customers.review.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerReview, review, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Straddle) -> None:
        review = client.customers.review.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerReview, review, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Straddle) -> None:
        response = client.customers.review.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(CustomerReview, review, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Straddle) -> None:
        with client.customers.review.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(CustomerReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Straddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.review.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: Straddle) -> None:
        review = client.customers.review.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
        )
        assert_matches_type(Customer, review, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Straddle) -> None:
        review = client.customers.review.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Customer, review, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Straddle) -> None:
        response = client.customers.review.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(Customer, review, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Straddle) -> None:
        with client.customers.review.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(Customer, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Straddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.review.with_raw_response.update(
                id="",
                status="verified",
            )


class TestAsyncReview:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStraddle) -> None:
        review = await async_client.customers.review.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerReview, review, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncStraddle) -> None:
        review = await async_client.customers.review.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomerReview, review, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStraddle) -> None:
        response = await async_client.customers.review.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(CustomerReview, review, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStraddle) -> None:
        async with async_client.customers.review.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(CustomerReview, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStraddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.review.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStraddle) -> None:
        review = await async_client.customers.review.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
        )
        assert_matches_type(Customer, review, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStraddle) -> None:
        review = await async_client.customers.review.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Customer, review, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStraddle) -> None:
        response = await async_client.customers.review.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(Customer, review, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStraddle) -> None:
        async with async_client.customers.review.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="verified",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(Customer, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStraddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.review.with_raw_response.update(
                id="",
                status="verified",
            )
