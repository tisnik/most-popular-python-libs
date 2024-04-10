from decimal import Decimal, ExtendedContext, setcontext

setcontext(ExtendedContext)

x = Decimal("inf")
y = Decimal(1)
z = x+y

print(z)
