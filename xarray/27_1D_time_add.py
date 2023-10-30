import numpy as np
import xarray as xr

measured_at1 = np.arange(
        np.datetime64("2023-01-01"),
        np.datetime64("2023-06-01"),
        np.timedelta64(1, "D")).astype('datetime64[ns]')

temperatures1 = 10 + 20 * np.random.rand(len(measured_at1))

measured_at2 = np.arange(
        np.datetime64("2023-03-01"),
        np.datetime64("2023-09-01"),
        np.timedelta64(1, "D")).astype('datetime64[ns]')

temperatures2 = 10 + 20 * np.random.rand(len(measured_at2))

array1 = xr.DataArray(temperatures1,
                     name="Temperature measurement",
                     dims=("time",),
                     coords={"time":measured_at1},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in time serie #1",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })

array2 = xr.DataArray(temperatures2,
                     name="Temperature measurement",
                     dims=("time",),
                     coords={"time":measured_at2},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in time serie #2",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })

print(array1 + array2)
print()
print()
