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

f = 5 * x ** 3 + 5

pprint(f)

solution = solve(f, x)
pprint(solution)
