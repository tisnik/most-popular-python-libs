from decimal import Decimal, getcontext

x = Decimal(1)
y = Decimal(3)

for precision in range(1, 30):
    getcontext().prec = precision
    z = x/y
    print(z*Decimal(3))
