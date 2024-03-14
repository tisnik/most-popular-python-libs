from toolz import curry, iterate, take


def inc(x):
    return x+1


def divisible_by(y, x):
    return x % y == 0


curried = curry(divisible_by)
even = curried(2)

sequence = iterate(inc, 0)
evens = filter(even, sequence)

sequence = take(10, evens)
print(list(sequence))

