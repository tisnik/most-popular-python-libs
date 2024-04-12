from pint import UnitRegistry

ureg = UnitRegistry()

c1 = 1 * ureg.byte
c2 = 1 * ureg.kibibyte
c3 = 1 * ureg.mebibyte
c4 = 1 * ureg.gibibyte
c5 = 1 * ureg.tebibyte
c6 = 1 * ureg.pebibyte
c7 = 1 * ureg.exbibyte
c8 = 1 * ureg.zebibyte
c9 = 1 * ureg.yobibyte

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)

print()

print(c1.to(ureg.bit))
print(c2.to(ureg.bit))
print(c3.to(ureg.bit))
print(c4.to(ureg.bit))
print(c5.to(ureg.bit))
print(c6.to(ureg.bit))
print(c7.to(ureg.bit))
print(c8.to(ureg.bit))
print(c9.to(ureg.bit))
