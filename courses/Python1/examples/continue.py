x = 1

while True:
    if x > 1000:
        break
    x *= 2
    if x < 100:
        continue
    print(x)
