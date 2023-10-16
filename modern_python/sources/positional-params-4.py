def foo(x, /, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(1, z=1, y=2))
