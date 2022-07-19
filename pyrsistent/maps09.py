from pyrsistent import pmap

map1 = pmap({1: "first", 2: "second", 3: "third"})

vector1 = map1.items()

print("Items:")
print(vector1)
print(type(vector1))

vector2 = map1.values()

print("\nValues:")
print(vector2)
print(type(vector2))
