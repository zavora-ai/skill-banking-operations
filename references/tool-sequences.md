# Banking Tool Sequences Reference

## Tool Inventory (mcp-banking, 15 tools)

| Tool | Risk | Revenue Impact |
|------|------|---------------|
| `list_accounts` | read | Account visibility |
| `get_account` | read | Account details |
| `get_balances` | read | **Cash position awareness** |
| `list_transactions` | read | **Revenue tracking (deposits)** |
| `get_transaction` | read | Transaction details |
| `search_transactions` | read | Find specific payments |
| `categorize_transaction` | read | Spending analysis |
| `sync_transactions` | read | **Real-time data** |
| `get_identity` | read | Account holder verification |
| `list_institutions` | read | Bank discovery |
| `get_institution` | read | Bank details |
| `initiate_payment` | financial | **Outbound payments** |
| `get_payment_status` | read | Payment tracking |
| `list_payments` | read | Payment history |
| `get_statement` | read | Official statements |

## Sequence: Account Overview (2 calls)

```
1. list_accounts()
   → [{id: "acc_1", name: "Operating", type: "checking", institution: "Chase"},
      {id: "acc_2", name: "Savings", type: "savings", institution: "Chase"}]

2. get_balances(account_id: "acc_1")
   → {current: 2500000, available: 2450000, currency: "usd"}
   # Current: $25,000 | Available: $24,500 (pending transactions reduce available)
```

## Sequence: Daily Transaction Sync (2-3 calls)

```
1. sync_transactions(account_id: "acc_1")
   → {synced: 12, new: 3, last_sync: "2025-01-18T10:00:00Z"}

2. list_transactions(account_id: "acc_1", start_date: "2025-01-17", end_date: "2025-01-18")
   → [{id: "txn_1", amount: 55000, type: "deposit", merchant: "ACME CORP", date: "2025-01-18"},
      {id: "txn_2", amount: -12000, type: "withdrawal", merchant: "AWS", date: "2025-01-18"}]

3. [For uncategorized] categorize_transaction(id: "txn_2", category: "cloud_infrastructure")
```

## Sequence: Payment Initiation (3 calls)

```
1. get_balances(account_id: "acc_1")
   → {available: 2450000}
   → Verify: available (2450000) > payment amount (100000) ✅

2. initiate_payment(
     account_id: "acc_1",
     amount: 100000,
     currency: "usd",
     recipient: {name: "TechSupply Inc", account: "****4567", routing: "021000021"},
     reference: "PO-2025-045"
   )
   → {id: "pmt_abc", status: "pending"}

3. get_payment_status(payment_id: "pmt_abc")
   → {status: "processing", estimated_arrival: "2025-01-20"}
```

## Sequence: Revenue Detection (Deposits)

```
1. sync_transactions(account_id: "acc_1")
2. list_transactions(account_id: "acc_1", type: "deposit", since: "yesterday")
   → [{amount: 55000, merchant: "ACME CORP"}, {amount: 120000, merchant: "TECHCO INC"}]
3. Total new revenue: $550 + $1,200 = $1,750
4. [Cross-MCP] Match to invoices for reconciliation
```

## Backend Capabilities

| Capability | Plaid | Mono | Open Banking |
|-----------|:-----:|:----:|:------------:|
| List accounts | ✅ | ✅ | ✅ |
| Real-time balance | ✅ | ✅ | ✅ |
| Transaction history | ✅ (2yr) | ✅ (1yr) | ✅ (90d) |
| Transaction search | ✅ | ✅ | ❌ |
| Categorization | ✅ (auto) | ✅ (manual) | ❌ |
| Payment initiation | ✅ (US) | ✅ (Africa) | ✅ (UK/EU) |
| Identity verification | ✅ | ✅ | ✅ |
| Statements | ✅ | ✅ | ❌ |
