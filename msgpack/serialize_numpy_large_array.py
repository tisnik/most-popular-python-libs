import msgpack
import msgpack_numpy as m

import numpy as np

m.patch()

value = np.zeros([10000], dtype=np.float32)
print(value.shape)

with open("array_1d_large.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
