import numpy as np
import xarray as xr

temperatures = -10 + 40*np.random.rand(5, 5)

xcoords = np.linspace(10, 100, 5)
ycoords = np.linspace(-100, -10, 5)

array = xr.DataArray(temperatures,
                     name="Temperature measurement",
                     dims=("x", "y"),
                     coords={"x":xcoords, "y":ycoords},
                     attrs={
                         "units": "centigrees",
                         "description": "Local temperature values measured in grid",
                         "measured_by": {"name": "ThermometerBot",
                              "vendor": "BIY",
                              "version": (1, 0, 0)}
                         })


print(array)
print()

print(xr.where(array <= 0, "freezing", "above 0°C"))
