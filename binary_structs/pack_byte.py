import struct

bytes1 = struct.pack("b", 42)
print(type(bytes1))
print(bytes1.hex(" ", 1))

print()

bytes2 = struct.pack("B", 42)
print(type(bytes2))
print(bytes2.hex(" ", 1))
