import struct

# Width:              4 bytes
# Height:             4 bytes
# Bit depth:          1 byte
# Color type:         1 byte
# Compression method: 1 byte
# Filter method:      1 byte
# Interlace method:   1 byte

width = 1024
height = 768
bit_depth = 8
color_type = 6  # RGB
compression_method = 0  # deflate
filter_method = 0  # adaptive filter
interlace_method = 0 # no interlace

bytes1 = b"IHDR" + struct.pack(
    "!2I5B",
    width,
    height,
    bit_depth,
    color_type,
    compression_method,
    filter_method,
    interlace_method,
)

print(type(bytes1))
print(bytes1.hex(" ", 1))
