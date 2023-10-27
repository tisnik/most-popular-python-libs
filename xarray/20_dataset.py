import numpy as np
import xarray as xr

temperatures = -10 + 40*np.random.rand(10, 10)
wind = 100*np.random.rand(10, 10)

xcoords = np.linspace(10, 100, 10)
ycoords = np.linspace(-100, -10, 10)

dataset = xr.Dataset({"temperatures": (["x", "y"], temperatures),
                      "wind": (["x", "y"], wind)},
                       coords={"x":xcoords, "y":ycoords})

print(dataset)
