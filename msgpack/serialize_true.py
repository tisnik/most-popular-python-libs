import msgpack

value = True

with open("true.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
