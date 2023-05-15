from time import sleep


@profile
def foo_construct():
    x = "*foo*"

    y = ""
    for i in range(200000):
        y += x

    print(len(y))

    del x
    del y


@profile
def bar_construct():
    x = bytearray(10000000)
    print(len(x))
    del x


foo_construct()
bar_construct()
