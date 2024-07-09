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

from sympy import init_printing, pprint, solve, symbols
from sympy.physics.units import second

init_printing(use_unicode=True)

t = symbols("t")

f1 = t > 10 * second
f2 = t < 20 * second

pprint(f1)
pprint(f2)

print()

solution = solve((f1, f2), t)
pprint(solution)
