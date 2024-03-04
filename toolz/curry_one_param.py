from toolz import curry


def inc(x):
    return x+1


curried = curry(inc)
print(inc)
print(curried)
print(curried())
print(curried(1))
