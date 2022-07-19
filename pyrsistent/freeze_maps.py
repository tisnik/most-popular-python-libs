from pyrsistent import freeze

map1 = freeze({1: "first", 2: "second", 3: "third"})

print(map1)
print(type(map1))
