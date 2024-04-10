from decimal import Decimal, getcontext

c = getcontext()

for trap, state in c.traps.items():
    print(trap, state)
