from pint import UnitRegistry

ureg = UnitRegistry()

t = 1 * ureg.second
s = 100 * ureg.meter
v = s/t
a = v/t

print(t)
print(v)
print(a)
