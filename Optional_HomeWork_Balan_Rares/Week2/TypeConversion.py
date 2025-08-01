x = 100
y = -30
z = 0

xFloat = float(x)
yBool = bool(y)
zBool = bool(z)
zFloat = float(z)

print("x == x_float:", x == xFloat)
print("y == y_bool:", y == yBool)
print("z == z_bool:", z == zBool)
print("z == z_float:", z == zFloat)


print("id(x):", id(x), "| id(x_float):", id(xFloat))
print("id(y):", id(y), "| id(y_bool):", id(yBool))
print("id(z):", id(z), "| id(z_bool):", id(zBool))
print("id(z):", id(z), "| id(z_float):", id(zFloat))