import sympy as sp
from pint import UnitRegistry

ureg = UnitRegistry()

s = sp.Symbol("s") * ureg.meter
t = sp.Symbol("t") * ureg.second

print(s/t)
