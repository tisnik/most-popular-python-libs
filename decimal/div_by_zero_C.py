from decimal import Decimal, ExtendedContext, setcontext

setcontext(ExtendedContext)

x = Decimal(1)
y = Decimal("-0")
z = x/y

print(z)
