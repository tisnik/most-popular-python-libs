from toolz.itertoolz import first, iterate, take


def nextval(x):
    return x + [x[-1]+1]


sequence = iterate(nextval, [1])

sequence = take(10, sequence)
print(list(sequence))
