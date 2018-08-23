#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageMath

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    modified_image = ImageMath.eval("convert(src, '1')", src=test_image)

    modified_image.save("Lenna_BW.png")

except Exception as e:
    print(e)
