# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from .representatives import (
    RepresentativesResource,
    AsyncRepresentativesResource,
    RepresentativesResourceWithRawResponse,
    AsyncRepresentativesResourceWithRawResponse,
    RepresentativesResourceWithStreamingResponse,
    AsyncRepresentativesResourceWithStreamingResponse,
)
from .accounts.accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .linked_bank_accounts import (
    LinkedBankAccountsResource,
    AsyncLinkedBankAccountsResource,
    LinkedBankAccountsResourceWithRawResponse,
    AsyncLinkedBankAccountsResourceWithRawResponse,
    LinkedBankAccountsResourceWithStreamingResponse,
    AsyncLinkedBankAccountsResourceWithStreamingResponse,
)

__all__ = ["EmbedResource", "AsyncEmbedResource"]


class EmbedResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        """Accounts represent businesses using Straddle through your platform.

        Each account must complete automated verification before processing payments. Use accounts to manage your users' payment capabilities, track verification status, and control access to features. Accounts can be instantly created in sandbox and require additional verification for production access.
        """
        return AccountsResource(self._client)

    @cached_property
    def linked_bank_accounts(self) -> LinkedBankAccountsResource:
        """
        Linked bank accounts connect your platform users' external bank accounts to Straddle for settlements and payment funding. Each linked account undergoes automated verification and continuous monitoring. Use linked accounts to manage where clients receive deposits, fund payouts, and track settlement preferences.
        """
        return LinkedBankAccountsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        """
        Organizations are a powerful feature in Straddle that allow you to manage multiple accounts under a single umbrella. This hierarchical structure is particularly useful for businesses with complex operations, multiple departments, or legally related entities.
        """
        return OrganizationsResource(self._client)

    @cached_property
    def representatives(self) -> RepresentativesResource:
        """
        Representatives are individuals who have legal authority or significant responsibility within a business entity associated with a Straddle account. Each representative undergoes automated verification as part of KYC/KYB compliance. Use representatives to collect and verify beneficial owners, control persons, and authorized signers required for account onboarding. Representatives also determine who can legally operate the account and make important changes.
        """
        return RepresentativesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/straddleio/straddle-python#accessing-raw-response-data-eg-headers
        """
        return EmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/straddleio/straddle-python#with_streaming_response
        """
        return EmbedResourceWithStreamingResponse(self)


class AsyncEmbedResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Accounts represent businesses using Straddle through your platform.

        Each account must complete automated verification before processing payments. Use accounts to manage your users' payment capabilities, track verification status, and control access to features. Accounts can be instantly created in sandbox and require additional verification for production access.
        """
        return AsyncAccountsResource(self._client)

    @cached_property
    def linked_bank_accounts(self) -> AsyncLinkedBankAccountsResource:
        """
        Linked bank accounts connect your platform users' external bank accounts to Straddle for settlements and payment funding. Each linked account undergoes automated verification and continuous monitoring. Use linked accounts to manage where clients receive deposits, fund payouts, and track settlement preferences.
        """
        return AsyncLinkedBankAccountsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        """
        Organizations are a powerful feature in Straddle that allow you to manage multiple accounts under a single umbrella. This hierarchical structure is particularly useful for businesses with complex operations, multiple departments, or legally related entities.
        """
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def representatives(self) -> AsyncRepresentativesResource:
        """
        Representatives are individuals who have legal authority or significant responsibility within a business entity associated with a Straddle account. Each representative undergoes automated verification as part of KYC/KYB compliance. Use representatives to collect and verify beneficial owners, control persons, and authorized signers required for account onboarding. Representatives also determine who can legally operate the account and make important changes.
        """
        return AsyncRepresentativesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/straddleio/straddle-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/straddleio/straddle-python#with_streaming_response
        """
        return AsyncEmbedResourceWithStreamingResponse(self)


class EmbedResourceWithRawResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """Accounts represent businesses using Straddle through your platform.

        Each account must complete automated verification before processing payments. Use accounts to manage your users' payment capabilities, track verification status, and control access to features. Accounts can be instantly created in sandbox and require additional verification for production access.
        """
        return AccountsResourceWithRawResponse(self._embed.accounts)

    @cached_property
    def linked_bank_accounts(self) -> LinkedBankAccountsResourceWithRawResponse:
        """
        Linked bank accounts connect your platform users' external bank accounts to Straddle for settlements and payment funding. Each linked account undergoes automated verification and continuous monitoring. Use linked accounts to manage where clients receive deposits, fund payouts, and track settlement preferences.
        """
        return LinkedBankAccountsResourceWithRawResponse(self._embed.linked_bank_accounts)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        """
        Organizations are a powerful feature in Straddle that allow you to manage multiple accounts under a single umbrella. This hierarchical structure is particularly useful for businesses with complex operations, multiple departments, or legally related entities.
        """
        return OrganizationsResourceWithRawResponse(self._embed.organizations)

    @cached_property
    def representatives(self) -> RepresentativesResourceWithRawResponse:
        """
        Representatives are individuals who have legal authority or significant responsibility within a business entity associated with a Straddle account. Each representative undergoes automated verification as part of KYC/KYB compliance. Use representatives to collect and verify beneficial owners, control persons, and authorized signers required for account onboarding. Representatives also determine who can legally operate the account and make important changes.
        """
        return RepresentativesResourceWithRawResponse(self._embed.representatives)


class AsyncEmbedResourceWithRawResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Accounts represent businesses using Straddle through your platform.

        Each account must complete automated verification before processing payments. Use accounts to manage your users' payment capabilities, track verification status, and control access to features. Accounts can be instantly created in sandbox and require additional verification for production access.
        """
        return AsyncAccountsResourceWithRawResponse(self._embed.accounts)

    @cached_property
    def linked_bank_accounts(self) -> AsyncLinkedBankAccountsResourceWithRawResponse:
        """
        Linked bank accounts connect your platform users' external bank accounts to Straddle for settlements and payment funding. Each linked account undergoes automated verification and continuous monitoring. Use linked accounts to manage where clients receive deposits, fund payouts, and track settlement preferences.
        """
        return AsyncLinkedBankAccountsResourceWithRawResponse(self._embed.linked_bank_accounts)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        Organizations are a powerful feature in Straddle that allow you to manage multiple accounts under a single umbrella. This hierarchical structure is particularly useful for businesses with complex operations, multiple departments, or legally related entities.
        """
        return AsyncOrganizationsResourceWithRawResponse(self._embed.organizations)

    @cached_property
    def representatives(self) -> AsyncRepresentativesResourceWithRawResponse:
        """
        Representatives are individuals who have legal authority or significant responsibility within a business entity associated with a Straddle account. Each representative undergoes automated verification as part of KYC/KYB compliance. Use representatives to collect and verify beneficial owners, control persons, and authorized signers required for account onboarding. Representatives also determine who can legally operate the account and make important changes.
        """
        return AsyncRepresentativesResourceWithRawResponse(self._embed.representatives)


class EmbedResourceWithStreamingResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Accounts represent businesses using Straddle through your platform.

        Each account must complete automated verification before processing payments. Use accounts to manage your users' payment capabilities, track verification status, and control access to features. Accounts can be instantly created in sandbox and require additional verification for production access.
        """
        return AccountsResourceWithStreamingResponse(self._embed.accounts)

    @cached_property
    def linked_bank_accounts(self) -> LinkedBankAccountsResourceWithStreamingResponse:
        """
        Linked bank accounts connect your platform users' external bank accounts to Straddle for settlements and payment funding. Each linked account undergoes automated verification and continuous monitoring. Use linked accounts to manage where clients receive deposits, fund payouts, and track settlement preferences.
        """
        return LinkedBankAccountsResourceWithStreamingResponse(self._embed.linked_bank_accounts)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        """
        Organizations are a powerful feature in Straddle that allow you to manage multiple accounts under a single umbrella. This hierarchical structure is particularly useful for businesses with complex operations, multiple departments, or legally related entities.
        """
        return OrganizationsResourceWithStreamingResponse(self._embed.organizations)

    @cached_property
    def representatives(self) -> RepresentativesResourceWithStreamingResponse:
        """
        Representatives are individuals who have legal authority or significant responsibility within a business entity associated with a Straddle account. Each representative undergoes automated verification as part of KYC/KYB compliance. Use representatives to collect and verify beneficial owners, control persons, and authorized signers required for account onboarding. Representatives also determine who can legally operate the account and make important changes.
        """
        return RepresentativesResourceWithStreamingResponse(self._embed.representatives)


class AsyncEmbedResourceWithStreamingResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Accounts represent businesses using Straddle through your platform.

        Each account must complete automated verification before processing payments. Use accounts to manage your users' payment capabilities, track verification status, and control access to features. Accounts can be instantly created in sandbox and require additional verification for production access.
        """
        return AsyncAccountsResourceWithStreamingResponse(self._embed.accounts)

    @cached_property
    def linked_bank_accounts(self) -> AsyncLinkedBankAccountsResourceWithStreamingResponse:
        """
        Linked bank accounts connect your platform users' external bank accounts to Straddle for settlements and payment funding. Each linked account undergoes automated verification and continuous monitoring. Use linked accounts to manage where clients receive deposits, fund payouts, and track settlement preferences.
        """
        return AsyncLinkedBankAccountsResourceWithStreamingResponse(self._embed.linked_bank_accounts)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        Organizations are a powerful feature in Straddle that allow you to manage multiple accounts under a single umbrella. This hierarchical structure is particularly useful for businesses with complex operations, multiple departments, or legally related entities.
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self._embed.organizations)

    @cached_property
    def representatives(self) -> AsyncRepresentativesResourceWithStreamingResponse:
        """
        Representatives are individuals who have legal authority or significant responsibility within a business entity associated with a Straddle account. Each representative undergoes automated verification as part of KYC/KYB compliance. Use representatives to collect and verify beneficial owners, control persons, and authorized signers required for account onboarding. Representatives also determine who can legally operate the account and make important changes.
        """
        return AsyncRepresentativesResourceWithStreamingResponse(self._embed.representatives)
