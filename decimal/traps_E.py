from decimal import Decimal, Rounded, getcontext

c = getcontext()
c.traps[Rounded] = True
c.Emax = 5

x = Decimal(1)
y = Decimal(2)

for i in range(20):
    x *= y
    print(x)
