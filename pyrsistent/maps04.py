from pyrsistent import m

map1 = m(first=1, second=2, third=3)
print("Original map")
print(map1)

map2 = map1.set("fourth", 4)
print("\nAfter set")
print(map1)
print(map2)

map3 = map1.remove("first")
print("\nAfter remove")
print(map1)
print(map2)
print(map3)
