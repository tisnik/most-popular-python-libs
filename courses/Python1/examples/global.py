x = 1

def fn1():
    pass


def fn2():
    x = 2


def fn3():
    global x
    x = 3


print(x)
fn1()
print(x)
fn2()
print(x)
fn3()
print(x)
