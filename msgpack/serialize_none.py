import msgpack

value = None

with open("nil.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
