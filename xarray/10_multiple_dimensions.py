import numpy as np
import xarray as xr

temperatures = -10 + 40*np.random.rand(2, 2, 3)

longitudes = [[-99.83, -99.32], [-99.79, -99.23]]
latitudes = [[42.25, 42.21], [42.63, 42.59]]
times = ["2023-10-01", "2023-10-02", "2023-10-03"]

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y", "time"),
                     coords={
                        "lon": (["x", "y"], longitudes),
                        "lat": (["x", "y"], latitudes),
                        "time": times,
                     },
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in grid",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })


print(array)
