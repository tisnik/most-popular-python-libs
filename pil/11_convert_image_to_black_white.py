#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageMath

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    modified_image = ImageMath.eval("convert(src, '1')", src=test_image)

    test_image.show()
    modified_image.show()

except Exception as e:
    print(e)
