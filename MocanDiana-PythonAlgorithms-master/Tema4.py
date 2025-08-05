# 1. Are two words anagrams? (dictionary-based, not sorted or Counter)
word1 = "listen"
word2 = "silent"

def letter_count(word):
    freq = {}
    for letter in word:
        freq[letter] = freq.get(letter, 0) + 1
    return freq

dict1 = letter_count(word1)
dict2 = letter_count(word2)

# Compare by checking keys and values
is_anagram = dict1.keys() == dict2.keys() and all(dict1[k] == dict2[k] for k in dict1)
print(f"'{word1}' and '{word2}' are anagrams:", is_anagram)

# Modify dict1: remove one letter
dict1.pop('t')
print("After removing 't' from dict1:", dict1)
print("dict2 remains:", dict2)

print("\n---\n")

# 2. Invert a dictionary with duplicates in values
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C"
}
inverted = {}
for k, v in grades.items():
    inverted.setdefault(v, []).append(k)
print("Inverted dictionary:", inverted)

print("\n---\n")

# 3. Set analysis for conference attendees
testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}

# Attended all three: check membership in all sets
all_three = {name for name in testing | development | devops
             if name in testing and name in development and name in devops}
print("Attended all three sessions:", all_three)

# Attended only one session: count membership
all_attendees = testing | development | devops
only_one = {name for name in all_attendees
            if sum([name in testing, name in development, name in devops]) == 1}
print("Attended only one session:", only_one)

# Are all testing attendees in devops?
all_testing_in_devops = all(name in devops for name in testing)
print("All testing attendees in devops:", all_testing_in_devops)

# Unique attendees, sorted
unique_sorted = sorted(all_attendees)
print("All unique attendees sorted:", unique_sorted)

# Copy and clear development set
dev_copy = development.copy()
development.clear()
print("Copy of development set:", dev_copy)
print("Original development set after clear:", development)

print("\n---\n")

# 4. Create data with comprehensions
# List of squares
squares = [x * x for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

# Set of numbers divisible by 7 between 1 and 50
div7 = {x for x in range(1, 51) if x // 7 * 7 == x}
print("Numbers divisible by 7 (1-50):", div7)

# Dictionary of students who passed
score = {"Alice": 85, "Bob": 59, "Charlie": 92}
passed = {k: v for k, v in score.items() if v >= 60}
print("Students who passed:", passed)

# Nested dictionary comprehension for weekly attendance
students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
attendance = {
    f" {student} ": {day: (day in ("Mon", "Wed")) for day in weekdays}
    for student in students
}
print("Weekly attendance log:", attendance)