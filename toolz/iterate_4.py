from toolz.itertoolz import iterate, take


def one_step(p):
    return (p[1], p[0]+p[1])


sequence = iterate(one_step, (0, 1))
sequence = take(10, sequence)
print(list(sequence))
