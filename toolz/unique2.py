from random import randrange
from toolz.itertoolz import unique

values = [randrange(1, 11, 1) for _ in range(30)]
print(values)

values2 = unique(values)
print(list(values2))
