from pyrsistent import pmap

map1 = pmap({1:"first", 2:"second"})
map2 = pmap({3:"third", 4:"fourth"})

print(map1)
print(map2)

map3 = map1 + map2
print(map3)
