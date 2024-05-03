import sympy as sp
from sympy.physics.units import Quantity, meter, second


def unit(expr):
    return expr.subs({x: 1 for x in expr.args if not x.has(Quantity)})


s = sp.Symbol("m") * meter
t = sp.Symbol("t") * second
v = s/t
a = sp.diff(v, "t")

print(v)
print(a)
