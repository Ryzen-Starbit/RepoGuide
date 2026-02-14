import os
CHUNK_SIZE = 1200
OVERLAP = 200
def split_code(text):
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start += CHUNK_SIZE - OVERLAP
    return chunks
def parse_repo(path):
    chunks = []
    for root, _, files in os.walk(path):
        if "test" in root.lower():
            continue
        for f in files:
            if f.endswith((".py", ".js", ".ts", ".java")):
                fp = os.path.join(root, f)
                try:
                    with open(fp, errors="ignore") as file:
                        content = file.read()
                    parts = split_code(content)
                    for part in parts:
                        chunks.append({
                            "file": fp,
                            "content": part
                        })
                except:
                    pass
    return chunks
