from fastapi import FastAPI
from backend.repo_loader import clone_repo
from backend.parser import parse_repo
from backend.embeddings import build_index
from backend.retriever import retrieve
from backend.rag import answer
from backend.complexity import complexity_score
from backend.risk import bug_risk
from backend.impact import impact_analysis
from backend.architecture import architecture_summary
from backend.change_risk import change_risk
app = FastAPI()
index = None
texts = None
chunks = None
@app.post("/load")
def load(url: str):
    global index, texts, chunks
    path = clone_repo(url)
    chunks = parse_repo(path)
    for c in chunks:
        c["complexity"] = complexity_score(c["content"])
        c["risks"] = bug_risk(c["content"])
    index, texts = build_index(chunks)
    arch = architecture_summary(chunks)
    return {
        "status": "Repository indexed",
        "architecture": arch
    }
@app.post("/ask")
def ask(query: str):
    global index, texts, chunks
    contexts = retrieve(query, index, texts, chunks)
    ans = answer(query, [c["content"] for c in contexts])
    enriched = []
    for c in contexts:
        impact = impact_analysis(c["file"], chunks)
        risk_level = change_risk(c)
        c["impact"] = impact
        c["risk_level"] = risk_level
        enriched.append(c)
    return {
        "answer": ans,
        "contexts": enriched
    }
