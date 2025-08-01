squares = [x**2 for x in range(1,11)]
print(squares)
div7 = {x for x in range(1,51) if x%7 == 0}
print(div7)
score = {"alice":85, "Bob": 59, "Cipri": 92}
passed = {name: s for name, s in score.items() if s>= 60}
print(passed)
students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
attendance = {
    student: {day: (day in ["Mon", "Wed"]) for day in weekdays}
    for student in students
}
print("Weekly attendance log:")
for student, days in attendance.items():
    print(f"{student}: {days}")