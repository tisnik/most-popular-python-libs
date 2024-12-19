"""Zápis rastrového obrázku s RGB pixely do formátu PNG."""

# Inspirace: https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image

import struct
import zlib

PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'
FILTER_TYPE = b'\x00'

def prepare_raw_data(buffer, width, height):
    """Konverze barev pixelů z bufferu do podoby se specifikací filtru na každém řádku."""
    raw_data = bytearray()
    offset = 0
    for _ in range(height):
        # nastavit filtr + zkopirovat jeden radek (scanline)
        raw_data += FILTER_TYPE + buffer[offset:offset+width*3]
        # na dalsi radek ve zdrojovem bufferu
        offset += width*3
    return raw_data


def png_chunk(png_tag, chunk_data):
    """Konstrukce jednoho PNG chunku s tagem i závěrečným kontrolním kódem."""
    chunk_header = png_tag + chunk_data
    return (struct.pack("!I", len(chunk_data)) +
            chunk_header +
            struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_header)))


def write_png(buffer, width, height):
    """Uložení rastrového obrázku z bufferu do PNG."""
    raw_data = prepare_raw_data(buffer, width, height)

    return b''.join([
        PNG_SIGNATURE,
        png_chunk(b'IHDR', struct.pack("!2I5B", width, height, 8, 2, 0, 0, 0)),
        png_chunk(b'IDAT', zlib.compress(raw_data, level=9, wbits=15)),
        png_chunk(b'IEND', b'')])


WIDTH = 256
HEIGHT = 256

# buffer pro rastrová data
pixels = bytearray(WIDTH*HEIGHT*3)

# vybarvení testovacího obrázku
index = 0
for i in range(HEIGHT):
    for j in range(WIDTH):
        pixels[index] = 0xff
        index+=1
        pixels[index] = i
        index+=1
        pixels[index] = j
        index+=1

data = write_png(pixels, WIDTH, HEIGHT)
with open("test.png", 'wb') as fout:
    fout.write(data)

