

def foo(x):
    y = False
    z = False
    w = []

    if x > 0:
        y = True

    if 0:
        z = True

    if x >= 1:
        return 10

    return 0


print(foo(0))
print(foo(1))
print(foo(2))
