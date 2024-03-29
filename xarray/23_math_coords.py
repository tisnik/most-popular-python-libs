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

temperatures1 = np.arange(100).reshape(10, 10)
temperatures2 = np.array([100] * 100).reshape(10, 10)

xcoords1 = np.linspace(1, 10, 10)
ycoords1 = np.linspace(1, 10, 10)

print("Coordinates for 1st DataArray")
print("x:", xcoords1)
print("y:", ycoords1)
print()

xcoords2 = np.linspace(6, 15, 10)
ycoords2 = np.linspace(6, 15, 10)

print("Coordinates for 2nd DataArray")
print("x:", xcoords2)
print("y:", ycoords2)
print()

array1 = xr.DataArray(
    temperatures1,
    name="Temperature measurement #1",
    dims=("x", "y"),
    coords={"x": xcoords1, "y": ycoords1},
    attrs={
        "units": "centigrees",
        "description": "Local temperature values measured in grid #1",
        "measured_by": {"name": "ThermometerBot", "vendor": "BIY", "version": (1, 0, 0)},
    },
)


array2 = xr.DataArray(
    temperatures2,
    name="Temperature measurement #2",
    dims=("x", "y"),
    coords={"x": xcoords2, "y": ycoords2},
    attrs={
        "units": "centigrees",
        "description": "Local temperature values measured in grid #2",
        "measured_by": {"name": "ThermometerBot", "vendor": "BIY", "version": (1, 0, 0)},
    },
)


print("Array #1:")
print(array1)
print()
print()

print("Array #2:")
print(array2)
print()
print()

print("Array #1 + Array #2:")
array3 = array1 + array2
print(array3)
print()
print()
