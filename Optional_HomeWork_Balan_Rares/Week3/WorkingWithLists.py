numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[len(numbers)-1])
print(numbers[int((len(numbers))/2)])
numbers.append(60)
print(numbers)
numbers.insert(1, 15)
print(numbers)
numbers.remove(numbers[len(numbers)-1])
print(numbers)
print(len(numbers))
numbers.sort()
print(numbers)

