from pint import UnitRegistry

ureg = UnitRegistry()

f1 = 10 * ureg.newton
f2 = 20 * ureg.newton
f3 = f1 + f2
l = 100 * ureg.meter
e = f3 * l

print(f1)
print(f2)
print(f3)
print(e)
