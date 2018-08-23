#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image
from PIL import ImageEnhance

filename = "Lenna.png"

try:
    # načtení originálního obrázku Leny
    test_image = Image.open(filename)
    test_image.load()

    # inicializace "vylepšovače" obrázků
    enhancer = ImageEnhance.Brightness(test_image)

    # vytvoření "vylepšených" i "zhoršených" obrázků
    more_brightness_image = enhancer.enhance(2.0)
    less_brightness_image = enhancer.enhance(0.5)

    # uložení upravených obrázků
    more_brightness_image.save("enhancer_brightness_more.png")
    less_brightness_image.save("enhancer_brightness_less.png")

    # zobrazení originálu i upravených obrázků
    test_image.show()
    more_brightness_image.show()
    less_brightness_image.show()

except Exception as e:
    print(e)
