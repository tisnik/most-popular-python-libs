#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageMath
from PIL import ImageOps

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    grayscale_image = ImageMath.eval("convert(src, 'L')", src=test_image)

    for bits in range(8, 0, -1):
        modified_image = ImageOps.posterize(grayscale_image, bits)
        modified_image.save("Lenna_grayscale_posterize_" + str(bits) + ".png")

except Exception as e:
    print(e)
