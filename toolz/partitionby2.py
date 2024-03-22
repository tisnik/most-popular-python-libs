from random import randrange

from toolz.recipes import partitionby

values = [randrange(-5, 5, 1) for _ in range(30)]
print(values)

values2 = partitionby(lambda x: x < 0, values)
print(list(values2))
