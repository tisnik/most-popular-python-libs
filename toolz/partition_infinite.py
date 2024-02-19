from toolz.itertoolz import iterate, partition, take

def inc(x):
    return x+1


values = iterate(inc, 0)

print(list(take(10, partition(3, values))))
