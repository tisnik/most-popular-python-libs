import msgpack

value = 200

with open("int_small.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
