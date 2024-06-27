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

from astropy import units as u

length = u.Quantity(1, u.meter)
time = u.Quantity(2, u.second)
velocity = u.Quantity(1/5, u.meter/u.second)

print(length)
print(time)
print(velocity)
