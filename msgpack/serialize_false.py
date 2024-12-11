import msgpack

value = False

with open("false.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
