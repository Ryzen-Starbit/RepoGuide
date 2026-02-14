import ollama
def generate_docs(code):
    prompt = f"Generate documentation for:\n{code}"
    res = ollama.chat(
        model="codellama",
        messages=[{"role":"user","content":prompt}]
    )
    return res["message"]["content"]
