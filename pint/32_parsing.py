from pint import UnitRegistry

ureg = UnitRegistry()
value = ureg("1 hour 30 minutes")

print(value)
print(value.to_base_units())
