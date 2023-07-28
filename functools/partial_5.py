from functools import partial, reduce


def mul(x, y, z, w):
    return x * y * z * w


f1 = mul
print(f1)

f2 = partial(mul, 2)
print(f2)

f3 = partial(mul, 2, 3)
print(f3)

f4 = partial(mul, 2, 3, 4)
print(f4)

f5 = partial(mul, 2, 3, 4, 5)
print(f5)

f6 = partial(mul, 2, 3, 4, 5, 6)
print(f6)

print()

print(f1(2, 3, 4, 5))
print(f2(3, 4, 5))
print(f3(4, 5))
print(f4(5))
print(f5())
print(f6())
