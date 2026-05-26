# Banking Operations Skill

> Real-time banking intelligence for AI agents — account monitoring, transaction analysis, anomaly detection, and payment initiation across Plaid (US/EU), Mono (Africa), and Open Banking (UK/EU).

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--banking-green)](https://github.com/zavora-ai/mcp-banking)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## Revenue Impact

This skill enables revenue operations by:
- **Detecting incoming payments** in real-time for instant reconciliation
- **Verifying balances** before outbound payments (prevent overdrafts)
- **Flagging anomalies** to protect revenue from fraud
- **Multi-region coverage** — collect from US, EU, UK, and Africa

| Workflow | Revenue Impact | Tool Calls |
|----------|---------------|-----------|
| Account Overview | Cash visibility | 2 |
| Transaction Analysis | Revenue tracking | 2-3 |
| Payment Initiation | Outbound payments | 3 |
| Anomaly Detection | Fraud prevention | 2-3 |
| Sync & Reconcile | Revenue recognition | 2-3 |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-banking-operations.git \
  ~/.skills/skills/banking-operations
```

## Requirements

**Required:** `mcp-banking` (Plaid, Mono, or Open Banking)

**Revenue-accelerating combos:**
- `mcp-finance` — auto-reconcile deposits to invoices
- `mcp-payments` — balance-verified payment execution
- `mcp-notifications` — anomaly alerts
- `mcp-slack` — daily cash flow updates

## Multi-Region Coverage

| Backend | Region | Capabilities |
|---------|--------|-------------|
| Plaid | US, Canada, EU | Full (accounts, transactions, payments, identity) |
| Mono | Nigeria, Kenya, Ghana, SA | Full (accounts, transactions, payments) |
| Open Banking | UK, EU (PSD2) | Accounts, balances, payments (90-day history) |

## Folder Structure

```
banking-operations/
├── SKILL.md                       # Main skill
├── scripts/
│   └── detect_anomalies.py        # Transaction anomaly detection
├── references/
│   ├── tool-sequences.md          # 15 tools with backend matrix
│   ├── cross-mcp-workflows.md     # Banking + Finance + Payments + CRM
│   └── examples.md                # Cash position, deposits, anomalies
├── README.md
└── LICENSE
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)

## Success Criteria

| Metric | Target |
|--------|--------|
| Balance verification | Always check before payments |
| Anomaly detection | Flag unusual transactions within 1 sync |
| Reconciliation | 95%+ auto-matched to invoices |
| Multi-region | Works across Plaid, Mono, Open Banking |
