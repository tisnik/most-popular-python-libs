x = 0

def fn1():
    x = 1
    def fn2():
        nonlocal x
        x = 2
        print(x)
    fn2()
    print(x)


print(x)
fn1()
print(x)
