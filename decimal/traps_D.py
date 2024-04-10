from decimal import Decimal, getcontext, Rounded

c = getcontext()
c.traps[Rounded] = True

for trap, state in c.traps.items():
    print(trap, state)

x = Decimal(1)
y = Decimal(2)
z = x/y

print(z)

x = Decimal(1)
y = Decimal(7)
z = x/y

print(z)
