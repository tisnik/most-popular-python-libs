from pint import UnitRegistry

ureg = UnitRegistry()

m = 1.5 * ureg.kilogram
t = 1 * ureg.second
s = 100 * ureg.meter
v = s/t
a = v/t
f = m*a

print(m.units, "\n", m.dimensionality, "\n")
print(t.units, "\n", t.dimensionality, "\n")
print(v.units, "\n", v.dimensionality, "\n")
print(a.units, "\n", a.dimensionality, "\n")
print(f.units, "\n", f.dimensionality, "\n")
