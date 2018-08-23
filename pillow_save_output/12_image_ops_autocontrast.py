#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageOps

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    modified_image = ImageOps.autocontrast(test_image)

    modified_image.save("Lenna_autocontrast.png")

except Exception as e:
    print(e)
