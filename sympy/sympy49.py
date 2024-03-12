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

from sympy import Interval, init_printing, maximum, pprint, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = x ** 3 - 2 * x ** 2

pprint(f)

print()

print(maximum(f, x, Interval(-2, 2)))
print(maximum(f, x, Interval(-1, 1)))
