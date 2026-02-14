import ollama
from backend.compress import compress_context
def answer(query, contexts):
    context = compress_context("\n\n".join(contexts))
    prompt = f"""
Explain the code:
Context:
{context}
Question:
{query}
"""
    res = ollama.chat(
        model="qwen2.5-coder:3b",
        messages=[{"role":"user","content":prompt}]
    )
    return res["message"]["content"]
