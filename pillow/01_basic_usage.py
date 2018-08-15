#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from PIL import Image

filename = "Lenna.png"

test_image = Image.open(filename)
test_image.load()
print(test_image)
