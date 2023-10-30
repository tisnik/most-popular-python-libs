import numpy as np
import xarray as xr

measured_at = np.arange(
        np.datetime64("2023-01-01"),
        np.datetime64("2024-01-01"),
        np.timedelta64(1, "D")).astype('datetime64[ns]')

temperatures = 10 + 20 * np.random.rand(365)

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("time",),
                     coords={"time":measured_at},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in time serie #1",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })

print(array.groupby("time.season"))
print()
print()
