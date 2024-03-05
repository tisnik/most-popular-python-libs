from toolz import curry


@curry
def add3(x, y, z):
    return x + y + z


print(add3)
print(add3(1))
print(add3(1)(2))      # pozor na umístění závorek!
print(add3(1)(2)(3))   # pozor na umístění závorek!
