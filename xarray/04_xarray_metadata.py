import numpy as np
import xarray as xr

array = xr.DataArray(np.identity(10),
                     dims=("x", "y"),
                     coords={"x":[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
print(array)
