# tuple-urile sunt immutable

tuple1 = (1, 2, 3)
tuple1[0] = 5
print(tuple1)

# error returned:
# line 4, in <module>
#     tuple1[0] = 5
# TypeError: 'tuple' object does not support item assignment
