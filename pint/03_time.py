from pint import UnitRegistry

ureg = UnitRegistry()

t1 = 10 * ureg.second
t2 = 1 * ureg.minute

print(t1)
print(t2)
print(t1*t1)
print(1/t1)
print(t1+t2)
print(t1-t2)
print(t2/t1)
