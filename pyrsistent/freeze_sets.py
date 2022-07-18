from pyrsistent import freeze

set1 = freeze({1,2,3})

print(set1)
print(type(set1))

print()

for i in range(0, 5):
    print(i, i in set1)
