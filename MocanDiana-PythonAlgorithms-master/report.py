
def generate_report(data: dict):
    passed = {name: score for name, score in data.items() if score >= 80}
    lines = [f"{name}: {score}" for name, score in sorted(passed.items())]
    return "Student Report\n" + "\n".join(lines)