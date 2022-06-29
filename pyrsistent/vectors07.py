from pyrsistent import v

vector1 = v(1, "foo", (1, 2, 3), None)
print(vector1)
print(type(vector1))

print(0, vector1[0])
print(3, vector1[3])
print(-1, vector1[-1])
print(-2, vector1[-2])
