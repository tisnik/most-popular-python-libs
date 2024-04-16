from pint import UnitRegistry

ureg = UnitRegistry()
value = ureg("1 meter 23 centimeters 4 millimeters")

print(value)
print(value.to_base_units())
