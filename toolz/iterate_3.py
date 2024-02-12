from toolz.itertoolz import iterate, take


def double(x):
    return x*2


sequence = iterate(double, 1)

sequence = take(10, sequence)
print(list(sequence))
