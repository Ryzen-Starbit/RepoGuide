import numpy as np
from backend.embeddings import model
def retrieve(query, index, texts, chunks, k=5):
    q = model.encode([query])
    D, I = index.search(np.array(q), k)
    results = []
    seen_files = set()
    for i in I[0]:
        chunk = chunks[i]
        if chunk["file"] not in seen_files:
            results.append(chunk)
            seen_files.add(chunk["file"])
        if len(results) >= 3:
            break
    return results
