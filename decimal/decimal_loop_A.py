from decimal import Decimal

x = Decimal(0)
step = Decimal(0.1)

while x != Decimal("1.0"):
    x += step
    print(x)
