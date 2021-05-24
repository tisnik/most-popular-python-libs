#!/usr/bin/env python
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

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("RGB", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    # vykreslení různobarevných čtverců
    for y in range(0, height, 32):
        for x in range(0, width, 32):
            draw.rectangle((x+1, y+1, x+28, y+28), outline=(255, 255, 255), fill=(x, 255, y))

    # uložení upraveného obrázku
    test_image.save("color_rectangles.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
