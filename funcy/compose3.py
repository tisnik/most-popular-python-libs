from funcy import compose


def add(x, y):
    return x+y


def double(x):
    return 2*x


def abs(x):
    if x < 0:
        return -x
    return x


composed = compose(abs, double, add)

print(composed(2, 3))
print(composed(-2, -3))
