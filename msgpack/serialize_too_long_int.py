import msgpack

value = 2**64

with open("too_long_int.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
