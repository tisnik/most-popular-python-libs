#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 1: kostra aplikace, v níž se používá
#                  knihovna Pygame

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

import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Inicializace knihovny Pygame
pygame.init()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #1")


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# finito
