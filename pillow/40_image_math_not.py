#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageMath

filename = "Lenna.png"


try:
    # načtení originálního obrázku Leny
    original_image = Image.open(filename)
    original_image.load()

    # převod na úrovně šedi
    grayscale_image = ImageMath.eval("convert(src, 'L')", src=original_image)

    # aplikace operace
    result_image = ImageMath.eval("(~first) & 255", first=grayscale_image)

    # další převod výsledku na stupně šedi
    result_image = ImageMath.eval("convert(src, 'L')", src=result_image)

    # zobrazení výsledného obrázku uživateli
    result_image.show()

    # uložení výsledného obrázku
    result_image.save("40_image_math_not.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
