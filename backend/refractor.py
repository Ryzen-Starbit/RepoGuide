import ollama
def suggest_refactor(code):
    prompt = f"Suggest refactoring improvements:\n{code}"
    res = ollama.chat(
        model="codellama",
        messages=[{"role":"user","content":prompt}]
    )
    return res["message"]["content"]
