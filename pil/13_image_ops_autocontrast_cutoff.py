#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageOps

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    modified_image_1 = ImageOps.autocontrast(test_image, cutoff=0)
    modified_image_2 = ImageOps.autocontrast(test_image, cutoff=50)
    modified_image_3 = ImageOps.autocontrast(test_image, cutoff=75)

    test_image.show()
    modified_image_1.show()
    modified_image_2.show()
    modified_image_3.show()

except Exception as e:
    print(e)
