from pyrsistent import v

l = []

vector1 = v(1, "foo", (1, 2, 3), l)
print(vector1)
print(type(vector1))

l.append(1)
print(vector1)
print(type(vector1))

l.append(2)
print(vector1)
print(type(vector1))

l = []
print(vector1)
print(type(vector1))
