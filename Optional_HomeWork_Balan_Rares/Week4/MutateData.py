data = [
    ['2021-01-01', 20, 10],
    ['2021-01-02', 20, 18],
    ['2021-01-03', 10, 10],
    ['2021-01-04', 102, 100],
    ['2021-01-05', 45, 25]
]
for row in data:
    date, stop, start = row
    diff = stop - start
    row.insert(1, diff)
maxRow = max(data,key = lambda x: x[1])
print(maxRow[0])