#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 10: použití objektů typu Surface a metoda blit().

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

import os
import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #10")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)


image_surface = pygame.image.load(os.path.join("images", "gnome-globe.png"))

display.blit(image_surface, (0, 0))
display.blit(image_surface, (100, 100))


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(20)

# finito
