import msgpack

value = 3.14

with open("float.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
