from sys import getsizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(getsizeof(value), "\t", typename, "\t", value)


print_sizeof(())
print_sizeof((1,))
print_sizeof((1, 2))
print_sizeof((1, 2, 3))
print_sizeof((1, 2, 3, 4))
print()

print_sizeof([])
print_sizeof([1])
print_sizeof([1, 2])
print_sizeof([1, 2, 3])
print_sizeof([1, 2, 3, 4])
print()

print_sizeof({})
print_sizeof({1:1})
print_sizeof({1:1, 2:2})
print_sizeof({1:1, 2:2, 3:3})
print_sizeof({1:1, 2:2, 3:3, 4:4})
