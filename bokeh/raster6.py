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
# taktéž budeme potřebovat některé funkce z knihovny `numpy`
import numpy as np
from bokeh.plotting import figure, show

# textura by měla být čtvercová a její šířka i výška by měla být
# mocninou čísla 2
IMAGE_WIDTH = 512
IMAGE_HEIGHT = 512

# souřadnice mřížky na x-ové a y-ové ose
x = np.linspace(-500, 500, IMAGE_WIDTH)
y = np.linspace(-500, 500, IMAGE_HEIGHT)

# matice s x-ovými a y-ovými souřadnicemi tvořícími mřížku
xx, yy = np.meshgrid(x, y)

# výpočet vzorku, který se má zobrazit
d = np.mod((xx * xx + yy * yy).astype(int), 255)

# plocha pro graf
p = figure(width=IMAGE_WIDTH, height=IMAGE_HEIGHT)
p.x_range.range_padding = p.y_range.range_padding = 0

# vykreslení rastrového obrázku do grafu
p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="RdGy11", level="image")
p.grid.grid_line_width = 0.5


# vykreslení grafu do plochy webové stránky
show(p)
