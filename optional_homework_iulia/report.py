def generate_report(data: dict) -> str:
    # Filter students with scores >= 80
    filtered = {name: score for name, score in data.items() if score >= 80}
    # Sort by name
    sorted_items = sorted(filtered.items())
    # Build report string
    report_lines = ["Student Report (Scores >= 80):"]
    for name, score in sorted_items:
        report_lines.append(f"{name}: {score}")
    return "\n".join(report_lines)