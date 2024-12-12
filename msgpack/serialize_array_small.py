import msgpack

value = [1, 2, 3, 4]

with open("array.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
