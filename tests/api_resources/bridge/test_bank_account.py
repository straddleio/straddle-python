# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from straddle import Straddle, AsyncStraddle
from tests.utils import assert_matches_type
from straddle.types import Paykey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBankAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Straddle) -> None:
        bank_account = client.bridge.bank_account.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
        )
        assert_matches_type(Paykey, bank_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Straddle) -> None:
        bank_account = client.bridge.bank_account.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
            metadata={"foo": "string"},
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Paykey, bank_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Straddle) -> None:
        response = client.bridge.bank_account.with_raw_response.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(Paykey, bank_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Straddle) -> None:
        with client.bridge.bank_account.with_streaming_response.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(Paykey, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBankAccount:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStraddle) -> None:
        bank_account = await async_client.bridge.bank_account.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
        )
        assert_matches_type(Paykey, bank_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStraddle) -> None:
        bank_account = await async_client.bridge.bank_account.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
            metadata={"foo": "string"},
            correlation_id="Correlation-Id",
            request_id="Request-Id",
            straddle_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Paykey, bank_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStraddle) -> None:
        response = await async_client.bridge.bank_account.with_raw_response.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(Paykey, bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStraddle) -> None:
        async with async_client.bridge.bank_account.with_streaming_response.create(
            account_number="account_number",
            account_type="checking",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            routing_number="xxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(Paykey, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True
