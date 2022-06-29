from pyrsistent import v

vector1 = v(1, "foo", (1, 2, 3), None)
print(vector1)
print(type(vector1))

print(vector1[1:3])
print(vector1[1:])
print(vector1[:3])
print(vector1[:])
