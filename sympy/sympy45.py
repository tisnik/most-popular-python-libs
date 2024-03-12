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

from sympy import pprint, sin, singularities, symbols

a, b, c, d, e, x = symbols("a,b,c,d,e,x")

f = 1 / (sin(x))

pprint(f)

print()

s = singularities(f, x)
pprint(s)
