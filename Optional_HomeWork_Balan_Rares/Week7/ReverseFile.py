with open("log.txt", "w") as log_file:
    log_file.write("""AAAAAAAAAAAAAAAAAAAAAA
Line 2 Line 2 Line 2 Line 2
Line Line Line Line Line
Line Line Line Line
Line Line
""")
with open("log.txt", "r") as log_file:
    lines = log_file.readlines()
with open("reversed_log.txt", "w") as reversed_file:
    reversed_file.writelines(reversed(lines))