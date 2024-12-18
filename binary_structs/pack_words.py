import struct

for word_type in "bhilq":
    print(f"Packing as word type '{word_type}'")
    bytes1 = struct.pack(word_type, 42)
    print(type(bytes1))
    print(bytes1.hex(" ", 1))
    print()
