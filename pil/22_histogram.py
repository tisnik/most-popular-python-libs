#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PIL import Image

filename = "Lenna.png"

try:
    # načtení originálního obrázku Leny
    test_image = Image.open(filename)
    test_image.load()

    histogram = test_image.histogram()

    print(histogram[0:255])
    print()
    print(histogram[256:511])
    print()
    print(histogram[512:767])
    print()

except Exception as e:
    print(e)
