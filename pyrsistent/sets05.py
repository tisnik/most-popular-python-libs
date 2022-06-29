from pyrsistent import s

set1 = s(1,2,3)

for i in range(0, 5):
    print(i, i in set1)
