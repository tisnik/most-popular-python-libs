from toolz.sandbox.parallel import fold
from toolz.itertoolz import take


def one_step(p, q):
    print(p, q)
    return p*q


result = fold(one_step, range(1, 11), 1)
print(result)
