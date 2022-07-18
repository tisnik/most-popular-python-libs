from pyrsistent import freeze, v

vector1 = freeze([1, "foo", v(1, [2, 3]), None], strict=False)
print(vector1)
print(type(vector1))

vector2 = vector1.append("Five!")
print(vector1)
print(type(vector1))

print(vector2)
print(type(vector2))
