from toolz.itertoolz import iterate, interleave, take


def inc(x):
    return x+1


values1 = iterate(inc, 0)
values2 = ["odd", "even"]*5
interleaved = interleave((values1, values2))

print(list(take(20, interleaved)))
