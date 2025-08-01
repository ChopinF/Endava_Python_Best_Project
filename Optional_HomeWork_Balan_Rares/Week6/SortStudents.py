names = ["Lucas", "Nataly", "Megi", "Steven"]
scores = [85, 92, 78, 81]
final = dict(zip(names, scores))
final_sorted = dict(sorted(final.items(), key=lambda item: item[0]))
final_sorted.pop('Megi')
print(final_sorted)
