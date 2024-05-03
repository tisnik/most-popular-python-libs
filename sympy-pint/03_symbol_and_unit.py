import sympy as sp
from pint import UnitRegistry

ureg = UnitRegistry()

x = sp.symbols("x") * ureg.meter
print(x)

expression = x * x
print(expression)
