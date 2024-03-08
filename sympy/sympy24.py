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

from sympy import integrate, pprint, symbols

a, b, x = symbols("a,b,x")

f = a * x + b

pprint(f)

solution = integrate(f, x)
pprint(solution)
