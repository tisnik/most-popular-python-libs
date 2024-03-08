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

a, b, c, d, e, x, y = symbols("a,b,c,d,e,x,y")

f = a * x ** 2 + b * x + c * y ** 2 + d * y + e

pprint(f)

diff1 = diff(f, x)
pprint(diff1)

diff2 = diff(f, y)
pprint(diff2)
