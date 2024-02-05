@micropython.native
def foo(x):
    return x+x


for i in range(0x7ffffffc, 0x80000008):
    print(hex(foo(i)))
