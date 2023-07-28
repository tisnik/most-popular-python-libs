import operator
from functools import partial, reduce


def mul(*args):
    return reduce(operator.mul, args, 1)


print(mul(2, 3, 7))


print()


doubler = partial(mul, 2)


for i in range(11):
    print(i, doubler(i, 10))


print()


doubleDoubler = partial(mul, 2, 2)


for i in range(11):
    print(i, doubleDoubler(i, 10))
