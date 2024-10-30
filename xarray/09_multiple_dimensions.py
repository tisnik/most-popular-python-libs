#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Pouziti vetsiho mnozstvi dimenzi u objektu typu xarray.DataArray."""

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

temperatures = -10 + 40 * np.random.rand(2, 2)

longitudes = [[-99.83, -99.32], [-99.79, -99.23]]
latitudes = [[42.25, 42.21], [42.63, 42.59]]

array = xr.DataArray(
    temperatures,
    name="Temperature measurement",
    dims=("x", "y"),
    coords={
        "lon": (["x", "y"], longitudes),
        "lat": (["x", "y"], latitudes),
    },
    attrs={
        "units": "centigrees",
        "description": "Local temperature values measured in grid",
        "measured_by": {"name": "ThermometerBot", "vendor": "BIY", "version": (1, 0, 0)},
    },
)


print(array)
