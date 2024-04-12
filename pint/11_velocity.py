from pint import UnitRegistry

ureg = UnitRegistry()

s = 1 * ureg.mile
t = 1 * ureg.hour
v = s/t
v2 = v.to(ureg.kilometer_per_hour)
v3 = v.to(ureg.meter_per_second)
v4 = v.to(ureg.knot)

print(v)
print(v2)
print(v3)
print(v4)
