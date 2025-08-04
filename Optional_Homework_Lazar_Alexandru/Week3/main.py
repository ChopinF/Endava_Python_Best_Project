numbers = [10, 20, 30, 40, 50]

# cerinta 3.1
print(numbers[0])
print(numbers[-1])
middleIndex = int((len(numbers) - 1) / 2)
print(numbers[middleIndex])
numbers.append(60)
numbers.insert(1, 15)
numbers.pop()
print(len(numbers))
numbers.sort()
print(numbers)

# cerinta 3.2
string = "Python is fun because Python is powerful"
target_word = "Python"
new_word = "Programming"
string.replace(target_word, new_word)

# cerinta 3.3
word = "level"
print(word == word[::-1])

# cerinta 3.4
name = "Alice"
age = 30
balance = 1234.56789
membership_date = "2023-08-12"
status = True

print(f"User : {name}, age: {age}")
print(f"${balance:.2f}")
print(f"Member since: {membership_date}")
status_message = "Yes" if status else "No"
print(f"Active member : {status_message}")
