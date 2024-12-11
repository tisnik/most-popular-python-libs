import msgpack

value = -10

with open("negative_int.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
