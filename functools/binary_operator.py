def calc(operator, x, y):
    return operator(x, y)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def less_than(x, y):
    return x < y


z = calc(add, 10, 20)
print(z)

z = calc(mul, 10, 20)
print(z)

z = calc(less_than, 10, 20)
print(z)
