#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageOps

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    test_image.show()

    for bits in range(8, 0, -1):
        modified_image = ImageOps.posterize(test_image, bits)
        modified_image.show()

except Exception as e:
    print(e)
