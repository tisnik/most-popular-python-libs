from random import randrange

from toolz.recipes import partitionby

values = [randrange(1, 11, 1) for _ in range(30)]
print(values)

values2 = partitionby(lambda x: x < 5, values)
print(list(values2))
