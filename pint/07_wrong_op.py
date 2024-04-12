from pint import UnitRegistry

ureg = UnitRegistry()

a = 10 * ureg.second
b = 1 * ureg.meter

c = a + b

print(a.dimensionality)
print(b.dimensionality)
print(c.dimensionality)
