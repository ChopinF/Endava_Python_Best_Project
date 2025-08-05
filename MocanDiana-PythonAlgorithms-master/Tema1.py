
# 1. Immutable Data Types
a = 10
print("a init:", id(a))
a += 1
print("a increment :", id(a))

b = 3.14
print("b :", id(b))
b *= 2
print(" b multiplication :", id(b))

print("\n---\n")

# 2. Leap year checker
year = input("year: ")
year_int = int(year)
if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
    print("This is a leap year.")
else:
    print("This isn't a leap year.")

print("\n---\n")

# 3. Ternary conditional operator
num = -7
print("Positive" if num > 0 else "Negative")

print("\n---\n")

# 4. Boolean logic practice
x = 5
y = 0
z = -3

print(">0:", x > 0 and y > 0 and z > 0)
print("=0 min 1:", x == 0 or y == 0 or z == 0)
print("!<0:", not (x < 0 or y < 0 or z < 0))

print("\n---\n")

# 5. Type conversion and identity
x = 100
y = -30
z = 0

# Conversions
x_float = float(x)
y_bool = bool(y)
z_int = int(z)

print("x float:", x_float)
print("y bool:", y_bool)
print("z int:", z_int)

# Identity comparison
print("id(x):", id(x))
print("id(int(x_float)):", id(int(x_float)))
print("x == int(x_float):", x == int(x_float))
print("x IS int(x_float):", x is int(x_float))