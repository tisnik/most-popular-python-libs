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

array = xr.DataArray(
    np.identity(10), dims=("x", "y"), coords={"x": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
)
print(array)
