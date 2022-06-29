from pyrsistent import v

l = []

vector1 = v(1, "foo", (1, 2, 3), l)
print(vector1)
print(type(vector1))

l = [1, 2, 3]
print(vector1)
print(type(vector1))
