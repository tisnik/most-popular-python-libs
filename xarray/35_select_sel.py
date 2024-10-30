#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

import numpy as np
import xarray as xr

values = np.arange(0, 10)

xcoords = np.linspace(20, 2, 10)

array = xr.DataArray(values, name="Temperature measurement", dims=("x",), coords={"x": xcoords})


print(array)
print()

print(array.sel(x=20))
print()

print(array.sel(x=10))
print()

print(array.sel(x=2))
