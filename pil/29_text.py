#!/usr/bin/env python
# vim: set fileencoding=utf-8

import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("RGBA", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # načtení fontu
    font = ImageFont.truetype('FreeMono.ttf', 72)

    # vykreslení jednoduchého textu
    draw.text((50, height/2 - 36), "Pillow", font=font, fill=(255, 128, 128))

    # uložení upraveného obrázku
    test_image.save("text.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
