from funcy import curry


def add(x, y):
    return x + y


curried = curry(add)

print(curried)
print(curried(1))
print(curried(1)(2))
