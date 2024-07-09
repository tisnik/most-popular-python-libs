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

from sympy import Symbol, pprint, solve
from sympy.physics.units import kelvin, meter, second

a = Symbol("a") * meter
b = Symbol("b") * second
c = Symbol("c") * kelvin

x = Symbol("x")

f = a * x ** 2 + b * x + c

pprint(f)
print()

solution = solve(f, x)
pprint(solution)
