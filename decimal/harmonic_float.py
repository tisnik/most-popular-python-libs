n = 1
h1 = 0.0
h2 = 0.0

while True:
        h2 = h1 + 1.0 / n

        if n % 10000000 == 0:
            print(n, h1, h2, h2 - h1)

        if h1 == h2:
            break
        h1 = h2
        n += 1

print(h1, h2, n)
