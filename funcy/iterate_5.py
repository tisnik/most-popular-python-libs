from funcy import first, iterate, take


def one_step(p):
    return (p[1], p[0]+p[1])


sequence = iterate(one_step, (0, 1))

slice = take(20, sequence)
print(list(map(first, slice)))
