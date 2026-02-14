from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
model = SentenceTransformer("all-MiniLM-L6-v2")
def build_index(chunks):
    texts = [c["content"] for c in chunks]
    emb = model.encode(texts)
    dim = emb.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(emb))
    return index, texts
