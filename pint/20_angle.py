from pint import UnitRegistry

ureg = UnitRegistry()

a = 0.5 * ureg.turns

print(a)
print(a.to(ureg.degrees))
print(a.to(ureg.radians))
print(a.to(ureg.arcminute))
