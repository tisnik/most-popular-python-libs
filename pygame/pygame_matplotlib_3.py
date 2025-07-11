#!/usr/bin/python
# vim: set fileencodings=utf-8

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

import matplotlib

matplotlib.use("Agg")
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pygame

# nutno importovat kvuli konstantam QUIT atd.
from pygame.locals import KEYDOWN, QUIT

# velikost okna na obrazovce (framebufferu)
WIDTH = 640
HEIGHT = 480

# DPI (umele zvolena hodnota)
DPI = 100

# jmeno souboru s grafem
IMAGE_FILE = "plot3.png"

# jmeno zarizeni implementujiciho rozhrani k framebufferu
FRAMEBUFFER_DEVICE = "/dev/fb0"


# Vytvoreni grafu
def create_graph(width, height, dpi):
    fig = plt.figure(figsize=(1.0 * width / dpi, 1.0 * height / dpi), dpi=dpi)
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    return fig


# Ulozeni grafu do souboru
def save_graph(fig, imageFile, dpi):
    plt.savefig(imageFile, facecolor=fig.get_facecolor(), dpi=dpi)


# Inicializace knihovny Pygame, inicializace video systemu a otevreni
# framebufferu
def initialize_pygame(width, height, background_color, framebuffer_device):
    os.environ["SDL_FBDEV"] = framebuffer_device
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.mouse.set_visible(0)
    screen.fill(background_color)
    return screen


# Zobrazeni rastroveho obrazku do framebufferu
def show_image(screen, imageFile):
    image = pygame.image.load(imageFile)
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()
    x = (screen_rect.width - image_rect.width) / 2
    y = (screen_rect.height - image_rect.height) / 2
    screen.blit(image, (x, y))
    pygame.display.flip()


# Cekani na ukonceni aplikace libovolnou klavesou
def wait_for_key():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                return
        clock.tick(20)


# Ukonceni aplikace
def exit():
    pygame.quit()
    sys.exit()


# Hlavni funkce aplikace
def main():
    fig = create_graph(WIDTH, HEIGHT, DPI)
    save_graph(fig, IMAGE_FILE, DPI)
    screen = initialize_pygame(WIDTH, HEIGHT, (10, 10, 40), FRAMEBUFFER_DEVICE)
    show_image(screen, IMAGE_FILE)
    wait_for_key()
    exit()


# Vstupni bod
if __name__ == "__main__":
    main()
