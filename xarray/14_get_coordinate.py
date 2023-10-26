import numpy as np
import xarray as xr

temperatures = -10 + 40*np.random.rand(10, 10, 3)

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

print(array["x"])
print()

print(array["y"])
print()

print(array["time"])
print()
