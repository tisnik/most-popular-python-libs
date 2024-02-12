from toolz.itertoolz import iterate, take


def inc(x):
    return x+1


sequence = iterate(inc, 0)

sequence = take(10, sequence)
print(list(sequence))
