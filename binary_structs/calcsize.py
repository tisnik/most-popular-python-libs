import struct


def size_for_format(format):
    size = struct.calcsize(format)
    print(f"{format:>6}:{size}")


size_for_format("b")

print()

size_for_format("iBi")
size_for_format("=iBi")
size_for_format("@iBi")

print()

size_for_format("lBl")
size_for_format("=lBl")
size_for_format("@lBl")

print()

size_for_format("fBf")
size_for_format("=fBf")
size_for_format("@fBf")

print()

size_for_format("dBd")
size_for_format("=dBd")
size_for_format("@dBd")

print()

size_for_format("dBBd")
size_for_format("=dBBd")
size_for_format("@dBBd")

print()

size_for_format("dBBBd")
size_for_format("=dBBBd")
size_for_format("@dBBBd")
