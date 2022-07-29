#!/usr/bin/env python

"""Texture rendering based on FM synthesis."""

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pywebio.input as inp
import pywebio.output as out

from PIL import Image
import palette_blues
from math import *

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def fm(image, palette, xmin, ymin, xmax, ymax, a, b, c):
    """Generate texture based on FM synthesis algorithm."""
    width, height = image.size  # rozmery obrazku
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height

    a /= 10.0

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            x1 += stepx
            val = 100 + 100.0 * sin(x / a + 2 * sin(x / b + y / c))
            i = int(val) & 255
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)
        y1 += stepy


def main():
    a = 40
    b = 20
    c = 50

    while True:
        image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

        fm(image, palette_blues.palette, -1.0, -1.0, 1.0, 1.0, a, b, c)
        out.put_image(image)

        # vstupní údaje
        info = inp.input_group(
            "FM synthesis",
            [
                inp.slider(label="a", name="a", value=a, min_value=1, max_value=100),
                inp.slider(label="b", name="b", value=b, min_value=1, max_value=50),
                inp.slider(label="c", name="c", value=c, min_value=1, max_value=100),
            ],
        )

        a = info["a"]
        b = info["b"]
        c = info["c"]


main()
