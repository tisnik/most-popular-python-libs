import msgpack

value = 42

with open("int_tiny.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
