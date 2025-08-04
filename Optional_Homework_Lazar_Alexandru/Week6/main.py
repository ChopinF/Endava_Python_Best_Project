# cerinta 6.1
def calculate(*args, operation="+"):
    if not args:
        return 0

    result = args[0]

    try:
        for num in args[1:]:
            if operation == "+":
                result += num
            elif operation == "-":
                result -= num
            elif operation == "*":
                result *= num
            elif operation == "/":
                if num == 0:
                    raise ZeroDivisionError("Cannot divide by 0.")
                result /= num
            else:
                raise ValueError("Invalid operation")
    except Exception as e:
        return f"Error: {e}"

    return result


print(calculate(2, 3, 4, operation="*"))  # 24
print(calculate(10, 0, operation="/"))  # error: Cannot divide by 0.
print(calculate(operation="-"))  # 0

# cerinta 6.2
names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]
scores = [85, 92, 78, 81, 67]

students = list(zip(names, scores))

sorted_students = sorted(
    [student for student in students if student[1] >= 80],
    key=lambda x: x[1],
    reverse=True,
)

for name, score in sorted_students:
    print(f"{name}: {score}")


# cerinta 6.3
def check_age(age):
    try:
        if not age:
            raise ValueError("Age input cannot be empty.")
        age = int(age)

        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age > 120:
            raise ValueError("Age cannot be greater than 120.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Validation complete")


check_age("25")
check_age("")
check_age("-5")
check_age("130")
check_age("abc")
