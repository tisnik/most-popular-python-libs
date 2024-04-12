from pint import UnitRegistry

ureg = UnitRegistry()

s1 = 100 * ureg.meter
a1 = s1*s1
a2 = a1.to(ureg.are)
a3 = a1.to(ureg.hectare)

print(s1, s1.dimensionality)
print(a1, a1.dimensionality)
print(a2, a2.dimensionality)
print(a3, a3.dimensionality)
