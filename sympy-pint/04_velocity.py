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

import sympy as sp
from pint import UnitRegistry

ureg = UnitRegistry()

s = sp.Symbol("s") * ureg.meter
t = sp.Symbol("t") * ureg.second

print(s/t)
