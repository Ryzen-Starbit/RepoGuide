def complexity_score(code: str) -> int:
    keywords = [
        "if", "elif", "else",
        "for", "while",
        "try", "except",
        "case",
        "and", "or"
    ]
    score = 1 
    for k in keywords:
        score += code.count(k)
    return score
