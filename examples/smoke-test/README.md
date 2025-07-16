## Examples

### Smoke Test Runner

A turnkey demo that walks through creating an organization → account → customer → paykey → charge → payout flows.

#### Important Note
In step 5d, Create a Customer, if you're using a SANDBOX_API_KEY for a Platform, the account_id header is required.  If you're using a Marketplace, it is not

```bash
cd examples/smoke-test
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
endure .env has the SANDBOX_API_KEY
python demo.py

