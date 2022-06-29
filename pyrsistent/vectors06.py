from pyrsistent import v

m = {}

vector1 = v(1, "foo", (1, 2, 3), m)
print(vector1)
print(type(vector1))

m["one"] = 1
print(vector1)
print(type(vector1))

m["two"] = 2
print(vector1)
print(type(vector1))

m = {"jedna": 1,
     "dva": 2}
print(vector1)
print(type(vector1))
