#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Zakladni aritmeticke operace nad celymi poli."""

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

temperatures = -10 + 40 * np.random.rand(5, 5)

xcoords = np.linspace(10, 100, 5)
ycoords = np.linspace(-100, -10, 5)

array = xr.DataArray(
    temperatures,
    name="Temperature measurement",
    dims=("x", "y"),
    coords={"x": xcoords, "y": ycoords},
    attrs={
        "units": "centigrees",
        "description": "Local temperature values measured in grid",
        "measured_by": {"name": "ThermometerBot", "vendor": "BIY", "version": (1, 0, 0)},
    },
)


print(array)
print()

print(-array)
print()

print(array * 2)
print()

print(array.round())
print()
