def impact_analysis(target_file, chunks):
    impacted = []
    for c in chunks:
        imports = c.get("imports", [])
        for imp in imports:
            if target_file in imp:
                impacted.append(c["file"])
    return list(set(impacted))
