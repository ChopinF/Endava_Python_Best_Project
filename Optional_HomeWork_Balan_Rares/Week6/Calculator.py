def calculate(*args, operation='+'):
    if not args:
        return 0
    if operation == '+':
        result = sum(args)
    elif operation == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operation == '*':
        result = 1
        for num in args:
            result *= num
    elif operation == '/':
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error"
            result /= num
    else:
        return "Error"
    return result

print(calculate(2, 3, 4, operation='*'))
print(calculate(10, 0, operation='/'))
