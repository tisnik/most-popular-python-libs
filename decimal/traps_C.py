from decimal import Decimal, DivisionByZero, getcontext

c = getcontext()
c.traps[DivisionByZero] = False

for trap, state in c.traps.items():
    print(trap, state)

x = Decimal(1)
y = Decimal(0)
z = x/y

print(z)
