import msgpack

value = [100, 200, 300, 400]

with open("array2.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
