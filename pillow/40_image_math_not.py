#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageMath

filename = "Lenna.png"


try:
    original_image = Image.open(filename)
    original_image.load()

    grayscale_image = ImageMath.eval("convert(src, 'L')", src=original_image)

    result_image = ImageMath.eval("(~first) & 255", first=grayscale_image)
    result_image = ImageMath.eval("convert(src, 'L')", src=result_image)

    result_image.show()

    result_image.save("40_image_math_not.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
