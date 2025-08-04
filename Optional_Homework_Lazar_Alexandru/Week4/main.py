# cerinta 4.1
data = [(100, "USD", "EUR", 0.83), (100, "USD", "CAD", 1.27), (100, "CAD", "EUR", 0.65)]

for amount, currency, target_currency, exchange_rate in data:
    converted_amount = amount * exchange_rate
    print(f"{amount} {currency} = {converted_amount:.2f} {target_currency}")

# cerinta 4.2
print(sum([i if i % 2 == 0 else 0 for i in range(0, 100)]))

# cerinta 4.3
magic_number = 7
count = 1
guessed_number = int(input("Guess number"))
while guessed_number != magic_number:
    if count > 3:
        print("Too many attempts")
        break
    guessed_number = int(input("Guess number"))

fruits = ["apple", "banana", "cherry", "date"]
for i in range(0, len(fruits)):
    print(f"Idx: {i}, name : {fruits[i]}, number of letters : {len(fruits[i])}")

# cerinta 4.4
data = (
    ["2021-01-01", 20, 10],
    ["2021-01-02", 20, 18],
    ["2021-01-03", 10, 10],
    ["2021-01-04", 102, 100],
    ["2021-01-05", 45, 25],
)

for record in data:
    start, stop = record[1], record[2]
    difference = stop - start
    record.insert(1, difference)

max_difference = float("-inf")
max_date = None

for record in data:
    if record[1] > max_difference:
        max_difference = record[1]
        max_date = record[0]

print(f"The date with the largest difference is: {max_date}")
