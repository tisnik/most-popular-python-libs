from toolz.itertoolz import accumulate, take


def one_step(p, q):
    print(p, q)
    return p*q


sequence = accumulate(one_step, range(1, 11))
print(list(sequence))
