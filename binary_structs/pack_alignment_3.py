import struct

bytes1 = struct.pack("lHl", 1, 0xffff, 3)
print(type(bytes1))
print(bytes1.hex(" ", 1))

print()

bytes2 = struct.pack("=lHl", 1, 0xffff, 3)
print(type(bytes2))
print(bytes2.hex(" ", 1))

print()

bytes3 = struct.pack("@lHl", 1, 0xffff, 3)
print(type(bytes3))
print(bytes3.hex(" ", 1))
