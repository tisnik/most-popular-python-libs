#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2020  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from PIL import Image
from PIL import ImageDraw

filename = "Lenna.png"

try:
    # načtení originálního obrázku Leny
    test_image = Image.open(filename)
    test_image.load()

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # vertikální úsečky
    for x in range(0, width, 30):
        draw.line((x, 0, x, height-1), fill=(255, 255, 255))

    # horizontální úsečky
    for y in range(0, height, 30):
        draw.line((0, y, width-1, y), fill=(255, 255, 255))

    # uložení upraveného obrázku
    test_image.save("grid.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
