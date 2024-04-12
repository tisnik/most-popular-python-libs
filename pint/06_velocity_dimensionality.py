from pint import UnitRegistry

ureg = UnitRegistry()

s = 100 * ureg.meter
t = 20 * ureg.second

v = s / t
print(v.dimensionality)
