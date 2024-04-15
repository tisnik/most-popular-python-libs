from sympy.physics.units import meter, second
from sympy.physics.units import Quantity
import sympy as sp


def unit(expr):
    return expr.subs({x: 1 for x in expr.args if not x.has(Quantity)})


s = sp.Symbol("m") * meter
t = sp.Symbol("t") * second
v = s/t
a = v/t
a2 = 100*a

print(v)
print(a)
print(a2)

print()

print(unit(v))
print(unit(a))
print(unit(a2))
