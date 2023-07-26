def odd(value):
    return value % 2 == 1


def even(value):
    return not odd(value)


data = range(0, 11)

filtered = [value for value in data if odd(value)]
print(filtered)

filtered = [value for value in data if even(value)]
print(filtered)
