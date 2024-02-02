@micropython.viper
def add(x: int, y: int) -> int:
    return x+y


import utime

t1 = utime.ticks_us()

x: int = 0
for i in range(10000):
    x = add(x, 10)

print(x)
t2 = utime.ticks_us()
print(utime.ticks_diff(t2, t1))
