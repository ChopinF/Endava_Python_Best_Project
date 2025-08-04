from .main import generate_report

students_scores = {"Lisa": 85, "Bart": 72, "Homer": 91, "Marge": 78}

report = generate_report(students_scores)
print(report)
