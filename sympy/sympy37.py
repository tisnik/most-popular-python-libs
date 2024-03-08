#
#  (C) Copyright 2023  Pavel Tisnovsky
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

init_printing(use_unicode=True)

x = symbols("x")

f1 = x ** 2 < 10
f2 = x ** 3 > -10

pprint(f1)
pprint(f2)

print()

solution = solve((f1, f2), x)
pprint(solution)
