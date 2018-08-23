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
    enhancer = ImageEnhance.Sharpness(test_image)

    # vytvoření "vylepšených" i "zhoršených" obrázků
    sharper_image = enhancer.enhance(5.0)
    blurred_image = enhancer.enhance(0.5)

    # uložení upravených obrázků
    sharper_image.save("enhancer_sharpness_sharper.png")
    blurred_image.save("enhancer_sharpness_blurred.png")

    # zobrazení originálu i upravených obrázků
    test_image.show()
    sharper_image.show()
    blurred_image.show()

except Exception as e:
    print(e)
