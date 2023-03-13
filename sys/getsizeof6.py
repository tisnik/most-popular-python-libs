from sys import getsizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(getsizeof(value), "\t", typename, "\t", value)


class C4:
    def __init__(self):
        pass

    def foo(self, x):
        self.x=x


o4 = C4()

print_sizeof(C4)
print_sizeof(o4)

o4.foo(o4)

print_sizeof(C4)
print_sizeof(o4)
