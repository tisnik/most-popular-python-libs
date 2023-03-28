from sys import getsizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(getsizeof(value), "\t", typename)


print_sizeof((1, 2))
print_sizeof((1, "?" * 1000000))
print()

print_sizeof([1, 2])
print_sizeof([1, "?" * 1000000])
print()

print_sizeof({1:1, 2:2})
print_sizeof({1:1, 2:"?" * 1000000})
