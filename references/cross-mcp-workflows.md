# Banking Cross-MCP Workflows

## Banking + Finance: Auto-Reconciliation Pipeline

```
BANKING: sync_transactions(account: "operating")
BANKING: list_transactions(type: "deposit", since: "yesterday")
  → [{amount: 55000, merchant: "ACME CORP", id: "txn_abc"}]
FINANCE: list_invoices(status: "unpaid", customer_search: "acme")
  → [{id: "inv_123", amount: 55000}]
FINANCE: reconcile_transaction(transaction_id: "txn_abc", invoice_id: "inv_123")
  → Invoice marked paid, revenue recognized
SLACK: send_message(channel: "#finance", text: "💰 Auto-reconciled: $550 from Acme → inv_123")
```

## Banking + Payments: Balance-Verified Payouts

```
BANKING: get_balances(account: "operating") → {available: 2450000}
PAYMENTS: create_payout_intent(amount: 100000, recipient: "vendor")
  → Verified: $24,500 available > $1,000 payout ✅
PAYMENTS: request_payment_approval(reason: "Vendor payout, balance verified")
```

## Banking + Notifications: Anomaly Alerts

```
BANKING: sync_transactions()
BANKING: list_transactions(since: "1h ago")
  → [{amount: 500000, merchant: "UNKNOWN", time: "03:15"}]
→ Run scripts/detect_anomalies.py → severity: critical
NOTIFICATIONS: notification_send(
  recipient: finance_team,
  channel: "push",
  title: "🚨 Suspicious: $5,000 to UNKNOWN at 3:15 AM",
  priority: "critical"
)
```

## Banking + CRM: Payment Received → Update Customer

```
BANKING: list_transactions(type: "deposit", since: "today")
  → [{amount: 75000, merchant: "ACME CORP"}]
CRM: search_contacts(query: "acme") → {contact_id: "c_123"}
CRM: create_activity(type: "note", subject: "Payment received: $750 from Acme Corp", record_id: "c_123")
CRM: update_deal(id: "d_456", custom_field: "last_payment_date", value: "2025-01-18")
```

## Full Cash Flow Monitoring (Daily)

```
1. BANKING: sync_transactions(all accounts)
2. BANKING: get_balances(all accounts) → total cash position
3. BANKING: list_transactions(type: "deposit") → revenue received
4. BANKING: list_transactions(type: "withdrawal") → expenses paid
5. FINANCE: reconcile unmatched deposits to invoices
6. Run detect_anomalies.py on new transactions
7. SLACK: send_message(#finance, "Daily cash: $X in, $Y out, balance: $Z")
```
