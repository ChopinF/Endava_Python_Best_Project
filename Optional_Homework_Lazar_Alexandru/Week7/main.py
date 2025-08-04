# cerinta 7.1
with open("students.txt", "w") as f:
    f.write("Ana\nBob\nCharlie\nEve\nOscar\nIan\nUrsula\nMike\nElliot\n")

vowels = {"A", "E", "I", "O", "U"}
with open("students.txt", "r") as f_in, open("filtered.txt", "w") as f_out:
    for line in f_in:
        name = line.strip()
        if name[0].upper() in vowels:
            f_out.write(name + "\n")

print("Names starting with vowels have been written to 'filtered.txt'.")

# cerinta 7.2
with open("log.txt", "w") as f:
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")
    f.write("This is line 4.\n")
    f.write("This is line 5.\n")

with open("log.txt", "r") as f_in, open("reversed_log.txt", "w") as f_out:
    lines = f_in.readlines()
    f_out.writelines(reversed(lines))

print("Content of 'log.txt' has been reversed and written to 'reversed_log.txt'.")


# cerinta 7.3
def generate_report(data):
    passed_students = {name: score for name, score in data.items() if score >= 80}

    sorted_students = sorted(passed_students.items(), key=lambda x: x[1], reverse=True)

    report = "Student Report:\n"
    for name, score in sorted_students:
        report += f"{name}: {score}\n"

    return report
