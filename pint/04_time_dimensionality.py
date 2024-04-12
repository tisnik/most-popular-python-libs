from pint import UnitRegistry

ureg = UnitRegistry()

t1 = 10 * ureg.second
t2 = 1 * ureg.minute

x = t1*t1
y = 1/t1
z = t1 + t2

print(x.dimensionality)
print(y.dimensionality)
print(z.dimensionality)
