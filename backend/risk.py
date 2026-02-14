def bug_risk(code):
    risks = []
    if "except:" in code:
        risks.append("Bare except")
    if "eval(" in code:
        risks.append("eval used")
    if "exec(" in code:
        risks.append("exec used")
    return risks
