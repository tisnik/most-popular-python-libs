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

import numpy as np
from astropy import units as u

a = np.array(range(10)) + 1
print("a = ", a)

t = a * u.second
print("t = ", t)

d = t / t
print("d = ", d)
