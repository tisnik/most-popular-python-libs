from toolz import reduce
from toolz.itertoolz import take


def one_step(p, q):
    print(p, q)
    return p*q


result = reduce(one_step, range(1, 11), 1)
print(result)
