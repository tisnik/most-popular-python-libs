#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pygame

import pygame
import sys

# Příklad číslo 6: výpis seznamu všech dostupných grafických
#                  režimů pro zadané bitové hloubky.

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

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import *

# Inicializace knihovny Pygame
pygame.init()

print("Driver: " + pygame.display.get_driver())
print("")

# Budou nás zajímat grafické režimy s bitovou hloubkou
# 8bpp (256 barev), 16bpp (hi-color), 24bpp a 32bpp (True Color)
for depth in [8, 16, 24, 32]:
    print("Graphics modes for %d bpp:" % depth)

    # Získat seznam grafických režimů pro danou bitovou hloubku
    gfx_modes = pygame.display.list_modes(depth)

    # Vypsat všechny získané režimy
    for gfx_mode in gfx_modes:
        print("    %d x %d pixels" % (gfx_mode[0], gfx_mode[1]))

pygame.quit()

# finito
