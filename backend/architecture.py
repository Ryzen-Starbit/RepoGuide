def architecture_summary(chunks):
    modules = set()
    total_files = len(chunks)
    for c in chunks:
        parts = c["file"].split("/")
        if len(parts) > 1:
            modules.add(parts[0])
    summary = f"""
Repository Architecture Overview:
• Total indexed files: {total_files}
• Major modules: {", ".join(list(modules)[:8])}
• System structured into logical components.
• Codebase separated by feature/modules.
"""
    return summary
