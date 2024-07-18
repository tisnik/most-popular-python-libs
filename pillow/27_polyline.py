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
from itertools import chain

from PIL import Image, ImageDraw

try:
    # vytvoření prázdného obrázku
    test_image = Image.new("RGB", (512, 512))

    # objekt umožňující kreslení do obrázku
    draw = ImageDraw.Draw(test_image)

    # rozměry obrázku
    width = test_image.size[0]
    height = test_image.size[1]

    def f(angle):
        return width / 2 + width * 0.4 * math.cos(angle * 3)

    def g(angle):
        return height / 2 + height * 0.4 * math.sin(angle * 2)

    endpoints = list(
        chain.from_iterable((f(angle), g(angle)) for angle in range(360))
    )

    draw.line(endpoints, fill=(255, 255, 256))

    # uložení upraveného obrázku
    test_image.save("polyline.png")

    # zobrazení upraveného obrázku
    test_image.show()

except Exception as e:
    print(e)
