import msgpack

value = 100000

with open("int_larger.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
