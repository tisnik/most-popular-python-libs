from decimal import Decimal, ExtendedContext, setcontext

setcontext(ExtendedContext)

x = Decimal(2)
y = Decimal(100)
z = x**y

print(z)
