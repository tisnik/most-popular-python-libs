#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageColor

try:
    # vytvoření prázdných obrázků
    test_image_1 = Image.new("RGB", (256, 256))
    test_image_2 = Image.new("RGB", (256, 256))

    # rozměry obrázku
    width = test_image_1.size[0]
    height = test_image_2.size[1]

    # vykreslení různobarevných pixelů
    for y in range(0, height):
        for x in range(0, width):
            color_rgb = (x, 0, y)
            test_image_1.putpixel((x, y), color_rgb)
            color_rgb = (x, 255, y)
            test_image_2.putpixel((x, y), color_rgb)

    # uložení upraveného obrázku
    test_image_1.save("rgb_palette_1.png")
    test_image_2.save("rgb_palette_2.png")

    # zobrazení upraveného obrázku
    test_image_1.show()
    test_image_2.show()

except Exception as e:
    print(e)
