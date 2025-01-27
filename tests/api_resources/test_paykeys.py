# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from straddle import Straddle, AsyncStraddle
from tests.utils import assert_matches_type
from straddle.types import PaykeyUnmasked, PaykeySummaryPaged
from straddle.types.shared import Paykey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaykeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Straddle) -> None:
        paykey = client.paykeys.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Paykey, paykey, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Straddle) -> None:
        paykey = client.paykeys.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Paykey, paykey, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Straddle) -> None:
        response = client.paykeys.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paykey = response.parse()
        assert_matches_type(Paykey, paykey, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Straddle) -> None:
        with client.paykeys.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paykey = response.parse()
            assert_matches_type(Paykey, paykey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Straddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.paykeys.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Straddle) -> None:
        paykey = client.paykeys.list()
        assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Straddle) -> None:
        paykey = client.paykeys.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=0,
            page_size=0,
            sort_by="institution_name",
            sort_order="asc",
            status=["pending"],
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Straddle) -> None:
        response = client.paykeys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paykey = response.parse()
        assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Straddle) -> None:
        with client.paykeys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paykey = response.parse()
            assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unmasked(self, client: Straddle) -> None:
        paykey = client.paykeys.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

    @parametrize
    def test_method_unmasked_with_all_params(self, client: Straddle) -> None:
        paykey = client.paykeys.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

    @parametrize
    def test_raw_response_unmasked(self, client: Straddle) -> None:
        response = client.paykeys.with_raw_response.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paykey = response.parse()
        assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

    @parametrize
    def test_streaming_response_unmasked(self, client: Straddle) -> None:
        with client.paykeys.with_streaming_response.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paykey = response.parse()
            assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unmasked(self, client: Straddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.paykeys.with_raw_response.unmasked(
                id="",
            )


class TestAsyncPaykeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStraddle) -> None:
        paykey = await async_client.paykeys.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Paykey, paykey, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncStraddle) -> None:
        paykey = await async_client.paykeys.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Paykey, paykey, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStraddle) -> None:
        response = await async_client.paykeys.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paykey = await response.parse()
        assert_matches_type(Paykey, paykey, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStraddle) -> None:
        async with async_client.paykeys.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paykey = await response.parse()
            assert_matches_type(Paykey, paykey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStraddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.paykeys.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStraddle) -> None:
        paykey = await async_client.paykeys.list()
        assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStraddle) -> None:
        paykey = await async_client.paykeys.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=0,
            page_size=0,
            sort_by="institution_name",
            sort_order="asc",
            status=["pending"],
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStraddle) -> None:
        response = await async_client.paykeys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paykey = await response.parse()
        assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStraddle) -> None:
        async with async_client.paykeys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paykey = await response.parse()
            assert_matches_type(PaykeySummaryPaged, paykey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unmasked(self, async_client: AsyncStraddle) -> None:
        paykey = await async_client.paykeys.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

    @parametrize
    async def test_method_unmasked_with_all_params(self, async_client: AsyncStraddle) -> None:
        paykey = await async_client.paykeys.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

    @parametrize
    async def test_raw_response_unmasked(self, async_client: AsyncStraddle) -> None:
        response = await async_client.paykeys.with_raw_response.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paykey = await response.parse()
        assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

    @parametrize
    async def test_streaming_response_unmasked(self, async_client: AsyncStraddle) -> None:
        async with async_client.paykeys.with_streaming_response.unmasked(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paykey = await response.parse()
            assert_matches_type(PaykeyUnmasked, paykey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unmasked(self, async_client: AsyncStraddle) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.paykeys.with_raw_response.unmasked(
                id="",
            )
