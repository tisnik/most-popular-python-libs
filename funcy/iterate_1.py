from funcy import iterate, take


def inc(x):
    return x+1


sequence = iterate(inc, 0)

slice = take(10, sequence)
print(slice)
