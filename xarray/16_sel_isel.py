import numpy as np
import xarray as xr

temperatures = np.arange(0, 300).reshape((10, 10, 3))

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

times = ["2023-10-01", "2023-10-02", "2023-10-03"]

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y", "time"),
                     coords={"x":xcoords, "y":ycoords, "time":times},
                     attrs=dict(
                         units = "centigrees",
                         description ="Local temperature values measured in grid",
                         measured_by = {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         ))


print(array)
print()

print(array.isel(x=4))
print()

print(array.isel(y=4))
print()

print(array.sel(time="2023-10-02"))
print()

print(array.sel(time="2023-10-02").isel(x=0))
print()

print(array.sel(time="2023-10-02").isel(x=0).isel(y=0))
print()
