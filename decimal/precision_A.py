from decimal import Decimal, getcontext

getcontext().prec = 100

x = Decimal(1)
y = Decimal(3)
z = x/y

print(z*Decimal(3))
