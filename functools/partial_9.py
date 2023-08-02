from functools import partial


def mul(x=1, y=1, z=1, w=1):
    return x * y * z * w


f1 = mul
print(f1())

f2 = partial(mul, x=2)
print(f2())

f3 = partial(mul, y=2)
print(f3())

f4 = partial(mul, y=2, z=2)
print(f4())

f5 = partial(mul, x=2, y=2, z=2)
print(f5())

f6 = partial(mul, x=2, y=2, z=2, w=2)
print(f6())
