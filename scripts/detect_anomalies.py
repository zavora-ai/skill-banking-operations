#!/usr/bin/env python3
"""
Transaction Anomaly Detector
Flags unusual transactions based on amount, timing, velocity, and merchant patterns.
Usage: python detect_anomalies.py '{"transactions": [...], "history_avg": 5000}'
"""
import json
import sys
from datetime import datetime

def detect_anomalies(data: dict) -> dict:
    transactions = data.get("transactions", [])
    history_avg = data.get("history_avg", 10000)  # average transaction in minor units
    
    anomalies = []
    
    for txn in transactions:
        amount = abs(txn.get("amount", 0))
        merchant = txn.get("merchant", "UNKNOWN")
        timestamp = txn.get("timestamp", "")
        category = txn.get("category", "uncategorized")
        
        flags = []
        severity = 0
        
        # Large amount (> 3x average)
        if amount > history_avg * 3:
            flags.append(f"Amount ${amount/100:.2f} is {amount/history_avg:.1f}x average")
            severity += 30
        
        # Very large (> 10x average)
        if amount > history_avg * 10:
            flags.append("Extremely large transaction (>10x average)")
            severity += 30
        
        # Unusual time (midnight to 5 AM)
        if timestamp:
            try:
                hour = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).hour
                if 0 <= hour < 5:
                    flags.append(f"Unusual time: {hour:02d}:00")
                    severity += 20
            except (ValueError, TypeError):
                pass
        
        # Unknown merchant with large amount
        if merchant == "UNKNOWN" and amount > history_avg:
            flags.append("Unknown merchant with above-average amount")
            severity += 25
        
        # Uncategorized + large
        if category == "uncategorized" and amount > history_avg * 2:
            flags.append("Uncategorized large transaction")
            severity += 10
        
        if flags:
            anomalies.append({
                "transaction_id": txn.get("id"),
                "amount": amount,
                "merchant": merchant,
                "timestamp": timestamp,
                "flags": flags,
                "severity": min(severity, 100),
                "risk": "critical" if severity >= 60 else "high" if severity >= 40 else "medium",
            })
    
    # Velocity check (multiple transactions in short window)
    if len(transactions) >= 5:
        # Simple: more than 5 transactions in the batch = velocity flag
        anomalies.append({
            "type": "velocity",
            "count": len(transactions),
            "flags": [f"{len(transactions)} transactions in short window"],
            "severity": 40 if len(transactions) > 10 else 20,
            "risk": "high" if len(transactions) > 10 else "medium",
        })
    
    return {
        "total_transactions": len(transactions),
        "anomalies_found": len(anomalies),
        "anomalies": sorted(anomalies, key=lambda x: x.get("severity", 0), reverse=True),
        "requires_review": any(a.get("risk") == "critical" for a in anomalies),
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python detect_anomalies.py \'{"transactions": [...], "history_avg": 5000}\'')
        sys.exit(1)
    data = json.loads(sys.argv[1])
    print(json.dumps(detect_anomalies(data), indent=2))
