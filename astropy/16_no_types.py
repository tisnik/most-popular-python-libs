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


def velocity(s, t):
    return s/t

s = 100 * u.meter
t = 20 * u.second
v = velocity(s, t)

print(v)
