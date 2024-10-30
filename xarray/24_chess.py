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

chessboard = np.array([" "] * 64).reshape(8, 8)
chessboard[0, 0] = "♚"
chessboard[1, 5] = "♔"
chessboard[2, 5] = "♙"
chessboard[3, 4] = "♜"

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = np.linspace(1, 8, 8, dtype=np.int8)

array = xr.DataArray(
    chessboard,
    name="Saavedra position",
    dims=("files", "ranks"),
    coords={"files": files, "ranks": ranks},
)

array.attrs["units"] = "chess pieces"
array.attrs["description"] = ("White to move and win",)
array.attrs["metadata"] = {
    "played by": "Fernando Saavedra",
    "winner": "white",
    "see also": "https://www.youtube.com/watch?v=Mg2OOsQPURs",
}

print(array)
print()

print(array.sel(files="c"))
print()

print(array.sel(ranks=6))
print()
