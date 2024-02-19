from random import randrange
from toolz.itertoolz import isdistinct, unique

values = [randrange(1, 11, 1) for _ in range(30)]
print(list(values))
print(isdistinct(values))

print()

values2 = unique(values)
print(list(values2))
print(isdistinct(values2))
