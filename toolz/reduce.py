from toolz import reduce


def one_step(p, q):
    print(p, q)
    return p*q


result = reduce(one_step, range(1, 11), 1)
print(result)
