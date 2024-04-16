from pint import UnitRegistry
import sympy as sp

ureg = UnitRegistry()

m = sp.Symbol("m") * ureg.kilogram
t = sp.Symbol("t") * ureg.second
s = sp.Symbol("s") * ureg.meter
v = s/t
a = v/t
f = m*a

g = sp.Symbol("g") * ureg.second

fx = f + g
