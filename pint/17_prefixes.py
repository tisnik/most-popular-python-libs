from pint import UnitRegistry

ureg = UnitRegistry()

p1 = 1 * ureg.watt
p2 = 1 * ureg.kilowatt
p3 = 1 * ureg.megawatt
p4 = 1 * ureg.gigawatt
p5 = 1 * ureg.terawatt
p6 = 1 * ureg.petawatt
p7 = 1 * ureg.exawatt
p8 = 1 * ureg.zettawatt
p9 = 1 * ureg.yottawatt
p10 = 1 * ureg.ronnawatt
p11 = 1 * ureg.quettawatt

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)

print()

print(p1.to(ureg.watt))
print(p2.to(ureg.watt))
print(p3.to(ureg.watt))
print(p4.to(ureg.watt))
print(p5.to(ureg.watt))
print(p6.to(ureg.watt))
print(p7.to(ureg.watt))
print(p8.to(ureg.watt))
print(p9.to(ureg.watt))
print(p10.to(ureg.watt))
print(p11.to(ureg.watt))
