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

import math

from PIL import Image
from PIL import ImageDraw

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("RGBA", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    draw.rectangle((0, 0, width, height), fill=(255, 255, 255))

    green = 255
    for i, r, red, blue in zip(
        range(0, 128), range(128, 0, -1), range(255, 0, -2), range(0, 256, 2)
    ):
        a = i / 12.0
        b = i + 80.0
        x = width / 2 + b * math.cos(a)
        y = height / 2 + b * math.sin(a)
        draw.ellipse(
            (x - r, y - r, x + r, y + r), fill=(red, green, blue), outline="black"
        )

    # uložení upraveného obrázku
    test_image.save("circle_pattern.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
