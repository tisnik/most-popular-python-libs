from toolz.itertoolz import groupby, iterate, take

def inc(x):
    return x+1


values = iterate(inc, 0)

grouped = groupby(lambda x:x % 10, values)
