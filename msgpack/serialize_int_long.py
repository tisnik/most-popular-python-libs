import msgpack

value = 2**60

with open("int_long.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
