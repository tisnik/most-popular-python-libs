#
#  (C) Copyright 2025  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
    "!IIBBBBB",
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
