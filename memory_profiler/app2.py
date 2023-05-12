from time import sleep


def foo_construct():
    x = "*foo*"

    sleep(2)

    y = ""
    for i in range(20000000):
        y += x

    print(len(y))


def bar_construct():
    x = bytearray(100000000)
    print(len(x))
    sleep(2)


sleep(2)
foo_construct()
sleep(2)
bar_construct()
sleep(2)
