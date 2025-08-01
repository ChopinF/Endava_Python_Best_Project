#Integers
a = 10
print("original value", a)
print("Adress of a ", id(a))

a = a + 5
print("Memory adress : ",id(a)) ## its different
#Floats
b = 2.16
print("original value", b)
print("Adress",id(b))
b = b*3
print("New adress",id(b))