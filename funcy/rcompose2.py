from funcy import rcompose


def add(x, y):
    return x+y


def double(x):
    return 2*x


composed = rcompose(add, double)

print(composed(2, 3))
print(composed(-2, -3))
