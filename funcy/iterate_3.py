from funcy import iterate, take


def double(x):
    return x*2


sequence = iterate(double, 1)

slice = take(10, sequence)
print(slice)
