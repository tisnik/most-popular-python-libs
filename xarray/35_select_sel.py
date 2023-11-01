import numpy as np
import xarray as xr

values = np.arange(0, 10)

xcoords = np.linspace(20, 2, 10)

array = xr.DataArray(values,
                     name="Temperature measurement",
                     dims=("x",),
                     coords={"x":xcoords})


print(array)
print()

print(array.sel(x=20))
print()

print(array.sel(x=10))
print()

print(array.sel(x=2))
