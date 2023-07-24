def odd(value):
    return value % 2 == 1


def even(value):
    return not odd(value)


data = range(0, 11)

filtered = filter(odd, data)
print(list(filtered))

filtered = filter(even, data)
print(list(filtered))
