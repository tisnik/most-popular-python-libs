import numpy as np
import xarray as xr

chessboard = np.array([" "]*64).reshape(8, 8)
chessboard[0, 0] = "♚"
chessboard[1, 5] = "♔"
chessboard[2, 5] = "♙"
chessboard[3, 4] = "♜"

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = np.linspace(1, 8, 8, dtype=np.int8)

array = xr.DataArray(chessboard,
                     name="Saavedra position",
                     dims=("files", "ranks"),
                     coords={"files":files, "ranks":ranks})

array.attrs["units"] = "chess pieces"
array.attrs["description"] ="White to move and win",
array.attrs["metadata"] = {"played by": "Fernando Saavedra",
                           "winner": "white",
                           "see also": "https://www.youtube.com/watch?v=Mg2OOsQPURs",}

print(array)
print()

print(array.sel(files="c"))
print()

print(array.sel(ranks=6))
print()

