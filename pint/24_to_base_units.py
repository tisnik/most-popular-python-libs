from pint import UnitRegistry

ureg = UnitRegistry()

s = 4.0 * ureg.ly
t = 10000 * ureg.year
v = s / t

print(s)
print(t)
print(v)
print(v.to_base_units())
