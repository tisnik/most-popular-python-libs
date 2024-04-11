from decimal import Decimal, ExtendedContext, setcontext

setcontext(ExtendedContext)

x = Decimal("inf")
y = Decimal("0")
z = x*y

print(z)
