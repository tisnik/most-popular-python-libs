import struct

for endianess in "=<>":
    for word_type in "bhilq":
        print(f"Packing as word type '{word_type}' using endianess set to {endianess}")
        bytes1 = struct.pack(f"{endianess}{word_type}", 42)
        print(type(bytes1))
        print(bytes1.hex(" ", 1))
        print()
