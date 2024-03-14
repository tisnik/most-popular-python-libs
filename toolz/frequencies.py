from random import randrange

from toolz.itertoolz import frequencies, unique

values = [randrange(1, 11, 1) for _ in range(30)]
print(frequencies(values))

values2 = unique(values)
print(frequencies(values2))
