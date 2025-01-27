# Shared Types

```python
from straddle.types import Paykey
```

# Accounts

Types:

```python
from straddle.types import Account, AccountPaged
```

Methods:

- <code title="post /v1/accounts">client.accounts.<a href="./src/straddle/resources/accounts/accounts.py">create</a>(\*\*<a href="src/straddle/types/account_create_params.py">params</a>) -> <a href="./src/straddle/types/account.py">Account</a></code>
- <code title="get /v1/accounts/{account_id}">client.accounts.<a href="./src/straddle/resources/accounts/accounts.py">retrieve</a>(account_id) -> <a href="./src/straddle/types/account.py">Account</a></code>
- <code title="put /v1/accounts/{account_id}">client.accounts.<a href="./src/straddle/resources/accounts/accounts.py">update</a>(account_id, \*\*<a href="src/straddle/types/account_update_params.py">params</a>) -> <a href="./src/straddle/types/account.py">Account</a></code>
- <code title="get /v1/accounts">client.accounts.<a href="./src/straddle/resources/accounts/accounts.py">list</a>(\*\*<a href="src/straddle/types/account_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>
- <code title="post /v1/accounts/{account_id}/onboard">client.accounts.<a href="./src/straddle/resources/accounts/accounts.py">onboard</a>(account_id, \*\*<a href="src/straddle/types/account_onboard_params.py">params</a>) -> <a href="./src/straddle/types/account.py">Account</a></code>
- <code title="post /v1/accounts/{account_id}/simulate">client.accounts.<a href="./src/straddle/resources/accounts/accounts.py">simulate</a>(account_id, \*\*<a href="src/straddle/types/account_simulate_params.py">params</a>) -> <a href="./src/straddle/types/account.py">Account</a></code>

## CapabilityRequests

Types:

```python
from straddle.types.accounts import CapabilityRequestPaged
```

Methods:

- <code title="post /v1/accounts/{account_id}/capability_requests">client.accounts.capability_requests.<a href="./src/straddle/resources/accounts/capability_requests.py">create</a>(account_id, \*\*<a href="src/straddle/types/accounts/capability_request_create_params.py">params</a>) -> <a href="./src/straddle/types/accounts/capability_request_paged.py">CapabilityRequestPaged</a></code>
- <code title="get /v1/accounts/{account_id}/capability_requests">client.accounts.capability_requests.<a href="./src/straddle/resources/accounts/capability_requests.py">list</a>(account_id, \*\*<a href="src/straddle/types/accounts/capability_request_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>

# LinkedBankAccounts

Types:

```python
from straddle.types import LinkedBankAccount, LinkedBankAccountPaged, LinkedBankAccountUnmask
```

Methods:

- <code title="post /v1/linked_bank_accounts">client.linked_bank_accounts.<a href="./src/straddle/resources/linked_bank_accounts.py">create</a>(\*\*<a href="src/straddle/types/linked_bank_account_create_params.py">params</a>) -> <a href="./src/straddle/types/linked_bank_account.py">LinkedBankAccount</a></code>
- <code title="get /v1/linked_bank_accounts/{linked_bank_account_id}">client.linked_bank_accounts.<a href="./src/straddle/resources/linked_bank_accounts.py">retrieve</a>(linked_bank_account_id) -> <a href="./src/straddle/types/linked_bank_account.py">LinkedBankAccount</a></code>
- <code title="put /v1/linked_bank_accounts/{linked_bank_account_id}">client.linked_bank_accounts.<a href="./src/straddle/resources/linked_bank_accounts.py">update</a>(linked_bank_account_id, \*\*<a href="src/straddle/types/linked_bank_account_update_params.py">params</a>) -> <a href="./src/straddle/types/linked_bank_account.py">LinkedBankAccount</a></code>
- <code title="get /v1/linked_bank_accounts">client.linked_bank_accounts.<a href="./src/straddle/resources/linked_bank_accounts.py">list</a>(\*\*<a href="src/straddle/types/linked_bank_account_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>
- <code title="get /v1/linked_bank_accounts/{linked_bank_account_id}/unmask">client.linked_bank_accounts.<a href="./src/straddle/resources/linked_bank_accounts.py">unmask</a>(linked_bank_account_id) -> <a href="./src/straddle/types/linked_bank_account_unmask.py">LinkedBankAccountUnmask</a></code>

# Organizations

Types:

```python
from straddle.types import Organization, OrganizationPaged
```

Methods:

- <code title="post /v1/organizations">client.organizations.<a href="./src/straddle/resources/organizations.py">create</a>(\*\*<a href="src/straddle/types/organization_create_params.py">params</a>) -> <a href="./src/straddle/types/organization.py">Organization</a></code>
- <code title="get /v1/organizations">client.organizations.<a href="./src/straddle/resources/organizations.py">list</a>(\*\*<a href="src/straddle/types/organization_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>

# Representatives

Types:

```python
from straddle.types import Representative, RepresentativePaged
```

Methods:

- <code title="post /v1/representatives">client.representatives.<a href="./src/straddle/resources/representatives.py">create</a>(\*\*<a href="src/straddle/types/representative_create_params.py">params</a>) -> <a href="./src/straddle/types/representative.py">Representative</a></code>
- <code title="get /v1/representatives/{representative_id}">client.representatives.<a href="./src/straddle/resources/representatives.py">retrieve</a>(representative_id) -> <a href="./src/straddle/types/representative.py">Representative</a></code>
- <code title="put /v1/representatives/{representative_id}">client.representatives.<a href="./src/straddle/resources/representatives.py">update</a>(representative_id, \*\*<a href="src/straddle/types/representative_update_params.py">params</a>) -> <a href="./src/straddle/types/representative.py">Representative</a></code>
- <code title="get /v1/representatives">client.representatives.<a href="./src/straddle/resources/representatives.py">list</a>(\*\*<a href="src/straddle/types/representative_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>

# Bridge

Types:

```python
from straddle.types import BridgeToken
```

Methods:

- <code title="post /v1/bridge/initialize">client.bridge.<a href="./src/straddle/resources/bridge/bridge.py">initialize</a>(\*\*<a href="src/straddle/types/bridge_initialize_params.py">params</a>) -> <a href="./src/straddle/types/bridge_token.py">BridgeToken</a></code>
- <code title="post /v1/bridge/plaid">client.bridge.<a href="./src/straddle/resources/bridge/bridge.py">plaid</a>(\*\*<a href="src/straddle/types/bridge_plaid_params.py">params</a>) -> <a href="./src/straddle/types/shared/paykey.py">Paykey</a></code>

## BankAccount

Methods:

- <code title="post /v1/bridge/bank_account">client.bridge.bank_account.<a href="./src/straddle/resources/bridge/bank_account.py">create</a>(\*\*<a href="src/straddle/types/bridge/bank_account_create_params.py">params</a>) -> <a href="./src/straddle/types/shared/paykey.py">Paykey</a></code>

# Customers

Types:

```python
from straddle.types import Customer, CustomerSummaryPaged, CustomerUnmasked
```

Methods:

- <code title="post /v1/customers">client.customers.<a href="./src/straddle/resources/customers/customers.py">create</a>(\*\*<a href="src/straddle/types/customer_create_params.py">params</a>) -> <a href="./src/straddle/types/customer.py">Customer</a></code>
- <code title="get /v1/customers/{id}">client.customers.<a href="./src/straddle/resources/customers/customers.py">retrieve</a>(id) -> <a href="./src/straddle/types/customer.py">Customer</a></code>
- <code title="put /v1/customers/{id}">client.customers.<a href="./src/straddle/resources/customers/customers.py">update</a>(id, \*\*<a href="src/straddle/types/customer_update_params.py">params</a>) -> <a href="./src/straddle/types/customer.py">Customer</a></code>
- <code title="get /v1/customers">client.customers.<a href="./src/straddle/resources/customers/customers.py">list</a>(\*\*<a href="src/straddle/types/customer_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>
- <code title="delete /v1/customers/{id}">client.customers.<a href="./src/straddle/resources/customers/customers.py">delete</a>(id) -> <a href="./src/straddle/types/customer.py">Customer</a></code>
- <code title="get /v1/customers/{id}/unmasked">client.customers.<a href="./src/straddle/resources/customers/customers.py">unmasked</a>(id) -> <a href="./src/straddle/types/customer_unmasked.py">CustomerUnmasked</a></code>

## Review

Types:

```python
from straddle.types.customers import CustomerReview
```

Methods:

- <code title="get /v1/customers/{id}/review">client.customers.review.<a href="./src/straddle/resources/customers/review.py">retrieve</a>(id) -> <a href="./src/straddle/types/customers/customer_review.py">CustomerReview</a></code>
- <code title="patch /v1/customers/{id}/review">client.customers.review.<a href="./src/straddle/resources/customers/review.py">update</a>(id, \*\*<a href="src/straddle/types/customers/review_update_params.py">params</a>) -> <a href="./src/straddle/types/customer.py">Customer</a></code>

# Paykeys

Types:

```python
from straddle.types import PaykeySummaryPaged, PaykeyUnmasked
```

Methods:

- <code title="get /v1/paykeys/{id}">client.paykeys.<a href="./src/straddle/resources/paykeys.py">retrieve</a>(id) -> <a href="./src/straddle/types/shared/paykey.py">Paykey</a></code>
- <code title="get /v1/paykeys">client.paykeys.<a href="./src/straddle/resources/paykeys.py">list</a>(\*\*<a href="src/straddle/types/paykey_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>
- <code title="get /v1/paykeys/{id}/unmasked">client.paykeys.<a href="./src/straddle/resources/paykeys.py">unmasked</a>(id) -> <a href="./src/straddle/types/paykey_unmasked.py">PaykeyUnmasked</a></code>

# Reports

Types:

```python
from straddle.types import ReportTotalCustomersByStatusResponse
```

Methods:

- <code title="post /v1/reports/total_customers_by_status">client.reports.<a href="./src/straddle/resources/reports.py">total_customers_by_status</a>() -> <a href="./src/straddle/types/report_total_customers_by_status_response.py">ReportTotalCustomersByStatusResponse</a></code>

# Charges

Types:

```python
from straddle.types import Charge
```

Methods:

- <code title="post /v1/charges">client.charges.<a href="./src/straddle/resources/charges.py">create</a>(\*\*<a href="src/straddle/types/charge_create_params.py">params</a>) -> <a href="./src/straddle/types/charge.py">Charge</a></code>
- <code title="get /v1/charges/{id}">client.charges.<a href="./src/straddle/resources/charges.py">retrieve</a>(id) -> <a href="./src/straddle/types/charge.py">Charge</a></code>
- <code title="put /v1/charges/{id}">client.charges.<a href="./src/straddle/resources/charges.py">update</a>(id, \*\*<a href="src/straddle/types/charge_update_params.py">params</a>) -> <a href="./src/straddle/types/charge.py">Charge</a></code>
- <code title="put /v1/charges/{id}/cancel">client.charges.<a href="./src/straddle/resources/charges.py">cancel</a>(id, \*\*<a href="src/straddle/types/charge_cancel_params.py">params</a>) -> <a href="./src/straddle/types/charge.py">Charge</a></code>
- <code title="put /v1/charges/{id}/hold">client.charges.<a href="./src/straddle/resources/charges.py">hold</a>(id, \*\*<a href="src/straddle/types/charge_hold_params.py">params</a>) -> <a href="./src/straddle/types/charge.py">Charge</a></code>
- <code title="put /v1/charges/{id}/release">client.charges.<a href="./src/straddle/resources/charges.py">release</a>(id, \*\*<a href="src/straddle/types/charge_release_params.py">params</a>) -> <a href="./src/straddle/types/charge.py">Charge</a></code>

# FundingEvents

Types:

```python
from straddle.types import FundingEventSummaryItem, FundingEventSummaryPaged
```

Methods:

- <code title="get /v1/funding_events/{id}">client.funding_events.<a href="./src/straddle/resources/funding_events.py">retrieve</a>(id) -> <a href="./src/straddle/types/funding_event_summary_item.py">FundingEventSummaryItem</a></code>
- <code title="get /v1/funding_events">client.funding_events.<a href="./src/straddle/resources/funding_events.py">list</a>(\*\*<a href="src/straddle/types/funding_event_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>

# Payments

Types:

```python
from straddle.types import PaymentSummaryPaged
```

Methods:

- <code title="get /v1/payments">client.payments.<a href="./src/straddle/resources/payments.py">list</a>(\*\*<a href="src/straddle/types/payment_list_params.py">params</a>) -> SyncPageNumberSchema[Data]</code>

# Payouts

Types:

```python
from straddle.types import Payout
```

Methods:

- <code title="post /v1/payouts">client.payouts.<a href="./src/straddle/resources/payouts.py">create</a>(\*\*<a href="src/straddle/types/payout_create_params.py">params</a>) -> <a href="./src/straddle/types/payout.py">Payout</a></code>
- <code title="get /v1/payouts/{id}">client.payouts.<a href="./src/straddle/resources/payouts.py">retrieve</a>(id) -> <a href="./src/straddle/types/payout.py">Payout</a></code>
- <code title="put /v1/payouts/{id}">client.payouts.<a href="./src/straddle/resources/payouts.py">update</a>(id, \*\*<a href="src/straddle/types/payout_update_params.py">params</a>) -> <a href="./src/straddle/types/payout.py">Payout</a></code>
- <code title="put /v1/payouts/{id}/cancel">client.payouts.<a href="./src/straddle/resources/payouts.py">cancel</a>(id, \*\*<a href="src/straddle/types/payout_cancel_params.py">params</a>) -> <a href="./src/straddle/types/payout.py">Payout</a></code>
- <code title="put /v1/payouts/{id}/hold">client.payouts.<a href="./src/straddle/resources/payouts.py">hold</a>(id, \*\*<a href="src/straddle/types/payout_hold_params.py">params</a>) -> <a href="./src/straddle/types/payout.py">Payout</a></code>
- <code title="put /v1/payouts/{id}/release">client.payouts.<a href="./src/straddle/resources/payouts.py">release</a>(id, \*\*<a href="src/straddle/types/payout_release_params.py">params</a>) -> <a href="./src/straddle/types/payout.py">Payout</a></code>
