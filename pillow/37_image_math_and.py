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
    draw.rectangle((0, 0, width/2, height/2), fill=0)
    draw.rectangle((width/2, 0, width, height/2), fill=127)
    draw.rectangle((0, height/2, width/2, height), fill=128)
    draw.rectangle((width/2, height/2, width, height), fill=255)

    del draw
    return second_image


try:
    original_image = Image.open(filename)
    original_image.load()

    grayscale_image = ImageMath.eval("convert(src, 'L')", src=original_image)

    second_image = create_second_image(512, 512)

    result_image = ImageMath.eval("first & second", first=grayscale_image, second=second_image)
    result_image = ImageMath.eval("convert(src, 'L')", src=result_image)

    result_image.show()

    result_image.save("37_image_math_and.png")

except Exception as e:
    print("Vyjimka: " + e.__str__())
