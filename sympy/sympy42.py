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

a, b, c, d, e, x = symbols("a,b,c,d,e,x")

f = a * x ** 3 + b * x ** 2 + c * x + d + e / x

pprint(f)

print()

diff1 = diff(f, x)
pprint(diff1)
print()

diff2 = diff(f, x, x)
pprint(diff2)
print()

diff3 = diff(f, x, x, x)
pprint(diff3)
print()

diff4 = diff(f, x, x, x, x)
pprint(diff4)
