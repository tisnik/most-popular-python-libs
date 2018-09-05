#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageMath

filename = "Lenna.png"


def create_second_image(width, height):
    second_image = Image.new("L", (width, height))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(second_image)

    # vykreslení čtverců
    for y in range(0, height, 32):
        for x in range(0, width, 32):
            draw.rectangle((x+0, y+0, x+29, y+29), outline=255, fill=x//4 + y//4)

    del draw
    return second_image


try:
    # načtení originálního obrázku Leny
    original_image = Image.open(filename)
    original_image.load()

    # převod na úrovně šedi
    grayscale_image = ImageMath.eval("convert(src, 'L')", src=original_image)

    # vytvoření druhého obrázku s maskou
    second_image = create_second_image(512, 512)

    # aplikace operace
    result_image = ImageMath.eval("first*second/256", first=grayscale_image, second=second_image)

    # další převod výsledku na stupně šedi
    result_image = ImageMath.eval("convert(src, 'L')", src=result_image)

    # zobrazení výsledného obrázku uživateli
    result_image.show()

    # uložení výsledného obrázku
    result_image.save("35_image_math_mul.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
