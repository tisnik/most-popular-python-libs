from functools import partial


def mul(x, y, z):
    return x * y * z


print(mul(2, 3, 7))

print()

doubler = partial(mul, 2)


for i in range(11):
    print(i, doubler(i, 10))
