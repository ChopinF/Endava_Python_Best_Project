path = "Week7/students.txt"
filterPath ="Week7/filtered.txt"
vowels = ('A', 'E', 'I', 'O', 'U')
with open("students.txt","r") as infile, open("filtered.txt","w") as outfile:
    for line in infile:
        name = line.strip()
        if name.startswith(vowels):
            outfile.write(name + '\n')

