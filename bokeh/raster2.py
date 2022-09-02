#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# naimportujeme vybrané funkce z knihovny `bokeh.plotting`
from bokeh.plotting import figure, output_file, show

# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np

# velikost rastrového obrázku
IMAGE_WIDTH = 16
IMAGE_HEIGHT = 10

# matice představující bázi rastrového obrázku
image = np.empty((IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.uint32)

# "pohled" na matici jako na trojrozměrné pole
view = image.view(dtype=np.uint8).reshape((IMAGE_HEIGHT, IMAGE_WIDTH, 4))

# vyplnění obrázku vzorkem
for j in range(IMAGE_HEIGHT):
    for i in range(IMAGE_WIDTH):
        view[j, i, 0] = int(255 * j / IMAGE_HEIGHT)  # red
        view[j, i, 1] = 0  # green
        view[j, i, 2] = int(255 * i / IMAGE_WIDTH)  # blue
        view[j, i, 3] = 255  # alpha

# plocha pro graf
p = figure(
    width=IMAGE_WIDTH * 30, height=IMAGE_HEIGHT * 30, x_range=(0, 10), y_range=(0, 10)
)

# vykreslení rastrového obrázku typu RGBA
p.image_rgba(image=[image], x=[0], y=[0], dw=[10], dh=[10])

# vykreslení grafu do plochy webové stránky
show(p)
