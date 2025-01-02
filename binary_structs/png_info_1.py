"""Informace o obrázku uloženého ve formátu PNG."""

import struct

PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

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
