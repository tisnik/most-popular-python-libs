@micropython.viper
def loop():
    x = 0
    for i in range(1000):
        for j in range(1000):
            x+=1
    return x


import utime

t1 = utime.ticks_us()
loop()
t2 = utime.ticks_us()
print(utime.ticks_diff(t2, t1))
