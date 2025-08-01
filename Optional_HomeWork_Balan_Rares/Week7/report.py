def generate_report(data: dict) -> str:
    passed_students = {name: score for name, score in data.items() if score >= 80}
    sorted_students = sorted(passed_students.items())
    report_lines = ["=== Final Report ==="]
    for name, score in sorted_students:
        report_lines.append(f"{name:<10} : {score:>3}")
    return "\n".join(report_lines)