from decimal import Decimal, getcontext

x = Decimal(2)

for precision in range(1, 30):
    getcontext().prec = precision
    z = x.sqrt()
    print(z)
