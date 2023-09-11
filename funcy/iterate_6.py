from funcy import iterate, take


def nextval(x):
    return x + [x[-1]+1]


sequence = iterate(nextval, [1])

slice = take(10, sequence)
print(slice)
