from sys import getsizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(getsizeof(value), "\t", typename, "\t", value)


class C1:
    pass


class C2:
    def __init__(self):
        pass

class C3:
    def __init__(self):
        pass

    def foo(self, x):
        self.x=x

    def bar(self, y):
        self.y=y


o1 = C1()
o2 = C2()
o3 = C3()

print_sizeof(C1)
print_sizeof(o1)

print_sizeof(C2)
print_sizeof(o2)

print_sizeof(C3)
print_sizeof(o3)

o3.foo(42)

print_sizeof(C3)
print_sizeof(o3)

o3.bar(0)

print_sizeof(C3)
print_sizeof(o3)
