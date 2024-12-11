import msgpack
import msgpack_numpy as m

import numpy as np

m.patch()

value = np.array([1, 2, 3], dtype=np.byte)

with open("array_1d_byte.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
