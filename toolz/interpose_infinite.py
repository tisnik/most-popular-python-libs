from toolz.itertoolz import interpose, iterate, take


def inc(x):
    return x+1


values = iterate(inc, 0)

print(list(take(20, interpose("*", values))))
