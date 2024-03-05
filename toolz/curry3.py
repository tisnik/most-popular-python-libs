from toolz import curry


@curry
def add(x, y):
    return x + y


print(add)
print(add(1))
print(add(1)(2))  # pozor na umístění závorek!
