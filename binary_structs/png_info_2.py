"""Informace o obrázku uloženého ve formátu PNG."""

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

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

with open("test.png", "rb") as fin:
    # nacteni signatury
    signature = fin.read(len(PNG_SIGNATURE))

    # kontrola signatury
    assert len(signature) == len(PNG_SIGNATURE)
    assert signature == PNG_SIGNATURE

    # postupne nacteni jednotlivych chunku
    print("Chunk  Length   CRC")
    while True:
        # nacteni hlavicky chunku
        chunk_header = fin.read(8)
        if len(chunk_header) < 8:
            print(f"End of file with remaining {len(chunk_header)} bytes")
            break
        # hlavicka obsahuje delku (4 bajty) a ctyri znaky se jmenem
        s = struct.Struct("!I4s")
        length, png_tag = s.unpack(chunk_header)

        if png_tag == b"IHDR":
            # hlavicku nacist celou - ocekava se tento format:
            # Width:              4 bytes
            # Height:             4 bytes
            # Bit depth:          1 byte
            # Color type:         1 byte
            # Compression method: 1 byte
            # Filter method:      1 byte
            # Interlace method:   1 byte
            h = struct.Struct("!2I5B")
            chunk_data = fin.read(length)
            width, height, bit_depth, color_type, compression, filter, interlace = (
                h.unpack(chunk_data)
            )
        else:
            # preskocit data chunku
            fin.seek(length, 1)

        # nacteni CRC32 chunku
        c = struct.Struct("!I")
        crc_block = fin.read(4)
        if len(crc_block) < 4:
            print("Error: not correct CRC block!")
            break
        crc = c.unpack(crc_block)[0]
        print(f"{png_tag.decode("ASCII")}  {length:5}   {crc:04x}")


color_type_desc = [
    "grayscale",
    "unknown",
    "RGB",
    "color palette",
    "grayscale+alpha",
    "unknown",
    "RGBA",
]


print(f"Resolution:  {width}x{height}")
print(f"Bit depth:   {bit_depth} bpp")
print(f"Color type:  {color_type} = {color_type_desc[color_type]}")
print(f"Compression: {compression}")
print(f"Filter type: {filter}")
print(f"Interlace:   {interlace}")
