import sympy as sp
from pint import UnitRegistry

ureg = UnitRegistry()

x = sp.symbols("x") * ureg.meter
print(x)

expression = 2 * x
print(expression)
