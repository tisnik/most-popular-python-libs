from time import sleep

sleep(2)

x = "*foo*"

sleep(2)

y = ""
for i in range(200000):
    y += x

print(len(y))

sleep(2)

x = 0
y = 0

sleep(2)

x = bytearray(1000000)

sleep(2)

x = 0

sleep(2)
