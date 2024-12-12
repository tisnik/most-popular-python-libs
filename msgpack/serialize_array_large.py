import msgpack

value = []

for i in range(1000):
    value.append(i)

with open("array3.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
