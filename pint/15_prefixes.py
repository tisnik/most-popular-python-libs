from pint import UnitRegistry

ureg = UnitRegistry()

m1 = 1.5 * ureg.gram
m2 = 1.5 * ureg.kilogram
m3 = 1.5 * ureg.milligram
m4 = 1.5 * ureg.decigram
m5 = 1.5 * ureg.decagram
m6 = 1.5 * ureg.microgram

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)

print()

print(m1.to(ureg.gram))
print(m2.to(ureg.gram))
print(m3.to(ureg.gram))
print(m4.to(ureg.gram))
print(m5.to(ureg.gram))
print(m6.to(ureg.gram))
