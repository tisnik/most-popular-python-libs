from funcy import rcompose


def add(x, y):
    return x+y


def double(x):
    return 2*x


def abs(x):
    if x < 0:
        return -x
    return x


composed = rcompose(add, double, abs)

print(composed(2, 3))
print(composed(-2, -3))
