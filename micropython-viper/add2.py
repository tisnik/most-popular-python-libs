@micropython.native
def add(x, y):
    return x+y


import utime

t1 = utime.ticks_us()
x = 0
for i in range(10000):
    x = add(x, 10)

print(x)
t2 = utime.ticks_us()
print(utime.ticks_diff(t2, t1))
