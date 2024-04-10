from decimal import Decimal, getcontext

c = getcontext()

for trap, state in c.traps.items():
    print(trap, state)

x = Decimal(1)
y = Decimal(0)
z = x/y

print(z)
