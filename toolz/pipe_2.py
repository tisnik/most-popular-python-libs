from toolz import pipe


def double(x):
    return x*2


print(pipe(1, abs, double))
print(pipe(42, abs, double))
print(pipe(1000, abs, double))
