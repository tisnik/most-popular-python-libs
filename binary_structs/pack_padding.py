import struct

bytes1 = struct.pack("lB", 1, 0xff)
print(type(bytes1))
print(bytes1.hex(" ", 1))

print()

bytes2 = struct.pack("lB0h", 1, 0xff)
print(type(bytes2))
print(bytes2.hex(" ", 1))

print()

bytes3 = struct.pack("lB0i", 1, 0xff)
print(type(bytes3))
print(bytes3.hex(" ", 1))

print()

bytes4 = struct.pack("lB0l", 1, 0xff)
print(type(bytes4))
print(bytes4.hex(" ", 1))
