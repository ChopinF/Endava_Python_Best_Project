# cerinta 5.1
from collections import Counter

s1 = "listen"
s2 = "silent"
if len(s1) != len(s2):
    print("No anagrams")
else:
    if Counter(s1) == Counter(s2):
        print("Yes")
    else:
        print("No")

# cerinta 5.2
grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "Diana": "C"}
dict_answer = {}
for k, v in grades.items():
    if k not in dict_answer:
        dict_answer[k] = []
    dict_answer[k].append(v)
print(dict_answer)

# cerinta 5.3
testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}

all_three_sessions = testing & development & devops
print(f"Attendees who attended all three sessions: {all_three_sessions}")

only_testing = testing - (development | devops)
only_development = development - (testing | devops)
only_devops = devops - (testing | development)
only_one_session = only_testing | only_development | only_devops
print(f"Attendees who attended only one session: {only_one_session}")

all_testing_in_devops = testing.issubset(devops)
print(f"All testing attendees are in devops session: {all_testing_in_devops}")

all_attendees = sorted(testing | development | devops)
print(f"All unique attendees sorted alphabetically: {all_attendees}")

dev_copy = development.copy()
development.clear()
print(f"Copy of development attendees: {dev_copy}")
print(f"Original development attendees after clear: {development}")

# cerinta 5.4
squares = [x**2 for x in range(1, 11)]
print(f"Squares from 1 to 10: {squares}")

div_by_7 = {x for x in range(1, 51) if x % 7 == 0}
print(f"Numbers divisible by 7 between 1 and 50: {div_by_7}")

score = {"Alice": 85, "Bob": 59, "Charlie": 92}
passed_students = {name: marks for name, marks in score.items() if marks >= 60}
print(f"Students who passed: {passed_students}")

students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

attendance_log = {
    student: {day: (day == "Mon" or day == "Wed") for day in weekdays}
    for student in students
}
print("Weekly attendance log:")
for student, attendance in attendance_log.items():
    print(f"{student}: {attendance}")
