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

from pint import UnitRegistry
from sympy import init_printing, pprint, solve, solveset, symbols
from sympy.physics.units import meter

ureg = UnitRegistry()


init_printing(use_unicode=True)

x = symbols("x")

f = x > 10 * meter

pprint(f)

print()

solution = solve(f, x)
pprint(solution)

print()

solution = solveset(f, x)
pprint(solution)
