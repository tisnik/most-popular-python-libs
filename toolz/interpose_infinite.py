from toolz.itertoolz import iterate, interpose, take

def inc(x):
    return x+1


values = iterate(inc, 0)

print(list(take(20, interpose("*", values))))
