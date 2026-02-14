from rag import answer
def repo_summary(chunks):
    combined = "\n".join(c["content"] for c in chunks[:5])
    return answer("Summarize repository", [combined])
