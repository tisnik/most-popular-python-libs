from sys import getsizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(getsizeof(value), "\t", typename, "\t", value)


print_sizeof(0)
print_sizeof(1)
print_sizeof(42)
print_sizeof(2<<30)
print_sizeof(2<<60)
print()

print_sizeof(1.0)
print_sizeof(3.1415)
print()

print_sizeof(True)
print_sizeof(False)
print_sizeof(None)
print()

print_sizeof("")
print_sizeof("f")
print_sizeof("fo")
print_sizeof("foo")
print_sizeof("foo bar")
print_sizeof("foo bar baz")
print_sizeof("foo bar baz xyz")
print_sizeof("foo bar baz xyzzy")
