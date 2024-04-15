from pint import UnitRegistry
import sympy as sp

ureg = UnitRegistry()

s = sp.Symbol("s") * ureg.meter
t = sp.Symbol("t") * ureg.second

print(s/t)
