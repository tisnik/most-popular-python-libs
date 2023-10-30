import numpy as np
import xarray as xr


measured_at = np.array([
    np.datetime64("2023-01-01"),
    np.datetime64("2023-01-02"),
    np.datetime64("2023-01-03"),
    np.datetime64("2023-01-04"),
    np.datetime64("2023-01-05")]).astype('datetime64[ns]')

temperatures = 10 + 20 * np.random.rand(5)

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("time",),
                     coords={"time":measured_at},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in grid #1",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })

print(array)
print()
print()
