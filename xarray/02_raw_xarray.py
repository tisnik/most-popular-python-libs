import numpy as np
import xarray as xr

array = xr.DataArray(np.identity(10))
print(array)
