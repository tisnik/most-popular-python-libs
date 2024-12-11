import msgpack

value = 1000

with open("int_large.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
