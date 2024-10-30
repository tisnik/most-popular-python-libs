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

temperatures = -10 + 40 * np.random.rand(2, 2, 3)
wind = 100 * np.random.rand(2, 2, 3)

longitudes = [[-99.83, -99.32], [-99.79, -99.23]]
latitudes = [[42.25, 42.21], [42.63, 42.59]]
times = ["2023-10-01", "2023-10-02", "2023-10-03"]

dataset = xr.Dataset(
    {"temperatures": (["x", "y", "time"], temperatures), "wind": (["x", "y", "time"], wind)},
    coords={"lon": (["x", "y"], longitudes), "lat": (["x", "y"], latitudes), "time": times},
)


print(dataset)

print()
print("Temperatures:")
print(dataset["temperatures"])

print()
print("Wind:")
print(dataset["wind"])
