# Banking Skill Examples

## Example 1: "What's our cash position?"

**User says:** "How much do we have in the bank?"

**Tool calls:**
```
1. list_accounts()
   → [{id: "acc_1", name: "Operating", type: "checking"}, {id: "acc_2", name: "Savings", type: "savings"}]

2. get_balances(account_id: "acc_1") → {current: 2500000, available: 2450000}
3. get_balances(account_id: "acc_2") → {current: 10000000, available: 10000000}
```

**Response:**
```
## Cash Position

| Account | Type | Current | Available |
|---------|------|---------|-----------|
| Operating | Checking | $25,000.00 | $24,500.00 |
| Savings | Savings | $100,000.00 | $100,000.00 |

**Total Cash:** $125,000.00
**Total Available:** $124,500.00

Note: $500 difference in Operating is pending transactions not yet cleared.
```

## Example 2: "Show me today's deposits"

**User says:** "What payments came in today?"

**Tool calls:**
```
1. sync_transactions(account_id: "acc_1")
2. list_transactions(account_id: "acc_1", type: "deposit", start_date: "2025-01-18")
   → [
       {amount: 55000, merchant: "ACME CORP", date: "2025-01-18T09:30:00Z"},
       {amount: 120000, merchant: "TECHCO INC", date: "2025-01-18T11:15:00Z"},
       {amount: 29900, merchant: "STRIPE TRANSFER", date: "2025-01-18T14:00:00Z"}
     ]
```

**Response:**
```
## Today's Deposits

| Time | From | Amount |
|------|------|--------|
| 9:30 AM | ACME CORP | $550.00 |
| 11:15 AM | TECHCO INC | $1,200.00 |
| 2:00 PM | STRIPE TRANSFER | $299.00 |

**Total received today:** $2,049.00

Would you like me to reconcile these against outstanding invoices?
```

## Example 3: "Flag any unusual transactions"

**User says:** "Check for suspicious activity on our accounts"

**Tool calls:**
```
1. sync_transactions(account_id: "acc_1")
2. list_transactions(account_id: "acc_1", start_date: "2025-01-17")
   → [...transactions...]
3. Run scripts/detect_anomalies.py
   → {anomalies_found: 1, anomalies: [{amount: 500000, merchant: "UNKNOWN VENDOR", time: "03:15", risk: "critical"}]}
```

**Response:**
```
🚨 Anomaly Detected

| Flag | Details |
|------|---------|
| Amount | $5,000.00 (10x your average transaction) |
| Merchant | UNKNOWN VENDOR (not seen before) |
| Time | 3:15 AM (outside business hours) |
| Risk | **CRITICAL** |

**Recommended actions:**
1. Verify this transaction with your bank immediately
2. Check if any team member authorized this
3. Consider freezing the card/account if unauthorized

Want me to alert the finance team via Slack?
```
