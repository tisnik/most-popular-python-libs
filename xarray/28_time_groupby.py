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

measured_at = np.arange(
    np.datetime64("2023-01-01"), np.datetime64("2024-01-01"), np.timedelta64(1, "D")
).astype("datetime64[ns]")

temperatures = 10 + 20 * np.random.rand(365)

array = xr.DataArray(
    temperatures,
    name="Temperature measurement",
    dims=("time",),
    coords={"time": measured_at},
    attrs={
        "units": "centigrees",
        "description": "Local temperature values measured in time serie #1",
        "measured_by": {"name": "ThermometerBot", "vendor": "BIY", "version": (1, 0, 0)},
    },
)

print(array.groupby("time.season"))
print()
print()
