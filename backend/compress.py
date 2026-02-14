def compress_context(text, limit=800):
    lines = text.splitlines()
    important = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(("import", "from", "def", "class")):
            important.append(line)
        elif len(important) < limit:
            important.append(line)
    return "\n".join(important)
