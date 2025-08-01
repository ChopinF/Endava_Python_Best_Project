def check_age(age_input):
    try:
        if age_input.strip() == "":
            raise ValueError("Age cannot be an empty string.")
        age = int(age_input)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        print(f"Valid age entered: {age}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError:
        print("TypeError: Age must be a number.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Validation complete\n")
test_inputs = [
    "25",
    "",
    "abc",
    "-5",
    "150",
    "  ",
    "0",
    "120",
    "30.5",
    "0030"
]

for i, test_input in enumerate(test_inputs, 1):
    print(f"Test case {i}: Input = '{test_input}'")
    check_age(test_input)
