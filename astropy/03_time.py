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

t1 = 10 * u.second
t2 = 1 * u.minute
t3 = 1 * u.second

print(t1)
print(t2)
print(t1*t1)
print(1/t1)
print(t1+t2)
print(t1-t2)
print(t2/t1)
print(t1/t3)
