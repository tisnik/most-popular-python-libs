from pint import UnitRegistry
import sympy as sp

ureg = UnitRegistry()

x = sp.symbols("x") * ureg.meter
print(x)

expression = x * x
print(expression)
