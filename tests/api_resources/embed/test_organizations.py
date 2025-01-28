# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from straddle import Straddle, AsyncStraddle
from tests.utils import assert_matches_type
from straddle.pagination import SyncPageNumberSchema, AsyncPageNumberSchema
from straddle.types.embed import Organization
from straddle.types.embed.organization_paged import Data

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Straddle) -> None:
        organization = client.embed.organizations.create(
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Straddle) -> None:
        organization = client.embed.organizations.create(
            name="name",
            external_id="external_id",
            metadata={"foo": "string"},
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Straddle) -> None:
        response = client.embed.organizations.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Straddle) -> None:
        with client.embed.organizations.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Straddle) -> None:
        organization = client.embed.organizations.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
        )
        assert_matches_type(SyncPageNumberSchema[Data], organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Straddle) -> None:
        organization = client.embed.organizations.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
            external_id="external_id",
            name="name",
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(SyncPageNumberSchema[Data], organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Straddle) -> None:
        response = client.embed.organizations.with_raw_response.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncPageNumberSchema[Data], organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Straddle) -> None:
        with client.embed.organizations.with_streaming_response.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncPageNumberSchema[Data], organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.embed.organizations.create(
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.embed.organizations.create(
            name="name",
            external_id="external_id",
            metadata={"foo": "string"},
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStraddle) -> None:
        response = await async_client.embed.organizations.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStraddle) -> None:
        async with async_client.embed.organizations.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.embed.organizations.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
        )
        assert_matches_type(AsyncPageNumberSchema[Data], organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.embed.organizations.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
            external_id="external_id",
            name="name",
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(AsyncPageNumberSchema[Data], organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStraddle) -> None:
        response = await async_client.embed.organizations.with_raw_response.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncPageNumberSchema[Data], organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStraddle) -> None:
        async with async_client.embed.organizations.with_streaming_response.list(
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(AsyncPageNumberSchema[Data], organization, path=["response"])

        assert cast(Any, response.is_closed) is True
