#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()

    test_image.save("Lenna.jpg")
    test_image.save("Lenna.bmp")
    test_image.save("Lenna.tiff")

except Exception as e:
    print(e)
