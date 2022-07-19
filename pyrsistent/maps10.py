from pyrsistent import pmap

map1 = pmap({1: "first", 2: "second", 3: "third"})

list1 = list(map1)

print("As list:")
print(list1)
print(type(list1))
