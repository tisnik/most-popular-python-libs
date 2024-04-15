from pint import UnitRegistry

ureg = UnitRegistry()

l = 1.5 * ureg.meter
s = l * l
v = s * l
d = v / (10 * ureg.hectare)

print(l)
print(s)
print(v)
print(d)
print(d.to_base_units())
