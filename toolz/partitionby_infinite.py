from toolz.itertoolz import iterate, take
from toolz.recipes import partitionby


def inc(x):
    return x+1


values = iterate(inc, 0)

values2 = partitionby(lambda x: x % 2 == 0, values)

print(list(take(10, values2)))
