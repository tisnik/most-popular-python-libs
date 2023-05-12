from time import sleep


def foo_construct():
    l = []
    for i in range(10000000):
        l.append(i)
        if i % 100000 == 0:
            sleep(0.05)

    for i in range(10000000, 0, -1):
        del l[i-1]
        if i % 100000 == 0:
            sleep(0.05)

    sleep(2)


sleep(2)
foo_construct()
sleep(2)
