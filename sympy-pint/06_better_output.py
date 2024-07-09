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

m = sp.Symbol("m") * ureg.kilogram
t = sp.Symbol("t") * ureg.second
s = sp.Symbol("s") * ureg.meter
v = s/t
a = v/t
f = m*a

print(f"{m.magnitude} \t [{m.units}]")
print(f"{t.magnitude} \t [{t.units}]")
print(f"{v.magnitude} \t [{v.units}]")
print(f"{a.magnitude} \t [{a.units}]")
print(f"{f.magnitude} \t [{f.units}]")
