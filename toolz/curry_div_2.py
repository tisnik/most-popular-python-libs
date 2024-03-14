from toolz import curry, iterate, take


def inc(x):
    return x+1


@curry
def divisible_by(y, x):
    return x % y == 0


even = divisible_by(2)


sequence = iterate(inc, 0)
evens = filter(even, sequence)

sequence = take(10, evens)
print(list(sequence))

