from pympler import asizeof


def print_sizeof(value):
    typename = "{:8}".format(type(value).__name__)
    print(asizeof.asizeof(value, stats=1), "\n", typename, "\t", value)


print_sizeof(())
print_sizeof((1,))
print_sizeof((1, 2))
print_sizeof((1, 2, 3))
print_sizeof((1, 2, 3, 4))
print_sizeof((1, 2, 3, 4, 5))
print_sizeof((1, 2, 3, 4, 5, 6))
print()

print_sizeof([])
print_sizeof([1])
print_sizeof([1, 2])
print_sizeof([1, 2, 3])
print_sizeof([1, 2, 3, 4])
print_sizeof([1, 2, 3, 4, 5])
print_sizeof([1, 2, 3, 4, 5, 6])
print()

print_sizeof({})
print_sizeof({1:1})
print_sizeof({1:1, 2:2})
print_sizeof({1:1, 2:2, 3:3})
print_sizeof({1:1, 2:2, 3:3, 4:4})
print_sizeof({1:1, 2:2, 3:3, 4:4, 5:5})
print_sizeof({1:1, 2:2, 3:3, 4:4, 5:5, 6:6})
