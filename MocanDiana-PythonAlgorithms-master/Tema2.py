# 1.  lists
numbers = [10, 20, 30, 40, 50]
print("init = ", numbers[0])
print("end =", numbers[-1])
middle_index = len(numbers) // 2
print("mid =", numbers[middle_index])

numbers.append(60)
numbers.insert(1, 15)
numbers.pop()
print("Length :", len(numbers))
numbers.sort()
print("Sorted list:", numbers)

print("\n---\n")

# 2. Change a specific word in a sentence (without replace)
sentence = "Python is fun because Python is powerful"
target_word = "Python"
new_word = "Programming"
words = sentence.split()
for i in range(len(words)):
    if words[i] == target_word:
        words[i] = new_word
new_sentence = " ".join(words)
print("Changed sentence:", new_sentence)

print("\n---\n")

# 3. Palindrome  with slicing
word = "level"
is_palindrome = word == word[::-1]
print(f"'{word}' is a palindrome:", is_palindrome)

print("\n---\n")

# 4. f-string formatting
name = "Alice"
age = 30
balance = 1234.56789
membership_date = "2023-08-12"# 1. Currency conversion with unpacking and f-strings
