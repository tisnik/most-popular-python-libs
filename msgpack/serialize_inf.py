import math
import msgpack

value = math.inf

with open("inf.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
