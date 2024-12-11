import msgpack

value = {
        "foo": 42,
        "bar": None,
        "baz": 3.14,
        }

with open("dict.bin", "wb") as outfile:
    packed = msgpack.packb(value)
    outfile.write(packed)
