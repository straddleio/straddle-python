# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from straddle import Straddle, AsyncStraddle
from tests.utils import assert_matches_type
from straddle.types import Organization, OrganizationPaged

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Straddle) -> None:
        organization = client.organizations.create(
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Straddle) -> None:
        organization = client.organizations.create(
            name="name",
            external_id="external_id",
            metadata={"foo": "string"},
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Straddle) -> None:
        response = client.organizations.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Straddle) -> None:
        with client.organizations.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Straddle) -> None:
        organization = client.organizations.list()
        assert_matches_type(OrganizationPaged, organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Straddle) -> None:
        organization = client.organizations.list(
            external_id="external_id",
            name="name",
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(OrganizationPaged, organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Straddle) -> None:
        response = client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationPaged, organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Straddle) -> None:
        with client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationPaged, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.organizations.create(
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.organizations.create(
            name="name",
            external_id="external_id",
            metadata={"foo": "string"},
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStraddle) -> None:
        response = await async_client.organizations.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStraddle) -> None:
        async with async_client.organizations.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.organizations.list()
        assert_matches_type(OrganizationPaged, organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStraddle) -> None:
        organization = await async_client.organizations.list(
            external_id="external_id",
            name="name",
            page_number=0,
            page_size=0,
            sort_by="sort_by",
            sort_order="asc",
            correlation_id="correlation-id",
            request_id="request-id",
        )
        assert_matches_type(OrganizationPaged, organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStraddle) -> None:
        response = await async_client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationPaged, organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStraddle) -> None:
        async with async_client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationPaged, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
