from pint import UnitRegistry

ureg = UnitRegistry()

m = 1.5 * ureg.kilogram
t = 1 * ureg.second
s = 100 * ureg.meter
v = s/t
a = v/t
f = m*a

area = 10 * ureg.meter * ureg.meter

pressure = f / area

print(f)
print(f"{f:H}")
print(f"{f:L}")

print(pressure)
print(f"{pressure:H}")
print(f"{pressure:L}")
