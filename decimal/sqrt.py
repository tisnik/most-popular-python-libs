from decimal import Decimal, getcontext

x = Decimal(2)

for precision in range(1, 30):
    getcontext().prec = precision
    z = x.sqrt()
    y = x.sqrt()
    print(f"{z:<30}   {y*y:<30}")

