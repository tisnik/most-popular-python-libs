import numpy as np
import xarray as xr

temperatures = -10 + 40*np.random.rand(10, 10)

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y"),
                     coords={"x":xcoords, "y":ycoords})

print(array)
