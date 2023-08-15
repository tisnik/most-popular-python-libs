from funcy import curry


def add3(x, y, z):
    return x + y + z


curried = curry(add3)

print(curried)
print(curried(1))
print(curried(1)(2))      # pozor na umístění závorek!
print(curried(1)(2)(3))   # pozor na umístění závorek!
