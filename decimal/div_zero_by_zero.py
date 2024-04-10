from decimal import Decimal, ExtendedContext, setcontext

setcontext(ExtendedContext)

x = Decimal(0)
y = Decimal(0)
z = x/y

print(z)
