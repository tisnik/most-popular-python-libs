from pint import UnitRegistry

ureg = UnitRegistry()
value = ureg("10 newtons")

print(value)
print(value.to_base_units())
