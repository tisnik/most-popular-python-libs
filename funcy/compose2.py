from funcy import compose


def add(x, y):
    return x+y


def double(x):
    return 2*x


composed = compose(double, add)

print(composed(2, 3))
print(composed(-2, -3))
