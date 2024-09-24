x = 1


def foo():
    global x
    x += 1
    print(x)


foo()
