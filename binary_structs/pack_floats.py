import struct

for float_type in "efd":
    print(f"Packing as word type '{float_type}'")
    bytes1 = struct.pack(float_type, 1.0)
    print(type(bytes1))
    print(bytes1.hex(" ", 1))
    print()
