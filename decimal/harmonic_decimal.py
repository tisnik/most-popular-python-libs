from decimal import Decimal

n = Decimal(1)
h1 = Decimal(0.0)
h2 = Decimal(0.0)
one = Decimal(1.0)

while True:
        h2 = h1 + one / n

        if n % 1000000 == 0:
            print(n, h1, h2, h2 - h1)

        if h1 == h2:
            break
        h1 = h2
        n += 1

print(h1, h2, n)
