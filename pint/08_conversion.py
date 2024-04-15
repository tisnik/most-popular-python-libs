from pint import UnitRegistry

ureg = UnitRegistry()

t1 = 1800 * ureg.second
t2 = t1.to(ureg.minute)
t3 = t1.to(ureg.hour)

print(t1, t1.dimensionality)
print(t2, t2.dimensionality)
print(t3, t3.dimensionality)
