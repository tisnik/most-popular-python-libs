#!/usr/bin/env python3
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

    modified_image_1.save("Lenna_autocontrast_cutoff_0.png")
    modified_image_2.save("Lenna_autocontrast_cutoff_50.png")
    modified_image_3.save("Lenna_autocontrast_cutoff_75.png")

except Exception as e:
    print(e)
