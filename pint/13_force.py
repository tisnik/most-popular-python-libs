from pint import UnitRegistry

ureg = UnitRegistry()

m = 1.5 * ureg.kilogram
t = 1 * ureg.second
s = 100 * ureg.meter
v = s/t
a = v/t
f = m*a

print(m)
print(t)
print(v)
print(a)
print(f)
