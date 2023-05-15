from time import sleep


@profile
def foo_construct():
    l = []
    for i in range(100000):
        l.append(i)

    for i in range(100000, 0, -1):
        del l[i-1]


foo_construct()
