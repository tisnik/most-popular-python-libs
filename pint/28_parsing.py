from pint import UnitRegistry

ureg = UnitRegistry()
value = ureg("10 kilometers")

print(value)
print(value.to_base_units())
