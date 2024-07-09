#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import sympy as sp
from sympy.physics.units import Quantity, meter, second


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
