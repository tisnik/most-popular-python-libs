import msgpack

value = "Hello"

with open("short_string.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
