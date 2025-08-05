# 1. Currency conversion
data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]
for amount, currency, target_currency, exchange_rate in data:
    converted = amount * exchange_rate
    print(f"{amount} {currency} = {converted:.0f} {target_currency}")

print("\n---\n")

# 2. Sum of odd numbers
odd_sum = 0
for i in range(1, 101, 2):
    odd_sum += i
print("Sum of odd numbers from 1 to 100:", odd_sum)

print("\n---\n")

# 3. Number guessing game
secret = 7
attempts = 3
for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}/{attempts}: Guess the number: "))
    if guess == secret:
        print("Congratulations! You guessed the number.")
        break
else:
    print("Sorry, you did not guess the number.")

print("\n---\n")

# 4. Enumerate list items
fruits = ['apple', 'banana', 'cherry', 'date']
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}: {fruit} ({len(fruit)} letters)")

print("\n---\n")

# 5. Mutate the data
data = (
    ['2021-01-01', 20, 10],
    ['2021-01-02', 20, 18],
    ['2021-01-03', 10, 10],
    ['2021-01-04', 102, 100],
    ['2021-01-05', 45, 25]
)
max_diff = None
max_date = None
for row in data:
    diff = row[1] - row[2]
    row.insert(1, diff)
    if max_diff is None or diff > max_diff:
        max_diff = diff
        max_date = row[0]
print("Date with largest difference:", max_date)