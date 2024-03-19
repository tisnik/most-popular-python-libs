from toolz.itertoolz import iterate, partition, sliding_window, take


def inc(x):
    return x+1


values = iterate(inc, 10)

sw = sliding_window(5, values)

for window in take(20, sw):
    print(window)
