from pympler import asizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(asizeof.asizeof(value, code=True), "\t", typename, "\t", value)


def foo():
    pass


def bar(x, y):
    return x+y


def baz(x=0, y=1):
    print(x)
    print(y)
    return x+y


print_sizeof(print)
print_sizeof(foo)
print_sizeof(bar)
print_sizeof(baz)
