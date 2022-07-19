from pyrsistent import pmap

map1 = pmap({1: "first", 2: "second", 3: "third"})
map2 = pmap({3: "3rd", 4: "4th"})

print(map1)
print(map2)

map3 = map1 + map2
print(map3)
