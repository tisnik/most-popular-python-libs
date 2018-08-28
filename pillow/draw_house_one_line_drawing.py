#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageDraw

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("1", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    endpoints = [100, 500,
                 400, 200,
                 100, 200,
                 250,  50,
                 400, 200,
                 400, 500,
                 100, 200,
                 100, 500,
                 400, 500]

    draw.line(endpoints, fill=255)

    # uložení upraveného obrázku
    test_image.save("house.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
