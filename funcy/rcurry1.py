from funcy import curry


def div(x, y):
    return x / y


curried = curry(div)

print(curried)
print(curried(1))
print(curried(1)(2))  # pozor na umístění závorek!
