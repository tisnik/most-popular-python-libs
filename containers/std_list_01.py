seznam = [1, 2, 3, 4]

print(seznam[0])
print(seznam[1])
print(seznam[-1])
print(seznam[-2])

seznam.append(5)
seznam.append(6)

seznam.insert(0, -10)
seznam.insert(0, -100)

print(seznam)

del seznam[0]
print(seznam)
del seznam[-1]
print(seznam)
