from functools import partial


def mul(x=1, y=1, z=1, w=1):
    return x * y * z * w


def displayInfo(name, obj):
    print("name:      ", name)
    print("function:  ", obj.func)
    print("arguments: ", obj.args)
    print("keywords:  ", obj.keywords)
    print()


#f1 = mul
#displayInfo(f1())

f2 = partial(mul, x=2)
displayInfo("f2", f2)

f3 = partial(mul, y=2)
displayInfo("f3", f3)

f4 = partial(mul, y=2, z=2)
displayInfo("f4", f4)

f5 = partial(mul, x=2, y=2, z=2)
displayInfo("f5", f5)

f6 = partial(mul, x=2, y=2, z=2, w=2)
displayInfo("f6", f6)
