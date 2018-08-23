#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import math

from PIL import Image
from PIL import ImageDraw

from itertools import chain

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("RGB", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    def f(angle):
        return width/2 + width * 0.4 * math.cos(angle * 3)

    def g(angle):
        return height/2 + height * 0.4 * math.sin(angle * 2)

    endpoints = list(chain.from_iterable((f(angle), g(angle)) for angle in range(0, 360)))

    draw.line(endpoints, fill=(255, 255, 256))

    # uložení upraveného obrázku
    test_image.save("polyline.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
