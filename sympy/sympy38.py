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

from sympy import diff, pprint, symbols

x = symbols("x")

f = 5 * x ** 3 + 4 * x ** 2 + 3 * x + 4 + 1 / x

pprint(f)

print()

diff1 = diff(f, x)
pprint(diff1)
