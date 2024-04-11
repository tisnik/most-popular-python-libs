from decimal import Decimal, getcontext, Overflow

c = getcontext()
c.traps[Overflow] = False
c.Emax = 5

x = Decimal(1)
y = Decimal(2)

for i in range(20):
    x *= y
    print(x)
