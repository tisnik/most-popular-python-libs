from pint import UnitRegistry

ureg = UnitRegistry()

t1 = 1 * ureg.second
t2 = 1 * ureg.millisecond
t3 = 1 * ureg.microsecond
t4 = 1 * ureg.nanosecond
t5 = 1 * ureg.picosecond
t6 = 1 * ureg.femtosecond
t7 = 1 * ureg.attosecond
t8 = 1 * ureg.zeptosecond
t9 = 1 * ureg.yoctosecond
t10 = 1 * ureg.rontosecond
t11 = 1 * ureg.quectosecond

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)
print(t10)
print(t11)

print()

print(t1.to(ureg.second))
print(t2.to(ureg.second))
print(t3.to(ureg.second))
print(t4.to(ureg.second))
print(t5.to(ureg.second))
print(t6.to(ureg.second))
print(t7.to(ureg.second))
print(t8.to(ureg.second))
print(t9.to(ureg.second))
print(t10.to(ureg.second))
print(t11.to(ureg.second))
