from decimal import Decimal, ExtendedContext, setcontext

setcontext(ExtendedContext)

x = Decimal("inf")
y = Decimal("inf")
z = x/y

print(z)
