from toolz import compose_left


def add(x, y):
    return x+y


def double(x):
    return 2*x


composed = compose_left(add, double)

print(composed(2, 3))
print(composed(-2, -3))
