import math

import msgpack

value = math.nan

with open("nan.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
