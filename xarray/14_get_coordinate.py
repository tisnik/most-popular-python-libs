#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Ziskani konkretnich koordinat z metadat o poli."""

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

temperatures = -10 + 40 * np.random.rand(10, 10, 3)

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

times = ["2023-10-01", "2023-10-02", "2023-10-03"]

array = xr.DataArray(
    temperatures,
    name="Temperature measurement",
    dims=("x", "y", "time"),
    coords={"x": xcoords, "y": ycoords, "time": times},
    attrs={
        "units": "centigrees",
        "description": "Local temperature values measured in grid",
        "measured_by": {"name": "ThermometerBot", "vendor": "BIY", "version": (1, 0, 0)},
    },
)


print(array)
print()

print(array["x"])
print()

print(array["y"])
print()

print(array["time"])
print()
