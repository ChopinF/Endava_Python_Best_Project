# 1. File filtering with context manager
vowels = {'A', 'E', 'I', 'O', 'U'}
with open('students.txt', 'r') as fin, open('filtered.txt', 'w') as fout:
    for name in fin:
        name_clean = name.strip()
        if name_clean and name_clean[0].upper() in vowels:
            fout.write(name_clean + '\n')

# 2. Reverse file content
with open('log.txt', 'r+') as f:
    lines = f.readlines()
    f.seek(0)
with open('reversed_log.txt', 'w') as fout:
    for line in reversed(lines):
        fout.write(line)

# 3. Modularize student report generator
from report import generate_report

data = {'Lisa': 85, 'Bart': 72, 'Homer': 91}
report = generate_report(data)
print(report)# report.py
