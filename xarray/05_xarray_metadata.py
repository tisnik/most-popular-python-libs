import numpy as np
import xarray as xr

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

array = xr.DataArray(np.identity(10),
                     dims=("x", "y"),
                     coords={"x":xcoords, "y":ycoords})
print(array)
