grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C"
}
dict = {}
for name, grade in grades.items():
    if grade not in dict:
        dict[grade]=[]
    dict[grade].append(name)
print(dict)