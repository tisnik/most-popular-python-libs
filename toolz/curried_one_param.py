from toolz import curry


@curry
def inc(x):
    return x+1


print(inc)
print(inc())
print(inc(1))
