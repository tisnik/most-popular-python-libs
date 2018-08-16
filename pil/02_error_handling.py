#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    print(test_image)

except Exception as e:
    print(e)
