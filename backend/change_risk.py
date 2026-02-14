def change_risk(chunk):
    score = chunk.get("complexity", 0)
    risks = chunk.get("risks", [])
    risk_level = "LOW"
    if score > 15 or len(risks) > 2:
        risk_level = "HIGH"
    elif score > 7:
        risk_level = "MEDIUM"
    return risk_level
